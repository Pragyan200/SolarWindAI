from app.services.deployment_optimization import generate_deployment_plan


def test_sites():

    sites = [
        {
            "name": "Solar Rich Site",
            "site_score": 85,
            "solar_score": 90,
            "wind_score": 50,
            "land_area": 100,
            "available_land": 60
        },
        {
            "name": "Wind Rich Site",
            "site_score": 80,
            "solar_score": 55,
            "wind_score": 90,
            "land_area": 70,
            "available_land": 10
        },
        {
            "name": "Hybrid Site",
            "site_score": 90,
            "solar_score": 85,
            "wind_score": 85,
            "land_area": 150,
            "available_land": 80
        }
    ]

    for site in sites:
        plan = generate_deployment_plan(
            site["site_score"],
            site["solar_score"],
            site["wind_score"],
            site["land_area"],
            site["available_land"]
        )

        print(site["name"])
        print(plan)
        print("----------------")


test_sites()