from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'maxim2k18gh8hg@gmail.com'
app.config['MAIL_PASSWORD'] = "0987654321"
app.config['MAIL_USE_SSL'] = True

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        msg = Message(request.form.get("Subject"), sender='maxim2k18gh8hg@gmail.com',
                      recipients=[request.form.get("Email")])
        msg.body = "Cool email dude"
        mail.send(msg)
        return render_template("result.html", result="Success!")
    else:
        return "f"



