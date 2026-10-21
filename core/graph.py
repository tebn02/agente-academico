
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from chains.academic_chain import crear_cadena
from tools.horario_tool import consultar_horario


class EstadoGrafo(TypedDict):
    pregunta: str
    tipo_consulta: str
    dia: str
    respuesta: str


DIAS = [
    "lunes",
    "martes",
    "miercoles",
    "miércoles",
    "jueves",
    "viernes",
]


def clasificar_consulta(estado: EstadoGrafo):
    pregunta = estado["pregunta"].lower()

    if "horario" in pregunta:
        for dia in DIAS:
            if dia in pregunta:
                dia_normalizado = (
                    "miercoles" if dia == "miércoles" else dia
                )
                return {
                    "tipo_consulta": "horario",
                    "dia": dia_normalizado,
                }

    return {"tipo_consulta": "general"}


def decidir_ruta(estado: EstadoGrafo):
    return estado["tipo_consulta"]


def consultar_horario_nodo(estado: EstadoGrafo):
    resultado = consultar_horario(estado["dia"])
    return {"respuesta": resultado}


def consultar_gemini_nodo(estado: EstadoGrafo):
    cadena = crear_cadena()
    resultado = cadena.invoke({
        "pregunta": estado["pregunta"]
    })

    if isinstance(resultado.content, list):
        texto = "".join(
            bloque.get("text", "")
            for bloque in resultado.content
            if isinstance(bloque, dict)
            and bloque.get("type") == "text"
        )
    else:
        texto = str(resultado.content)

    return {"respuesta": texto}


def crear_grafo():
    grafo = StateGraph(EstadoGrafo)

    grafo.add_node("clasificar", clasificar_consulta)
    grafo.add_node("horario", consultar_horario_nodo)
    grafo.add_node("gemini", consultar_gemini_nodo)

    grafo.add_edge(START, "clasificar")

    grafo.add_conditional_edges(
        "clasificar",
        decidir_ruta,
        {
            "horario": "horario",
            "general": "gemini",
        }
    )

    grafo.add_edge("horario", END)
    grafo.add_edge("gemini", END)

    return grafo.compile()
