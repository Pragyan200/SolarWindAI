from app.services.feature_engineering.solar import (
    SolarFeatureService
)

from app.services.feature_engineering.wind_assessment import (
    classify_wind_site
)

from app.services.site_scoring import (
    calculate_overall_score,
    renewable_resource_score,
    terrain_score,
    infrastructure_score,
)

from app.services.energy_estimation import (
    estimate_energy
)

from app.services.deployment_optimization import (
    generate_deployment_plan
)

from app.services.feasibility.feasibility_engine import (
    FeasibilityEngine
)

from app.services.financial_analysis.financial_calculations import (
    calculate_annual_revenue,
    calculate_project_cost,
    calculate_payback_period,
    calculate_roi,
)

from app.ml.model_inference import predict_energy

from app.data_sources.srtm import SRTMClient

from app.data_sources.osm import OSMClient

from app.data_sources.global_wind_atlas import (
    GlobalWindAtlasClient
)


class AnalysisPipeline:

    def __init__(self):

        self.solar_service = SolarFeatureService()

        self.srtm_client = SRTMClient()

        self.osm_client = OSMClient()

        self.wind_client = GlobalWindAtlasClient()

        self.feasibility_engine = FeasibilityEngine()


    # ========================================================
    # MAIN ANALYSIS
    # ========================================================

    def analyze_site(
        self,
        latitude: float,
        longitude: float,

        land_area: float = 10.0,
        available_land: float = 8.0,

        restricted_land: bool = False,

        slope: float = 0.0,

        distance_to_grid: float = 5.0,

        distance_to_road: float = 0.0,

        accessibility: str = "Unknown",

        electricity_tariff: float = 5.0,

        cost_per_mw: float = 5000000.0,

        additional_installation_percentage: float = 0.0,
    ):

        # ====================================================
        # 1. NASA POWER
        # ====================================================

        solar_features = (
            self.solar_service.build_features(
                latitude,
                longitude
            )
        )

        solar_irradiance = float(
            solar_features.get(
                "solar_irradiance",
                0.0
            )
        )

        temperature = float(
            solar_features.get(
                "temperature",
                25.0
            )
        )

        relative_humidity = float(
            solar_features.get(
                "relative_humidity",
                60.0
            )
        )

        nasa_wind_speed = float(
            solar_features.get(
                "wind_speed_50m",
                5.0
            )
        )


        # ====================================================
        # 2. SRTM
        # Elevation and slope are automatically obtained.
        # ====================================================

        terrain_data = (
            self.srtm_client.get_terrain_data(
                latitude,
                longitude
            )
        )

        elevation = float(
            terrain_data.get(
                "elevation",
                0.0
            )
        )

        # Slope comes from SRTM.
        slope = float(
            terrain_data.get(
                "slope",
                0.0
            )
        )


        # ====================================================
        # 3. GLOBAL WIND ATLAS
        # ====================================================

        wind_data = (
            self.wind_client.get_wind_data(
                latitude,
                longitude
            )
        )

        wind_speed = float(
            wind_data.get(
                "wind_speed",
                nasa_wind_speed
            )
        )

        power_density = float(
            wind_data.get(
                "power_density",
                0.0
            )
        )


        # ====================================================
        # 4. OPENSTREETMAP
        # Automatically obtains road information.
        # ====================================================

        infrastructure = (
            self.osm_client.get_infrastructure(
                latitude,
                longitude
            )
        )

        total_roads = int(
            infrastructure.get(
                "total_roads",
                0
            )
        )

        unique_road_types = int(
            infrastructure.get(
                "unique_road_types",
                0
            )
        )

        osm_distance_to_road = (
            infrastructure.get(
                "distance_to_road"
            )
        )

        if osm_distance_to_road is None:

            distance_to_road = 5.0

        else:

            distance_to_road = float(
                osm_distance_to_road
            )


        accessibility = infrastructure.get(
            "accessibility",
            "Poor"
        )


        # ====================================================
        # 5. WIND ASSESSMENT
        # ====================================================

        wind_result = classify_wind_site(
            wind_speed
        )

        wind_capacity_factor = float(
            wind_result.get(
                "capacity_factor",
                0.0
            )
        )


        # ====================================================
        # 6. SITE SCORING
        # ====================================================

        renewable_score = (
            renewable_resource_score(
                solar_irradiance=solar_irradiance,
                wind_speed=wind_speed,
            )
        )

        terrain = terrain_score(
            slope=slope,
            elevation=elevation,
        )

        infrastructure_score_value = (
            infrastructure_score(
                distance_to_grid=distance_to_grid,
                distance_to_road=distance_to_road,
            )
        )


        # Environmental score
        if restricted_land:

            environment_score = 0.0

        else:

            environment_score = 100.0


        # Economic/accessibility score
        accessibility_lower = str(
            accessibility
        ).lower()


        if accessibility_lower == "good":

            economic_score_value = 100.0

        elif accessibility_lower == "moderate":

            economic_score_value = 60.0

        else:

            economic_score_value = 30.0


        overall_score = (
            calculate_overall_score(

                renewable=renewable_score,

                terrain=terrain,

                infrastructure=(
                    infrastructure_score_value
                ),

                environment=environment_score,

                economic=economic_score_value,
            )
        )


        # ====================================================
        # 7. ML ENERGY PREDICTION
        # ====================================================

        ml_features = {

            "ALLSKY_SFC_SW_DWN":
                solar_irradiance,

            "T2M":
                temperature,

            "RH2M":
                relative_humidity,

            "WS50M":
                nasa_wind_speed,

            "wind_speed":
                wind_speed,

            "power_density":
                power_density,

            "mean_elevation":
                elevation,

            "total_roads":
                total_roads,
        }


        # Do NOT allow ML failure to crash the entire
        # site analysis.

        try:

            ml_prediction = predict_energy(
                ml_features
            )

        except Exception as e:

            ml_prediction = {

                "status":
                    "ML prediction unavailable",

                "message":
                    str(e)
            }


        # ====================================================
        # 8. TECHNICAL FEASIBILITY
        # ====================================================

        feasibility_result = (
            self.feasibility_engine.evaluate(
                {

                    "restricted_land":
                        restricted_land,

                    "slope":
                        slope,

                    "land_area":
                        land_area,

                    "distance_to_grid":
                        distance_to_grid,

                    "distance_to_road":
                        distance_to_road,

                    "accessibility":
                        accessibility,
                }
            )
        )


        technical_feasibility = bool(
            feasibility_result.get(
                "technical_feasibility",
                False
            )
        )


        # ====================================================
        # 9. DEPLOYMENT + ENERGY + FINANCIAL
        # ====================================================

        if technical_feasibility:

            deployment_plan = (
                generate_deployment_plan(

                    site_score=(
                        overall_score[
                            "overall_score"
                        ]
                    ),

                    solar_score=
                        renewable_score,

                    wind_score=
                        wind_speed,

                    land_area=
                        land_area,

                    available_land=
                        available_land,
                )
            )


            deployment_type = (
                deployment_plan.get(
                    "recommended_technology",
                    "Solar Deployment"
                )
            )


            deployment_type = (
                deployment_type.replace(
                    " Deployment",
                    ""
                )
            )


            installed_capacity = float(
                deployment_plan.get(
                    "recommended_capacity",
                    1.0
                )
            )


            # Safety check
            if installed_capacity <= 0:

                installed_capacity = 1.0


            # =================================================
            # Solar Capacity Factor
            # =================================================

            solar_capacity_factor = (

                solar_irradiance / 24.0

            )


            solar_capacity_factor = max(
                0.0,
                min(
                    1.0,
                    solar_capacity_factor
                )
            )


            # =================================================
            # WIND CAPACITY FACTOR
            # =================================================

            wind_capacity_factor = max(
                0.0,
                min(
                    1.0,
                    wind_capacity_factor
                )
            )


            # =================================================
            # SYSTEM EFFICIENCY
            # =================================================

            system_efficiency = 0.90


            # =================================================
            # ENERGY ESTIMATION
            # =================================================

            try:

                energy_estimation = (
                    estimate_energy(

                        site_result="Suitable",

                        deployment_type=
                            deployment_type,

                        installed_capacity=
                            installed_capacity,

                        solar_capacity_factor=
                            solar_capacity_factor,

                        wind_capacity_factor=
                            wind_capacity_factor,

                        system_efficiency=
                            system_efficiency,
                    )
                )

            except Exception as e:

                energy_estimation = {

                    "status":
                        "Energy estimation failed",

                    "message":
                        str(e),

                    "total_estimated_annual_energy":
                        0.0
                }


            annual_energy_yield = float(
                energy_estimation.get(
                    "total_estimated_annual_energy",
                    0.0
                )
            )


            # =================================================
            # FINANCIAL ANALYSIS
            # =================================================

            try:

                annual_revenue = (
                    calculate_annual_revenue(

                        annual_energy_yield=
                            annual_energy_yield,

                        electricity_tariff=
                            electricity_tariff,
                    )
                )

            except Exception:

                annual_revenue = 0.0


            try:

                estimated_project_cost = (
                    calculate_project_cost(

                        installed_capacity_mw=
                            installed_capacity,

                        cost_per_mw=
                            cost_per_mw,

                        additional_installation_percentage=
                            additional_installation_percentage,
                    )
                )

            except Exception:

                estimated_project_cost = (
                    installed_capacity
                    * cost_per_mw
                )


            # =================================================
            # PAYBACK / ROI
            # Avoid division-by-zero.
            # =================================================

            if (
                annual_revenue is None
                or annual_revenue <= 0
            ):

                payback_period = None

                roi = None

            else:

                try:

                    payback_period = (
                        calculate_payback_period(

                            total_project_cost=
                                estimated_project_cost,

                            annual_revenue=
                                annual_revenue,
                        )
                    )

                except Exception:

                    payback_period = None


                try:

                    roi = calculate_roi(

                        total_project_cost=
                            estimated_project_cost,

                        annual_revenue=
                            annual_revenue,
                    )

                except Exception:

                    roi = None


            financial_analysis = {

                "annual_energy_yield":
                    annual_energy_yield,

                "electricity_tariff":
                    electricity_tariff,

                "annual_revenue":
                    annual_revenue,

                "installed_capacity_mw":
                    installed_capacity,

                "cost_per_mw":
                    cost_per_mw,

                "estimated_project_cost":
                    estimated_project_cost,

                "payback_period":
                    payback_period,

                "roi":
                    roi,
            }


        else:

            deployment_plan = {

                "recommendation":
                    "Site is not technically feasible"
            }


            energy_estimation = {

                "status":
                    "Skipped because site is not technically feasible",

                "total_estimated_annual_energy":
                    0.0
            }


            financial_analysis = {

                "status":
                    "Skipped because site is not technically feasible"
            }


        # ====================================================
        # 10. FINAL RESPONSE
        # ====================================================

        return {

            "location": {

                "latitude":
                    latitude,

                "longitude":
                    longitude,
            },


            "environmental_data": {

                "solar_irradiance":
                    solar_irradiance,

                "temperature":
                    temperature,

                "relative_humidity":
                    relative_humidity,

                "elevation":
                    elevation,

                "slope":
                    slope,

                "wind_speed":
                    wind_speed,

                "power_density":
                    power_density,

                "total_roads":
                    total_roads,

                "unique_road_types":
                    unique_road_types,

                "distance_to_road":
                    distance_to_road,

                "accessibility":
                    accessibility,

                "distance_to_grid":
                    distance_to_grid,

                "land_area":
                    land_area,
            },


            "solar_assessment":
                solar_features,


            "wind_assessment":
                wind_result,


            "site_suitability":
                overall_score,


            "ml_energy_prediction":
                ml_prediction,


            "technical_feasibility": {

                "status":
                    feasibility_result.get(
                        "technical_feasibility",
                        False
                    ),

                "score":
                    feasibility_result.get(
                        "feasibility_score",
                        0.0
                    ),

                "constraint_summary":
                    feasibility_result.get(
                        "constraint_summary",
                        {}
                    ),
            },


            "recommended_deployment":
                deployment_plan,


            "energy_yield":
                energy_estimation,


            "financial_metrics":
                financial_analysis,
        }