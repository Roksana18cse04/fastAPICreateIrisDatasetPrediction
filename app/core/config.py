from pathlib import Path
from pydantic_settings import BaseSettings

# Get base directory using pathlib for cross-platform compatibility
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Iris Prediction API"
    MODEL_PATH: Path = BASE_DIR / "models" / "classifier.pkl"
    SCALER_PATH: Path = BASE_DIR / "models" / "scaler.pkl"

    class Config:
        case_sensitive = True

settings = Settings()