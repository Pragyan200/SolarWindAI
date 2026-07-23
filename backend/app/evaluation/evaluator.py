from app.evaluation.constraints import (
    check_slope,
    check_solar_irradiance,
    check_wind_speed,
    check_grid_distance,
    check_road_distance,
)
from app.evaluation.scorer import compute_score
from app.evaluation.recommendation import get_recommendation


class EvaluationService:
    """
    Orchestrates the complete suitability evaluation workflow.

    Workflow:
        Input Features
              │
              ▼
        Constraint Check
              │
              ▼
        Weighted Score
              │
              ▼
        Recommendation
              │
              ▼
        Evaluation Result
    """

    def evaluate(self, features: dict) -> dict:
        constraints = {
            "slope": check_slope(features.get("slope", 0)),
            "solar": check_solar_irradiance(features.get("solar", 0)),
            "wind": check_wind_speed(features.get("wind", 0)),
            "grid_distance": check_grid_distance(features.get("grid_distance", 0)),
            "road_distance": check_road_distance(features.get("road_distance", 0)),
        }

        failed_constraints = [
            name for name, passed in constraints.items() if not passed
        ]

        score = compute_score(features)
        recommendation = get_recommendation(score)

        return {
            "constraint_status": constraints,
            "overall_score": score,
            "recommendation": recommendation,
            "failed_constraints": failed_constraints,
        }