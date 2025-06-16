from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import cat_apis
from app.api.v1 import mission_apis

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Add other allowed origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow only these origins
    allow_credentials=True,
    allow_methods=["*"],    # allow all HTTP methods (GET, POST, etc)
    allow_headers=["*"],    # allow all headers
)

app.include_router(cat_apis.router, prefix="/cats", tags=["Cats"])
app.include_router(mission_apis.router, prefix="/missions", tags=["Missions"])