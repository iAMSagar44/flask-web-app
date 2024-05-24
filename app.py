from flask import Flask, request, redirect, url_for, render_template, session
import requests, os, uuid, json
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Get the user input from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # Load the values from .env
    key = os.getenv('KEY')
    endpoint = os.getenv('ENDPOINT')
    location = os.getenv('LOCATION')

    path = '/translate?api-version=3.0'
 
    target_language_parameter = '&to=' + target_language

    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': original_text}]

    translator_request = requests.post(constructed_url, headers=headers, json=body)
    translator_response = translator_request.json()
    logger.info(f"Response: {translator_response}")

     # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )
