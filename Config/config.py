class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = 'D:\\SpotifyandYoutube\\Extract\\Files\\Spotify_Youtube.csv'
    OUTPUT_PATH = 'D:\\SpotifyandYoutube\\Extract\\Files\\output_clean.csv'
    SQLITE_DB_PATH = 'Extract/Files/etl_data.db'
    SQLITE_TABLE = 'ride_bookings_clean'
