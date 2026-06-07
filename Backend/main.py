# imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.problem_routes import problem_router
from routes.execution_routes import execution_router


# FastAPI App
app = FastAPI()


# Allowed FrontEnd Origin
origins = [
    "http://localhost:5173"
]


# MiddleWare
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Route Registration
app.include_router(problem_router)
app.include_router(execution_router)



# Health Check Endpoint
@app.get("/")
def home():
    return {"message": "CodeForge Backend Running"}

