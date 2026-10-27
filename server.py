"""Flask web server exposing emotion detection to the frontend."""
from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emot_detector():
    """Handle emotion detection request from the web UI."""
    text_to_analyse = request.args.get("textToAnalyze")
    if not text_to_analyse:
        return "Invalid text! Please try again!"
    try:
        response = emotion_detector(text_to_analyse)
    except (requests.exceptions.RequestException, KeyError, TypeError):
        print("[emotionDetector] Watson call failed")
        return "Invalid text! Please try again!"
    if response is None or response["dominant_emotion"] is None:
        print("[emotionDetector] Watson returned no result "
              "(invalid text or service unreachable)")
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the main emotion detection page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
