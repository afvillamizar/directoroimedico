from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/sintomas")
def sintomas(a: str, b: str, c: str):
    texto = "Hemos recibido tus sintomas que incluyen "+ a+ ",  junto con "+b+", y por ultimo "+c +". Deacuerdo a esto se ha decidido que tienes "+ texto_aleatorio()
    return {"resultado": texto}






def texto_aleatorio():
    """
    Toma una lista de textos y devuelve uno aleatorio.
    
    Parámetros:
    textos (list): Lista de textos de la cual seleccionar.
    
    Retorna:
    str: Un texto seleccionado aleatoriamente.
    """
    textos = ["Dengue: Es una enfermedad viral transmitida por mosquitos que provoca fiebre alta repentina, dolor muscular y articular intenso, y sarpullido. En casa se recomienda reposo, hidratación abundante y el uso de paracetamol para la fiebre y el dolor, pero si hay sangrado, vómitos persistentes o dolor abdominal intenso, es necesario acudir a un centro asistencial.",
                       "Fiebre escarlatina: Causada por bacterias, se manifiesta con fiebre, dolor de garganta y una erupción cutánea rojiza. En casa, se pueden manejar los síntomas con hidratación y analgésicos, pero siempre se debe acudir al médico para iniciar un tratamiento con antibióticos.",
                       "Varicela: Es una infección viral que provoca fiebre, erupciones con ampollas que pican, y malestar general. En casa, los síntomas pueden aliviarse con lociones calmantes, baños de avena y paracetamol, pero si se presentan complicaciones como dificultad para respirar o infecciones en las lesiones, es necesario buscar atención médica.",
                       "Sarampión: Es una enfermedad viral caracterizada por fiebre alta, erupción cutánea, conjuntivitis y malestar general. El tratamiento en casa incluye reposo, hidratación y medidas para aliviar los síntomas, pero siempre se debe acudir al médico debido al riesgo de complicaciones graves como neumonía.",
                       "Lupus eritematoso sistémico (brote activo): Enfermedad autoinmune que puede provocar fiebre baja, dolor articular y erupción en la piel. En casa, es importante evitar la exposición al sol y descansar, pero siempre se requiere evaluación médica para ajustar el tratamiento.",
                       "Rubeola: Esta infección viral presenta fiebre leve, erupción rosada y ganglios linfáticos inflamados. En casa, se recomienda reposo y analgésicos, pero se debe buscar atención médica en caso de complicaciones o si afecta a mujeres embarazadas.",
                       "Fiebre por virus Zika: Se caracteriza por fiebre baja, sarpullido, dolor muscular y conjuntivitis. En casa, los síntomas se manejan con hidratación, reposo y paracetamol, pero si hay complicaciones neurológicas o embarazo, se requiere atención médica.",
                       "Mononucleosis infecciosa: Causada por el virus de Epstein-Barr, produce fiebre, dolor de garganta, erupciones cutáneas y fatiga. El tratamiento en casa incluye reposo, hidratación y analgésicos, pero si hay complicaciones como dificultad para respirar o dolor abdominal intenso, es necesario acudir al médico.",
                       "Eritema infeccioso: Es una enfermedad viral con fiebre leve, erupción rojiza en las mejillas y dolor articular. En casa, se pueden controlar los síntomas con reposo, hidratación y paracetamol, pero se debe buscar atención médica si el paciente tiene inmunosupresión o anemia severa.",
                       "Síndrome de Stevens-Johnson: Es una reacción alérgica severa con fiebre, ampollas dolorosas en la piel y las mucosas, y malestar general. Este cuadro no se trata en casa y requiere atención médica inmediata, ya que es una emergencia."]
    if not textos:
        raise ValueError("La lista de textos está vacía.")
    return random.choice(textos)

