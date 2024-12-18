from flask import Flask, render_template, request

# Создание приложения Flask
app = Flask(__name__)

# Пример списка товаров
products = [
    {"id": 1, "name": "Корм для собак", "price": "500 руб."},
    {"id": 2, "name": "Лакомства для кошек", "price": "300 руб."},
    {"id": 3, "name": "Игрушка для собак", "price": "150 руб."},
]

# Главная страница
@app.route('/')
def home():
    return render_template("index.html", products=products)

# Обработчик поиска товаров
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()
    results = [p for p in products if query in p['name'].lower()]
    return render_template("search_results.html", products=results, query=query)

# Запуск приложения Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=False)
