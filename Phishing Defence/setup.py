from flask import Flask, request, jsonify
from joblib import load
from flask_cors import CORS
import requests
import numpy as np
import os

# set the feature details
def n_AtSign(url):
    at =  url.count('@') 
    return at

def n_Length(url):
    length = len(url)           
    return length

def n_dots(url):
    dot = url.count('.')
    return dot

def n_hypens(url):
    hypen = url.count('-')
    return hypen

def n_underline(url):
    underline = url.count('_')
    return underline

def n_slash(url):
    slash = url.count('/')
    return slash

def n_questionmark(url):
    questionmark = url.count('?')
    return questionmark

def n_equal(url):
    equal = url.count('=')
    return equal

def n_and(url):
    ands = url.count('&')
    return ands

def n_exclamation(url):
    exclamation = url.count('!')
    return exclamation

def n_space(url):
    space = url.count(' ')
    return space

def n_tilde(url):
    tilde = url.count('~')
    return tilde

def n_comma(url):
    comma = url.count(',')
    return comma

def n_plus(url):
    plus = url.count('+')
    return plus

def n_asterisk(url):
    asterisk = url.count('*')
    return asterisk

def n_hastag(url):
    hastag = url.count('#')
    return hastag

def n_dollar(url):
    dollar = url.count('$')
    return dollar

def n_percent(url):
    percent = url.count('%')
    return percent

def n_redirection(url, max_redirects=6):
    try:
        # start to calculate the redirection number
        session = requests.Session()
        response = session.get(url, allow_redirects=True, timeout=10)
        redirection_count = len(response.history)
        # Check whether the number of redirections exceeds max_redirects
        if redirection_count > max_redirects:
            return max_redirects
        else:
            return redirection_count
    # Give corresponding results according to different error reports
    except requests.TooManyRedirects:
        return max_redirects
    except requests.RequestException:
        return 0
    finally:
        session.close()
# define the extract things
def extract_features(url):
    return [
        n_Length(url), n_dots(url), n_hypens(url), n_underline(url),
        n_slash(url), n_questionmark(url), n_equal(url), n_AtSign(url),
        n_and(url), n_exclamation(url), n_space(url), n_tilde(url),
        n_comma(url), n_plus(url), n_asterisk(url), n_hastag(url),
        n_dollar(url), n_percent(url), n_redirection(url)
    ]

# start to connect plug-in
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)
# set the relative path
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, "final_model.joblib")
model = load(model_path)
# define main process
@app.route('/detect', methods=['POST'])
def detect():
    # get url
    data = request.json
    url = data['url']
    print(url)
    # extract feature and predict result
    features = extract_features(url)
    prediction = model.predict([features])
    # confirm result
    isPhishing = bool(prediction[0] == 1) 
    print({'isPhishing': isPhishing})
    return jsonify({'isPhishing': isPhishing})

if __name__ == '__main__':
    app.run(debug=True)