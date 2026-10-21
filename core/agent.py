
from config.settings import validar_configuracion
from core.state import AgentState
from core.graph import crear_grafo


class AgenteAcademico:
    def __init__(self):
        validar_configuracion()
        self.state = AgentState()
        self.grafo = crear_grafo()

    def responder(self, mensaje: str) -> str:
        resultado = self.grafo.invoke({
            "pregunta": mensaje,
            "tipo_consulta": "",
            "dia": "",
            "respuesta": "",
        })

        respuesta = resultado["respuesta"]

        self.state.agregar_mensaje("Usuario", mensaje)
        self.state.agregar_mensaje("Asistente", respuesta)

        return respuesta
