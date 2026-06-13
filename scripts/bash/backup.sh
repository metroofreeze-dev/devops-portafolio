#!/bin/bash

# ==========================================
# Script de Backup — DevOps Semana 1
# Autor: Metroofreeze
# Descripción: Copia archivos importantes con fecha
# ==========================================

# Variables
FECHA=$(date '+%Y%m%d_%H%M%S')
ORIGEN="$HOME/Dev/devops-semana1"
DESTINO="$HOME/Dev/backups"
NOMBRE_BACKUP="backup_$FECHA"

hacer_backup() {
    echo "=== Iniciando Backup ==="
    echo "Fecha   : $FECHA"
    echo "Origen  : $ORIGEN"
    echo "Destino : $DESTINO/$NOMBRE_BACKUP"
    echo "---"

    # Crea la carpeta de destino si no existe
    mkdir -p "$DESTINO/$NOMBRE_BACKUP"

    # Copia los archivos
    cp -r "$ORIGEN/scripts" "$DESTINO/$NOMBRE_BACKUP/"
    cp -r "$ORIGEN/cheatsheet.md" "$DESTINO/$NOMBRE_BACKUP/"

    echo "Archivos copiados exitosamente"
    echo "Ubicación: $DESTINO/$NOMBRE_BACKUP"
    echo "=== Backup completado ==="
}

main() {
    hacer_backup
}

main