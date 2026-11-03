# Agente Académico

Proyecto universitario desarrollado en Python y Streamlit para consultar horarios y responder preguntas académicas.

## Tecnologías utilizadas

- Python
- Streamlit
- LangChain
- LangGraph
- Gemini API

## Funcionalidades

- Consultar horarios académicos.
- Responder preguntas generales mediante Gemini.
- Mostrar el historial de conversación.
- Limpiar el historial desde la barra lateral.
- Mostrar un indicador mientras se procesa una consulta.
- Manejar errores de la API.
- Registrar tiempos de ejecución y llamadas a herramientas.

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tebn02/agente-academico.git
```

2. Entrar a la carpeta:

```bash
cd agente-academico
```

3. Crear un entorno virtual:

```bash
python -m venv .venv
```

4. Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

5. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

6. Crear un archivo `.env` con la clave de Gemini:

```env
GEMINI_API_KEY=tu_clave_api
```

7. Ejecutar la aplicación:

```bash
python -m streamlit run app.py
```

## Pruebas

Se realizaron pruebas de horarios, historial, limpieza de conversación, manejo de errores y métricas.

Las consultas generales presentaron errores 503 y 429 de la API de Gemini. La prueba debe repetirse cuando el servicio esté disponible y se restablezca la cuota.

Los resultados están documentados en `PRUEBAS_P4.md`.

## Despliegue

La aplicación se despliega mediante Streamlit Community Cloud.