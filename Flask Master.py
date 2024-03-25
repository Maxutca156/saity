from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/contacts/")
def contacts():
    developer_name = "Аркадий Арутинян Борисович"
    developer_phone = "+79853310779"
    developer_city = "г.Ханты-Мансийск"
    return render_template('contacts.html', name=developer_name, phone=developer_phone, city=developer_city)


if __name__ == "__main__":
    app.run(debug=True)
