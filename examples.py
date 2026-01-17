"""
Ejemplo de uso del sistema de análisis PAES
Este script muestra cómo usar las clases PAESAnalyzer y PAESVisualizer
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from paes_analyzer import PAESAnalyzer
from visualizations import PAESVisualizer


def ejemplo_basico():
    """Ejemplo básico de análisis."""
    print("\n" + "="*60)
    print("EJEMPLO 1: Análisis Básico")
    print("="*60 + "\n")
    
    # Crear analizador
    analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
    
    # Procesar datos
    analyzer.load_data()
    analyzer.filter_graduates()
    ranking = analyzer.create_ranking()
    
    # Mostrar estadísticas
    stats = analyzer.get_statistics()
    print("\nEstadísticas Generales:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Top 10
    print("\nTop 10 Establecimientos:")
    top10 = analyzer.get_top_schools(10)
    for idx, row in top10.iterrows():
        print(f"  #{int(row['RANK'])}: RBD {int(row['RBD'])} - "
              f"Promedio: {row['PAES_PROMEDIO']:.2f}")


def ejemplo_consulta_especifica():
    """Ejemplo de consulta de un establecimiento específico."""
    print("\n" + "="*60)
    print("EJEMPLO 2: Consulta de Establecimiento Específico")
    print("="*60 + "\n")
    
    analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
    analyzer.load_data()
    analyzer.create_ranking()
    
    # Consultar un RBD específico
    rbd = 8609
    result = analyzer.get_school_position(rbd)
    
    if 'error' not in result:
        print(f"Información del RBD {rbd}:")
        print(f"  Ranking Nacional: #{result['rank']}")
        print(f"  Percentil: {result['percentil']}%")
        print(f"  Promedio PAES: {result['paes_promedio']}")
        print(f"  Comprensión Lectora: {result['clec']}")
        print(f"  Matemática 1: {result['mate1']}")
        print(f"  Número de Estudiantes: {result['n_estudiantes']}")
    else:
        print(f"Error: {result['error']}")


def ejemplo_visualizaciones():
    """Ejemplo de generación de visualizaciones."""
    print("\n" + "="*60)
    print("EJEMPLO 3: Generación de Visualizaciones")
    print("="*60 + "\n")
    
    analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
    analyzer.load_data()
    ranking = analyzer.create_ranking()
    
    visualizer = PAESVisualizer()
    
    # Crear dashboard
    print("Generando dashboard...")
    visualizer.create_summary_dashboard(
        ranking, 
        2025,
        'outputs/ejemplo_dashboard.png'
    )
    
    # Top 20 colegios
    print("Generando gráfico top 20...")
    visualizer.plot_top_schools(
        ranking, 
        n=20,
        save_path='outputs/ejemplo_top20.png'
    )
    
    print("\n✓ Visualizaciones generadas en outputs/")


def ejemplo_comparacion_anos():
    """Ejemplo de comparación entre años."""
    print("\n" + "="*60)
    print("EJEMPLO 4: Comparación entre Años")
    print("="*60 + "\n")
    
    # Cargar dos años
    analyzer_2024 = PAESAnalyzer('data/ArchivoC_Adm2024.csv', 2024)
    analyzer_2025 = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
    
    analyzer_2024.load_data()
    analyzer_2025.load_data()
    
    ranking_2024 = analyzer_2024.create_ranking()
    ranking_2025 = analyzer_2025.create_ranking()
    
    # Comparar un establecimiento
    rbd = 7700
    comparison = analyzer_2025.compare_years(analyzer_2024, rbd)
    
    if 'error' not in comparison:
        print(f"\nComparación RBD {rbd}:")
        print(f"  2024: Ranking #{comparison['comparison'][2024]['rank']}, "
              f"Promedio {comparison['comparison'][2024]['paes_promedio']}")
        print(f"  2025: Ranking #{comparison['comparison'][2025]['rank']}, "
              f"Promedio {comparison['comparison'][2025]['paes_promedio']}")
        print(f"  Cambio en ranking: {comparison['cambio_ranking']:+d} posiciones")
        print(f"  Cambio en puntaje: {comparison['cambio_puntaje']:+.2f} puntos")
        print(f"  Tendencia: {comparison['tendencia'].upper()}")
    
    # Generar gráfico comparativo
    visualizer = PAESVisualizer()
    print("\nGenerando gráfico comparativo...")
    visualizer.plot_year_comparison(
        ranking_2024, 
        ranking_2025, 
        2024, 
        2025,
        'outputs/ejemplo_comparacion.png'
    )


def ejemplo_exportacion():
    """Ejemplo de exportación de resultados."""
    print("\n" + "="*60)
    print("EJEMPLO 5: Exportación de Resultados")
    print("="*60 + "\n")
    
    analyzer = PAESAnalyzer('data/ArchivoC_Adm2025.csv', 2025)
    analyzer.load_data()
    analyzer.create_ranking()
    
    # Exportar en diferentes formatos
    print("Exportando ranking completo...")
    analyzer.export_ranking('outputs/ejemplo_ranking.csv', format='csv')
    analyzer.export_ranking('outputs/ejemplo_ranking.xlsx', format='excel')
    analyzer.export_ranking('outputs/ejemplo_ranking.json', format='json')
    
    # Exportar solo top 50
    print("Exportando top 50...")
    top50 = analyzer.get_top_schools(50)
    top50.to_csv('outputs/ejemplo_top50.csv', index=False)
    
    print("\n✓ Archivos exportados en outputs/")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("\n" + "="*70)
    print(" "*15 + "EJEMPLOS DE USO - PAES RANKING CHILE")
    print("="*70)
    
    # Descomentar los ejemplos que quieras ejecutar:
    
    # ejemplo_basico()
    # ejemplo_consulta_especifica()
    # ejemplo_visualizaciones()
    # ejemplo_comparacion_anos()
    # ejemplo_exportacion()
    
    print("\n" + "="*70)
    print("Para ejecutar un ejemplo específico, descomenta la línea correspondiente")
    print("en la función main() de este archivo.")
    print("="*70 + "\n")


if __name__ == '__main__':
    main()
