from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route("/<int:column>")
@app.route("/<int:row>/<int:column>")
@app.route("/<int:row>/<int:column>/<color1>/<color2>")
def index(row=8, column=8,color1="white", color2="black"):
    return render_template("index.html", row = row, column = column , color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)