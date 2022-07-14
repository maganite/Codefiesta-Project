# from crypt import methods
from re import TEMPLATE
from flask import Flask, render_template, request
from transliterate import TransliterateLanguage

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def getData():
    data=""
    if request.method == "POST":
        if len(str(request.form["data"])):
            original_text = request.form["data"]
            language=request.form["language"]
            data=TransliterateLanguage(language,original_text).convertTo()
        else:
            print("form is empty")
    return render_template('index.html', data=data)



if __name__ == '__main__':
   app.run(debug=True, port=5000)