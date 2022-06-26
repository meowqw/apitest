from fastapi import APIRouter
from apitest import blog

routes = APIRouter()

routes.include_router(blog.router, prefix='/blog')