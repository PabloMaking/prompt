from vertexai.language_models import ChatModel, InputOutputTextPair

def leer_archivo_md(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None

def science_tutoring(temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        #"max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    chat = chat_model.start_chat(
        context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
        examples=[
            InputOutputTextPair(
                input_text="How many moons does Mars have?",
                output_text="The planet Mars has two moons, Phobos and Deimos.",
            ),
        ],
    )
    tablas = leer_archivo_md("compute.googleapis.com.md")
    #print(tablas)
    prompt = "Eres un especialista en interpretar y explicar tablas. Dada una tabla sobre un iventario de un proyecto de GCP,  hazme un resumen explicativo sobre el contenido en español"
    prompt = prompt + tablas
    response = chat.send_message(
        prompt, **parameters
    )
    print(f"Response from Model: {response.text}")

    return response

science_tutoring()