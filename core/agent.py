from config.settings import validar_configuracion
from core.state import AgentState
from tools.horario_tool import consultar_horario
from chains.academic_chain import crear_cadena


class AgenteAcademico:
    def __init__(self):
        validar_configuracion()

        self.cadena = crear_cadena()
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

        respuesta = self.cadena.invoke(
            {"pregunta": mensaje}
        )

        if isinstance(respuesta.content, list):
            texto_respuesta = ""
            for bloque in respuesta.content:
                if isinstance(bloque, dict) and bloque.get("type") == "text":
                    texto_respuesta += bloque.get("text", "")
        else:
            texto_respuesta = respuesta.content

        self.state.agregar_mensaje(
            "Asistente",
            texto_respuesta
        )

        return texto_respuesta