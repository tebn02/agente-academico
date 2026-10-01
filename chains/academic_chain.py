from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from prompts.templates import SYSTEM_PROMPT

load_dotenv()


def crear_cadena():
    modelo = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{pregunta}")
    ])

    cadena = prompt | modelo

    return cadena