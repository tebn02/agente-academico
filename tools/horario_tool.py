import json
from pathlib import Path


RUTA_HORARIOS = Path(__file__).resolve().parent.parent / "data" / "horarios.json"


def consultar_horario(dia: str) -> str:
    dia_normalizado = dia.strip().lower()

    try:
        with open(RUTA_HORARIOS, "r", encoding="utf-8") as archivo:
            horarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return "No fue posible consultar la información de horarios."

    if dia_normalizado not in horarios:
        return f"No hay información disponible para el día {dia}."

    clases = horarios[dia_normalizado]

    if not clases:
        return f"No tienes clases registradas para el día {dia}."

    resultado = f"Horario del {dia_normalizado}:\n"

    for clase in clases:
        resultado += (
            f"- {clase['materia']}: {clase['hora']}, "
            f"aula {clase['aula']}\n"
        )

    return resultado
