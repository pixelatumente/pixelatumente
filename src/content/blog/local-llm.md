---
title: "Cómo ejecutar un LLM local: Guía de instalación, configuración y mejores modelos"
description: "En esta guía práctica descubrirás, paso a paso, todo lo que necesitas para montar tu propio"
date: "2025-09-09"
---
**¿Quieres sacarle el máximo provecho a la Inteligencia Artificial sin depender de la nube, reduciendo costos y garantizando la privacidad de tus datos?**
En esta guía práctica descubrirás, paso a paso, todo lo que necesitas para montar tu propio **local LLM**, desde el hardware indispensable hasta la selección del modelo ideal, pasando por las herramientas más amigables como **LM Studio AI** y **Ollama**, y la opción de ejecutarlos dentro de un contenedor **Ollama Docker**.

---

## Índice rápido

---

---

## 1. ¿Qué es un **local LLM** y por qué usarlo?

### 1.1 Definición sencilla

Un **Large Language Model** (LLM) es un modelo de IA entrenado con millones o miles de millones de parámetros para generar texto, código y, en algunos casos, interpretar imágenes. Cuando decimos *local* LLM nos referimos a que el modelo se ejecuta **en tu propio ordenador o servidor** en vez de en los servidores de una empresa externa.

### 1.2 Ventajas principales

---

---

## 2. Hardware recomendado

Ejecutar un LLM local no es magia; requiere recursos suficientes para que el modelo cargue en la memoria de la GPU y pueda responder en tiempo razonable. A continuación, la configuración mínima y la recomendada para diferentes tamaños de modelo.

### 2.1 GPU y VRAM (el factor crítico)

---
### 2.2 CPU y RAM

- **CPU:** Un procesador de 6‑8 núcleos (AMD Ryzen 5 5600X, Intel i5‑12400) es suficiente. Si vas a usar Docker intensivo o ejecutar varios contenedores simultáneos, opta por 8‑12 núcleos.

- **RAM:** Igual o superior a la VRAM de tu GPU (p.ej., 24 GB de RAM para una GPU de 12 GB). Con **32 GB** tendrás margen para cargar varios modelos o versiones cuantizadas.

### 2.3 Almacenamiento

- **SSD NVMe** de al menos **500 GB**. Los modelos pueden ocupar entre 4 GB y 80 GB cada uno, y el SSD garantiza una carga de modelo en segundos en vez de minutos.

- **Backup**: Un disco duro externo o NAS para guardar checkpoints y datasets personalizados.

### 2.4 Tip especial para Apple Silicon

Los chips **M1, M2, M3** cuentan con Unified Memory Architecture (UMA). Con **32 GB** de RAM puedes ejecutar modelos de hasta 13 B sin problemas, aunque la velocidad de inference será ligeramente menor que en una GPU dedicada de NVIDIA.

---

## 3. Software esencial

### 3.1 Categorías de software

---

### 3.2 Por qué elegir **LM Studio AI** o **Ollama**

- **LM Studio AI**: Interfaz visual amigable, búsqueda de modelos en Hugging Face directamente desde la app, compatibilidad multi‑plataforma. Ideal para principiantes y usuarios que prefieren “click‑and‑run”.

- **Ollama**: Ligero, basado en CLI, excelente para scripts y automatizaciones. Soporta **Ollama Docker**, lo que permite escalar o compartir el entorno con otros usuarios.
---

## 4. Instalación de **LM Studio AI**

A continuación, los pasos para cada sistema operativo. Todos los comandos se pueden ejecutar desde una terminal (PowerShell, iTerm, etc.).

### 4.1 Windows

