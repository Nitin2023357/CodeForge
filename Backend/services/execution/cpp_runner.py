import tempfile
import os
import subprocess


def compile_cpp(code):

    cpp_file = tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".cpp",
        delete=False
    )

    cpp_file.write(code)
    cpp_file.close()

    cpp_path = cpp_file.name

    exe_path = cpp_path.replace(
        ".cpp",
        ""
    )

    compile_result = subprocess.run(
        [
            "g++",
            cpp_path,
            "-o",
            exe_path
        ],
        capture_output=True,
        text=True
    )

    return (
        compile_result,
        cpp_path,
        exe_path
    )


def run_cpp_executable(
    exe_path,
    input_data
):

    result = subprocess.run(
        [exe_path],
        input=input_data,
        capture_output=True,
        text=True,
        timeout=2
    )

    return result


def cleanup_cpp(
    cpp_path,
    exe_path
):

    if cpp_path and os.path.exists(cpp_path):
        os.remove(cpp_path)

    if exe_path and os.path.exists(exe_path):
        os.remove(exe_path)


def run_cpp(
    code,
    input_data
):

    cpp_path = None
    exe_path = None

    try:

        (
            compile_result,
            cpp_path,
            exe_path
        ) = compile_cpp(code)

        if compile_result.returncode != 0:
            return compile_result

        return run_cpp_executable(
            exe_path,
            input_data
        )

    finally:

        cleanup_cpp(
            cpp_path,
            exe_path
        )