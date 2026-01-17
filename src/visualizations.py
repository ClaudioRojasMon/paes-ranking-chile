"""
Módulo de visualizaciones para análisis PAES
Genera gráficos y visualizaciones de los resultados
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List
import numpy as np

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


class PAESVisualizer:
    """
    Clase para crear visualizaciones de datos PAES.
    """
    
    def __init__(self, figsize: tuple = (12, 6)):
        """
        Inicializa el visualizador.
        
        Args:
            figsize: Tamaño por defecto de las figuras
        """
        self.figsize = figsize
        
    def plot_top_schools(self, ranking_df: pd.DataFrame, n: int = 20, 
                        save_path: Optional[str] = None):
        """
        Grafica los mejores establecimientos.
        
        Args:
            ranking_df: DataFrame con el ranking
            n: Número de establecimientos a mostrar
            save_path: Ruta para guardar la figura (opcional)
        """
        top_schools = ranking_df.head(n)
        
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Crear gráfico de barras horizontal
        bars = ax.barh(
            range(len(top_schools)), 
            top_schools['PAES_PROMEDIO'],
            color=plt.cm.viridis(np.linspace(0, 1, len(top_schools)))
        )
        
        # Configurar etiquetas
        ax.set_yticks(range(len(top_schools)))
        ax.set_yticklabels([f"#{int(row['RANK'])} - RBD {int(row['RBD'])}" 
                           for _, row in top_schools.iterrows()])
        ax.set_xlabel('Promedio PAES (CLEC + MATE1)', fontsize=12, fontweight='bold')
        ax.set_title(f'Top {n} Establecimientos - Ranking PAES', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Agregar valores en las barras
        for i, (idx, row) in enumerate(top_schools.iterrows()):
            ax.text(
                row['PAES_PROMEDIO'] + 5, 
                i, 
                f"{row['PAES_PROMEDIO']:.1f}",
                va='center', 
                fontweight='bold'
            )
        
        ax.invert_yaxis()
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Gráfico guardado en: {save_path}")
        
        return fig
    
    def plot_score_distribution(self, ranking_df: pd.DataFrame, 
                               save_path: Optional[str] = None):
        """
        Grafica la distribución de puntajes.
        
        Args:
            ranking_df: DataFrame con el ranking
            save_path: Ruta para guardar la figura (opcional)
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Distribución de Puntajes PAES', fontsize=16, fontweight='bold')
        
        # Histograma del promedio PAES
        ax1 = axes[0, 0]
        ax1.hist(ranking_df['PAES_PROMEDIO'], bins=50, 
                color='steelblue', edgecolor='black', alpha=0.7)
        ax1.axvline(ranking_df['PAES_PROMEDIO'].mean(), 
                   color='red', linestyle='--', linewidth=2, label='Media')
        ax1.axvline(ranking_df['PAES_PROMEDIO'].median(), 
                   color='green', linestyle='--', linewidth=2, label='Mediana')
        ax1.set_xlabel('Promedio PAES')
        ax1.set_ylabel('Frecuencia')
        ax1.set_title('Distribución Promedio PAES')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Box plot
        ax2 = axes[0, 1]
        bp = ax2.boxplot([ranking_df['CLEC_REG_ACTUAL'], 
                          ranking_df['MATE1_REG_ACTUAL']], 
                         labels=['Comprensión\nLectora', 'Matemática 1'],
                         patch_artist=True)
        for patch, color in zip(bp['boxes'], ['lightblue', 'lightgreen']):
            patch.set_facecolor(color)
        ax2.set_ylabel('Puntaje')
        ax2.set_title('Distribución por Prueba')
        ax2.grid(True, alpha=0.3)
        
        # Scatter plot CLEC vs MATE1
        ax3 = axes[1, 0]
        scatter = ax3.scatter(
            ranking_df['CLEC_REG_ACTUAL'], 
            ranking_df['MATE1_REG_ACTUAL'],
            c=ranking_df['PAES_PROMEDIO'],
            cmap='viridis',
            alpha=0.6,
            s=50
        )
        ax3.set_xlabel('Comprensión Lectora')
        ax3.set_ylabel('Matemática 1')
        ax3.set_title('Relación CLEC vs MATE1')
        plt.colorbar(scatter, ax=ax3, label='Promedio PAES')
        ax3.grid(True, alpha=0.3)
        
        # Distribución acumulada
        ax4 = axes[1, 1]
        sorted_scores = np.sort(ranking_df['PAES_PROMEDIO'])
        cumulative = np.arange(1, len(sorted_scores) + 1) / len(sorted_scores) * 100
        ax4.plot(sorted_scores, cumulative, linewidth=2, color='darkblue')
        ax4.set_xlabel('Promedio PAES')
        ax4.set_ylabel('Percentil (%)')
        ax4.set_title('Distribución Acumulada')
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Gráfico guardado en: {save_path}")
        
        return fig
    
    def plot_year_comparison(self, year1_df: pd.DataFrame, year2_df: pd.DataFrame,
                            year1: int, year2: int, 
                            save_path: Optional[str] = None):
        """
        Compara distribuciones entre dos años.
        
        Args:
            year1_df: DataFrame del primer año
            year2_df: DataFrame del segundo año
            year1: Año 1
            year2: Año 2
            save_path: Ruta para guardar la figura (opcional)
        """
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(f'Comparación PAES {year1} vs {year2}', 
                    fontsize=16, fontweight='bold')
        
        # Histogramas superpuestos
        ax1 = axes[0]
        ax1.hist(year1_df['PAES_PROMEDIO'], bins=40, alpha=0.6, 
                label=f'{year1}', color='blue', edgecolor='black')
        ax1.hist(year2_df['PAES_PROMEDIO'], bins=40, alpha=0.6, 
                label=f'{year2}', color='red', edgecolor='black')
        ax1.set_xlabel('Promedio PAES')
        ax1.set_ylabel('Frecuencia')
        ax1.set_title('Distribución de Puntajes')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Box plots comparativos
        ax2 = axes[1]
        bp = ax2.boxplot(
            [year1_df['PAES_PROMEDIO'], year2_df['PAES_PROMEDIO']], 
            labels=[str(year1), str(year2)],
            patch_artist=True
        )
        for patch, color in zip(bp['boxes'], ['lightblue', 'lightcoral']):
            patch.set_facecolor(color)
        ax2.set_ylabel('Promedio PAES')
        ax2.set_title('Comparación de Distribuciones')
        ax2.grid(True, alpha=0.3)
        
        # Agregar estadísticas
        stats_text = f"{year1}: μ={year1_df['PAES_PROMEDIO'].mean():.1f}, σ={year1_df['PAES_PROMEDIO'].std():.1f}\n"
        stats_text += f"{year2}: μ={year2_df['PAES_PROMEDIO'].mean():.1f}, σ={year2_df['PAES_PROMEDIO'].std():.1f}"
        fig.text(0.5, 0.02, stats_text, ha='center', fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Gráfico guardado en: {save_path}")
        
        return fig
    
    def plot_regional_comparison(self, df: pd.DataFrame, 
                                save_path: Optional[str] = None):
        """
        Compara puntajes por región.
        
        Args:
            df: DataFrame con datos incluyendo columna CODIGO_REGION
            save_path: Ruta para guardar la figura (opcional)
        """
        if 'CODIGO_REGION' not in df.columns:
            print("⚠ Columna CODIGO_REGION no encontrada")
            return None
        
        # Calcular promedios por región
        regional_avg = df.groupby('CODIGO_REGION').agg({
            'CLEC_REG_ACTUAL': 'mean',
            'MATE1_REG_ACTUAL': 'mean'
        }).reset_index()
        
        regional_avg['PAES_PROMEDIO'] = (
            regional_avg['CLEC_REG_ACTUAL'] + 
            regional_avg['MATE1_REG_ACTUAL']
        ) / 2
        
        regional_avg = regional_avg.sort_values('PAES_PROMEDIO', ascending=False)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        bars = ax.barh(
            range(len(regional_avg)), 
            regional_avg['PAES_PROMEDIO'],
            color=plt.cm.coolwarm(np.linspace(0, 1, len(regional_avg)))
        )
        
        ax.set_yticks(range(len(regional_avg)))
        ax.set_yticklabels([f"Región {int(r)}" for r in regional_avg['CODIGO_REGION']])
        ax.set_xlabel('Promedio PAES')
        ax.set_title('Promedio PAES por Región', fontsize=14, fontweight='bold')
        ax.invert_yaxis()
        
        # Agregar valores
        for i, val in enumerate(regional_avg['PAES_PROMEDIO']):
            ax.text(val + 5, i, f"{val:.1f}", va='center')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Gráfico guardado en: {save_path}")
        
        return fig
    
    def create_summary_dashboard(self, ranking_df: pd.DataFrame, year: int,
                                 save_path: Optional[str] = None):
        """
        Crea un dashboard resumen con múltiples gráficos.
        
        Args:
            ranking_df: DataFrame con el ranking
            year: Año de los datos
            save_path: Ruta para guardar la figura (opcional)
        """
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # Título principal
        fig.suptitle(f'Dashboard Análisis PAES {year}', 
                    fontsize=18, fontweight='bold')
        
        # 1. Top 10 establecimientos
        ax1 = fig.add_subplot(gs[0:2, 0])
        top10 = ranking_df.head(10)
        bars = ax1.barh(range(len(top10)), top10['PAES_PROMEDIO'],
                       color=plt.cm.viridis(np.linspace(0, 1, len(top10))))
        ax1.set_yticks(range(len(top10)))
        ax1.set_yticklabels([f"#{int(row['RANK'])}" for _, row in top10.iterrows()])
        ax1.set_xlabel('Promedio')
        ax1.set_title('Top 10 Establecimientos', fontweight='bold')
        ax1.invert_yaxis()
        
        # 2. Distribución de puntajes
        ax2 = fig.add_subplot(gs[0, 1:])
        ax2.hist(ranking_df['PAES_PROMEDIO'], bins=50, 
                color='steelblue', edgecolor='black', alpha=0.7)
        ax2.axvline(ranking_df['PAES_PROMEDIO'].mean(), 
                   color='red', linestyle='--', linewidth=2, label='Media')
        ax2.set_xlabel('Promedio PAES')
        ax2.set_ylabel('Frecuencia')
        ax2.set_title('Distribución de Puntajes', fontweight='bold')
        ax2.legend()
        
        # 3. Box plots por prueba
        ax3 = fig.add_subplot(gs[1, 1])
        bp = ax3.boxplot([ranking_df['CLEC_REG_ACTUAL'], 
                          ranking_df['MATE1_REG_ACTUAL']], 
                         labels=['CLEC', 'MATE1'],
                         patch_artist=True)
        for patch, color in zip(bp['boxes'], ['lightblue', 'lightgreen']):
            patch.set_facecolor(color)
        ax3.set_ylabel('Puntaje')
        ax3.set_title('Distribución por Prueba', fontweight='bold')
        
        # 4. Scatter CLEC vs MATE1
        ax4 = fig.add_subplot(gs[1, 2])
        scatter = ax4.scatter(ranking_df['CLEC_REG_ACTUAL'], 
                             ranking_df['MATE1_REG_ACTUAL'],
                             c=ranking_df['PAES_PROMEDIO'],
                             cmap='viridis', alpha=0.5, s=30)
        ax4.set_xlabel('CLEC')
        ax4.set_ylabel('MATE1')
        ax4.set_title('CLEC vs MATE1', fontweight='bold')
        
        # 5. Estadísticas clave
        ax5 = fig.add_subplot(gs[2, :])
        ax5.axis('off')
        
        stats = {
            'Total Establecimientos': f"{len(ranking_df):,}",
            'Total Estudiantes': f"{int(ranking_df['N_ESTUDIANTES'].sum()):,}",
            'Promedio Nacional': f"{ranking_df['PAES_PROMEDIO'].mean():.2f}",
            'Mediana': f"{ranking_df['PAES_PROMEDIO'].median():.2f}",
            'Desv. Estándar': f"{ranking_df['PAES_PROMEDIO'].std():.2f}",
            'Puntaje Máximo': f"{ranking_df['PAES_PROMEDIO'].max():.2f}",
            'Puntaje Mínimo': f"{ranking_df['PAES_PROMEDIO'].min():.2f}"
        }
        
        stats_text = "ESTADÍSTICAS GENERALES\n" + "="*50 + "\n"
        for key, value in stats.items():
            stats_text += f"{key:.<30} {value:>15}\n"
        
        ax5.text(0.5, 0.5, stats_text, 
                transform=ax5.transAxes,
                fontsize=11,
                verticalalignment='center',
                horizontalalignment='center',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Dashboard guardado en: {save_path}")
        
        return fig
