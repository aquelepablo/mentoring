# call: uv run python -m tests.solution_02_test

from solving_problems.e02_discount_calculator import discount_calc

print("--- INICIO TESTES ---") 

discount_calc("ana", 1, 100, "sim")
discount_calc("bruno", 5, 100, "nao")
discount_calc("carla", 2, 100, "nao")
discount_calc("daniel", 2, 99.99, "nao")
discount_calc("  elisa  ", 3, 100, "nao")
discount_calc("fabio", 1, 300, "Sim")
discount_calc("gabi", 1, 300, "não")
discount_calc("", 1, 100, "sim")
discount_calc("heitor", "", 100, "sim")
discount_calc("igor", 1, "", "sim")
discount_calc("joao", 1, 100, "")
discount_calc("karla", "abc", 100, "sim")
discount_calc("leo", 0, 100, "sim")
discount_calc("maria", -5, 100, "sim")
discount_calc("nina", 1, "abc", "sim")
discount_calc("otavio", 1, 0, "sim")
discount_calc("paula", 1, -10, "sim")
discount_calc("quiteria", 1, 100, "talvez")
discount_calc(None, 1, 100, "sim")
discount_calc("rafael", None, 100, "sim")
discount_calc("sara", 1, None, "sim")
discount_calc("tiago", 1, 100, None)

print("\nTeste com input manual:\n")
discount_calc(None, None, None, None, ask_for_input=True)
