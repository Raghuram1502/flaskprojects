from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route('/')
def oxfort():
    return render_template("oxfortdict.html")

@app.route('/search',methods = ["GET"])
def search():
    meaning = []
    word = request.args.get("word")
    print(word)
    headers = {"app_id": "fb507665", "app_key": "4877504bfc2316fa7c67f18fbdd799e5"}
    r = requests.get(f"https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-us/{word}", headers=headers)
    data = r.json()
    results = data.get("results",[])
    for result in results:
        lexicalEntries = result.get("lexicalEntries",[])
        for lexicalEntry in lexicalEntries:
            entries = lexicalEntry.get("entries",[])
            for entry in entries:
                senses = entry.get("senses",[])
                for sense in senses:
                    sense_definition = sense.get("definitions",[])
                    for definition in sense_definition:
                        meaning.append(definition)
    return render_template("meaning.html",d = {"word":word,"meaning":meaning})

