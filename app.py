from flask import Flask, jsonify, request
from flask_cors import CORS
from kotoba import *
import jsonpickle
import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

def check_input(word, hidden):
    kotoba = Kotoba()
    result = kotoba.find_kotoba(word, hidden)
    if not result:
        return 'Not a word'
    result = jsonpickle.encode(result)
    result_dict = {}
    result_dict = json.loads(result)[0]
    print(result_dict);
    for k,v in result_dict.items():
        print(k)
    kanji = None
    if result_dict['kanji_forms']:
        kanji = result_dict['kanji_forms'][0]['text']
    plain = result_dict['kana_forms'][0]['text']
    str = ''
    for i in range(len(result_dict['senses'][0]['gloss'])):
        print(result_dict['senses'][0]['gloss'][i]['text'])
        str += result_dict['senses'][0]['gloss'][i]['text'] + '/'

    english = str[:-1]

    new_dict = {}
    new_dict['Word'] = word
    new_dict['English'] = english
    new_dict['Kanji'] = kanji

    return new_dict
    

@app.route('/test', methods=['GET'])
def test():
    kotoba = Kotoba()
    get_moras = kotoba.generate_moras()
    moras = get_moras[0]
    hidden = get_moras[2]
    ht = {}
    ht['moras'] = hidden
    ht['hidden'] = ''.join(moras)

    return jsonify(ht)

@app.route('/check', methods=['GET'])
def check():
    word_check = request.args.get("word")
    print(word_check)
    hidden_check = (request.args.get("hidden"))
    print(hidden_check)
    test = check_input(word_check, hidden_check)
    return jsonify(test)

if __name__ == '__main__':
    app.run()
