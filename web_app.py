from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список товаров
products = [
    {"id": 1, "name": "Кроссовки Nike", "price": "5000 руб.", "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Футболка Adidas", "price": "2000 руб.", "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Часы Casio", "price": "7000 руб.", "image": "https://via.placeholder.com/150"},
]

# Главная страница: вывод товаров
@app.route('/')
def home():
    return render_template("index.html", products=products)

# Страница оформления заказа
@app.route('/order/<int:product_id>', methods=["GET", "POST"])
def order(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]
        print(f"Заказ получен: {name}, {phone}, {address}, Товар: {product['name']}")
        return redirect(url_for("home"))
    return render_template("order.html", product=product)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

 
