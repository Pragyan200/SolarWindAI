from app.services.energy_estimation import estimate_energy


def run_tests():
    sample_sites = [
        {
            "site_result": "Suitable",
            "deployment_type": "Solar",
            "installed_capacity": 10,
            "solar_capacity_factor": 0.20,
        },
        {
            "site_result": "Highly Suitable",
            "deployment_type": "Wind",
            "installed_capacity": 10,
            "wind_capacity_factor": 0.35,
        },
        {
            "site_result": "Excellent",
            "deployment_type": "Hybrid",
            "installed_capacity": 10,
            "solar_capacity_factor": 0.20,
            "wind_capacity_factor": 0.35,
        },
    ]

    for site in sample_sites:
        result = estimate_energy(
            site_result=site["site_result"],
            deployment_type=site["deployment_type"],
            installed_capacity=site["installed_capacity"],
            solar_capacity_factor=site.get("solar_capacity_factor", 0.20),
            wind_capacity_factor=site.get("wind_capacity_factor", 0.35),
        )

        print(result)


if __name__ == "__main__":
    run_tests()