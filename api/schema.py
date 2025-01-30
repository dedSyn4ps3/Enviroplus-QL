# api/schema.py

import strawberry
from .types.env import Env, EnvPlus
from .types.env import get_env_data, get_env_data_plus

@strawberry.type
class Query:
    @strawberry.field(description="Query current environmental data for Standard Enviro HAT")
    async def current_readings(self) -> Env:
        return await get_env_data()
    @strawberry.field(description="Query current environmental data for Enviro+ HAT")
    async def current_readings_plus(self) -> EnvPlus:
        return await get_env_data_plus()

schema = strawberry.Schema(query=Query)