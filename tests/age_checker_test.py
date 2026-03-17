#call: uv run python -m tests.solution_01_test

from e01_age_checker import age_checker

age_checker("ana", "17")
age_checker("bruno", "18")
age_checker("carla", "65")
age_checker("daniel", "66")
age_checker("  elisa  ", "30")
age_checker("fred", 15)
age_checker("gabi", "-16")
age_checker("heitor", "")
age_checker("joão")
age_checker(None, 66)
age_checker()