from typing import Self
from pathlib import Path

from pydantic import HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    app_url: HttpUrl
    headless: bool
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    expect_timeout: float
    width: int
    height: int

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = Path("./videos")
        tracing_dir = Path("./tracing")

        videos_dir.mkdir(parents=True, exist_ok=True)
        tracing_dir.mkdir(parents=True, exist_ok=True)

        return cls(
            videos_dir=str(videos_dir),
            tracing_dir=str(tracing_dir),
            width = 1920,
            height = 1080
        )