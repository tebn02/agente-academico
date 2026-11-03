
import streamlit as st

from core.agent import AgenteAcademico


st.set_page_config(
    page_title="Agente Académico",
    page_icon="🎓",
    layout="centered"
)


# Inicializar agente e historial
if "agente" not in st.session_state:
    st.session_state.agente = AgenteAcademico()

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []


# Barra lateral
with st.sidebar:
    st.title("🎓 Agente Académico")
    st.write("Asistente para organizar tus actividades académicas.")

    st.divider()

    st.subheader("Opciones")

    if st.button("🗑️ Limpiar conversación", use_container_width=True):
        st.session_state.mensajes = []
        st.session_state.agente = AgenteAcademico()
        st.rerun()

    st.divider()

    st.subheader("Conversación")
    cantidad_mensajes = len(st.session_state.mensajes)
    st.metric("Mensajes en el historial", cantidad_mensajes)

    st.divider()
    st.caption("Proyecto académico - Versión P4")


# Encabezado principal
st.title("🎓 Agente Académico")
st.write("Consulta tus horarios y resuelve dudas académicas.")

st.divider()


# Mostrar historial de conversación
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["rol"]):
        st.write(mensaje["contenido"])


# Entrada del usuario
mensaje_usuario = st.chat_input(
    "Escribe tu consulta académica..."
)


# Procesar consulta
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
        try:
            with st.spinner("Analizando tu consulta..."):
                respuesta = st.session_state.agente.responder(
                    mensaje_usuario
                )

            st.write(respuesta)

        except Exception as e:
            respuesta = "Ocurrió un error al procesar tu consulta. Inténtalo nuevamente."
            st.error(respuesta)

            # Mostrar detalles técnicos en la terminal
            print(f"ERROR DEL AGENTE: {type(e).__name__}: {e}")

    st.session_state.mensajes.append(
        {
            "rol": "assistant",
            "contenido": respuesta
        }
    )

    st.rerun()
