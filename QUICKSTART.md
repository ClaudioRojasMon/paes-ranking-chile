# 🚀 Guía de Inicio Rápido - PAES Ranking Chile

Esta guía te ayudará a empezar a usar el proyecto en **menos de 5 minutos**.

## ⚡ Instalación Express

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/paes-ranking-chile.git
cd paes-ranking-chile

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Listo! Ya puedes empezar
```

## 📁 Preparar Datos

Descarga los archivos CSV de PAES desde [demre.cl](https://demre.cl) y colócalos en la carpeta `data/`:

```
data/
  ├── ArchivoC_Adm2023.csv
  ├── ArchivoC_Adm2024.csv
  └── ArchivoC_Adm2025.csv
```

## 🎯 Primer Análisis

### Opción 1: Usando la Línea de Comandos

```bash
# Análisis básico
python main.py --file data/ArchivoC_Adm2025.csv --year 2025

# Con visualizaciones
python main.py --file data/ArchivoC_Adm2025.csv --year 2025 --visualize

# Consultar un colegio específico (RBD)
python main.py --file data/ArchivoC_Adm2025.csv --year 2025 --rbd 8609
```

### Opción 2: Usando Python

Crea un archivo `mi_analisis.py`:

```python
from src.paes_analyzer import PAESAnalyzer

# Crear analizador
analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)

# Procesar
analyzer.load_data()
analyzer.filter_graduates()
ranking = analyzer.create_ranking()

# Ver top 10
print(analyzer.get_top_schools(10))

# Exportar
analyzer.export_ranking('outputs/mi_ranking_2025.csv')
```

Ejecutar:
```bash
python mi_analisis.py
```

## 📊 Generar Visualizaciones

```python
from src.paes_analyzer import PAESAnalyzer
from src.visualizations import PAESVisualizer

# Cargar datos
analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
analyzer.load_data()
ranking = analyzer.create_ranking()

# Crear visualizador
viz = PAESVisualizer()

# Dashboard completo
viz.create_summary_dashboard(ranking, 2025, 'outputs/dashboard.png')

# Top 20 colegios
viz.plot_top_schools(ranking, n=20, save_path='outputs/top20.png')
```

## 🔍 Consultar un Colegio

```python
from src.paes_analyzer import PAESAnalyzer

analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
analyzer.load_data()
analyzer.create_ranking()

# Consultar RBD 8609
info = analyzer.get_school_position(8609)
print(f"Ranking: #{info['rank']}")
print(f"Promedio: {info['paes_promedio']}")
print(f"Percentil: {info['percentil']}%")
```

## 📈 Comparar Años

```python
from src.paes_analyzer import PAESAnalyzer

# Cargar ambos años
analyzer_2024 = PAESAnalyzer('data/ArchivoC_Adm2024.csv', 2024)
analyzer_2025 = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)

analyzer_2024.load_data()
analyzer_2025.load_data()

analyzer_2024.create_ranking()
analyzer_2025.create_ranking()

# Comparar
comp = analyzer_2025.compare_years(analyzer_2024, rbd=8609)
print(f"Cambio en ranking: {comp['cambio_ranking']} posiciones")
print(f"Cambio en puntaje: {comp['cambio_puntaje']} puntos")
```

## 📝 Obtener Estadísticas

```python
from src.paes_analyzer import PAESAnalyzer

analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
analyzer.load_data()
analyzer.create_ranking()

stats = analyzer.get_statistics()
print(f"Promedio Nacional: {stats['promedio_nacional']}")
print(f"Total Estudiantes: {stats['total_estudiantes']:,}")
print(f"Total Colegios: {stats['total_establecimientos']:,}")
```

## 🎨 Ejemplos Completos

El proyecto incluye `examples.py` con 5 ejemplos listos para usar:

```bash
# Edita examples.py y descomenta el ejemplo que quieras
python examples.py
```

Ejemplos disponibles:
1. Análisis básico
2. Consulta de establecimiento específico
3. Generación de visualizaciones
4. Comparación entre años
5. Exportación de resultados

## 📚 Estructura de Salida

Después de ejecutar el análisis, encontrarás en `outputs/`:

```
outputs/
  ├── ranking_paes_2025.csv          # Ranking completo
  ├── ranking_paes_2025.xlsx         # Ranking en Excel
  ├── estadisticas_paes_2025.json    # Estadísticas
  ├── dashboard_paes_2025.png        # Dashboard visual
  └── top_20_paes_2025.png          # Gráfico top 20
```

## ⚠️ Solución Rápida de Problemas

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "File not found"
```bash
# Verifica que el archivo existe
ls data/ArchivoC_Adm2025.csv
```

### Visualizaciones no se generan
```bash
# Asegúrate de tener matplotlib instalado
pip install matplotlib seaborn
```

## 📖 Próximos Pasos

1. Lee el [README.md](README.md) completo para más detalles
2. Revisa [docs/metodologia.md](docs/metodologia.md) para entender los cálculos
3. Explora los notebooks en `notebooks/` para análisis interactivos
4. Lee [CONTRIBUTING.md](CONTRIBUTING.md) si quieres contribuir

## 🆘 ¿Necesitas Ayuda?

- Revisa el [README.md](README.md) principal
- Abre un [Issue](https://github.com/tu-usuario/paes-ranking-chile/issues)
- Consulta los ejemplos en `examples.py`

---

**¡Feliz análisis!** 🎓📊
