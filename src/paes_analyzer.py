"""
PAES Analyzer - Módulo principal para análisis de resultados PAES
Analiza los resultados de la Prueba de Acceso a la Educación Superior en Chile
"""

import pandas as pd
import numpy as np
from typing import Optional, List, Dict
import warnings
warnings.filterwarnings('ignore')


class PAESAnalyzer:
    """
    Clase para analizar datos de PAES y generar rankings de establecimientos educacionales.
    """
    
    def __init__(self, file_path: str, year: int):
        """
        Inicializa el analizador con un archivo de datos PAES.
        
        Args:
            file_path: Ruta al archivo CSV con datos PAES
            year: Año de la admisión (2023, 2024, 2025, etc.)
        """
        self.file_path = file_path
        self.year = year
        self.df = None
        self.filtered_data = None
        self.rbd_averages = None
        self.ranking = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Carga los datos desde el archivo CSV.
        
        Returns:
            DataFrame con los datos cargados
        """
        print(f"Cargando datos PAES {self.year}...")
        self.df = pd.read_csv(self.file_path, sep=';', low_memory=False)
        print(f"✓ Datos cargados: {len(self.df):,} registros")
        return self.df
    
    def filter_graduates(self) -> pd.DataFrame:
        """
        Filtra estudiantes que egresaron regularmente (SITUACION_EGRESO = 1).
        
        Returns:
            DataFrame filtrado con egresados regulares
        """
        if self.df is None:
            self.load_data()
            
        self.filtered_data = self.df[self.df['SITUACION_EGRESO'] == 1].copy()
        print(f"✓ Estudiantes egresados regulares: {len(self.filtered_data):,}")
        return self.filtered_data
    
    def calculate_school_averages(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Calcula promedios por establecimiento (RBD).
        
        Args:
            columns: Lista de columnas para calcular promedios. 
                    Si es None, usa columnas estándar PAES.
        
        Returns:
            DataFrame con promedios por RBD
        """
        if self.filtered_data is None:
            self.filter_graduates()
        
        if columns is None:
            columns = [
                'CLEC_REG_ACTUAL', 
                'MATE1_REG_ACTUAL', 
                'MATE2_REG_ACTUAL', 
                'HCSOC_REG_ACTUAL', 
                'CIEN_REG_ACTUAL'
            ]
        
        # Verificar qué columnas existen
        available_columns = [col for col in columns if col in self.filtered_data.columns]
        
        self.rbd_averages = (
            self.filtered_data
            .groupby('RBD')[available_columns]
            .mean()
            .reset_index()
        )
        
        print(f"✓ Promedios calculados para {len(self.rbd_averages):,} establecimientos")
        return self.rbd_averages
    
    def create_ranking(self) -> pd.DataFrame:
        """
        Crea ranking basado en el promedio de Comprensión Lectora y Matemática 1.
        
        Returns:
            DataFrame con el ranking ordenado
        """
        if self.filtered_data is None:
            self.filter_graduates()
        
        # Calcular promedio PAES (CLEC + MATE1)
        paes_columns = ['CLEC_REG_ACTUAL', 'MATE1_REG_ACTUAL']
        
        ranking_df = (
            self.filtered_data
            .groupby('RBD')[paes_columns]
            .mean()
        )
        
        # Calcular promedio entre ambas pruebas
        ranking_df['PAES_PROMEDIO'] = ranking_df.mean(axis=1)
        
        # Agregar información adicional
        # Contar estudiantes por establecimiento
        student_counts = self.filtered_data.groupby('RBD').size()
        ranking_df['N_ESTUDIANTES'] = student_counts
        
        # Crear ranking
        ranking_df['RANK'] = ranking_df['PAES_PROMEDIO'].rank(
            ascending=False, 
            method='min'
        )
        
        # Ordenar y resetear índice
        self.ranking = (
            ranking_df
            .sort_values('PAES_PROMEDIO', ascending=False)
            .reset_index()
        )
        
        print(f"✓ Ranking creado con {len(self.ranking):,} establecimientos")
        return self.ranking
    
    def get_school_position(self, rbd: int) -> Dict:
        """
        Consulta la posición de un establecimiento en el ranking.
        
        Args:
            rbd: Código RBD del establecimiento
            
        Returns:
            Diccionario con información del establecimiento o mensaje de error
        """
        if self.ranking is None:
            self.create_ranking()
        
        result = self.ranking[self.ranking['RBD'] == rbd]
        
        if result.empty:
            return {
                'error': f'El RBD {rbd} no se encuentra en el ranking',
                'year': self.year
            }
        
        row = result.iloc[0]
        return {
            'rbd': int(row['RBD']),
            'rank': int(row['RANK']),
            'paes_promedio': round(row['PAES_PROMEDIO'], 2),
            'clec': round(row['CLEC_REG_ACTUAL'], 2),
            'mate1': round(row['MATE1_REG_ACTUAL'], 2),
            'n_estudiantes': int(row['N_ESTUDIANTES']),
            'year': self.year,
            'percentil': round((1 - row['RANK'] / len(self.ranking)) * 100, 1)
        }
    
    def get_top_schools(self, n: int = 10) -> pd.DataFrame:
        """
        Obtiene los mejores n establecimientos del ranking.
        
        Args:
            n: Número de establecimientos a retornar
            
        Returns:
            DataFrame con los top n establecimientos
        """
        if self.ranking is None:
            self.create_ranking()
        
        return self.ranking.head(n)
    
    def get_statistics(self) -> Dict:
        """
        Calcula estadísticas generales del año.
        
        Returns:
            Diccionario con estadísticas descriptivas
        """
        if self.ranking is None:
            self.create_ranking()
        
        return {
            'year': self.year,
            'total_establecimientos': len(self.ranking),
            'total_estudiantes': int(self.ranking['N_ESTUDIANTES'].sum()),
            'promedio_nacional': round(self.ranking['PAES_PROMEDIO'].mean(), 2),
            'mediana_nacional': round(self.ranking['PAES_PROMEDIO'].median(), 2),
            'desviacion_estandar': round(self.ranking['PAES_PROMEDIO'].std(), 2),
            'puntaje_maximo': round(self.ranking['PAES_PROMEDIO'].max(), 2),
            'puntaje_minimo': round(self.ranking['PAES_PROMEDIO'].min(), 2),
            'promedio_clec': round(self.ranking['CLEC_REG_ACTUAL'].mean(), 2),
            'promedio_mate1': round(self.ranking['MATE1_REG_ACTUAL'].mean(), 2)
        }
    
    def export_ranking(self, output_path: str, format: str = 'csv') -> str:
        """
        Exporta el ranking a un archivo.
        
        Args:
            output_path: Ruta donde guardar el archivo
            format: Formato de exportación ('csv', 'excel', 'json')
            
        Returns:
            Ruta del archivo generado
        """
        if self.ranking is None:
            self.create_ranking()
        
        if format == 'csv':
            self.ranking.to_csv(output_path, index=False, encoding='utf-8-sig')
        elif format == 'excel':
            self.ranking.to_excel(output_path, index=False)
        elif format == 'json':
            self.ranking.to_json(output_path, orient='records', indent=2)
        else:
            raise ValueError(f"Formato no soportado: {format}")
        
        print(f"✓ Ranking exportado a: {output_path}")
        return output_path
    
    def compare_years(self, other_analyzer: 'PAESAnalyzer', rbd: int) -> Dict:
        """
        Compara el desempeño de un establecimiento entre dos años.
        
        Args:
            other_analyzer: Otro analizador PAES para comparar
            rbd: Código RBD del establecimiento
            
        Returns:
            Diccionario con comparación entre años
        """
        year1_data = self.get_school_position(rbd)
        year2_data = other_analyzer.get_school_position(rbd)
        
        if 'error' in year1_data or 'error' in year2_data:
            return {
                'error': 'Establecimiento no encontrado en uno o ambos años',
                'year1': self.year,
                'year2': other_analyzer.year
            }
        
        rank_change = year1_data['rank'] - year2_data['rank']
        score_change = year1_data['paes_promedio'] - year2_data['paes_promedio']
        
        return {
            'rbd': rbd,
            'comparison': {
                self.year: year1_data,
                other_analyzer.year: year2_data
            },
            'cambio_ranking': rank_change,
            'cambio_puntaje': round(score_change, 2),
            'tendencia': 'mejora' if score_change > 0 else 'baja' if score_change < 0 else 'estable'
        }
