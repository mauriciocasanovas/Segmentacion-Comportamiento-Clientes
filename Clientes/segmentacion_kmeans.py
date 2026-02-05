import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def ejecutar_segmentacion():
    """Análisis de segmentación de clientes utilizando el algoritmo K-Means."""
    
    # Conexión y extracción de datos
    if not os.path.exists('empresa.db'):
        print("Error: No se encuentra la base de datos 'empresa.db'.")
        return
        
    conn = sqlite3.connect('empresa.db')
    df = pd.read_sql_query("SELECT * FROM clientes", conn)
    conn.close()

    # Pre-procesamiento: Selección de variables y escalamiento estándar
    X = df[['gasto_total', 'frecuencia_visitas']]
    scaler = StandardScaler()
    X_escalado = scaler.fit_transform(X)

    # Aplicación del modelo K-Means (Segmentación en 4 clusters)
    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['segmento'] = model.fit_predict(X_escalado)

    # Análisis de centroides (Valores promedio por segmento)
    centros_reales = scaler.inverse_transform(model.cluster_centers_)
    df_centros = pd.DataFrame(centros_reales, columns=['Gasto Promedio', 'Frecuencia Promedio'])
    
    # Gestión de exportación a Excel
    if not os.path.exists('Resultados'):
        os.makedirs('Resultados')

    try:
        ruta_excel = 'Resultados/Reporte_Final_Clientes.xlsx'
        with pd.ExcelWriter(ruta_excel) as writer:
            df.to_excel(writer, sheet_name='Lista de Clientes', index=False)
            df_centros.to_excel(writer, sheet_name='Resumen Estratégico')
        print(f"Reporte estratégico generado en: {ruta_excel}")
    except Exception as e:
        print(f"Error al exportar Excel: {e}")

    # Visualizaciones técnicas
    sns.set_theme(style="whitegrid")
    
    # Gráfico de dispersión (Clusters)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='frecuencia_visitas', y='gasto_total', hue='segmento', palette='viridis', s=100)
    plt.title('Segmentación de Clientes: Análisis de Clusters', fontsize=14)
    plt.savefig('Resultados/segmentacion_final.png', dpi=300, bbox_inches='tight')

    # Gráfico de distribución (Market Share interno)
    plt.figure(figsize=(8, 8))
    df['segmento'].value_counts().sort_index().plot(
        kind='pie', 
        labels=[f'Segmento {i}' for i in range(4)], 
        autopct='%1.1f%%', 
        colors=sns.color_palette('viridis', 4)
    )
    plt.title('Distribución de Clientes por Segmento')
    plt.ylabel('')
    plt.savefig('Resultados/distribucion_segmentos.png')

if __name__ == "__main__":
    print("Iniciando motor de segmentación de clientes...")
    ejecutar_segmentacion()