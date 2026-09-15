from dataclasses import dataclass, field


@dataclass
class AgentState:
    nombre: str = ""
    objetivo: str = ""
    historial: list[dict] = field(default_factory=list)

    def agregar_mensaje(self, rol: str, contenido: str) -> None:
        self.historial.append(
            {
                "rol": rol,
                "contenido": contenido
            }
        )

    def obtener_historial(self) -> str:
        if not self.historial:
            return "No hay conversación previa."

        return "\n".join(
            f"{mensaje['rol']}: {mensaje['contenido']}"
            for mensaje in self.historial
        )
    