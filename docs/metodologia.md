# Metodología de Cálculo del Ranking PAES

## Resumen

Este documento describe la metodología utilizada para calcular el ranking de establecimientos educacionales basado en los resultados de la Prueba de Acceso a la Educación Superior (PAES) en Chile.

## 1. Fuente de Datos

- **Origen**: Archivos públicos del DEMRE (Departamento de Evaluación, Medición y Registro Educacional)
- **Formato**: CSV con separador punto y coma (`;`)
- **Período**: Años 2023, 2024, 2025
- **Unidad de análisis**: Estudiante individual con su establecimiento de egreso

## 2. Filtrado de Datos

### 2.1 Criterios de Inclusión

Se incluyen en el ranking únicamente los estudiantes que cumplen:

- `SITUACION_EGRESO = 1` (Egreso regular)
- Poseen puntajes válidos en las pruebas obligatorias

### 2.2 Criterios de Exclusión

Se excluyen:
- Estudiantes con egreso irregular
- Estudiantes sin RBD asociado
- Puntajes inválidos o nulos en pruebas obligatorias

## 3. Cálculo de Puntajes

### 3.1 Promedio por Establecimiento

Para cada establecimiento (RBD), se calculan los promedios de:

1. **Comprensión Lectora** (CLEC_REG_ACTUAL)
2. **Matemática 1** (MATE1_REG_ACTUAL)
3. **Matemática 2** (MATE2_REG_ACTUAL) - opcional
4. **Historia y Ciencias Sociales** (HCSOC_REG_ACTUAL) - opcional
5. **Ciencias** (CIEN_REG_ACTUAL) - opcional

**Fórmula**:
```
Promedio_RBD_CLEC = Σ(CLEC_estudiantes) / N_estudiantes
Promedio_RBD_MATE1 = Σ(MATE1_estudiantes) / N_estudiantes
```

### 3.2 Promedio PAES (Ranking Principal)

El puntaje utilizado para el ranking se calcula como:

```
PAES_PROMEDIO = (CLEC_REG_ACTUAL + MATE1_REG_ACTUAL) / 2
```

**Justificación**: Se utilizan las dos pruebas obligatorias que todos los estudiantes deben rendir.

## 4. Generación del Ranking

### 4.1 Ordenamiento

Los establecimientos se ordenan de manera descendente según `PAES_PROMEDIO`.

### 4.2 Asignación de Posiciones

Se utiliza el método `min` para manejar empates:
- Si dos establecimientos tienen el mismo puntaje, se les asigna la misma posición
- La siguiente posición disponible salta según el número de empates

**Ejemplo**:
```
Puesto 1: RBD 12036 - 883.71 puntos
Puesto 2: RBD 8862 - 870.83 puntos
Puesto 3: RBD 3204 - 867.73 puntos
Puesto 3: RBD 8871 - 867.73 puntos (empate)
Puesto 5: RBD 8998 - 862.03 puntos
```

## 5. Métricas Adicionales

### 5.1 Estadísticas Calculadas

Para cada año se calculan:

- **Promedio Nacional**: Media de todos los promedios por establecimiento
- **Mediana Nacional**: Valor central de la distribución
- **Desviación Estándar**: Medida de dispersión
- **Puntaje Máximo/Mínimo**: Valores extremos
- **Número de Estudiantes**: Total por establecimiento y nacional

### 5.2 Percentiles

Para cada establecimiento se calcula su percentil:

```
Percentil = (1 - Ranking / Total_Establecimientos) × 100
```

Un percentil de 95% significa que el establecimiento está en el top 5% nacional.

## 6. Comparación Temporal

### 6.1 Cambio en Ranking

```
Cambio_Ranking = Ranking_Año_Actual - Ranking_Año_Anterior
```

- Valor negativo = mejora en el ranking
- Valor positivo = baja en el ranking
- Valor cero = posición estable

### 6.2 Cambio en Puntaje

```
Cambio_Puntaje = PAES_PROMEDIO_Año_Actual - PAES_PROMEDIO_Año_Anterior
```

### 6.3 Clasificación de Tendencia

- **Mejora**: Cambio_Puntaje > 0
- **Baja**: Cambio_Puntaje < 0
- **Estable**: Cambio_Puntaje = 0

## 7. Análisis Regional

### 7.1 Promedio por Región

Se calcula el promedio de todos los establecimientos en cada región:

```
Promedio_Regional = Σ(PAES_PROMEDIO_establecimientos_región) / N_establecimientos_región
```

### 7.2 Ranking Regional

Se genera un ranking separado para cada región usando la misma metodología.

## 8. Validación de Resultados

### 8.1 Controles de Calidad

- Verificación de puntajes dentro del rango válido (0-1000)
- Validación de número de estudiantes por establecimiento
- Detección de valores atípicos (outliers)

### 8.2 Consistencia Temporal

- Comparación de distribuciones entre años
- Análisis de cambios extremos en puntajes
- Verificación de continuidad de establecimientos

## 9. Limitaciones

### 9.1 Limitaciones Metodológicas

1. **Promedio Simple**: No se pondera por tamaño del establecimiento
2. **Solo Obligatorias**: No incluye pruebas electivas en el ranking principal
3. **Egresados Regulares**: Excluye estudiantes con egreso irregular
4. **Sin Contexto**: No considera variables socioeconómicas

### 9.2 Limitaciones de Datos

1. Datos públicos pueden tener información parcial
2. No incluye nombre del establecimiento (solo RBD)
3. Variables de contexto limitadas

## 10. Consideraciones Éticas

### 10.1 Uso Responsable

- Los rankings deben interpretarse con contexto
- No son la única medida de calidad educativa
- Reflejan un momento específico en el tiempo
- No capturan todos los aspectos del proceso educativo

### 10.2 Privacidad

- No se publican datos individuales de estudiantes
- Solo se reportan agregados por establecimiento
- Se respetan políticas de datos abiertos del DEMRE

## 11. Referencias

- DEMRE. (2025). "Manual de Uso de Archivos de Datos PAES"
- Ministerio de Educación de Chile. "Indicadores de Calidad Educativa"
- Documentación técnica de pandas para cálculos estadísticos

---

**Versión**: 1.0  
**Última actualización**: Enero 2025  
**Autor**: Sistema PAES Ranking Chile
