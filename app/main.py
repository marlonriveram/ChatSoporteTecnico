import uuid
import json

from .core.chat_chain import chat_with_memory
from langchain_core.messages import AIMessage

# Definir un ID de sesión para este chat, simulando un usuario único
# En una aplicación web, esto se generaría por sesión de usuario.
SESSION_ID = str(uuid.uuid4())

print("¡Hola! Soy tu bot de soporte técnico. ¿En qué puedo ayudarte hoy? (Escribe 'salir' para terminar el chat)")

# Bucle principal de la conversación
while True:
    user_input = input("Tú: ")
    if user_input.lower() == 'salir':
        print("Bot: ¡Adiós! Que tengas un buen día.")
        break

    # La cadena que creamos en el Paso 4 es la que vamos a invocar.
    # Necesita el `input` del usuario y el `configurable` para el `session_id`.
    response = chat_with_memory.invoke(
    {"input": user_input},
    config={"configurable": {"session_id": SESSION_ID}},
)
    
    # Procesar la respuesta
    # La respuesta del bot puede ser un string o un objeto JSON
    if isinstance(response, AIMessage):
        # Si la respuesta es un mensaje de la IA, extraemos el contenido.
        bot_output = response.content
    else:
        # Si la respuesta es un objeto JSON, lo mostramos de forma bonita.
        bot_output = json.dumps(response, indent=2, ensure_ascii=False)

    print(f"Bot: {bot_output}")