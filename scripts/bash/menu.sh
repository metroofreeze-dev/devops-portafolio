#!/bin/bash
# ==========================================
# Menu Principal - DevOps Semana 1
# Autor: Metroofreeze
# Descripcion: Panel de control de scripts
# ==========================================

mostrar_menu() {
    echo ""
    echo "=========================================="
    echo "   Panel de Control - DevOps Semana 1"
    echo "=========================================="
    echo "  1. Monitor del sistema"
    echo "  2. Backup de archivos"
    echo "  3. Analizar logs"
    echo "  4. Consultar API"
    echo "  0. Salir"
    echo "=========================================="
    echo -n "  Selecciona una opcion: "
}

ejecutar_opcion() {
    local opcion=$1

    case $opcion in
        1)
            echo "Ejecutando monitor del sistema..."
            bash ~/Dev/devops-semana1/scripts/bash/monitor_sistema.sh
            ;;
        2)
            echo "Ejecutando backup..."
            bash ~/Dev/devops-semana1/scripts/bash/backup.sh
            ;;
        3)
            echo "Analizando logs..."
            python3 ~/Dev/devops-semana1/scripts/python/analizador_logs.py
            ;;
        4)
            echo "Consultando API..."
            python3 ~/Dev/devops-semana1/scripts/python/consumidor_api.py
            ;;
        0)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opcion invalida"
            ;;
    esac
}

main() {
    while true; do
        mostrar_menu
        read opcion
        ejecutar_opcion $opcion
        echo ""
        echo "Presiona Enter para continuar..."
        read
    done
}

main
