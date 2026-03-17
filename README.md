# Python Mentorship Exercises 01

![Python](https://img.shields.io/badge/Python-3.14%2B-blue)
![Mentorship](https://img.shields.io/badge/Mentorship-Squad%20Academy-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Project-green)

This repository contains the first exercise list developed during my Python mentorship journey. The focus of this project is to practice programming fundamentals through small, scenario-based exercises treated with the same care as a real software project.

## Overview

This repository is organized as a study project for the first exercise list of the mentorship.

Main practice areas:

- input handling
- conditional logic
- validation rules
- exception handling
- code organization
- scenario-based testing

## Repository Structure

The exercises are currently stored in the project root for easier access during practice.

- `e01_age_checker.py` to `e13_atm_simulator.py`: exercise implementations
- `tests/`: lightweight test files for selected exercises
- `docs/`: mentoring notes, references, and project documentation
- `main.py`: simple project entry point
- `PROJECT_STRUCTURE.md`: quick guide to the repository layout

## Environment

This project uses `uv` to manage the local environment and run Python commands.

Install dependencies with:

```powershell
uv sync
```

## Running Files

Run the project entry point:

```powershell
uv run python .\main.py
```

Run an individual exercise:

```powershell
uv run python .\e01_age_checker.py
```

Run a test file:

```powershell
uv run python .\tests\age_checker_test.py
```

## Project Notes

This repository follows the idea of treating even exercise lists as structured projects. The goal is not only to solve problems, but also to build good habits around naming, documentation, repository organization, and maintainable code.

## Mentorship Context

This is part of a broader Python mentorship path that includes exercise lists, small applications, APIs, and a final project.

The study path and technical guidance for this phase were provided by [Michel Silva](https://github.com/michelgomessilva).

The naming convention adopted for repositories in this path is:
`python-mentorship-<type>-<theme-or-number>`
