from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate
)
# from langchain_core.pydantic_v1 import BaseModel, Field # Mantenemos esto para referencia futura, pero no lo usaremos en este paso

# 1. Plantilla para los ejemplos de Few-Shot
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

# 2. Plantilla general del sistema
general_system_template = """
Eres un bot de soporte técnico amigable y servicial para una aplicación ficticia.
Tu objetivo es ayudar a los usuarios con sus problemas técnicos.

Responde de manera concisa y profesional.

Si el usuario te reporta un problema, tu tarea es extraer la información clave y devolverla en un formato JSON estructurado, tal como se muestra en los ejemplos.

Si la pregunta del usuario es una consulta general, como "cómo reiniciar la contraseña" o "dónde ver el estado de la cuenta", responde de manera útil y concisa, siguiendo el estilo de los ejemplos proporcionados.

A continuación, se presentan algunos ejemplos de interacciones para que sigas mi estilo y comportamiento.

Historial de conversación:
{history}
"""