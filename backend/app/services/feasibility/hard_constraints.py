class HardConstraintValidator:
    """
    Validates mandatory engineering constraints.
    If any constraint fails, the site is not technically feasible.
    """

    def validate(self, site_data):
        failed_constraints = []

        # 1. Restricted land use
        if site_data.get("restricted_land", False):
            failed_constraints.append("Restricted land use")

        # 2. Maximum allowable slope
        if site_data.get("slope", 0) > 30:
            failed_constraints.append("Slope exceeds 30 degrees")

        # 3. Minimum land area
        if site_data.get("land_area", 0) < 1:
            failed_constraints.append("Insufficient land area")

        return {
            "is_feasible": len(failed_constraints) == 0,
            "failed_constraints": failed_constraints
        }