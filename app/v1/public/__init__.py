from fastapi import (
    APIRouter,
)

from app.v1.public.posts import posts

public = APIRouter(prefix="/public")

public.include_router(posts, prefix="/posts")
