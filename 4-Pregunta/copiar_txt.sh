#!/bin/bash

# Crear el directorio 'copias' si no existe
mkdir -p copias

# Buscar y copiar archivos .txt
for file in *.txt; do
  if [ -f "$file" ]; then
    cp "$file" "copias/${file%.txt}_copia.txt"
  fi
done