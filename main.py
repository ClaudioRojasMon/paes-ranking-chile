"""
Script principal para análisis de resultados PAES
Ranking de establecimientos educacionales en Chile
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from paes_analyzer import PAESAnalyzer
from visualizations import PAESVisualizer
import argparse
import json


def main():
    """Función principal del programa."""
    
    parser = argparse.ArgumentParser(
        description='Análisis y Ranking de Resultados PAES'
    )
    
    parser.add_argument(
        '--file', 
        type=str, 
        required=True,
        help='Ruta al archivo CSV con datos PAES'
    )
    
    parser.add_argument(
        '--year', 
        type=int, 
        required=True,
        help='Año de admisión'
    )
    
    parser.add_argument(
        '--output-dir', 
        type=str, 
        default='outputs',
        help='Directorio para guardar resultados (default: outputs)'
    )
    
    parser.add_argument(
        '--top', 
        type=int, 
        default=50,
        help='Número de establecimientos top a exportar (default: 50)'
    )
    
    parser.add_argument(
        '--rbd', 
        type=int,
        help='Consultar posición de un RBD específico'
    )
    
    parser.add_argument(
        '--visualize', 
        action='store_true',
        help='Generar visualizaciones'
    )
    
    parser.add_argument(
        '--compare', 
        type=str,
        help='Archivo CSV de otro año para comparar (formato: ruta,año)'
    )
    
    args = parser.parse_args()
    
    # Crear directorio de salida si no existe
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Inicializar analizador
    print(f"\n{'='*60}")
    print(f"   ANÁLISIS PAES {args.year}")
    print(f"{'='*60}\n")
    
    analyzer = PAESAnalyzer(args.file, args.year)
    
    # Cargar y procesar datos
    analyzer.load_data()
    analyzer.filter_graduates()
    analyzer.calculate_school_averages()
    ranking = analyzer.create_ranking()
    
    # Mostrar estadísticas
    print(f"\n{'='*60}")
    print("   ESTADÍSTICAS GENERALES")
    print(f"{'='*60}\n")
    
    stats = analyzer.get_statistics()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title():.<40} {value}")
    
    # Exportar ranking completo
    output_csv = os.path.join(args.output_dir, f'ranking_paes_{args.year}.csv')
    analyzer.export_ranking(output_csv, format='csv')
    
    output_excel = os.path.join(args.output_dir, f'ranking_paes_{args.year}.xlsx')
    analyzer.export_ranking(output_excel, format='excel')
    
    # Exportar top establecimientos
    top_schools = analyzer.get_top_schools(args.top)
    top_output = os.path.join(args.output_dir, f'top_{args.top}_paes_{args.year}.csv')
    top_schools.to_csv(top_output, index=False, encoding='utf-8-sig')
    print(f"✓ Top {args.top} exportado a: {top_output}")
    
    # Exportar estadísticas como JSON
    stats_output = os.path.join(args.output_dir, f'estadisticas_paes_{args.year}.json')
    with open(stats_output, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"✓ Estadísticas exportadas a: {stats_output}")
    
    # Mostrar top 10
    print(f"\n{'='*60}")
    print(f"   TOP 10 ESTABLECIMIENTOS {args.year}")
    print(f"{'='*60}\n")
    
    top10 = analyzer.get_top_schools(10)
    for idx, row in top10.iterrows():
        print(f"#{int(row['RANK']):3d}  RBD {int(row['RBD']):5d}  |  "
              f"Promedio: {row['PAES_PROMEDIO']:6.2f}  |  "
              f"CLEC: {row['CLEC_REG_ACTUAL']:6.2f}  |  "
              f"MATE1: {row['MATE1_REG_ACTUAL']:6.2f}  |  "
              f"N: {int(row['N_ESTUDIANTES']):3d}")
    
    # Consultar RBD específico
    if args.rbd:
        print(f"\n{'='*60}")
        print(f"   CONSULTA RBD {args.rbd}")
        print(f"{'='*60}\n")
        
        result = analyzer.get_school_position(args.rbd)
        
        if 'error' in result:
            print(f"❌ {result['error']}")
        else:
            print(f"RBD: {result['rbd']}")
            print(f"Ranking Nacional: #{result['rank']}")
            print(f"Percentil: {result['percentil']}%")
            print(f"Promedio PAES: {result['paes_promedio']}")
            print(f"Comprensión Lectora: {result['clec']}")
            print(f"Matemática 1: {result['mate1']}")
            print(f"Número de Estudiantes: {result['n_estudiantes']}")
    
    # Generar visualizaciones
    if args.visualize:
        print(f"\n{'='*60}")
        print("   GENERANDO VISUALIZACIONES")
        print(f"{'='*60}\n")
        
        visualizer = PAESVisualizer()
        
        # Dashboard principal
        dashboard_path = os.path.join(
            args.output_dir, 
            f'dashboard_paes_{args.year}.png'
        )
        visualizer.create_summary_dashboard(ranking, args.year, dashboard_path)
        
        # Top establecimientos
        top_path = os.path.join(
            args.output_dir, 
            f'top_20_paes_{args.year}.png'
        )
        visualizer.plot_top_schools(ranking, n=20, save_path=top_path)
        
        # Distribución
        dist_path = os.path.join(
            args.output_dir, 
            f'distribucion_paes_{args.year}.png'
        )
        visualizer.plot_score_distribution(ranking, dist_path)
    
    # Comparación entre años
    if args.compare:
        try:
            compare_file, compare_year = args.compare.split(',')
            compare_year = int(compare_year)
            
            print(f"\n{'='*60}")
            print(f"   COMPARACIÓN {args.year} vs {compare_year}")
            print(f"{'='*60}\n")
            
            analyzer2 = PAESAnalyzer(compare_file, compare_year)
            analyzer2.load_data()
            analyzer2.filter_graduates()
            ranking2 = analyzer2.create_ranking()
            
            if args.rbd:
                comparison = analyzer.compare_years(analyzer2, args.rbd)
                
                if 'error' not in comparison:
                    print(f"\nComparación RBD {args.rbd}:")
                    print(f"Año {args.year}: Ranking #{comparison['comparison'][args.year]['rank']}, "
                          f"Promedio {comparison['comparison'][args.year]['paes_promedio']}")
                    print(f"Año {compare_year}: Ranking #{comparison['comparison'][compare_year]['rank']}, "
                          f"Promedio {comparison['comparison'][compare_year]['paes_promedio']}")
                    print(f"Cambio en ranking: {comparison['cambio_ranking']:+d} posiciones")
                    print(f"Cambio en puntaje: {comparison['cambio_puntaje']:+.2f} puntos")
                    print(f"Tendencia: {comparison['tendencia'].upper()}")
            
            if args.visualize:
                comp_path = os.path.join(
                    args.output_dir, 
                    f'comparacion_{args.year}_vs_{compare_year}.png'
                )
                visualizer.plot_year_comparison(
                    ranking, ranking2, 
                    args.year, compare_year, 
                    comp_path
                )
        
        except Exception as e:
            print(f"❌ Error en comparación: {e}")
    
    print(f"\n{'='*60}")
    print("   ✓ ANÁLISIS COMPLETADO")
    print(f"{'='*60}\n")
    print(f"Los resultados se guardaron en: {args.output_dir}/\n")


if __name__ == '__main__':
    main()
