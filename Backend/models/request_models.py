from pydantic import BaseModel

class UserInput(BaseModel):
    text: str
    language: str
    input: str


class Submission(BaseModel):
    text: str
    language: str
    problem_id: int


class ExampleRun(BaseModel):
    text: str
    language: str
    problem_id: int