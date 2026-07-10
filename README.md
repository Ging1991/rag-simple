# Sistema de Recuperación Aumentada por Generación (RAG) Local: Evaluación de Modos Estático y Adaptativo

## Contexto Académico
* **Institución:** Universidad Nacional de General Sarmiento (UNGS)
* **Asignatura:** Sistemas Operativos y Redes 2
* **Tipo de Trabajo:** Trabajo Final Individual
* **Autor Principal y Desarrollador:** Carlos Enrique Caballero Morel
* **Coautor y Director Académico:** Prof. Benjamín Chuquimango
---

## Descripción del Proyecto y Pipeline

Este proyecto implementa y evalúa un sistema simplificado de tipo **RAG (Retrieval-Augmented Generation) Local** diseñado específicamente para responder consultas sobre eventos históricos. El sistema permite al usuario interactuar a través de la consola bajo dos modalidades de funcionamiento bien diferenciadas con el objetivo de contrastar su rendimiento, precisión y consumo de recursos informáticos:

1. **Modo Estático (RAG Clásico):** Recupera la información del dataset de manera lineal y predecible a través de una configuración fija de recuperación de datos.
2. **Modo Dinámico (RAG Adaptativo):** Preprocesa la pregunta del usuario para determinar de forma inteligente la estrategia de recuperación óptima (actuando de manera estricta o flexible según la naturaleza de la consulta).

Al iniciar la aplicación, el usuario puede seleccionar el modo de ejecución. A lo largo del proceso, la interfaz de consola expone de forma transparente los pasos internos de la arquitectura (procesamiento de la consulta, recuperación del contexto y generación de la respuesta final).

---

## Arquitectura y Modelos Compactos Evaluados

En el desarrollo de este Trabajo Final se profundizó en el estudio y la implementación práctica de la arquitectura RAG, analizando las siguientes variantes:
* **Enfoque RAG Estático:** Se evaluó bajo dos perfiles de configuración manual:
  * *Configuración Estricta y Precisa:* Alta selectividad de datos, óptima para consultas específicas de fechas o países puntuales.
  * *Configuración Flexible:* Mayor tolerancia en la búsqueda, ideal para consultas conceptuales pero con riesgo de incluir ruido en el contexto.
* **Enfoque RAG Adaptativo (Dinámico):** Implementación de una lógica de ruteo de consultas y preprocesamiento que adapta dinámicamente los parámetros de búsqueda del recuperador en función del input del usuario.

---

## Descripción del Dataset

El sistema opera de forma local y exclusiva sobre una base de conocimiento estructurada en formato JSON, la cual recopila eventos históricos clasificados por país y año. Ubicación del archivo: `datos/DATOS.json`

**Formato de los datos:**
```json
{
  "eventos": [
    {
      "pais": "ARGENTINA",
      "fecha": "1874",
      "evento": "En 1874 en Argentina Nicolas Avellaneda asume la presidencia."
    }
  ]
}
```

## Instalación y Requisitos

### Requisitos de Software

1.  **Python 3.10 o superior**
    
2.  **Ollama:** El sistema requiere que el servicio de Ollama esté instalado y ejecutándose localmente (`localhost`).
    
3.  **Librerías de Python:** Dependencias de la API de Ollama (se pueden instalar mediante `pip install ollama`).
    
4.  **Modelo de Lenguaje (LLM):** A elección del usuario a través de Ollama (el rendimiento del RAG dependerá directamente del modelo compacto local seleccionado). Puntualmente se utilizó _"Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"_, pero el usuario puede optar por otro.
    

### Entorno de Pruebas (Hardware de Referencia)

El sistema fue evaluado localmente con las siguientes especificaciones técnicas:

-   **Sistema Operativo:** Windows 10
    
-   **Memoria RAM:** 8 GB
    
-   **Tarjeta Gráfica (GPU):** AMD Radeon RX 590 (8 GB VRAM)
    
-   _Nota: Los requerimientos de hardware definitivos variarán en función de la escala del modelo LLM que el usuario decida descargar en Ollama._

## 🛠️ Instalación y Configuración

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 📋 Prerrequisitos

Antes de empezar, asegúrate de tener instalado lo siguiente en tu sistema:
* **Python 3.10 o superior**
* **Git**
---
### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local y accede a la carpeta del proyecto:
```bash
git clone https://github.com/core-lab-ungs/local-rag-adaptive-chatbot
```
### 2. Configurar Ollama (Modelos Locales)

Este sistema RAG utiliza Ollama para procesar las consultas de forma local.

