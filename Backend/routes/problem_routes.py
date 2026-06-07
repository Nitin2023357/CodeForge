from fastapi import APIRouter
from problems import problems

problem_router = APIRouter()


@problem_router.get("/problem/{problem_id}")
def get_problem(problem_id: int):
    return problems[problem_id]