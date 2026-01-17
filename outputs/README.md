# Directorio de Resultados

Esta carpeta contiene todos los archivos generados por el sistema de análisis.

## Archivos Generados

### Rankings
- `ranking_paes_YYYY.csv` - Ranking completo en formato CSV
- `ranking_paes_YYYY.xlsx` - Ranking completo en formato Excel
- `top_N_paes_YYYY.csv` - Top N establecimientos

### Estadísticas
- `estadisticas_paes_YYYY.json` - Estadísticas generales del año en JSON

### Visualizaciones
- `dashboard_paes_YYYY.png` - Dashboard resumen con múltiples gráficos
- `top_20_paes_YYYY.png` - Gráfico de top 20 establecimientos
- `distribucion_paes_YYYY.png` - Distribución de puntajes
- `comparacion_YYYY_vs_YYYY.png` - Comparación entre años

## Estructura de los Archivos

### Ranking CSV/Excel

Columnas:
- `RBD` - Código del establecimiento
- `CLEC_REG_ACTUAL` - Promedio Comprensión Lectora
- `MATE1_REG_ACTUAL` - Promedio Matemática 1
- `PAES_PROMEDIO` - Promedio entre CLEC y MATE1
- `N_ESTUDIANTES` - Número de estudiantes evaluados
- `RANK` - Posición en el ranking nacional

### Estadísticas JSON

```json
{
  "year": 2025,
  "total_establecimientos": 3292,
  "total_estudiantes": 180000,
  "promedio_nacional": 521.45,
  "mediana_nacional": 498.32,
  "desviacion_estandar": 156.78,
  "puntaje_maximo": 883.71,
  "puntaje_minimo": 0.00,
  "promedio_clec": 534.21,
  "promedio_mate1": 508.69
}
```

## Notas

⚠️ Los archivos de resultados NO se incluyen en el repositorio de GitHub.

🔄 Los archivos se regeneran cada vez que ejecutas el análisis.

💾 Asegúrate de tener suficiente espacio en disco para los resultados.
