from fastapi import (
    FastAPI,
    Depends
)
from fastapi.middleware.cors import CORSMiddleware

import app.v1 as v1

app = FastAPI(title="FastAPICore", debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     pass

app.include_router(v1.api, prefix="/api")