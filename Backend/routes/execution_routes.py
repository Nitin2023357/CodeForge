from fastapi import APIRouter
import subprocess

# Request Models
from models.request_models import (
    UserInput,
    Submission,
    ExampleRun
)

# Shared code execution service
from services.execution.executor import (
    execute_code
)

# Problem and testcase data
from problems import problems
from testcases import testcases

#
from special_judges.registry import (
    SPECIAL_JUDGES
)

from services.execution.cpp_runner import (
    compile_cpp,
    run_cpp_executable,
    cleanup_cpp
)



# Router for all execution-related endpoints
execution_router = APIRouter()



# Run user code against custom input
@execution_router.post("/run")
def run_code(data: UserInput):
    try:
        result = execute_code(
            data.language,
            data.text,
            data.input
        )
        output = result.stdout
        if result.stderr:
            output = result.stderr
        return {
            "output": output
        }
    except subprocess.TimeoutExpired:
        return {
            "output": "Time Limit Exceeded"
        }
    except ValueError as e:
        return {
            "output": str(e)
        }
    


# Run user code against the visible example testcase
@execution_router.post("/run-example")
def run_example(data: ExampleRun):
    try:
        problem = problems[data.problem_id]
        example = problem["examples"][0]
        example_input = example["input"]
        expected_output = example["output"]

        result = execute_code(
            data.language,
            data.text,
            example_input
        )
        if result.stderr:
            if (
                data.language == "cpp"
                and result.returncode != 0
            ):
                return {
                    "verdict": "Compilation Error"
                }
            return {
                "verdict": "Runtime Error"
            }
        
        actual_output = result.stdout.strip()

        if result.stderr:
            return {
                "verdict": "Runtime Error"
            }

        judge = SPECIAL_JUDGES.get(
            data.problem_id
        )
        if judge:
            is_correct = judge(
                actual_output,
                expected_output,
                {
                    "input": example_input,
                    "output": expected_output
                }
            ) 
        else:
            is_correct = (
                actual_output ==
                expected_output.strip()
            )
        if is_correct:
            return {
                "verdict": "Passed",
                "input": example_input,
                "expected": expected_output,
                "actual": actual_output
            }
        return {
            "verdict": "Failed",
            "input": example_input,
            "expected": expected_output,
            "actual": actual_output
        }

    except subprocess.TimeoutExpired:
        return {
            "verdict": "Time Limit Exceeded"
        }
    except ValueError as e:
        return {
            "verdict": str(e)
        }
    


# Submit user solution against hidden testcase set
@execution_router.post("/submit")
def submit_solution(data: Submission):

    # Problem has no testcase configuration
    if (
        data.problem_id not in testcases
        or len(testcases[data.problem_id]) == 0
    ):
        return {
            "verdict": "Problem not configured yet"
        }
    testcase_list = testcases[data.problem_id]
    total_testcases = len(testcase_list)
    passed_testcases = 0

    cpp_path = None
    exe_path = None
    try:
        if data.language == "cpp":
        
            compile_result, cpp_path, exe_path = (
                compile_cpp(data.text)
            )
        
            if compile_result.returncode != 0:
                return {
                    "verdict": "Compilation Error",
                    "passed": 0,
                    "total": total_testcases
                }
        
        # Run solution against every hidden testcase
        for testcase in testcase_list:
            try:
                if data.language == "cpp":
                    result = run_cpp_executable(
                        exe_path,
                        testcase["input"]
                    )
                else:
                    result = execute_code(
                        data.language,
                        data.text,
                        testcase["input"]
                    )
    
                # Runtime Error
                if result.stderr:
                    return {
                        "verdict": "Runtime Error",
                        "passed": passed_testcases,
                        "total": total_testcases
                    }
    
                actual_output = result.stdout.strip()
                expected_output = testcase["output"].strip()
                
                judge = SPECIAL_JUDGES.get(
                    data.problem_id
                )
                
                if judge:
                    is_correct = judge(
                        actual_output,
                        expected_output,
                        testcase
                    ) 
                else:
                    is_correct = (
                        actual_output ==
                        expected_output
                    )
                
                # Wrong Answer
                if not is_correct:
                    return {
                        "verdict": "Wrong Answer",
                        "passed": passed_testcases,
                        "total": total_testcases,
                        "failed_input": testcase["input"],
                        "expected_output": expected_output,
                        "actual_output": actual_output
                    }
    
                passed_testcases += 1
    
            except subprocess.TimeoutExpired:
                return {
                    "verdict": "Time Limit Exceeded",
                    "passed": passed_testcases,
                    "total": total_testcases
                }
            except ValueError as e:
                return {
                    "verdict": str(e)
                }
            
        # All hidden testcases passed
        return {
            "verdict": "Accepted",
            "passed": total_testcases,
            "total": total_testcases
        }
    
    finally:
        if (
            data.language == "cpp"
            and cpp_path is not None
        ):
            cleanup_cpp(
                cpp_path,
                exe_path
            )