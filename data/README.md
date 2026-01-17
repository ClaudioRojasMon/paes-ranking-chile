# Directorio de Datos

Esta carpeta debe contener los archivos CSV con los datos PAES.

## Archivos Esperados

Los archivos deben tener el siguiente formato:
```
ArchivoC_Adm2023.csv
ArchivoC_Adm2024.csv
ArchivoC_Adm2025.csv
```

## Dónde Obtener los Datos

Los datos PAES son de acceso público y se pueden obtener de:

- **DEMRE**: [https://demre.cl](https://demre.cl)
- **Ministerio de Educación**: [https://www.mineduc.cl](https://www.mineduc.cl)
- **Portal de Datos Abiertos**: [https://datos.gob.cl](https://datos.gob.cl)

## Estructura de los Archivos

Los archivos CSV deben tener al menos las siguientes columnas:
- `RBD`: Código del establecimiento
- `SITUACION_EGRESO`: Situación de egreso del estudiante
- `CLEC_REG_ACTUAL`: Puntaje Comprensión Lectora
- `MATE1_REG_ACTUAL`: Puntaje Matemática 1
- `MATE2_REG_ACTUAL`: Puntaje Matemática 2 (opcional)
- `HCSOC_REG_ACTUAL`: Puntaje Historia y Ciencias Sociales (opcional)
- `CIEN_REG_ACTUAL`: Puntaje Ciencias (opcional)
- `CODIGO_REGION`: Código de región
- `CODIGO_COMUNA`: Código de comuna

## Formato

- Separador: punto y coma (`;`)
- Encoding: UTF-8 o Latin-1
- Decimales: coma (`,`) en los archivos originales

## Notas

⚠️ Los archivos de datos NO se incluyen en el repositorio de GitHub debido a su tamaño.

💡 Asegúrate de descargar los datos antes de ejecutar el análisis.

📝 Los archivos pueden tener más columnas; el sistema usará solo las necesarias.
