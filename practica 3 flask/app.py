from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


user = []

@app.route("/")
def index():
    return render_template("index.html", user = user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        return redirect("/")
    else:
        return render_template("login.html", )

@app.route("/singup", methods=["GET", "POST"])
def singup():
   if  request.method== "POST":
        nuevo_user = []
        for username in request.form.usernames():
            nuevo_user.append(request.form[username])
        user.append(list(nuevo_user))
        return redirect("/")
    else:    
        return render_template("singup.html")


if __name__ == "__main__":
    app.run(debug=True)