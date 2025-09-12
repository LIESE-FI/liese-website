# Makefile para la documentación LaTeX del proyecto MQTT-PostgreSQL

# Variables
MAIN_DOC = A0-main
BUILD_DIR = build
DOCS_DIR = docs
PDF_NAME = MQTT_PostgreSQL_Documentation

# Comandos LaTeX
LATEX = pdflatex
BIBTEX = bibtex

# Opciones para pdflatex
LATEX_OPTS = -interaction=nonstopmode -halt-on-error -shell-escape

.PHONY: all clean build help view install-deps

# Objetivo principal
all: build

# Compilar el documento
build: $(BUILD_DIR)/$(PDF_NAME).pdf

$(BUILD_DIR)/$(PDF_NAME).pdf: $(DOCS_DIR)/$(MAIN_DOC).tex
	@echo "Compilando documentación LaTeX..."
	@mkdir -p $(BUILD_DIR)
	@cd $(DOCS_DIR) && $(LATEX) $(LATEX_OPTS) -output-directory=../$(BUILD_DIR) $(MAIN_DOC).tex
	@cd $(DOCS_DIR) && $(LATEX) $(LATEX_OPTS) -output-directory=../$(BUILD_DIR) $(MAIN_DOC).tex
	@mv $(BUILD_DIR)/$(MAIN_DOC).pdf $(BUILD_DIR)/$(PDF_NAME).pdf
	@echo "✅ Documentación compilada: $(BUILD_DIR)/$(PDF_NAME).pdf"

# Limpiar archivos temporales
clean:
	@echo "Limpiando archivos temporales..."
	@rm -rf $(BUILD_DIR)
	@echo "✅ Limpieza completada"

# Compilación rápida (una sola pasada)
quick: 
	@echo "Compilación rápida de documentación..."
	@mkdir -p $(BUILD_DIR)
	@cd $(DOCS_DIR) && $(LATEX) $(LATEX_OPTS) -output-directory=../$(BUILD_DIR) $(MAIN_DOC).tex
	@mv $(BUILD_DIR)/$(MAIN_DOC).pdf $(BUILD_DIR)/$(PDF_NAME).pdf
	@echo "✅ Compilación rápida completada"

# Ver el PDF generado
view: $(BUILD_DIR)/$(PDF_NAME).pdf
	@if command -v xdg-open >/dev/null 2>&1; then \
		xdg-open $(BUILD_DIR)/$(PDF_NAME).pdf; \
	elif command -v open >/dev/null 2>&1; then \
		open $(BUILD_DIR)/$(PDF_NAME).pdf; \
	else \
		echo "Por favor, abra manualmente: $(BUILD_DIR)/$(PDF_NAME).pdf"; \
	fi

# Instalar dependencias de LaTeX (Ubuntu/Debian)
install-deps:
	@echo "Instalando dependencias de LaTeX..."
	@sudo apt-get update
	@sudo apt-get install -y texlive-full texlive-latex-extra texlive-fonts-recommended
	@sudo apt-get install -y python3-pygments  # Para minted
	@echo "✅ Dependencias instaladas"

# Verificar sintaxis de todos los archivos .tex
check:
	@echo "Verificando sintaxis de archivos LaTeX..."
	@for file in $(DOCS_DIR)/*.tex; do \
		echo "Verificando $$file..."; \
		cd $(DOCS_DIR) && $(LATEX) -interaction=nonstopmode -halt-on-error \
			-output-directory=/tmp "$$(basename $$file)" >/dev/null 2>&1 && \
		echo "✅ $$file - OK" || echo "❌ $$file - ERROR"; \
	done

# Contar palabras en el documento
wordcount:
	@echo "Contando palabras en la documentación..."
	@detex $(DOCS_DIR)/*.tex | wc -w
	@echo "palabras en total"

# Generar tabla de contenido de archivos
toc:
	@echo "=== Estructura de la Documentación ==="
	@echo
	@for file in $(DOCS_DIR)/*.tex; do \
		if [ "$$(basename $$file)" != "A0-main.tex" ] && [ "$$(basename $$file)" != "A1-Portada.tex" ]; then \
			echo "📄 $$(basename $$file)"; \
			grep "\\\\chapter{" $$file 2>/dev/null | sed 's/.*{\\(.*\\)}.*/  └─ \\1/' || true; \
			grep "\\\\section{" $$file 2>/dev/null | head -3 | sed 's/.*{\\(.*\\)}.*/    ├─ \\1/' || true; \
		fi; \
	done

# Ayuda
help:
	@echo "Makefile para Documentación LaTeX - Proyecto MQTT-PostgreSQL"
	@echo
	@echo "Objetivos disponibles:"
	@echo "  build        - Compilar la documentación completa (2 pasadas)"
	@echo "  quick        - Compilación rápida (1 pasada)"
	@echo "  clean        - Limpiar archivos temporales"
	@echo "  view         - Abrir el PDF generado"
	@echo "  check        - Verificar sintaxis de archivos LaTeX"
	@echo "  wordcount    - Contar palabras en la documentación"
	@echo "  toc          - Mostrar estructura de la documentación"
	@echo "  install-deps - Instalar dependencias de LaTeX (Ubuntu/Debian)"
	@echo "  help         - Mostrar esta ayuda"
	@echo
	@echo "Ejemplos:"
	@echo "  make build   # Compilar documentación"
	@echo "  make view    # Compilar y abrir PDF"
	@echo "  make clean   # Limpiar archivos temporales"

# Objetivo por defecto cuando se ejecuta solo 'make'
.DEFAULT_GOAL := help
