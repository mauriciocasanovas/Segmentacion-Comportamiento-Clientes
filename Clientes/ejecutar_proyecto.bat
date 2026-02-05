@echo off
title Sistema de Segmentacion de Clientes - K-Means
echo ==========================================================
echo   Analisis de Clusters y Perfiles de Consumo
echo ==========================================================
echo.

echo [1/1] Ejecutando motor de segmentacion...
python segmentacion_kmeans.py
if %errorlevel% neq 0 (echo Error en el proceso de clustering & pause & exit)
echo.

echo ==========================================================
echo   PROCESO FINALIZADO EXITOSAMENTE
echo   Reporte y graficos disponibles en la carpeta /Resultados
echo ==========================================================
pause