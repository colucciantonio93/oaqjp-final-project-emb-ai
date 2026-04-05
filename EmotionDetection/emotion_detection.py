import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    
    # Task 7: Gestione errore 400
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    

    
    # Task 3: Parsing del JSON
    formatted_response = json.loads(response.text)
    
    # Estrazione delle emozioni dal primo elemento di 'emotionPredictions'
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Logica per trovare l'emozione con il punteggio più alto
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Costruzione del dizionario finale richiesto dal test
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result