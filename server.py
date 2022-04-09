import sys
from flask import Flask
from flask import render_template
from flask_frozen import Freezer

FREEZER_DESTINATION = 'docs'
URL_EASYCHAIR_SUBMISSION = 'https://easychair.org/conferences/?conf=ieeeichi2022'

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/call_for_sponsors.html")
def call_for_sponsors():
    return render_template('call_for_sponsors.html')


@app.route("/call_for_contributions.html")
def call_for_contributions():
    return render_template('call_for_contributions.html')


@app.route("/call_for_papers.html")
def call_for_papers():
    return render_template('call_for_papers.html')


@app.route("/call_for_posters_and_demos.html")
def call_for_posters_and_demos():
    return render_template('call_for_posters_and_demos.html')


@app.route("/call_for_workshops.html")
def call_for_workshops():
    return render_template('call_for_workshops.html')


@app.route("/call_for_doctorial_consortium.html")
def call_for_doctorial_consortium():
    return render_template('call_for_doctorial_consortium.html')


@app.route("/call_for_industry_track.html")
def call_for_industry_track():
    return render_template('call_for_industry_track.html')


@app.route("/call_for_tutorials.html")
def call_for_tutorials():
    return render_template('call_for_tutorials.html')


@app.route("/attending.html")
def attending():
    return render_template('attending.html')


@app.route("/venue_and_logistics.html")
def venue_and_logistics():
    return render_template('venue_and_logistics.html')


@app.route("/workshops.html")
def workshops():
    return render_template('workshops.html')


@app.route("/program.html")
def program():
    session_list = [
        'k-1', 'k-2', 'k-3', 'k-4'  # keynote
        'a-1', 'a-2', 'a-3', 'a-4', 'a-5', 'a-6', 'a-7', # analytics
        'h-1', 'h-2', 'h-3', # human factor
        's-1', 's-2', 's-3', # system
        'w-1', 'w-2', 'w-3', # workshop
        'd-1', 'd-2', 'd-3', # doctoral consortium
        't-1', 't-2',        # tutorial
        'i-1', 'i-2',        # industry 
        'p-1', 'p-2',        # poster
    ]
    return render_template(
        'program.html'
    )


@app.route("/keynotes.html")
def keynotes():
    return render_template('keynotes.html')


@app.route("/committees.html")
def committees():
    return render_template('committees.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        print('* built static version by Flask-Freezer')
    else:
        app.run(host='0.0.0.0', debug=True)