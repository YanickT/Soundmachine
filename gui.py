from flask import Flask, render_template, request, redirect, url_for
from music_admin import MUSIC
from bot import BOT


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html', state=BOT.state, channel=BOT.channel, **MUSIC.files)


if __name__ == "__main__":
    app.run(host="0.0.0.0")