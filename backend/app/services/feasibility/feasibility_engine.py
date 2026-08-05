from app.services.feasibility.hard_constraints import HardConstraintValidator
from app.services.feasibility.soft_constraints import SoftConstraintScorer


class FeasibilityEngine:
    """
    Combines hard constraint validation and soft constraint scoring.
    """

    def __init__(self):
        self.hard_validator = HardConstraintValidator()
        self.soft_scorer = SoftConstraintScorer()

    def evaluate(self, site_data):
        # Check hard constraints
        hard_result = self.hard_validator.validate(site_data)

        # If hard constraints fail, reject the site
        if not hard_result["is_feasible"]:
            return {
                "technical_feasibility": False,
                "feasibility_score": 0,
                "constraint_summary": hard_result["failed_constraints"]
            }

        # Calculate soft constraint score
        soft_result = self.soft_scorer.calculate_score(site_data)

        return {
            "technical_feasibility": True,
            "feasibility_score": soft_result["feasibility_score"],
            "constraint_summary": soft_result["summary"]
        }