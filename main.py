from flask import Flask, request
import telebot
import sys
from abc import ABC
from time import sleep
from flask import request, render_template, redirect



app = Flask(__name__)

token = ''

bot = telebot.TeleBot(token)

chanel_id = ''


@app.route('/')
def mainPage():
    
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def getData():
    if request.method == 'POST':
        description = request.form.get('description') 
        entry = request.form.get('entry') 
        stop = request.form.get('stop')
        profit = request.form.get('profit')
        image = request.files['image']
        pair = request.form.get('pair')
        picture = image

        caption = f'{pair}\n\n{description}\n\nТочка Входа: {entry}\n\nТейк профит: {profit}\n\nСтоп Лос: {stop}\n\n'
        print(caption)
        bot.send_photo(chanel_id, picture, caption=caption)
        import requests

        # User's Token
        header = {
            'authorization': "",
        }
        # File
        files = picture
        # Optional message to send with the picture
        payload = {
            "content":f"{description}"
        }
        channel_id = "channel_id" # Channel where we send the picture
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header, files=files)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)