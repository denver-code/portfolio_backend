import time
from fastapi import (
    APIRouter,
    Request,
    HTTPException
)
from pydantic import (
    BaseModel,
)
from datetime import datetime
from dotenv import load_dotenv
from app.v1.api.database_api import *


load_dotenv()


class PostModel(BaseModel):
    name: str
    short_description: str
    description: str
    text: str


posts = APIRouter()


@posts.get("/get")
async def posts_get_event():
    post_list = await find_query("posts", {})
    post_list.reverse()
    return {"posts":post_list}

@posts.get("/get/{id}")
async def post_get_event(id: int):
    post = await find_one_query("posts", {"_id":id})
    if post:
        return post

    raise HTTPException(status_code=404, detail="Post not found")

@posts.post("/new")
async def post_create_event(_post: PostModel, request: Request):
    secret_key_header = request.headers.get('secret_key')
    if secret_key_header == os.getenv("secret_key"):
        post_list = await find_query("posts", {})
        e = datetime.now()
        post = {
            "_id": len(post_list) + 1,
            "data": _post.dict(),
            "date": f"{e.day}/{e.month}/{e.year} {time.strftime('%H:%M:%S')}",
            "author": "admin"
        }
        await insert_db("posts", post)
        return post
    return "Not authed."