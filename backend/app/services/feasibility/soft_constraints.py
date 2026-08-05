class SoftConstraintScorer:
    """
    Scores non-mandatory engineering constraints.
    Higher score = better technical feasibility.
    """

    def calculate_score(self, site_data):
        score = 0
        summary = {}

        # Distance to grid (km)
        distance_to_grid = site_data.get("distance_to_grid", 10)
        if distance_to_grid <= 5:
            score += 40
        elif distance_to_grid <= 10:
            score += 25
        else:
            score += 10
        summary["distance_to_grid"] = distance_to_grid

        # Distance to road (km)
        distance_to_road = site_data.get("distance_to_road", 10)
        if distance_to_road <= 2:
            score += 30
        elif distance_to_road <= 5:
            score += 20
        else:
            score += 10
        summary["distance_to_road"] = distance_to_road

        # Accessibility
        accessibility = site_data.get("accessibility", "medium").lower()
        if accessibility == "high":
            score += 30
        elif accessibility == "medium":
            score += 20
        else:
            score += 10
        summary["accessibility"] = accessibility

        return {
            "feasibility_score": score,
            "summary": summary
        }