"""
Application settings loaded from environment / .env file.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── Supabase ──────────────────────────────────────
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""  # anon/public key
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    SUPABASE_JWT_SECRET: str = ""  # Settings → API → JWT Secret

    # ── App ───────────────────────────────────────────
    APP_ENV: str = "development"
    DEBUG: bool = True
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    # ── External Services ─────────────────────────────
    GOOGLE_MAPS_API_KEY: str = ""
    RAZORPAY_KEY_ID: str = ""
    RAZORPAY_KEY_SECRET: str = ""

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


settings = Settings()