1.  Descarga e instala Ollama desde su [sitio oficial](https://ollama.com/).
    
2.  Abre tu terminal y descarga un modelo utilizar (por ejemplo, `llama3` o `mistral`):
```
ollama pull llama3
```

3.  Asegúrate de que el servicio de Ollama se esté ejecutando en segundo plano antes de iniciar la aplicación.
    

### 3. Instalar Dependencias de Python

Instala la librería oficial de Ollama directamente en tu sistema utilizando el archivo de requerimientos incluido:
```
pip install -r requirements.txt
```

### 4. Ejecución del RAG

Con Ollama corriendo y las dependencias instaladas, ya puedes ejecutar el script principal:
```
python main.py
```
---
## Metodología, Resultados y Limitaciones

### Metodología de Evaluación

Se realizó una validación experimental manual aplicando un mismo conjunto de preguntas de prueba a ambos modos del sistema. Se analizaron las respuestas del RAG Estático (tanto en su variante estricta como flexible) frente a las respuestas obtenidas por el RAG Adaptativo, evaluando la pertinencia del contexto recuperado y la coherencia de la respuesta final.

### Resultados Obtenidos

Las pruebas demostraron que el **Modo Adaptativo (Dinámico) presenta una clara tendencia a resolver mejor las consultas generales y complejas**, ya que emula el comportamiento de los perfiles estricto o flexible según la necesidad de la pregunta. Se verificó que en el modo estático, cuando la configuración flexible fallaba, la estricta acertaba, y viceversa; el modo adaptativo logró mitigar este problema balanceando ambos enfoques. Como contrapartida experimental, el modo adaptativo demanda un mayor costo y tiempo de cómputo debido a la etapa previa de análisis de la consulta.
### Preguntas especificas
A continuación se señalan las preguntas (y peticiones) puntuales que se hicieron durante las pruebas para cada uno de los modos: Clásico Estricto, Clásico Flexible y Adaptativo, junto con el resultado obtenido y una interpretación del mismo.

_Dime una lista de eventos históricos ocurridos en 2022._
FLEXIBLE - ACIERTA: Menciona los 2 eventos correspondientes.
ESTRICTO - FALLA: Al no mencionar un país, no recupera ningún contexto.
ADAPTATIVO - ACIERTA: Responde similar al flexible. El pre procesamiento decidió que el año debía ser si o si 2022 pero el país podría ser cualquiera, además clasificó la pregunta como larga por eso recupero varios eventos.

_Dame una lista de eventos históricos ocurridos en Argentina._
FLEXIBLE - ACIERTA: Menciona hasta 5 eventos correctamente.
ESTRICTO - FALLA: Al no mencionar ningún año, no recupera ningún contexto.
ADAPTATIVO - ACIERTA: Responde similar al flexible. Se considera que el año es obligatorio pero el país no, además de que se trataba de una pregunta larga por lo que recuperó un contexto amplio.

_Dame una lista de eventos ocurridos en Argentina en 2022._
FLEXIBLE - ACIERTA: Devuelve los 2 eventos.
ESTRICTO - ACIERTO PARCIAL: Devuelve 1 de los 2 eventos en la base de datos. Esto se debe a que el límite es bajo y solo puede recuperar un evento como máximo, dejando otro afuera, que en este caso era igual de importante.
ADAPTATIVO - ACIERTA: Responde similar al flexible.

_¿En qué año salió Argentina campeón del mundo?_
FLEXIBLE - ACIERTA: Responde bien.
ESTRICTO - FALLA: Al no mencionar ningún año, no recupera ningún contexto.
ADAPTATIVO - FALLA: No consideró que el año fuera obligatorio, a la vez que asumió que la pregunta era corta. Esto fue un fallo en el módulo de preprocesamiento que no fue capaz de clasificar bien la pregunta.

_¿Qué ocurrió en Argentina en 2001?_
FLEXIBLE - FALLA: Trajo demasiada información y el evento de 2001 en Argentina no entró al contexto (supera el límite de 5).
ESTRICTO - ACIERTO PARCIAL: Técnicamente es una respuesta correcta, pero da más información de la que provee el contexto, y eso podría ser señal de que no lo está usando. Por lo que este caso es dudoso.
ADAPTATIVO - ACIERTO PARCIAL: Responde similar al estricto.

_Dame una lista de eventos ocurridos en Argentina entre 2000 y 2002._
_(Nota: el único evento correcto es la crisis financiera de 2001.)_
FLEXIBLE - FALLA: Falló porque trajo demasiada información y no trajo el dato puntual.
ESTRICTO - FALLA: No trajo contexto porque busca por coincidencia exacta en 2000 y 2002, y el evento buscado es de 2001. No busca por rangos.
ADAPTATIVO - FALLA: Procesó bien la pregunta, pero falló de la misma forma que el modo flexible. Trajo muchos datos, y el dato relevante no llegó a entrar al contexto por falta de espacio.


### Limitaciones del Sistema

-   **Dominio Cerrado:** El agente de chat está estrictamente restringido al dominio de la base de conocimiento local. No procesa ni responde consultas ajenas a eventos históricos.
    
-   **Dependencia del JSON:** El conocimiento del sistema es estático y limitado a los eventos explícitamente indexados en el origen de datos de `DATOS.json`.
    

## Estado y Licencia
-   **Estado:** Repositorio institucional privado, en revisión técnica y académica.
 -   **Licencia:**  Pendiente de definición.