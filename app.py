import streamlit as st

from core.agent import AgenteAcademico


st.set_page_config(
    page_title="Agente Académico",
    page_icon="🎓"
)

st.title("🎓 Agente Académico")
st.write(
    "Asistente inteligente para organizar tus actividades académicas."
)


if "agente" not in st.session_state:
    st.session_state.agente = AgenteAcademico()

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []


for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["rol"]):
        st.write(mensaje["contenido"])


mensaje_usuario = st.chat_input(
    "Escribe tu consulta académica..."
)

if mensaje_usuario:
    st.session_state.mensajes.append(
        {
            "rol": "user",
            "contenido": mensaje_usuario
        }
    )

    with st.chat_message("user"):
        st.write(mensaje_usuario)

    with st.chat_message("assistant"):
        with st.spinner("Analizando..."):
            respuesta = st.session_state.agente.responder(
                mensaje_usuario
            )

        st.write(respuesta)

    st.session_state.mensajes.append(
        {
            "rol": "assistant",
            "contenido": respuesta
        }
    )
    