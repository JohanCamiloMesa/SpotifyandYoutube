# 🎶 Spotify and Youtube 🎶 Data Analysis Project

Este proyecto realiza un proceso ETL (Extract, Transform, Load) sobre datos que relacionan métricas de Spotify y YouTube.

## Estructura del Proyecto

```
SpotifyandYoutube/
│
├── Clean/
│   ├── __init__.py
│   └── SpotifyandYoutubeClean.py           # Gestiona la limpieza de datos, eliminando nulos y reemplazandolos
│
├── Config/
│   ├── __init__.py
│   └── config.py                           # Funcion en donde se llama el dataset y se guarda
│
├── Extract/
│   ├── Files/
│   │   ├── Spotify_Youtube.csv             # Dataset original con datos sin procesar
│   │   └── output_clean.csv                # Dataset resultante después de la limpieza
│   ├── __init__.py
│   └── SpotifyandYoutubeExtract.py         # Maneja la extracción y carga inicial del dataset desde CSV
│
├── main.py                                 # Coordina todo el proceso ETL y muestra resultados
├── README.md                               # Documentación del proyecto
├── requirements.txt                        # Lista de dependencias y librerías necesarias
└── .gitignore                              # Especifica archivos y carpetas ignorados por Git
```

## Requisitos
- Python 3.x
- Pandas

## 🔗 Dataset

El dataset que se utilizo en este proyecto fue creado por Marco Sallustio, Marco Guarisco y Salvatore Rastelli, esta disponible en Kaggle:

**[Spotify and Youtube](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube)**

## 📁 Explicación Detallada por Carpetas

### 1️⃣ Extract/ 
Encargada de la extracción inicial de datos
```python
class SpotifyandYoutubeExtract:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
    
    def queries(self):
        # Lee el archivo CSV y lo carga en self.data
        self.data = pd.read_csv(self.filepath)
```
- **Función**: Carga inicial del dataset desde el CSV

- **Archivos**:

  - `Spotify_Youtube.csv`: Dataset original

  - `output_clean.csv`: Resultado del proceso de limpieza

### 2️⃣ Clean/
Maneja la limpieza y transformación de datos
```python
class SpotifyandYoutubeClean:
    def __init__(self, df):
        self.df = df
    
    def verificar_nulos_ceros(self):
        # Analiza valores nulos y ceros
        return resultados
    
    def limpiar_columnas(self):
        # Procesa y limpia el DataFrame
        return df_limpio
```
- **Función**: Elimina valores nulos, transforma datos incorrectos

- **Métodos principales**:

  - `verificar_nulos_ceros()`: Detecta valores problemáticos

  - `limpiar_columnas()`: Aplica transformaciones

### 3️⃣ Config/
Gestiona la configuración del proyecto
```python
class Config:
    INPUT_PATH = 'D:\\SpotifyandYoutube\\Extract\\Files\\Spotify_Youtube.csv'
    OUTPUT_PATH = 'D:\\SpotifyandYoutube\\Extract\\Files\\output_clean.csv'
```
- **Función**: Centraliza rutas de archivos

- **Variables**:

  - `INPUT_PATH`: Ruta del dataset original

  - `OUTPUT_PATH`: Ruta donde se guarda el resultado

### 🔄 Flujo de Trabajo

1️⃣ **Extracción** (`Extract/`)

   - Lee el archivo CSV original
   - Carga datos en memoria

2️⃣ **Limpieza** (`Clean/`)

   - Identifica valores nulos/ceros
   - Aplica transformaciones
   - Genera dataset limpio

3️⃣ **Configuración** (`Config/`)

   - Provee rutas de archivos
   - Facilita mantenimiento

4️⃣ **Coordinación** (`main.py`)
   ```python
   # Extracción
   extractor = SpotifyandYoutubeExtract(Config.INPUT_PATH)
   df = extractor.queries()

   # Limpieza
   limpieza = SpotifyandYoutubeClean(df)
   df_limpio = limpieza.limpiar_columnas()

   # Guardado
   df_limpio.to_csv(Config.OUTPUT_PATH)
   ```

## 🔧 Detalles Técnicos
- Cada carpeta tiene su `__init__.py` para funcionar como módulo Python
- Los resultados intermedios se almacenan en DataFrames de pandas
- La configuración centralizada permite cambiar rutas fácilmente

## Uso

1. Asegúrate de tener los archivos de datos en la carpeta `Extract/Files/`
2. Ejecuta el script principal:
```bash
python main.py
```
3. El resultado se guardará en `Extract/Files/output_clean.csv`

## Resultados
El proceso genera:
- Visualización del dataset original
- Reporte de valores nulos y ceros por columna
- Dataset limpio
- Reporte final de valores nulos y ceros en el dataset procesado

## Notas
El proyecto está configurado para trabajar con rutas Windows. Ajusta las rutas en `config.py` según tu sistema operativo si es necesario.