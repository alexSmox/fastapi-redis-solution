from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    host: str
    port: int
    db: int

    model_config = SettingsConfigDict(
        env_prefix="redis_", env_file=(".env"), extra="allow"
    )
