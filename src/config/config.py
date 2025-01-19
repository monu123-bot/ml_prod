from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from loguru import logger
from sqlalchemy import create_engine


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="config/.env", env_file_encoding="utf-8")

    model_path: DirectoryPath
    model_name: str
    log_level: str
    db_conn_str: str
    table_name: str


session = Settings()
logger.remove()
logger.add(
    "./logs/app.log",
    rotation="1 day",
    retention="2 days",
    compression="zip",
    level=session.log_level,
)
engine = create_engine(session.db_conn_str)
