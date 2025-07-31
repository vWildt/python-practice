# AGENTS.md

## Running checks
1. **Formatting**  
   - Run `black .` before committing.

2. **Linting**  
   - Run `flake8` to catch style issues.

3. **Testing**  
   - If you add tests, run them with `pytest`.  
   - For now, ensure existing scripts still execute (e.g., `python circle_area.py`) after your change.

## Commit messages
- Use short imperative phrases (e.g., “Add fruit selection script”).
- Group changes logically; avoid mixing unrelated updates in one commit.

## Pull requests
- Title: brief summary of the change (e.g., “Add temperature conversion utilities”).
- Body: mention what you changed and how to run any new functionality or tests.
- Run formatting, linting, and tests before opening a PR.

## Coding conventions
- Follow PEP 8 style (indent with 4 spaces, max line length 79).
- Include docstrings for functions and modules.
- Prefer Python 3.10+ features when possible.

## Documentation
- Update `README.md` when you introduce new scripts or change usage instructions.
- Provide simple examples in docstrings if the script requires user input.

