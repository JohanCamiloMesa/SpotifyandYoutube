from pathlib import Path

class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    BASE_DIR = Path(__file__).parent.parent
    INPUT_PATH = BASE_DIR / 'Extract' / 'Files' / 'Spotify_Youtube.csv'
    OUTPUT_PATH = BASE_DIR / 'Extract' / 'Files' / 'output_clean.csv'
    SQLITE_DB_PATH = BASE_DIR / 'Extract' / 'Files' / 'spotify_youtube.db'
    SQLITE_TABLE = 'spotify_youtube_data'