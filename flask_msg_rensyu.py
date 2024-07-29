#s24019
#Flaskを使ったメッセージアプリ
#~/ protrai/flask_msg_rensyu.py
#実行はプロンプト(Git Bash)から Python flask_msg_rensyu.pyで実行
#フロントエンド部分のHTMLをtemplates/msg.html
#実際のメッセージを記録するファイルは~protrai/data.txtとする

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/himitsu')
def himitsu():
    return"<small>秘密のページ</small>"

@app.route('/msg')
def msg():
    return render_template('msg.html')

@app.route('/submit', methods=['POST'])
def submit():
    #フォームから入力された内容を習得
    content = request.form['content']
    #data.txtに追記する
    with open('data.txt', 'a') as file:
        file.write(f"\n{datetime.datetime.now()}\n{content}\n")
        return f"書き込みました"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