1. **Descarga** el instalador desde [https://lmstudio.ai/download](https://lmstudio.ai/download).

1. Ejecuta el archivo **.exe** y sigue el asistente; elige la carpeta de instalación (recomendado: C:\Program Files\LMStudio).

1. Al iniciar la app, permite que descargue los **drivers CUDA** si tu GPU es NVIDIA.

1. En la pestaña *Model Hub*, busca “Llama‑3 8B Q4_K_M”. Haz clic en **Download** → **Load**.

1. Configura la **memoria de la GPU**: *Settings → Advanced → GPU VRAM limit* (ej. 10 GB).

1. ¡Listo! Empieza a chatear con el modelo desde la interfaz.

### 4.2 macOS (Apple Silicon & Intel)

1. **Homebrew**: brew install --cask lmstudio.

1. Si usas **M1/M2**, LM Studio detectará automáticamente la arquitectura y usará **Metal** como backend.

1. Abre la app desde *Launchpad* y sigue los mismos pasos de descarga de modelo que en Windows.

### 4.3 Linux (Ubuntu/Debian)

```
# 1. Instala dependencias
sudo apt update && sudo apt install -y curl git unzip

# 2. Descarga el tarball
curl -L -o lmstudio.tar.gz https://downloads.lmstudio.ai/linux/latest

# 3. Extrae
tar -xzf lmstudio.tar.gz -C $HOME/.local/share/

# 4. Añade al PATH
echo 'export PATH=$HOME/.local/share/lmstudio:$PATH' >
~/.bashrc
source ~/.bashrc

# 5. Ejecuta
lmstudio
```
**Tip**: En sistemas sin GPU, LM Studio soporta inference en CPU mediante **ggml**; sin embargo la latencia será alta (>10 s por respuesta).

### 4.4 Configuración avanzada (opcional)

---

---

## 5. Instalación de **Ollama**

### 5.1 Versión nativa (macOS, Linux, Windows)

1. **macOS (Homebrew)**

```
 brew install ollama
```

1. **Linux (Debian/Ubuntu)**

```
 curl -fsSL https://ollama.com/install.sh | sh
```

1. **Windows (Scoop)**

```
 scoop install ollama
```

1. Verifica la instalación: ollama --version.

1. Descarga un modelo (ej.: Llama‑3 8B):

```
 ollama pull llama3
```

1. Ejecuta el modelo en modo chat:

```
 ollama run llama3
```

### 5.2 **Ollama Docker** (ideal para entornos aislados)

```
# docker‑compose.yml
version: "3.8"
services:
 ollama:
 image: ollama/ollama:latest
 container_name: ollama
 restart: unless‑stopped
 ports:
 - "11434:11434" # API REST
 - "8080:8080" # UI opcional (OpenWebUI)
 volumes:
 - ./ollama_data:/root/.ollama # Persistencia de modelos
 environment:
 - OLLAMA_NUM_THREADS=8
 - OLLAMA_MAX_CTX=4096
 deploy:
 resources:
 reservations:
 devices:
 - driver: nvidia
 count: all
 capabilities: [gpu]
```

1. **Crear la carpeta**: mkdir -p ollama_data.

1. **Iniciar**: docker compose up -d.

1. **Descargar modelo** dentro del contenedor:

```
 docker exec -it ollama ollama pull llama3
```

1. **Acceder a la API**: http://localhost:11434/api/generate.
### 5.3 Integración con **OpenWebUI** (interfaz web ligera)

```
docker run -d \
 -p 8080:8080 \
 -v $(pwd)/openwebui:/app/backend/data \
 --restart unless‑stopped \
 ghcr.io/open-webui/open-webui:latest
```

Conecta la UI a Ollama mediante la variable de entorno OLLAMA_HOST=http://ollama:11434. Así podrás chatear con el modelo desde cualquier navegador.

---

## 6. Los mejores modelos para correr localmente

A continuación, una tabla que resume los principales modelos open‑source disponibles en **Hugging Face** y compatibles con **LM Studio** y **Ollama**. Se incluyen detalles de tamaño, requisitos de VRAM y caso de uso recomendado.

---

*VRAM mínima estimada para ejecutar el modelo **sin offloading**. Con técnicas de *CPU offload* puedes reducir este número, pero la latencia aumentará.

### 6.1 Cómo elegir el modelo ideal

1. **Define el caso de uso**: Chat general → Llama‑3 8B; generación de código → Qwen‑2.5‑Coder; razonamiento profundo → Mixtral‑8x7B.

1. **Comprueba tu VRAM**: Si dispones de 12 GB, evita modelos >13 B sin cuantización avanzada.

1. **Evalúa la licencia**: Algunas empresas requieren que los modelos sean usados bajo licencia compatible con su política de datos.

1. **Prueba cuantizaciones**: Los formatos **GGUF Q4 / Q5** reducen el consumo de VRAM hasta un 60 % con pérdida mínima de calidad.

---

## 7. Optimización y cuantización

### 7.1 Qué es la cuantización

Consiste en representar los pesos del modelo con menos bits (por ejemplo, 4 bits en vez de 16 bits). El objetivo es **reducir la memoria ocupada** y **acelerar la inferencia**. Los principales formatos son:

---

### 7.2 Herramientas para cuantizar

- **gguf-convert** (incluido en Ollama)

- **lmstudio-quantize** (CLI de LM Studio)

- **torch.quantization** (para usuarios de PyTorch)

#### Paso a paso: cuantizar un modelo con LM Studio

```
lmstudio quantize \
 --model llama3-8b \
 --output llama3-8b-q4.gguf \
 --bits 4 \
 --format q4_k_m
```

Una vez convertido, cárgalo desde la UI de LM Studio seleccionando *Add local model* y eligiendo el archivo .gguf.

### 7.3 Offloading a CPU

Si tu GPU tiene menos memoria que el modelo, puedes usar **offload** (carga parcial en GPU y el resto en RAM). En **Ollama**, agrega la variable:

```
export OLLAMA_GPU_OFFLOAD=0.5 # 50 % del modelo en GPU, 50 % en RAM
```

En **LM Studio**, habilita *GPU Offload* desde *Settings → Advanced* y elige el porcentaje deseado.

---

## 8. Integración con herramientas de automatización

### 8.1 Usando la API REST de Ollama

```
curl -X POST http://localhost:11434/api/generate \
 -H "Content-Type: application/json" \
 -d '{
 "model": "llama3",
 "prompt": "Resume las novedades de la IA en 2025 en 3 párrafos.",
 "max_tokens": 300,
 "temperature": 0.6
 }'
```

La respuesta JSON contiene el texto generado, que puedes usar en scripts Python, Bash o incluso en herramientas **no‑code** como **n8n**.

### 8.2 Conexión a **n8n** (workflow de automatización)

1. Crear un **HTTP Request** node con la URL http://localhost:11434/api/generate.

1. Configurar el cuerpo con *JSON* (ver ejemplo anterior).

1. Añadir un **Set** node para formatear la salida (por ejemplo, enviar por correo, guardar en base de datos o publicar en Slack).

1. Ejecutar el workflow automáticamente al recibir un email o al detectar un archivo nuevo en una carpeta.

### 8.3 Scripts de ejemplo (Python)

```
import requests, json

def ask_llm(prompt, model="llama3"):
 url = "http://localhost:11434/api/generate"
 payload = {
 "model": model,
 "prompt": prompt,
 "max_tokens": 512,
 "temperature": 0.7
 }
 resp = requests.post(url, json=payload)
 return resp.json()["response"]

print(ask_llm("Explica la diferencia entre LLM y ChatGPT en menos de 100 palabras."))
```

Con este script puedes crear *chatbots locales* o generar contenido para blogs sin tocar la nube.

---

## 9. Solución de problemas comunes

---

---

## 10. Recursos adicionales

****[](https://github.com/ollama/ollama)****[](https://lmstudio.ai/download)****[](https://huggingface.co/models)****[](https://discord.gg/ollama)****[](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)****[](https://github.com/n8n-io/n8n/tree/master/workflows)****[](https://arxiv.org/abs/2409.11234)
