# api/query.py

import strawberry
from .types.env import Env

@strawberry.type
class Query:
    @strawberry.field(description="Query current environmental data")
    def current_readings() -> Env:
        return Env(
            temperature=25.9,
            humidity=50.1,
            pressure=1013.25,
            co=1286.24,
            nh3=244.79
        )