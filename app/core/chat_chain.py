from dotenv import load_dotenv
import os
import json

from langchain_groq import ChatGroq
from langchain_core.prompts import (
    FewShotChatMessagePromptTemplate,
    ChatPromptTemplate
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

from .prompts import (
    general_system_template, 
    example_prompt
)
from .memory import get_session_history

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Cargar los ejemplos de few-shot desde el archivo JSON
with open("data/few_shot_examples.json", "r", encoding="utf-8") as f:
    few_shot_examples = json.load(f)

# Inicializar el modelo de lenguaje de Groq
llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

# Crear la plantilla de pocos disparos
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=few_shot_examples,
)

# Unir la plantilla del sistema y la plantilla de pocos disparos en una plantilla de chat completa
full_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", general_system_template),
    few_shot_prompt,
    ("human", "{input}"),
])

parcer = StrOutputParser()
# Construir la cadena principal de chat
# La cadena toma el input, lo pasa por el prompt, luego por el modelo,
# y finalmente el resultado es parseado como una cadena de texto.
chat_chain = full_chat_prompt | llm | parcer

# Ahora, envuelve la cadena principal (`chat_chain`) con la memoria.
# Esto le da la capacidad de recordar conversaciones.
chat_with_memory = RunnableWithMessageHistory(
    chat_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)