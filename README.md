=======================================================================================
SISTEMA DE SEGMENTACION Y COMPORTAMIENTO DE CLIENTES (K-MEANS)
=======================================================================================

DESCRIPCIÓN:
Solucion de Inteligencia de Negocios orientada al marketing basado en datos. El 
sistema utiliza algoritmos de aprendizaje no supervisado (Clustering) para 
agrupar clientes segun su comportamiento de compra y frecuencia, permitiendo 
diseñar estrategias comerciales personalizadas para cada segmento.

ESTRUCTURA DEL PROYECTO:

1. empresa.db (Base de Datos):
   Repositorio SQLite que contiene la informacion transaccional historica 
   de los clientes, incluyendo facturacion total y recurrencia.

2. segmentacion_kmeans.py (Motor de Analitica):
   Script principal que ejecuta el proceso de Ciencia de Datos:
   - Limpieza y escalamiento de variables mediante StandardScaler.
   - Implementacion del algoritmo K-Means para la deteccion de 4 clusters.
   - Generacion de visualizaciones de dispersion y distribucion de mercado.
   - Exportacion de perfiles de clientes a la carpeta /Resultados.

3. ejecutar_proyecto.bat (Lanzador de Automatizacion):
   Archivo ejecutable que permite correr el flujo de analitica completo y 
   generar los reportes actualizados con un solo clic.

4. Carpeta Resultados:
   - Reporte_Final_Clientes.xlsx: Clasificacion detallada de cada cliente.
   - segmentacion_final.png: Grafico de clusters para analisis tecnico.
   - distribucion_segmentos.png: Visualizacion de la cuota por cada segmento.

TECNOLOGIAS UTILIZADAS:
- Python 3.x (Lenguaje principal)
- Scikit-Learn (Algoritmo de Clustering K-Means)
- Pandas (Manipulacion y estructuracion de perfiles)
- Seaborn & Matplotlib (Analisis visual de datos)

VALOR AGREGADO:
- Segmentacion Automatizada: Sustituye el analisis manual por una agrupacion 
  matematica precisa basada en la distancia entre perfiles de compra.
- Accionabilidad Directa: El sistema genera reportes que el equipo de marketing 
  puede utilizar inmediatamente para campañas de email o promociones.
- Escalabilidad: La arquitectura permite procesar miles de clientes y 
  actualizar los segmentos en tiempo real conforme cambian los datos en la DB.

=======================================================================================