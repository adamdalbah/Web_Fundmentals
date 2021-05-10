from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World'
@app.route('/Dojo')
def success():
    return "Dojo"  # Return the string 'Hello World!' as a response
@app.route('/say/<name>')
def flask(name):
    print(name)
    return "Hi " + name

@app.route('/say/<int:num>/<word>')
def repeat(num, word):
    string = ""
    for i in range (int(num)):
        string += "<p>" + word + "</p>"
    return string   
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

