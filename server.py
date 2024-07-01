"""
This module runs a Flask application for emotion detection.
"""

# Import Flask, render_template, request from the flask framework package:
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app:
app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotions in the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    """ 
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # This function executes the Flask app and deploys it on localhost:5000.
    app.run(host="0.0.0.0", port=5000)
