from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# import numpy as np
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/', methods=['POST'])

def api_post():
    # data = request.data.decode() + 'flask'
    result =  {
                "kekka": 'ok'
            }
    return jsonify(result)



@app.route('/result', methods=['POST'])
def result():
    kekka = request.kekka

    result =  {
                "kekka": matching(kekka)
            }
    return jsonify(result)



@app.route('/questions', methods=['POST'])
def questions():
    print('kiteru')
    # result = executeQuery('select body, score from questions')
    result =  {
                '0':{'question':'質問1', 'ans':['はい', 'はい', 'どちらでもない', 'いいえ', 'いいえ'] },
                '1':{'question':'質問2', 'ans':['はい', 'はい', 'どちらでもない', 'いいえ', 'いいえ'] },
                '2':{'question':'質問3', 'ans':['はい', 'はい', 'どちらでもない', 'いいえ', 'いいえ'] }
            }
    return jsonify(result)



# Returns:てんぽid
def matching(kekka):
    return 'aaa'


def executeQuery(query):
    dbname = 'gotannodb.db'
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    result = c.execute(query)
    return result



def dbtest():
    dbname = 'gotannodb.db'
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    result = c.execute("select 1, 'test' from dual")
    print(result)
    # db = create_engine('sqlite:///gotannodb.db')
    # result = db.execute('select * from testdata')
    # print(result)
    # for row in result:
    #     print(row)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
