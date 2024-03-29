from flask import Flask, request
import re, math
from collections import Counter

WORD = re.compile(r'\w+')
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)
def run(txt1, txt2):
    vector1 = text_to_vector(txt1)
    vector2 = text_to_vector(txt2)
    cosine = get_cosine(vector1, vector2)
    return cosine

app = Flask(__name__)

@app.route('/similarity', methods = ['POST'])
def similarity():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        res = run(text1, text2)
        return '{similarity: ' + str(res) + '}'

if __name__ == '__main__':
    app.run(debug=True, port=5000)