# Diseño simple de RAG Adaptativo

Este proyecto para la facultad implementa un sistema **RAG (Retrieval-Augmented Generation)** local y modular utilizando **Ollama (Llama 3.1 8B / Dolphin)**. El sistema cuenta con dos modos de ejecución interactivos: un enfoque **Clásico** (con inyección estática de contexto) y un enfoque **Adaptativo** (*Adaptive RAG*), el cual utiliza capas previas de inferencia (clasificadores binarios de pocos disparos o *Few-Shot*) para enrutar la consulta y optimizar dinámicamente el tamaño del prompt.

🛠️ Requisitos e Instalación
Ollama instalado localmente.
Tener descargado el modelo correspondiente (por defecto configurado como Delfin o llama3.1):
Python 3.10+ instalado en tu entorno local.

Instalar la biblioteca oficial de Ollama para Python: pip install ollama

Para iniciar la suite interactiva, simplemente ejecuta el archivo principal desde la raíz del proyecto:
python main.py

Opciones del Menú Principal:
Opción 1 (Chat RAG Clásico): Abre un bucle interactivo donde cada pregunta inyecta un bloque de contexto fijo definido en las configuraciones. Para salir de este chat, ingresa el número 1.

Opción 2 (Chat RAG Adaptativo): Activa el enrutador inteligente. Analiza semánticamente la pregunta y decide si aplica filtros restrictivos en la base de datos antes de consultar al LLM.

Opción 3: Cierra el sistema.