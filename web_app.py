from flask import Flask

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return "<h1>Добро пожаловать на сайт вашего бота!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
 
