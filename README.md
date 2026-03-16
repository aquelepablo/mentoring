# Python Mentoring Exercises

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Mentoring](https://img.shields.io/badge/Mentoring-Squad%20Academy-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Project-green)

This repository gathers Python exercises developed during mentoring sessions, with emphasis on programming logic, input validation, conditional flows, and scenario-based testing.

## Project Overview

The exercises in this repository are designed to reinforce core Python concepts through small practical problems and iterative improvements.

Main areas of practice:

- string handling
- input validation
- conditional logic
- exception handling
- code organization
- simple test design

## Project Structure

- `solving_problems/`: exercise implementations
- `tests/`: scenario-based test files
- `docs/`: mentoring notes, references, and feedback materials
- `main.py`: local entry point for experiments

## Prerequisites

This project uses `uv` to manage the environment and run Python commands.

Install project dependencies with:

```powershell
uv sync
```

## Running the Exercises

Run a solution file:

```powershell
uv run python .\solving_problems\solution_01.py
```

Run a test file:

```powershell
uv run python -m tests.solution_01_test
uv run python -m tests.solution_02_test
```

## Notes

The tests in this repository are intentionally lightweight. Their purpose is to explore different input scenarios, expose edge cases, and help identify bugs during the learning process.

## Mentoring Context

This is a study repository used as part of Python mentoring practice and exercise review.

The mentoring process for this repository has been guided by [Michel Silva](https://github.com/michelgomessilva/).
