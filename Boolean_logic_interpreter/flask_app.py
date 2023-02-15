from flask import Flask, render_template, request
from variable_assignment import evaluate_with_variables
from boolean_logic_interpreter import InvalidOperatorException, UnknownSymbolException

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
    result = None
    error = None
    try:
        result = evaluate_with_variables(boolean_string)
    except InvalidOperatorException:
        error = "You have entered an invalid operator. Please use only the ones in the list below."
    except UnknownSymbolException as e:
        error = str(e)
    return render_template("answer.html", result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
