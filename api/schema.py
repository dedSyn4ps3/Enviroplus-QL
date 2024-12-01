# api/schema.py

import strawberry
from .types.env import Env
from .types.env import get_env_data

@strawberry.type
class Query:
    @strawberry.field(description="Query current environmental data")
    async def current_readings(self) -> Env:
        return await get_env_data()

schema = strawberry.Schema(query=Query)