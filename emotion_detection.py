import requests

def emotion_detector(text_to_analyze):
url = (
"https://sn-watson-emotion.labs.skills.network/"
"v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

```
myobj = {
    "raw_document": {
        "text": text_to_analyze
    }
}

response = requests.post(url, json=myobj)

formatted_response = response.json()

emotions = formatted_response["emotionPredictions"][0]["emotion"]

return {
    "anger": emotions["anger"],
    "disgust": emotions["disgust"],
    "fear": emotions["fear"],
    "joy": emotions["joy"],
    "sadness": emotions["sadness"],
    "dominant_emotion": max(emotions, key=emotions.get)
}
```
