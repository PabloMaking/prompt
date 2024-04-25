# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from vertexai.generative_models import GenerativeModel, ChatSession
from vertexai import generative_models
import pandas as pd

# Initialize Vertex AI
vertexai.init(project="aie-sandbox--pct--ac", location="europe-west1")
model = GenerativeModel(model_name="gemini-1.5-pro-preview-0409")
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True)
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

def leer_archivo_md(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None

tablas = leer_archivo_md("compute.googleapis.com.md")
#print(tablas)
persona = "Eres un especialista en interpretar y explicar tablas."
context = " Dada una tabla sobre un inventario de un proyecto de GCP"
response_format = "Respondeme en formato markdown"
objetivo = "Resumeme el contenido poniendo de título el que aparece escrito en markdown. En español"
prompt = persona + objetivo + tablas + response_format
print(get_chat_response(chat, prompt))
# Load the model
# multimodal_model = GenerativeModel(model_name="gemini-1.5-pro")
# generation_config = generative_models.GenerationConfig(
#     max_output_tokens=2048, temperature=0.4, top_p=1, top_k=32
# )
# # Query the model
# response = multimodal_model.generate_content(
#     [
#         # Add an example image
#         Part.from_uri(
#             "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
#         ),
#         # Add an example query
#         "what is shown in this image?",
#     ]
# )
# print(response)
# print(response.text)
