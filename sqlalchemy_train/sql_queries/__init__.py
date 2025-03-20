__all__ = (
    "engine",
    "Base"
)

from pathlib import Path
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


BASE_DIR = Path(__file__).parent.parent.parent
ENV_PATH = Path(BASE_DIR / ".env")

load_dotenv(ENV_PATH)

engine = create_engine(
    url=os.getenv("SQLA_URL", Path(BASE_DIR / "sqlite3.db")),
    echo=True,
    echo_pool=True,
)

Base = declarative_base()
