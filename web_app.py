from flask import Flask, render_template, request, jsonify

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

# Обработчик AJAX поиска
@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = [p for p in products if query in p['name'].lower()]
    return jsonify({"products": results})

# Запуск приложения Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=False)
