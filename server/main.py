# server/main.py
################################################
#             Enviro+ Web Backend              #
#               GraphQL FastAPI                #
################################################

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from strawberry.fastapi import GraphQLRouter
from api.schema import schema

app = FastAPI()

# Adjust the origins to match your frontend URL or IP
origins = [
    "http://localhost:8081",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middleware to set Referrer-Policy header
class ReferrerPolicyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Referrer-Policy'] = 'no-referrer'
        return response

app.add_middleware(ReferrerPolicyMiddleware)

graphql_router = GraphQLRouter(schema, path="/", graphql_ide="apollo-sandbox")

app.include_router(graphql_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)