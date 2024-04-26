# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

'''
Objetivo
Instrucciones

Persona
Constraints
Tone
Context
Shot-Exmaples
Response format

'''


import vertexai
from vertexai.generative_models import GenerativeModel, Part
from vertexai.generative_models import GenerativeModel, ChatSession
from vertexai import generative_models
import os
import glob
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

def load_md():
    os.chdir("./md")
    md_s = glob.glob("*.md")
    return md_s


def leer_archivo_md(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None

tablas = leer_archivo_md("md/compute.googleapis.com.md")
files = load_md()
persona = "Hola eres un paciente e inteligente especialista de google en interpretar y explicar tablas sobre recursos de Google-Cloud en español."
context = " voy a proporcionarte unas tablas sobre los assets de un proyecto de GCP. Cada asset family con sus hijos"
objetivo = "Explicame las columnas, analiza su contenido y proporcioname tu analisis, tus observaciones y consideraciones"
response_format = "Respondeme en formato markdown, sin ninguna introducción y únicamente cuando te proporcione tablas"
shot_exmaple = "Ejemplo:   Columnas:...  Observaciones:... Análisis y consideraciones: ..."

prompt = persona + context + objetivo + response_format + shot_exmaple
print(get_chat_response(chat, prompt))
print(get_chat_response(chat, tablas))
'''for file in files:
    tablas = leer_archivo_md(file)
    prompt = persona + context + objetivo + tablas + response_format'''

#print(get_chat_response(chat, prompt))
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
