from app.services.feature_engineering.solar import SolarFeatureService
from app.services.feature_engineering.wind_assessment import classify_wind_site
from app.services.site_scoring import calculate_overall_score
from app.services.energy_estimation import estimate_energy
from app.services.deployment_optimization import generate_deployment_plan

from app.ml.model_inference import predict_energy


class AnalysisPipeline:

    def __init__(self):
        self.solar_service = SolarFeatureService()


    def analyze_site(
        self,
        latitude: float,
        longitude: float,
        land_area: float,
        available_land: float
    ):

        # Solar features
        solar_features = self.solar_service.build_features(
            latitude,
            longitude
        )


        # Wind assessment
        wind_result = classify_wind_site(6.2)


        # Site scoring
        overall_score = calculate_overall_score(
            renewable=85,
            terrain=75,
            infrastructure=70,
            environment=80,
            economic=75
        )


        # Deployment optimization
        deployment_plan = generate_deployment_plan(
            site_score=overall_score["overall_score"],
            solar_score=85,
            wind_score=wind_result["wind_speed"],
            land_area=land_area,
            available_land=available_land
        )


        # Energy estimation
        energy_estimation = estimate_energy(
            site_result="Suitable",
            deployment_type=deployment_plan["recommended_technology"].replace(
                " Deployment",
                ""
            ),
            installed_capacity=deployment_plan["recommended_capacity"]
        )


        # ML Prediction Features
        ml_features = {
    "ALLSKY_SFC_SW_DWN": solar_features["solar_irradiance"],
    "T2M": solar_features["temperature"],
    "RH2M": solar_features["relative_humidity"],
    "WS50M": solar_features["wind_speed_50m"],
    "wind_speed": 6.2,
    "power_density": 500,
    "mean_elevation": 260.387452,
    "total_roads": 258238,
    "average_pixel_value": 105.462166
}

        ml_prediction = predict_energy(ml_features)
        


        # ML prediction
        ml_prediction = predict_energy(
            ml_features
        )


        return {
        
            "solar_features": solar_features,
            "wind_result": wind_result,
            "overall_score": overall_score,
            "deployment_plan": deployment_plan,
            "energy_estimation": energy_estimation,
            "ml_energy_prediction": ml_prediction
        }