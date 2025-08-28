
import pandas as pd
import numpy as np

class SpotifyandYoutubeClean:
    def __init__(self, df):
        self.df = df

    def verificar_nulos_ceros(self):
        nulos = self.df.isnull().sum()
        ceros = (self.df == 0).sum()
        resultados = pd.DataFrame({'Nulos': nulos, 'Ceros': ceros})
        return resultados

    def limpiar_columnas(self):
        # Calcular la mediana de 'Danceability' y reemplazar nulos
        if 'Danceability' in self.df.columns:
            mediana_Danceability = self.df['Danceability'].median()
            self.df['Danceability'] = self.df['Danceability'].fillna(mediana_Danceability)
        
        # Calcular la mediana de 'Energy' y reemplazar nulos

        if 'Energy' in self.df.columns:
            mediana_Energy = self.df['Energy'].median()
            self.df['Energy'] = self.df['Energy'].fillna(mediana_Energy)

        # Calcular la mediana de 'Key' y reemplazar nulos

        if 'Key' in self.df.columns:
            mediana_Key = self.df['Key'].median()
            self.df['Key'] = self.df['Key'].fillna(mediana_Key)
        
        # Calcular la mediana de 'Loudness' y reemplazar nulos

        if 'Loudness' in self.df.columns:
            mediana_Loudness = self.df['Loudness'].median()
            self.df['Loudness'] = self.df['Loudness'].fillna(mediana_Loudness)

        # Calcular la mediana de 'Speechiness' y reemplazar nulos

        if 'Speechiness' in self.df.columns:
            mediana_Speechiness = self.df['Speechiness'].median()
            self.df['Speechiness'] = self.df['Speechiness'].fillna(mediana_Speechiness)

        # Calcular la mediana de 'Acousticness' y reemplazar nulos

        if 'Acousticness' in self.df.columns:
            mediana_Acousticness = self.df['Acousticness'].median()
            self.df['Acousticness'] = self.df['Acousticness'].fillna(mediana_Acousticness)

        # Calcular la mediana de 'Instrumentalness' y reemplazar nulos

        if 'Instrumentalness' in self.df.columns:
            mediana_Instrumentalness = self.df['Instrumentalness'].median()
            self.df['Instrumentalness'] = self.df['Instrumentalness'].fillna(mediana_Instrumentalness)

        # Calcular la mediana de 'Liveness' y reemplazar nulos

        if 'Liveness' in self.df.columns:
            mediana_Liveness = self.df['Liveness'].median()
            self.df['Liveness'] = self.df['Liveness'].fillna(mediana_Liveness)

        # Calcular la mediana de 'Valence' y reemplazar nulos

        if 'Valence' in self.df.columns:
            mediana_Valence = self.df['Valence'].median()
            self.df['Valence'] = self.df['Valence'].fillna(mediana_Valence)

        # Calcular la mediana de 'Tempo' y reemplazar nulos

        if 'Tempo' in self.df.columns:
            mediana_Tempo = self.df['Tempo'].median()
            self.df['Tempo'] = self.df['Tempo'].fillna(mediana_Tempo)

        # Calcular la mediana de 'Duration_ms' y reemplazar nulos

        if 'Duration_ms' in self.df.columns:    
            mediana_Duration_ms = self.df['Duration_ms'].median()
            self.df['Duration_ms'] = self.df['Duration_ms'].fillna(mediana_Duration_ms)

        # Calcular la mediana de 'Views' y reemplazar nulos

        if 'Views' in self.df.columns:
            mediana_views = self.df['Views'].median()
            self.df['Views'] = self.df['Views'].fillna(mediana_views)
        
        # Calcular la mediana de 'Likes' y reemplazar nulos

        if 'Likes' in self.df.columns:
            mediana_Likes = self.df['Likes'].median()
            self.df['Likes'] = self.df['Likes'].fillna(mediana_Likes)

        # Calcular la mediana de 'Comments' y reemplazar nulos

        if 'Comments' in self.df.columns:
            mediana_Comments = self.df['Comments'].median()
            self.df['Comments'] = self.df['Comments'].fillna(mediana_Comments)

        # Calcular la mediana de 'Stream' y reemplazar nulos

        if 'Stream' in self.df.columns:
            mediana_Stream = self.df['Stream'].median()
            self.df['Stream'] = self.df['Stream'].fillna(mediana_Stream)

        # Reemplazar valores nulos o vacíos en 'Url_spotify' con el mensaje "No disponible / No existe"

        if 'Url_spotify' in self.df.columns:
            self.df['Url_spotify'] = self.df['Url_spotify'].fillna("No disponible / No existe").replace("", "No disponible / No existe")

        # Reemplazar valores nulos o vacíos en 'Url_youtube' con el mensaje "No disponible / No existe"

        if 'Url_youtube' in self.df.columns:
            self.df['Url_youtube'] = self.df['Url_youtube'].fillna("No disponible / No existe").replace("", "No disponible / No existe")

        # Reemplazar valores nulos o vacíos en 'Title' con el mensaje "No disponible / No existe"

        if 'Title' in self.df.columns:
            self.df['Title'] = self.df['Title'].fillna("No disponible / No existe").replace("", "No disponible / No existe")

        # Reemplazar valores nulos o vacíos en 'Channel' con el mensaje "No disponible / No existe"

        if 'Channel' in self.df.columns:
            self.df['Channel'] = self.df['Channel'].fillna("No disponible / No existe").replace("", "No disponible / No existe")

        # Reemplazar valores nulos o vacíos en 'Description' con el mensaje "No disponible / No existe"

        if 'Description' in self.df.columns:
            self.df['Description'] = self.df['Description'].fillna("No disponible / No existe").replace("", "No disponible / No existe")

        # Calcular la moda para 'License' y reemplazar

        if 'Licensed' in self.df.columns:
            moda_license = self.df['Licensed'].mode()[0]  # Toma el primer valor de la moda
            self.df['Licensed'] = self.df['Licensed'].fillna(moda_license).replace(0, moda_license)
            self.df['Licensed'] = self.df['Licensed'].infer_objects(copy=False)

        # Calcular la moda para 'official_video'

        if 'official_video' in self.df.columns:
            moda_official_video = self.df['official_video'].mode()[0]  # Toma el primer valor de la moda
            self.df['official_video'] = self.df['official_video'].fillna(moda_official_video).replace(0, moda_official_video)
            self.df['official_video'] = self.df['official_video'].infer_objects(copy=False)
        return self.df
