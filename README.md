# LearningModels

This project contains various machine learning models and algorithms implemented in Python. It aims to provide a clear and modular structure for research and development.

## Setup

To set up the project, ensure you have `uv` installed. If not, you can install it using:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, navigate to the project root and create a virtual environment:

```bash
vx venv
source .venv/bin/activate
```

Install the dependencies:

```bash
uv pip install -e .
```

## Project Structure

- `src/`: Contains all the source code, organized into subdirectories for different models and algorithms.
- `tests/`: Contains unit and integration tests for the project.
- `pyproject.toml`: Project metadata and dependency management using Poetry.
- `requirements.txt` and `requirements-dev.txt`: Legacy dependency files, now managed by Poetry.

## Running Tests

To run tests, activate the virtual environment and use `pytest`:

```bash
source .venv/bin/activate
pytest
```

## Code Style and Linting

This project uses `ruff` for linting and `black` for code formatting. These are configured in `pyproject.toml`.

To run linting and formatting checks:

```bash
source .venv/bin/activate
ruff check src/
ruff format src/
```

## Contributing

Contributions are welcome! Please ensure your code adheres to the established style guidelines and passes all tests.
