from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()  # Carga .env desde aquí también si quieres que funcione en pruebas unitarias

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Validación por si acaso
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar definidos en el archivo .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)