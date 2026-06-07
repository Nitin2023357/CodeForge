from services.execution.python_runner import (
    run_python
)

from services.execution.cpp_runner import (
    run_cpp
)


LANGUAGE_RUNNERS = {
    "python": run_python,
    "cpp": run_cpp
}