from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/results', methods=['POST'])
def create_user():
    print("submitted info")
    print(request.form)
    name_from_form = request.form['name']
    dojo_location_from_form = request.form['dojo_location']
    favoriate_language_from_form=request.form['favorite_language']
    comment_from_form=request.form['comment']
    return render_template("page.html", name_on_template=name_from_form,dojo_location_on_template=dojo_location_from_form,favoriate_language_on_template=favoriate_language_from_form,comment_on_template=comment_from_form)

if __name__=="__main__":
    app.run(debug=True)