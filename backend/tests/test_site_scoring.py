from app.services.site_scoring import (
    renewable_resource_score,
    terrain_score,
    infrastructure_score,
    environmental_score,
    economic_score,
    calculate_overall_score,
    rank_candidate_sites,
)


def test_site_scoring():
    # Site 1 (Good site)
    renewable = renewable_resource_score(7.0, 12.0)
    terrain = terrain_score(5.0, 1000.0)
    infrastructure = infrastructure_score(5.0, 10.0)
    environment = environmental_score(85.0)
    economic = economic_score(90.0)

    site1 = calculate_overall_score(
        renewable,
        terrain,
        infrastructure,
        environment,
        economic,
    )

    # Site 2 (Poor site)
    renewable2 = renewable_resource_score(3.0, 4.0)
    terrain2 = terrain_score(30.0, 200.0)
    infrastructure2 = infrastructure_score(40.0, 35.0)
    environment2 = environmental_score(60.0)
    economic2 = economic_score(50.0)

    site2 = calculate_overall_score(
        renewable2,
        terrain2,
        infrastructure2,
        environment2,
        economic2,
    )

    ranked = rank_candidate_sites([
        {"name": "Site 1", **site1},
        {"name": "Site 2", **site2},
    ])

    assert ranked[0]["name"] == "Site 1"
    assert ranked[0]["overall_score"] > ranked[1]["overall_score"]