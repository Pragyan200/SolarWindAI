from app.services.feature_engineering.solar import SolarFeatureService
from app.services.feature_engineering.wind_assessment import (
    classify_wind_site,
)
from app.services.site_scoring import (
    calculate_overall_score,
    renewable_resource_score,
    terrain_score,
    infrastructure_score,
)
from app.services.energy_estimation import estimate_energy
from app.services.deployment_optimization import generate_deployment_plan
from app.services.feasibility.feasibility_engine import FeasibilityEngine

from app.services.financial_analysis.financial_calculations import (
    calculate_annual_revenue,
    calculate_project_cost,
    calculate_payback_period,
    calculate_roi,
)

from app.ml.model_inference import predict_energy

from app.data_sources.srtm import SRTMClient
from app.data_sources.osm import OSMClient
from app.data_sources.global_wind_atlas import GlobalWindAtlasClient


class AnalysisPipeline:

    def __init__(self):
        self.solar_service = SolarFeatureService()
        self.srtm_client = SRTMClient()
        self.osm_client = OSMClient()
        self.wind_client = GlobalWindAtlasClient()
        self.feasibility_engine = FeasibilityEngine()

    def analyze_site(
        self,
        latitude: float,
        longitude: float,
        land_area: float,
        available_land: float,
        restricted_land: bool,
        slope: float,
        distance_to_grid: float,
        distance_to_road: float,
        accessibility: str,
        electricity_tariff: float,
        cost_per_mw: float,
        additional_installation_percentage: float = 0.0,
    ):

        # ---------------------------------------------------------
        # 1. NASA POWER
        # ---------------------------------------------------------
        solar_features = self.solar_service.build_features(
            latitude,
            longitude
        )

        solar_irradiance = solar_features["solar_irradiance"]
        temperature = solar_features["temperature"]
        relative_humidity = solar_features["relative_humidity"]
        nasa_wind_speed = solar_features["wind_speed_50m"]

        # ---------------------------------------------------------
        # 2. SRTM
        # ---------------------------------------------------------
        elevation = self.srtm_client.get_elevation(
            latitude,
            longitude
        )

        # ---------------------------------------------------------
        # 3. Global Wind Atlas
        # ---------------------------------------------------------
        wind_data = self.wind_client.get_wind_data(
            latitude,
            longitude
        )

        wind_speed = wind_data["wind_speed"]
        power_density = wind_data["power_density"]

        # ---------------------------------------------------------
        # 4. OSM
        # ---------------------------------------------------------
        infrastructure = self.osm_client.get_infrastructure(
            latitude,
            longitude
        )

        total_roads = infrastructure["total_roads"]

        # ---------------------------------------------------------
        # 5. Wind Assessment
        # ---------------------------------------------------------
        wind_result = classify_wind_site(wind_speed)

        wind_capacity_factor = wind_result["capacity_factor"]

        # ---------------------------------------------------------
        # 6. Site Scoring
        # ---------------------------------------------------------
        renewable_score = renewable_resource_score(
            solar_irradiance=solar_irradiance,
            wind_speed=wind_speed,
        )

        terrain = terrain_score(
            slope=slope,
            elevation=elevation,
        )

        infrastructure_score_value = infrastructure_score(
            distance_to_grid=distance_to_grid,
            distance_to_road=distance_to_road,
        )

        environment_score = 0.0 if restricted_land else 100.0

        if accessibility.lower() == "good":
            economic_score_value = 100.0
        elif accessibility.lower() == "moderate":
            economic_score_value = 60.0
        else:
            economic_score_value = 30.0

        overall_score = calculate_overall_score(
            renewable=renewable_score,
            terrain=terrain,
            infrastructure=infrastructure_score_value,
            environment=environment_score,
            economic=economic_score_value,
        )

        # ---------------------------------------------------------
        # 7. ML Prediction
        # ---------------------------------------------------------
        ml_features = {
            "ALLSKY_SFC_SW_DWN": solar_irradiance,
            "T2M": temperature,
            "RH2M": relative_humidity,
            "WS50M": nasa_wind_speed,
            "wind_speed": wind_speed,
            "power_density": power_density,
            "mean_elevation": elevation,
            "total_roads": total_roads,
        }

        # Sentinel is not included because the available
        # Sentinel ZIP has no geographic coordinate mapping.
        ml_prediction = predict_energy(ml_features)

        # ---------------------------------------------------------
        # 8. Technical Feasibility
        # ---------------------------------------------------------
        feasibility_result = self.feasibility_engine.evaluate({
            "restricted_land": restricted_land,
            "slope": slope,
            "land_area": land_area,
            "distance_to_grid": distance_to_grid,
            "distance_to_road": distance_to_road,
            "accessibility": accessibility,
        })

        # ---------------------------------------------------------
        # 9. Deployment + Energy + Financial Analysis
        # ---------------------------------------------------------
        if feasibility_result["technical_feasibility"]:

            deployment_plan = generate_deployment_plan(
                site_score=overall_score["overall_score"],
                solar_score=renewable_score,
                wind_score=wind_speed,
                land_area=land_area,
                available_land=available_land,
            )

            deployment_type = deployment_plan[
                "recommended_technology"
            ].replace(" Deployment", "")

            installed_capacity = deployment_plan[
                "recommended_capacity"
            ]

            # Solar capacity factor derived from solar resource.
            solar_capacity_factor = max(
                0.0,
                min(
                    1.0,
                    solar_irradiance / 24.0
                )
            )

            # Use wind capacity factor derived from
            # location-specific wind speed.
            wind_capacity_factor = wind_result[
                "capacity_factor"
            ]

            # Configurable system efficiency.
            system_efficiency = 0.90

            energy_estimation = estimate_energy(
                site_result="Suitable",
                deployment_type=deployment_type,
                installed_capacity=installed_capacity,
                solar_capacity_factor=solar_capacity_factor,
                wind_capacity_factor=wind_capacity_factor,
                system_efficiency=system_efficiency,
            )

            annual_energy_yield = energy_estimation[
                "total_estimated_annual_energy"
            ]

            annual_revenue = calculate_annual_revenue(
                annual_energy_yield=annual_energy_yield,
                electricity_tariff=electricity_tariff,
            )

            estimated_project_cost = calculate_project_cost(
                installed_capacity_mw=installed_capacity,
                cost_per_mw=cost_per_mw,
                additional_installation_percentage=(
                    additional_installation_percentage
                ),
            )

            payback_period = calculate_payback_period(
                total_project_cost=estimated_project_cost,
                annual_revenue=annual_revenue,
            )

            roi = calculate_roi(
                total_project_cost=estimated_project_cost,
                annual_revenue=annual_revenue,
            )

            financial_analysis = {
                "annual_energy_yield": annual_energy_yield,
                "electricity_tariff": electricity_tariff,
                "annual_revenue": annual_revenue,
                "installed_capacity_mw": installed_capacity,
                "cost_per_mw": cost_per_mw,
                "estimated_project_cost": estimated_project_cost,
                "payback_period": payback_period,
                "roi": roi,
            }

        else:

            deployment_plan = {
                "recommendation": "Site is not technically feasible"
            }

            energy_estimation = {
                "status": (
                    "Skipped because site is not technically feasible"
                )
            }

            financial_analysis = {
                "status": (
                    "Skipped because site is not technically feasible"
                )
            }

        # ---------------------------------------------------------
        # 10. Final Response
        # ---------------------------------------------------------
        return {
            "location": {
                "latitude": latitude,
                "longitude": longitude,
            },

            "environmental_data": {
                "solar_irradiance": solar_irradiance,
                "temperature": temperature,
                "relative_humidity": relative_humidity,
                "elevation": elevation,
                "wind_speed": wind_speed,
                "power_density": power_density,
                "total_roads": total_roads,
            },

            "solar_assessment": solar_features,

            "wind_assessment": wind_result,

            "site_suitability": overall_score,

            "ml_energy_prediction": ml_prediction,

            "technical_feasibility": {
                "status": feasibility_result[
                    "technical_feasibility"
                ],
                "score": feasibility_result[
                    "feasibility_score"
                ],
                "constraint_summary": feasibility_result[
                    "constraint_summary"
                ],
            },

            "recommended_deployment": deployment_plan,

            "energy_yield": energy_estimation,

            "financial_metrics": financial_analysis,
        }