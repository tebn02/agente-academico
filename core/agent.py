
import time

from config.settings import validar_configuracion
from core.state import AgentState
from core.graph import crear_grafo


class AgenteAcademico:
    def __init__(self):
        validar_configuracion()
        self.state = AgentState()
        self.grafo = crear_grafo()

    def responder(self, mensaje: str) -> str:
        inicio = time.perf_counter()

        try:
            resultado = self.grafo.invoke({
                "pregunta": mensaje,
                "tipo_consulta": "",
                "dia": "",
                "respuesta": "",
            })

            respuesta = resultado["respuesta"]

            self.state.agregar_mensaje("Usuario", mensaje)
            self.state.agregar_mensaje("Asistente", respuesta)

            duracion = time.perf_counter() - inicio

            print(
                f"Tiempo total de consulta: {duracion:.3f} segundos"
            )

            return respuesta

        except Exception:
            duracion = time.perf_counter() - inicio

            print(
                f"Tiempo total hasta el error: {duracion:.3f} segundos"
            )

            raise
