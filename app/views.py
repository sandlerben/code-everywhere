from app import app
from flask import render_template
import string


@app.route('/learnpython/ex<int:example_id>')
def load_example(example_id):
    return render_template('ex' + str(example_id) + '.html')
