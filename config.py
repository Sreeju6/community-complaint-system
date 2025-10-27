import os
from dotenv import load_dotenv

# Load .env for local testing
load_dotenv()

class Config:
    # Secret key for forms & sessions
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # -------------------------------
    # DATABASE CONFIGURATION
    # -------------------------------
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        # Ensure correct SQLAlchemy driver format
        if database_url.startswith("mysql://"):
            database_url = database_url.replace("mysql://", "mysql+pymysql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Local fallback (SQLite)
        SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -------------------------------
    # FILE UPLOAD CONFIGURATION
    # -------------------------------
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "app", "static", "uploads")

    # -------------------------------
    # GOOGLE MAPS API KEY (Optional)
    # -------------------------------
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")
