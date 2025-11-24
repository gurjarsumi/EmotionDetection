"""
Emotion Detection Server Application.

This file initiates a Flask server to host the Emotion Detection application
over the web. It handles the deployment and the routing of the application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app (Renamed to APP to satisfy Pylint constant naming)
APP = Flask("Emotion Detector")

@APP.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the sentiment of the text passed via query parameters.

    Retrieves the text from the request, passes it to the emotion_detector
    function, and formats the response for display.

    Returns:
        str: A formatted string containing the emotion scores and dominant emotion
             or an error message if the input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant emotion is None (indicating invalid input)
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # If valid, extract the rest of the scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Return the formatted string
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@APP.route("/")
def render_index_page():
    """
    Renders the main index page.

    Returns:
        The rendered HTML template for the application interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost:5000
    APP.run(host="0.0.0.0", port=5000)