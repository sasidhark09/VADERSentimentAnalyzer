from flask import Flask,render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vador_lexicon')
app=Flask(__name__)
application=app

@app.route('/',methods=["GET","POST"])
def main():
    if request.method=="POST":
        inp=request.form.get("inp")
        sid=SentimentIntensityAnalyzer()
        score=sid.polarity_scores(inp)
        if score["neg"]!=0:
            return render_template('home.html',message="Negative🙁")
        else:
            return render_template('home.html',message="Positive😊")
    else:
        return render_template('home.html')



if __name__=="__main__":
    app.run(host="0.0.0.0")