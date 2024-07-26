from flask import Flask,render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle
import nltk
nltk.download('vador_lexicon')
app=Flask(__name__)
application=app

model=pickle.load(open('models/sentiment.pkl','rb'))

@app.route('/',methods=["GET","POST"])
def main():
    if request.method=="POST":
        inp=request.form.get("inp")
        score=model.polarity_scores(inp)
        if score["neg"]!=0:
            return render_template('home.html',message="Negative🙁")
        else:
            return render_template('home.html',message="Positive😊")
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")