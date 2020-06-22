import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
from scipy import sparse as sp
    


app = Flask(__name__)
CORS(app)

@app.route('/rs', methods=['POST'])
def apicall():
    try:
        data = request.get_json()
        data = data['titleabstract']

    except Exception as e:
        raise e

    vectorizer = pickle.load(open('vectorizer', 'rb'))

    data_vect = vectorizer.transform([data])

    vectorizer = None

    centroids = pickle.load(open('centroids', 'rb'))

    predict= np.argsort(pairwise_distances(data_vect, centroids, metric='euclidean'))
    
    data_vect = None
    centroids = None

    classes = pickle.load(open('classes', 'rb'))
    researcher = pickle.load(open('researcher', 'rb'))

    ranking = list()
    count = 1
    for i in classes[predict[0]][0:15]:
        ranking.append(str(count)+": "+researcher['name'][researcher['id'] == i].values[0])
        count += 1

    responses = jsonify(ranking)
    responses.status_code = 200

    classes = None
    researcher = None

    return (responses)

        
        
        
        
        
        