"""Emotion detection using Watson NLP embeddable library."""
import requests

MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def emotion_detector(text_to_analyse):
    """Detect emotions for the given text via Watson NLP.

    Args:
        text_to_analyse (str): raw customer feedback text.

    Returns:
        dict: scores for anger, disgust, fear, joy, sadness
            plus the dominant_emotion key.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers, timeout=30)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = response.json()

    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
