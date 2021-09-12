# 使用heroku要建立專案描述檔runtime.txt，告訴人家我們使用的python是哪一個版本
# 建立專案描述檔requierments.txt，專案運作時需要使用那些套件，gunicorn我們沒用到，但是要在heroku上啟動專案，必須加入
# 建立專案描述檔Procfile，告訴heroku我們要如何啟動專案heroku是使用gunicorn啟動我們的web專案，後面加上專案名稱:啟動的Flask物件名稱
from flask import Flask

app = Flask(__name__)  # __name__ 代表目前執行的模組


@app.route("/")  # 函式的裝飾 (Decorator) : 以函式為基礎，提供附加的功能
def home():
    return "Hello Flask 2"


@app.route("/test")  # 代表我們要處理的網站路徑
def test():
    return "test now 222"


if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 立刻啟動伺服器
