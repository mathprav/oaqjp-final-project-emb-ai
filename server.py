''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detecting():
    ''' This code receives the text from the HTML interface and
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the emotion scores and
        dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return " Invalid text! Please try again!"
    return "For the given statement, the system response is \
    'anger': {anger}, 'disgust': {disgust}, 'fear':{fear}, 'joy': {joy} \
    and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.".\
    format(**response)
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
