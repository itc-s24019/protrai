#s24019
#Flask_rensyu.py

#事前にflaskモジュールをインストールすると使える
from flask import Flask

#Flaskライブラリをインスタンス化し、app変数に割り当て
#その際、コントラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートURLに対するリクエストを処理する関数を定義するデコレーター
#引数にルート'/'を指定するとアクセスした際index()関数が呼び出される
@app.route('/')
def index():
    return "Hello World</h1>"

if __name__=='__main__':
    #それぞれのユニークなIPアドレスでアクセスするように設定
    app.run(host='0.0.0.0 ', port=5000, debug=True)

#python flask_rensyu2.pyで実行し、ブラウザから表示させてみましょう。
