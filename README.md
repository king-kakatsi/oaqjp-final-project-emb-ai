# Final Project — Emotion Detection Web App

AI-based web app that performs analytics on customer feedback: it detects
the dominant emotion (**anger, disgust, fear, joy, sadness**) expressed in a
text statement, using the embeddable Watson NLP library. Built as the final
project of the IBM *Developing AI Applications with Python and Flask* course.

## Project structure

```text
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # emotion_detector(): calls Watson NLP, formats scores
├── static/
│   └── mywebscript.js         # frontend: calls GET /emotionDetector
├── templates/
│   └── index.html             # web UI
├── server.py                  # Flask app: / and /emotionDetector routes
├── test_emotion_detection.py  # unit tests (one per emotion)
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- Reachability of the Watson EmotionPredict service
  (available inside the Skills Network lab environment)

## Installation

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## Run the web app

```bash
./venv/bin/python server.py
```

Open `http://localhost:5000`, enter a statement and click
**Run Sentiment Analysis**.

API directly:

```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy"
# For the given statement, the system response is 'anger': ..., ... The dominant emotion is joy.

curl "http://localhost:5000/emotionDetector?textToAnalyze="
# Invalid text! Please try again!
```

## Run the tests

```bash
./venv/bin/python -m unittest -v
# or
./venv/bin/python -m pytest -v
```

## Static code analysis

```bash
./venv/bin/python -m flake8 server.py test_emotion_detection.py EmotionDetection/
./venv/bin/python -m pylint EmotionDetection/emotion_detection.py server.py
```

## Error handling

- Empty/invalid text (Watson HTTP 400), network timeouts and unexpected
  responses all yield `None` scores, and the web app answers
  `Invalid text! Please try again!` instead of a `500` error.
  Diagnostics are printed to the server console.
