import tempfile
import os
import sys
import subprocess


def execute_python(code, input_data):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False
    ) as temp_file:

        temp_file.write(code)

        temp_path = temp_file.name

    try:

        result = subprocess.run(
            [sys.executable, temp_path],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=2
        )

        return result

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)