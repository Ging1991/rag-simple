# Diseño simple de RAG Adaptativo

Este proyecto implementa un sistema **RAG (Retrieval-Augmented Generation)** local y modular utilizando **Ollama (Llama 3.1 8B / Dolphin)**. El sistema cuenta con dos modos de ejecución interactivos: un enfoque **Clásico** (con inyección estática de contexto) y un enfoque **Adaptativo** (*Adaptive RAG*), el cual utiliza capas previas de inferencia (clasificadores binarios de pocos disparos o *Few-Shot*) para enrutar la consulta y optimizar dinámicamente el tamaño del prompt.

## 🚀 Características Principales

* **Motor RAG Adaptativo:** Clasifica la pregunta del usuario en tiempo de ejecución para determinar de forma dinámica si requiere filtrado estricto por Año, por País y el volumen de contexto óptimo (Top-K / Límite dinámico).
* **Pipeline Modular:** Código desacoplado en capas limpias de *Recuperación*, *Inferencia*, *Orquestación* e *Interfaz de usuario*.
* **Modo de Prueba de Estrés (Context Window Test):** Diseñado con un entorno robusto de control tipográfico para evaluar fenómenos como el *Lost in the Middle* (Pérdida de contexto en el centro) mediante la inyección de alta densidad de datos sintéticos/históricos.
* **Determinismo Estricto:** Configurado con `temperature: 0.0` y restricciones de tokens (`num_predict`) para mitigar alucinaciones y garantizar respuestas binarias estables en el enrutamiento.

---

## 📂 Estructura del Proyecto

La arquitectura modular se organiza de la siguiente manera desde la raíz de ejecución:

text
CODIGO/
├── main.py                 # Panel de control y punto de entrada principal
├── chat_rag_clasico.py     # Interfaz de bucle de consola para el modo clásico
├── config.json             # Archivo de configuración global de respaldo
├── datos/
│   └── eventos.json        # Base de datos histórica en formato JSON
├── fases/
│   ├── __init__.py
│   └── recuperacion.py     # Lógica de extracción, normalización y filtrado de datos
├── rag/
    ├── __init__.py
    ├── rag_clasico.py      # Orquestador del pipeline clásico
    └── inferencia.py       # Capa de IA pura (adaptar_anios, adaptar_paises, adaptar_limite)
🛠️ Requisitos e Instalación
Ollama instalado localmente.

Tener descargado el modelo correspondiente (por defecto configurado como Delfin o llama3.1):

Bash
ollama run llama3.1
Python 3.10+ instalado en tu entorno local.

Instalar la biblioteca oficial de Ollama para Python:

Bash
pip install ollama
💻 Uso del Sistema
Para iniciar la suite interactiva, simplemente ejecuta el archivo principal desde la raíz del proyecto:

Bash
python main.py
Opciones del Menú Principal:
Opción 1 (Chat RAG Clásico): Abre un bucle interactivo donde cada pregunta inyecta un bloque de contexto fijo definido en las configuraciones. Para salir de este chat, ingresa el número 1.

Opción 2 (Chat RAG Adaptativo): Activa el enrutador inteligente. Analiza semánticamente la pregunta y decide si aplica filtros restrictivos en la base de datos antes de consultar al LLM.

Opción 3: Cierra el sistema.

🔬 Experimentos de Contexto (Casos de Estudio)
El proyecto cuenta con capacidades analíticas documentadas sobre la ventana de atención de los LLM pequeños (8B):

0 a 30 Eventos (Zona Segura): Alta precisión y determinismo puro.

30 a 50 Eventos (Lost in the Middle): El modelo empieza a omitir información ubicada en el centro exacto del prompt, respondiendo con cláusulas de seguridad ("No tengo esa información").

50 a 60 Eventos (Saturación Semántica): El modelo experimenta entropía de atención, mezclando años y descripciones de eventos adyacentes por la alta redundancia estructural del JSON.

200+ Eventos (Desborde de Ventana): Se supera el búfer nativo de Ollama, aplicando una ventana deslizante (sliding window) que recorta las instrucciones del sistema del principio y fuerza al modelo a responder bajo su conocimiento base preentrenado.