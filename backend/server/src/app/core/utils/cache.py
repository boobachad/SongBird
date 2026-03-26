from collections.abc import AsyncGenerator

from redis.asyncio import ConnectionPool, Redis

# Populated at startup by lifespan in setup.py
pool: ConnectionPool | None = None
client: Redis | None = None


async def async_get_redis() -> AsyncGenerator[Redis, None]:
    """FastAPI dependency — yields a Redis client per request."""
    r = Redis(connection_pool=pool)
    try:
        yield r
    finally:
        await r.aclose()
