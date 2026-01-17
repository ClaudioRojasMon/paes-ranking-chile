# Notebooks Jupyter

Esta carpeta contiene los notebooks originales de análisis PAES.

## Notebooks Disponibles

### 1. PAES_2023.ipynb
Análisis de resultados PAES año 2023
- Carga de datos
- Filtrado de egresados
- Cálculo de promedios por RBD
- Generación de ranking
- Consultas interactivas

### 2. PAES_2024.ipynb
Análisis de resultados PAES año 2024
- Misma estructura que 2023
- Datos actualizados

### 3. PAES_2025.ipynb
Análisis de resultados PAES año 2025
- Versión más reciente
- Incluye últimos resultados

### 4. Ranking_Colegios.ipynb
Notebook consolidado con análisis comparativo
- Análisis multi-año
- Comparaciones temporales
- Visualizaciones adicionales

## Cómo Usar los Notebooks

### 1. Instalar Jupyter

```bash
pip install jupyter notebook
```

### 2. Iniciar Jupyter

```bash
jupyter notebook
```

### 3. Navegar

Abre el navegador y ve a `http://localhost:8888`

### 4. Abrir Notebook

Click en cualquiera de los archivos `.ipynb`

## Datos Requeridos

Los notebooks esperan encontrar los archivos CSV en la misma carpeta:

```
notebooks/
  ├── PAES_2023.ipynb
  ├── PAES_2024.ipynb
  ├── PAES_2025.ipynb
  ├── Ranking_Colegios.ipynb
  ├── ArchivoC_Adm2023.csv  ← Debes agregar este
  ├── ArchivoC_Adm2024.csv  ← Debes agregar este
  └── ArchivoC_Adm2025.csv  ← Debes agregar este
```

O puedes modificar las rutas en los notebooks para apuntar a la carpeta `../data/`

## Conversión a Scripts Python

Los notebooks originales fueron la base para crear los módulos en `src/`:

- **PAES_*.ipynb** → **src/paes_analyzer.py**
- Visualizaciones → **src/visualizations.py**
- CLI → **main.py**

## Notas

- Los notebooks son versiones exploratorias originales
- Para análisis en producción, usa los scripts Python en `src/`
- Los notebooks son útiles para:
  - Exploración interactiva de datos
  - Pruebas rápidas
  - Análisis ad-hoc
  - Visualizaciones experimentales

## Ejecutar en Google Colab

También puedes ejecutar estos notebooks en Google Colab:

1. Sube los notebooks a Google Drive
2. Haz click derecho → Abrir con → Google Colaboratory
3. Sube los archivos CSV cuando sea necesario

## Recomendaciones

Para análisis repetitivos o en producción, es mejor usar los scripts Python:

```bash
# En lugar de ejecutar el notebook cada vez:
python main.py --file data/ArchivoC_Adm2025.csv --year 2025 --visualize
```

Esto es más rápido, reproducible y fácil de automatizar.
