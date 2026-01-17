# Guía de Contribución

¡Gracias por tu interés en contribuir al proyecto PAES Ranking Chile! 🎉

## Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Cómo Contribuir](#cómo-contribuir)
- [Reportar Bugs](#reportar-bugs)
- [Sugerir Mejoras](#sugerir-mejoras)
- [Pull Requests](#pull-requests)
- [Guía de Estilo](#guía-de-estilo)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)

## Código de Conducta

Este proyecto se adhiere a un código de conducta de colaboración. Al participar, se espera que mantengas un ambiente respetuoso y constructivo.

### Nuestros Estándares

✅ **Comportamiento Aceptable:**
- Ser respetuoso con diferentes puntos de vista
- Aceptar críticas constructivas
- Enfocarse en lo mejor para la comunidad
- Mostrar empatía hacia otros miembros

❌ **Comportamiento Inaceptable:**
- Uso de lenguaje o imágenes sexualizadas
- Comentarios insultantes o despectivos
- Acoso público o privado
- Publicar información privada de otros sin permiso

## Cómo Contribuir

Hay muchas formas de contribuir al proyecto:

### 1. Reportar Bugs
- Usa el template de issues para bugs
- Incluye pasos para reproducir el problema
- Especifica tu entorno (OS, versión de Python, etc.)

### 2. Mejorar Documentación
- Corregir typos
- Agregar ejemplos
- Mejorar explicaciones
- Traducir documentación

### 3. Agregar Funcionalidades
- Nuevas visualizaciones
- Análisis adicionales
- Mejoras de performance
- Tests automatizados

### 4. Optimizar Código
- Mejorar eficiencia
- Refactorizar código duplicado
- Agregar type hints
- Mejorar manejo de errores

## Reportar Bugs

Antes de reportar un bug, verifica:
- [ ] ¿Ya existe un issue similar?
- [ ] ¿Estás usando la última versión?
- [ ] ¿El problema persiste con datos de ejemplo?

### Template para Reportar Bugs

```markdown
**Descripción del Bug**
Descripción clara y concisa del problema.

**Para Reproducir**
Pasos para reproducir el comportamiento:
1. Ir a '...'
2. Ejecutar '...'
3. Ver error

**Comportamiento Esperado**
Qué esperabas que sucediera.

**Screenshots**
Si aplica, agrega capturas de pantalla.

**Entorno:**
 - OS: [e.g. Windows 10, macOS 12, Ubuntu 20.04]
 - Python Version: [e.g. 3.9.7]
 - Pandas Version: [e.g. 2.0.0]

**Información Adicional**
Cualquier otro contexto sobre el problema.
```

## Sugerir Mejoras

### Template para Nuevas Funcionalidades

```markdown
**Descripción de la Funcionalidad**
Descripción clara de qué quieres agregar.

**Motivación**
¿Por qué esta funcionalidad sería útil?

**Solución Propuesta**
¿Cómo imaginas que funcionaría?

**Alternativas Consideradas**
¿Qué otras soluciones has considerado?

**Contexto Adicional**
Screenshots, ejemplos, referencias, etc.
```

## Pull Requests

### Proceso

1. **Fork el Repositorio**
   ```bash
   git clone https://github.com/tu-usuario/paes-ranking-chile.git
   cd paes-ranking-chile
   ```

2. **Crear una Rama**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   # o
   git checkout -b fix/correccion-bug
   ```

3. **Hacer Cambios**
   - Escribe código limpio y documentado
   - Agrega tests si es posible
   - Actualiza la documentación

4. **Commit**
   ```bash
   git add .
   git commit -m "feat: agregar nueva visualización de tendencias"
   ```

5. **Push**
   ```bash
   git push origin feature/nueva-funcionalidad
   ```

6. **Crear Pull Request**
   - Usa un título descriptivo
   - Explica los cambios realizados
   - Referencia issues relacionados

### Convenciones de Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formato, punto y coma, etc (sin cambios de código)
- `refactor:` Refactorización de código
- `test:` Agregar tests
- `chore:` Tareas de mantenimiento

**Ejemplos:**
```bash
feat: agregar análisis por tipo de dependencia
fix: corregir cálculo de percentiles
docs: actualizar README con nuevos ejemplos
refactor: simplificar función de exportación
test: agregar tests para PAESAnalyzer
```

### Checklist para Pull Requests

Antes de enviar un PR, verifica:

- [ ] El código sigue el estilo del proyecto
- [ ] He actualizado la documentación
- [ ] He agregado tests para nuevas funcionalidades
- [ ] Todos los tests pasan
- [ ] He revisado mi propio código
- [ ] El PR está enfocado en un solo tema
- [ ] He actualizado el CHANGELOG (si aplica)

## Guía de Estilo

### Python

Seguimos [PEP 8](https://www.python.org/dev/peps/pep-0008/) con algunas especificaciones:

#### Formateo

```python
# Usar black para formateo automático
black src/

# Verificar con flake8
flake8 src/
```

#### Nombres

```python
# Variables y funciones: snake_case
promedio_nacional = 500
def calcular_ranking():
    pass

# Clases: PascalCase
class PAESAnalyzer:
    pass

# Constantes: UPPER_CASE
MAX_SCORE = 1000
```

#### Docstrings

```python
def calcular_promedio(valores: List[float]) -> float:
    """
    Calcula el promedio de una lista de valores.
    
    Args:
        valores: Lista de números flotantes
        
    Returns:
        Promedio de los valores
        
    Raises:
        ValueError: Si la lista está vacía
        
    Example:
        >>> calcular_promedio([1, 2, 3])
        2.0
    """
    if not valores:
        raise ValueError("La lista no puede estar vacía")
    return sum(valores) / len(valores)
```

#### Type Hints

```python
from typing import List, Dict, Optional

def procesar_datos(
    archivo: str,
    columnas: List[str],
    filtros: Optional[Dict[str, any]] = None
) -> pd.DataFrame:
    """Procesa datos con type hints."""
    pass
```

### Organización de Imports

```python
# 1. Imports de biblioteca estándar
import os
import sys
from typing import List, Dict

# 2. Imports de terceros
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 3. Imports locales
from .paes_analyzer import PAESAnalyzer
from .utils import cargar_datos
```

### Comentarios

```python
# Buenos comentarios: explican el "por qué"
# Usamos método 'min' para que empates mantengan la misma posición
ranking['RANK'] = ranking['PAES_PROMEDIO'].rank(ascending=False, method='min')

# Malos comentarios: explican el "qué" (obvio en el código)
# Asignar 10 a la variable x
x = 10
```

## Configuración del Entorno de Desarrollo

### 1. Clonar y Configurar

```bash
# Clonar
git clone https://github.com/tu-usuario/paes-ranking-chile.git
cd paes-ranking-chile

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar dependencias de desarrollo
pip install black flake8 pytest pytest-cov
```

### 2. Verificar Instalación

```bash
# Ejecutar tests
pytest

# Verificar estilo
black src/ --check
flake8 src/

# Ejecutar ejemplo
python examples.py
```

### 3. Pre-commit Hooks (Opcional)

```bash
# Instalar pre-commit
pip install pre-commit

# Configurar hooks
pre-commit install

# Ejecutar manualmente
pre-commit run --all-files
```

## Tests

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Con cobertura
pytest --cov=src

# Tests específicos
pytest tests/test_analyzer.py
```

### Escribir Tests

```python
import pytest
from src.paes_analyzer import PAESAnalyzer

def test_calcular_promedio():
    """Test del cálculo de promedios."""
    analyzer = PAESAnalyzer('data/test.csv', 2025)
    result = analyzer.calculate_school_averages()
    assert result is not None
    assert len(result) > 0

def test_ranking_ordenado():
    """Test que el ranking está ordenado correctamente."""
    analyzer = PAESAnalyzer('data/test.csv', 2025)
    ranking = analyzer.create_ranking()
    
    # Verificar orden descendente
    promedios = ranking['PAES_PROMEDIO'].tolist()
    assert promedios == sorted(promedios, reverse=True)
```

## Preguntas Frecuentes

**P: ¿Necesito conocimientos avanzados de Python?**  
R: No necesariamente. Contribuciones a documentación, reportes de bugs, y mejoras simples son bienvenidas.

**P: ¿Cuánto tiempo toma revisar un PR?**  
R: Normalmente de 3-7 días. Ten paciencia, somos un proyecto mantenido por voluntarios.

**P: ¿Puedo trabajar en múltiples issues al mismo tiempo?**  
R: Es mejor enfocarse en uno a la vez para mantener PRs pequeños y enfocados.

**P: ¿Hay issues buenos para principiantes?**  
R: Sí, busca issues etiquetados como `good first issue` o `beginner-friendly`.

## Reconocimientos

Todos los contribuidores serán agregados al archivo CONTRIBUTORS.md y mencionados en los releases.

---

¡Gracias por contribuir al proyecto! 🙌

Si tienes preguntas, no dudes en abrir un issue de discusión.
