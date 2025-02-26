from pydantic import BaseModel, PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class APIPrefix(BaseModel):
    prefix: str = "/api"
    notes: str = "/notes"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class AccessTokenConfig(BaseModel):
    lifetime_seconds: int = 3600


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
        env_file=".env"
    )

    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()
    db: DataBaseConfig


settings = Settings()
