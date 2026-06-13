#!/bin/bash
# ==========================================
# Monitor del Sistema — DevOps Semana 1
# Autor: Metroofreeze
# Fecha: Junio 2026
# Descripción: Monitorea CPU, memoria y disco
# ==========================================

# Variables
FECHA=$(date '+%Y-%m-%d %H:%M:%S')
USUARIO=$(whoami)
HOSTNAME=$(hostname)

# Función principal de monitoreo
mostrar_encabezado() {
    echo "=========================================="
    echo " Monitor del Sistema - DevOps Semana 1"
    echo " Autor: Metroofreeze"
    echo " Fecha: $FECHA"
    echo " Usuario: $USUARIO"
    echo " Hostname: $HOSTNAME"
    echo "=========================================="
}

mostrar_cpu_memoria() {
    echo ""
    echo "--- CPU y Memoria ---"

    #Uso de CPU
    CPU=$(top -l 1 | grep "CPU usage" | awk '{print $3}')
    echo "CPU en uso  :$CPU"
    
    #Uso de Memoria
    MEMORIA=$(top -l 1 | grep "PhysMem" | awk '{print $2, $4, $6}')
    echo "Memoria  :$MEMORIA"
}

mostrar_disco() {
    echo""
    echo "--- Uso de Disco ---"
    df -h | grep -E "^/|Filesystem"
}

main() {
    mostrar_encabezado
    mostrar_cpu_memoria
    mostrar_disco
    echo ""
    echo "=========================================="
    echo "   Monitoreo completado"
    echo "=========================================="
}

# Punto de arranque
main