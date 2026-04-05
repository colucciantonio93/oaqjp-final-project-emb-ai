import requests  # Libreria per gestire le chiamate HTTP

def emotion_detector(text_to_analyze):
    # URL del servizio Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header richiesti dall'API per identificare il modello
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload con il testo da analizzare
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Esecuzione della richiesta POST
    response = requests.post(url, json = myobj, headers=header)
    
    # Restituiamo il testo della risposta (per ora grezzo come richiesto dal Task 2)
    return response.text