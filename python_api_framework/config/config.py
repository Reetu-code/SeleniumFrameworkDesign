import configparser
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()


class Config:
    """Centralized configuration loader supporting environment variables and INI configs."""

    def __init__(self, env: str = None):
        self.config_dir = Path(__file__).parent
        self.ini_path = self.config_dir / "env.ini"

        # Determine active environment (CLI arg > env var > default)
        self.env = env or os.getenv("TEST_ENV", "dev").lower()

        self.parser = configparser.ConfigParser()
        if self.ini_path.exists():
            self.parser.read(self.ini_path)
        else:
            raise FileNotFoundError(f"Config file not found at {self.ini_path}")

        if not self.parser.has_section(self.env):
            available = self.parser.sections()
            raise ValueError(f"Environment '{self.env}' not found in config. Available: {available}")

    @property
    def base_url(self) -> str:
        env_url = os.getenv("BASE_URL")
        return env_url if env_url else self.parser.get(self.env, "base_url")

    @property
    def timeout(self) -> int:
        return int(self.parser.get(self.env, "timeout", fallback=10))

    @property
    def api_key(self) -> str:
        return os.getenv("API_KEY", self.parser.get(self.env, "api_key", fallback=""))

    @property
    def default_headers(self) -> dict:
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json",
            "User-Agent": "Python-API-Framework/1.0",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers


# Module-level instance for easy import
config = Config()
