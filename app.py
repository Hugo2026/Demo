from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def index():
    result = None
    img = ""
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        result = num1 + num2
        if result%2 ==0:
            img= "static/mouse.png"
        else:
            img= "static/chicken.jpg"
    return render_template('index.html', result=result, img = img )

@app.route("/hello")
def hello_world():
    return "Hello"

@app.route("/Daniel")
def hello_sam():
    return "Hello Daniel"

if __name__ == '__main__':
    app.run(debug=True)
