# 🎓 Ranking PAES Chile - Análisis de Resultados

Sistema completo de análisis y ranking de resultados de la **Prueba de Acceso a la Educación Superior (PAES)** en Chile. Este proyecto permite procesar, analizar y visualizar los datos de rendimiento de establecimientos educacionales a nivel nacional.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Instalación](#-instalación)
- [Obtener los Datos](#-obtener-los-datos)
- [Uso Rápido](#-uso-rápido)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Ejemplos](#-ejemplos)
- [Documentación](#-documentación)
- [Contribuir](#-contribuir)
- [Créditos](#-créditos-y-agradecimientos)
- [Licencia](#-licencia)

## ✨ Características

- **Procesamiento de Datos**: Carga y limpieza automática de datos PAES
- **Ranking Nacional**: Generación de rankings basados en promedio de Comprensión Lectora y Matemática 1
- **Análisis Estadístico**: Estadísticas descriptivas completas por año y región
- **Comparación Temporal**: Comparación de rendimiento entre diferentes años
- **Visualizaciones**: Gráficos profesionales y dashboards interactivos
- **Consultas por RBD**: Búsqueda de posición específica de cualquier establecimiento
- **Exportación Múltiple**: Resultados en CSV, Excel y JSON
- **Análisis Regional**: Comparaciones por región y comuna

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación desde GitHub

```bash
# Clonar el repositorio
git clone https://github.com/ClaudioRojasMon/paes-ranking-chile.git
cd paes-ranking-chile

# Instalar dependencias
pip install -r requirements.txt
```

### Instalación Manual

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install pandas numpy matplotlib seaborn openpyxl
```

## 📊 Obtener los Datos

**IMPORTANTE:** Los archivos CSV con datos PAES NO están incluidos en este repositorio por su tamaño y porque son datos públicos que se actualizan periódicamente.

### Descargar los Datos

1. **Fuente oficial:** [DEMRE - Bases de Datos](https://demre.cl)
2. Busca la sección de "Bases de datos" o "Archivos de rendición"
3. Descarga los archivos para los años que necesites:
   - `ArchivoC_Adm2023.csv`
   - `ArchivoC_Adm2024.csv`
   - `ArchivoC_Adm2025.csv`
4. Colócalos en la carpeta `data/` del proyecto:
   ```
   paes-ranking-chile/
   └── data/
       ├── ArchivoC_Adm2023.csv  ← Aquí
       ├── ArchivoC_Adm2024.csv  ← Aquí
       └── ArchivoC_Adm2025.csv  ← Aquí
   ```

### Formato Esperado

Los archivos deben:
- Estar en formato CSV con separador `;` (punto y coma)
- Incluir las columnas: `RBD`, `SITUACION_EGRESO`, `CLEC_REG_ACTUAL`, `MATE1_REG_ACTUAL`
- Tener encoding UTF-8 o Latin-1

## 🎯 Uso Rápido

### Análisis Básico

```bash
# Análisis simple de un año
python main.py --file data/ArchivoC_Adm2025.csv --year 2025

# Análisis con visualizaciones
python main.py --file data/ArchivoC_Adm2025.csv --year 2025 --visualize

# Consultar un establecimiento específico
python main.py --file data/ArchivoC_Adm2025.csv --year 2025 --rbd 8609
```

### Comparación entre Años

```bash
# Comparar 2024 vs 2025
python main.py \
  --file data/ArchivoC_Adm2025.csv \
  --year 2025 \
  --compare data/ArchivoC_Adm2024.csv,2024 \
  --visualize
```

### Ejemplo en Python

```python
from src.paes_analyzer import PAESAnalyzer
from src.visualizations import PAESVisualizer

# Crear analizador
analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)

# Procesar datos
analyzer.load_data()
analyzer.filter_graduates()
ranking = analyzer.create_ranking()

# Obtener estadísticas
stats = analyzer.get_statistics()
print(f"Promedio Nacional: {stats['promedio_nacional']}")

# Top 10 establecimientos
top10 = analyzer.get_top_schools(10)
print(top10)

# Consultar un colegio específico
result = analyzer.get_school_position(8609)
print(f"Ranking: #{result['rank']}")
print(f"Promedio: {result['paes_promedio']}")

# Generar visualizaciones
visualizer = PAESVisualizer()
visualizer.create_summary_dashboard(ranking, 2025, 'dashboard.png')
```

## 📁 Estructura del Proyecto

```
paes-ranking-chile/
│
├── data/                          # Datos PAES (no incluidos en repo)
│   ├── ArchivoC_Adm2023.csv
│   ├── ArchivoC_Adm2024.csv
│   └── ArchivoC_Adm2025.csv
│
├── src/                           # Código fuente
│   ├── __init__.py
│   ├── paes_analyzer.py          # Clase principal de análisis
│   └── visualizations.py         # Generación de gráficos
│
├── notebooks/                     # Jupyter notebooks exploratorios
│   ├── PAES_2023.ipynb
│   ├── PAES_2024.ipynb
│   └── PAES_2025.ipynb
│
├── outputs/                       # Resultados generados
│   ├── rankings/                 # Rankings en CSV/Excel
│   ├── visualizations/           # Gráficos y dashboards
│   └── statistics/               # Estadísticas en JSON
│
├── docs/                          # Documentación adicional
│   ├── metodologia.md            # Metodología de cálculo
│   └── diccionario_datos.md      # Diccionario de variables
│
├── main.py                        # Script principal
├── requirements.txt               # Dependencias
├── .gitignore                    # Archivos ignorados por git
└── README.md                      # Este archivo
```

## 📊 Ejemplos

### 1. Generar Ranking Completo

```python
from src.paes_analyzer import PAESAnalyzer

analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
analyzer.load_data()
ranking = analyzer.create_ranking()

# Exportar
analyzer.export_ranking('outputs/ranking_2025.csv')
analyzer.export_ranking('outputs/ranking_2025.xlsx', format='excel')
```

### 2. Análisis Regional

```python
# Filtrar por región
region_13 = ranking[ranking['CODIGO_REGION'] == 13]
print(f"Establecimientos en RM: {len(region_13)}")
print(f"Promedio regional: {region_13['PAES_PROMEDIO'].mean():.2f}")
```

### 3. Comparar Dos Años

```python
analyzer_2024 = PAESAnalyzer('data/ArchivoC_Adm2024.csv', 2024)
analyzer_2025 = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)

analyzer_2024.load_data()
analyzer_2025.load_data()

ranking_2024 = analyzer_2024.create_ranking()
ranking_2025 = analyzer_2025.create_ranking()

# Comparar un colegio específico
comparison = analyzer_2025.compare_years(analyzer_2024, rbd=8609)
print(comparison)
```

### 4. Visualización Dashboard

```python
from src.visualizations import PAESVisualizer

visualizer = PAESVisualizer()

# Dashboard completo
visualizer.create_summary_dashboard(
    ranking, 
    year=2025,
    save_path='outputs/dashboard_2025.png'
)

# Top 20 colegios
visualizer.plot_top_schools(
    ranking, 
    n=20,
    save_path='outputs/top_20_2025.png'
)

# Distribución de puntajes
visualizer.plot_score_distribution(
    ranking,
    save_path='outputs/distribucion_2025.png'
)
```

## 📖 Documentación

### Clase PAESAnalyzer

#### Métodos Principales

| Método | Descripción |
|--------|-------------|
| `load_data()` | Carga datos desde archivo CSV |
| `filter_graduates()` | Filtra estudiantes egresados regulares |
| `calculate_school_averages()` | Calcula promedios por establecimiento |
| `create_ranking()` | Genera ranking nacional |
| `get_school_position(rbd)` | Consulta posición de un colegio |
| `get_top_schools(n)` | Obtiene top N establecimientos |
| `get_statistics()` | Calcula estadísticas generales |
| `export_ranking(path, format)` | Exporta ranking a archivo |

### Clase PAESVisualizer

#### Métodos de Visualización

| Método | Descripción |
|--------|-------------|
| `plot_top_schools()` | Gráfico de mejores colegios |
| `plot_score_distribution()` | Distribución de puntajes |
| `plot_year_comparison()` | Comparación entre años |
| `plot_regional_comparison()` | Comparación regional |
| `create_summary_dashboard()` | Dashboard completo |

### Variables Principales

- **RBD**: Código único del establecimiento educacional
- **CLEC_REG_ACTUAL**: Puntaje Comprensión Lectora
- **MATE1_REG_ACTUAL**: Puntaje Matemática 1
- **PAES_PROMEDIO**: Promedio entre CLEC y MATE1
- **SITUACION_EGRESO**: Estado de egreso (1 = regular)
- **CODIGO_REGION**: Código de región
- **CODIGO_COMUNA**: Código de comuna

## 🎨 Personalización

### Modificar Cálculo del Ranking

```python
# En paes_analyzer.py, método create_ranking()
# Puedes modificar qué pruebas incluir:

paes_columns = ['CLEC_REG_ACTUAL', 'MATE1_REG_ACTUAL', 'HCSOC_REG_ACTUAL']
# Esto incluiría también Historia
```

### Cambiar Estilo de Gráficos

```python
# En visualizations.py
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Cambiar estilo
sns.set_palette("Set2")  # Cambiar paleta de colores
```

## 🔧 Solución de Problemas

### Error: "File not found"
```bash
# Asegúrate de que el archivo existe y la ruta es correcta
ls data/ArchivoC_Adm2025.csv
```

### Error: "Module not found"
```bash
# Reinstala las dependencias
pip install -r requirements.txt --force-reinstall
```

### Advertencia: "DtypeWarning"
```python
# Es normal, el código ya maneja esto con low_memory=False
```

## 📈 Métricas del Proyecto

- **Líneas de Código**: ~1,000+
- **Cobertura de Tests**: En desarrollo
- **Establecimientos Analizados**: ~3,300 por año
- **Estudiantes Procesados**: ~200,000+ por año

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guía de Estilo

- Usar `black` para formateo de código
- Documentar funciones con docstrings
- Agregar type hints cuando sea posible
- Escribir tests para nuevas funcionalidades

## 📝 Notas

- Los datos PAES son de acceso público y se pueden obtener desde el sitio oficial del DEMRE
- Este proyecto es con fines educativos y de investigación
- Los rankings se basan únicamente en el promedio de Comprensión Lectora y Matemática 1
- No se incluyen los archivos CSV de datos por su tamaño (debes obtenerlos por separado)

## 📊 Fuentes de Datos

- **DEMRE** (Departamento de Evaluación, Medición y Registro Educacional)
- **Ministerio de Educación de Chile**
- Datos disponibles en: [Datos Abiertos](https://datosabiertos.mineduc.cl)

## 🙏 Créditos y Agradecimientos

### Autor Principal
**Claudio Rojas** - Análisis inicial, notebooks exploratorios y conceptualización
- GitHub: [@ClaudioRojasMon](https://github.com/ClaudioRojasMon)

### Desarrollo
Este proyecto fue desarrollado mediante colaboración humano-IA:
- **Análisis y notebooks originales:** Claudio Rojas
- **Transformación a proyecto profesional:** Asistencia de Claude (Anthropic)

Para más detalles sobre las contribuciones, ver [CREDITS.md](CREDITS.md)

### Fuentes de Datos
- DEMRE (Departamento de Evaluación, Medición y Registro Educacional)
- Ministerio de Educación de Chile

### Agradecimientos
- DEMRE por proporcionar los datos abiertos
- Comunidad de data science en Python
- Todos los contribuidores del proyecto

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

⭐ Si este proyecto te fue útil, ¡considera darle una estrella en GitHub!

📧 Para preguntas o sugerencias, abre un issue en el repositorio.
