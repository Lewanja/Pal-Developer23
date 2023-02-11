from flask import Flask, render_template, request
from boolean_logic_interpreter import evaluate_with_brackets

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/get_logic', methods=["GET"])
def get_logic():
    return render_template("boolean_logic_form.html")


@app.route('/post_logic', methods=["POST"])
def post_logic():

    boolean_string = request.form["boolean_expression"]
    result = evaluate_with_brackets(boolean_string)
    return render_template("boolean_logic.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
