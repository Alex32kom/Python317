from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zvmwerwekrl435435werwetwe544s4dg3sdg44'

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template('about.html', title="О нас", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category='success')
            print(request.form)
        else:
            flash("Ошибка отправки", category='error')

        # print(request.form['username'])
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        #
        # return render_template('contact.html', **context, title="Обратная  связь", menu=menu)
    return render_template('contact.html', title="Обратная  связь", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("page404.html", tittle="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
