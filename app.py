from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'maximgh8hg1@gmail.com'
app.config['MAIL_PASSWORD'] = '1234567890'
# app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        msg = Message(request.form.get("Subject"), sender='maximgh8hg1@gmail.com',
                      recipients=[request.form.get("Email")])
        msg.body = "Cool email bro"
        mail.send(msg)
        return render_template("result.html", result="Success!")
    else:
        return render_template("result.html", result="Failure.")


if __name__ == '__main__':
    app.run(debug=True)
