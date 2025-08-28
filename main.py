from Extract.SpotifyandYoutubeExtract import SpotifyandYoutubeExtract
from Clean.SpotifyandYoutubeClean import SpotifyandYoutubeClean
from Config.config import Config


# Extracción de datos
extractor = SpotifyandYoutubeExtract(Config.INPUT_PATH)
extractor.queries()
df = extractor.data


# Mostrar el dataset original completo antes de la limpieza
print("\n--- DATASET ORIGINAL ---\n")
print(df)

# Limpieza de datos
limpieza = SpotifyandYoutubeClean(df)
resultados_nulos_ceros = limpieza.verificar_nulos_ceros()
df_limpio = limpieza.limpiar_columnas()

# Mostrar el DataFrame de nulos y ceros
print("\n--- NULOS Y CEROS POR COLUMNA ---\n")
print(resultados_nulos_ceros)


# Mostrar el dataset limpio completo después de la limpieza
print("\n--- DATASET LIMPIO ---\n")
print(df_limpio)

# Guardar el DataFrame limpio en la ruta de salida configurada
df_limpio.to_csv(Config.OUTPUT_PATH, index=False)

# Mostrar el DataFrame de nulos y ceros del dataset limpio
print("\n--- NULOS Y CEROS EN DATASET LIMPIO ---\n")
resultados_nulos_ceros_limpio = SpotifyandYoutubeClean(df_limpio).verificar_nulos_ceros()
print(resultados_nulos_ceros_limpio)

