from flask import Flask, render_template, request, redirect, url_for
from music_admin import MUSIC
import bot
import threading


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.json is not None:
        bot.play(request.json["play"])
    channel = bot.CHANNEL if bot.CHANNEL is None else bot.CHANNEL.channel
    return render_template('home.html', state=bot.STATUS, channel=channel, **MUSIC.files)


if __name__ == "__main__":
    thread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0"})
    thread.start()

    # bot needs to be the main thread
    bot.client.run(bot.TOKEN)