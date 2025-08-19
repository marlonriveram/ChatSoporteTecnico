from typing import Dict # Permite tipar
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

# `store` es nuestro "almacén" de historial de conversaciones.
# Usamos un diccionario simple para guardar un historial por cada `session_id`.
# En un proyecto real, esto sería una base de datos como Redis o PostgreSQL.
# Dict[ la key tipo: string, valor: tipo BaseChatMessageHistory]
store: Dict[str, BaseChatMessageHistory] = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """
    Función que devuelve el historial de chat para un `session_id` dado.
    Si no existe, crea un nuevo historial en memoria.
    """
    # Si el `session_id` no está en nuestro almacén, creamos un nuevo historial.
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]