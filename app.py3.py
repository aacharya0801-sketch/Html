from flask import flask, render_template, request

app= Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", method=["POST"])
def calculate():
    units = int(request.form["units"])
    bill = units * 5

    if units <= 100:
        message: "Great! You are an energy saver! 👍"
    elif units <= 200:
        message = "Not bad! Try saving a little more! 🎃"
    else:
        message = "Whoa! Time to switch off some lights💡"
    return render_template("index.html", units=units, bill=bill, message=message)

if_name__=="__main__":
   app.run(debug=True)