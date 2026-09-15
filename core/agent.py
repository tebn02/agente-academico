from google import genai

from config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    validar_configuracion,
)
from core.state import AgentState
from tools.horario_tool import consultar_horario


class AgenteAcademico:
    def __init__(self):
        validar_configuracion()

        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.state = AgentState()

    def responder(self, mensaje: str) -> str:
        self.state.agregar_mensaje("Usuario", mensaje)

        mensaje_lower = mensaje.lower()

        dias = [
            "lunes",
            "martes",
            "miercoles",
            "miércoles",
            "jueves",
            "viernes",
        ]

        if "horario" in mensaje_lower:
            for dia in dias:
                if dia in mensaje_lower:
                    dia_consulta = "miercoles" if dia == "miércoles" else dia
                    resultado = consultar_horario(dia_consulta)

                    self.state.agregar_mensaje(
                        "Asistente",
                        resultado
                    )

                    return resultado

        historial = self.state.obtener_historial()

        instrucciones = f"""
Eres un asistente académico inteligente.

Tu objetivo es ayudar a estudiantes universitarios a organizar
sus actividades académicas.

Puedes:
- Ayudar a organizar tareas.
- Recomendar qué actividad realizar primero.
- Analizar fechas de entrega.
- Ayudar a establecer prioridades.
- Orientar al estudiante sobre su organización académica.

No debes:
- Inventar información académica.
- Modificar fechas establecidas por profesores.
- Eliminar actividades sin autorización.
- Realizar o enviar trabajos automáticamente.

Historial de conversación:
{historial}

Solicitud actual del estudiante:
{mensaje}

Responde de manera clara, breve y útil.
"""

        respuesta = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=instrucciones,
        )

        texto_respuesta = respuesta.text

        self.state.agregar_mensaje(
            "Asistente",
            texto_respuesta
        )

        return texto_respuesta
    