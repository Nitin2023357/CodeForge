from services.execution.language_registry import (
    LANGUAGE_RUNNERS
)


def execute_code(
    language,
    code,
    input_data
):

    runner = LANGUAGE_RUNNERS.get(
        language
    )

    if not runner:
        raise ValueError(
            f"Unsupported language: {language}"
        )

    return runner(
        code,
        input_data
    )