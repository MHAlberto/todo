from dotenv import load_dotenv
import os
from pathlib import Path

# Carga el .env desde el directorio raíz
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Accede a las variables
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no definida en el archivo .env")

