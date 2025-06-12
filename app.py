from flask import Flask, render_template, request
from genai import recip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    ingredients = request.form['ingredients']
    preference = request.form['preference']
    recipe = recip(ingredients, preference)
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__': 
    app.run(debug=True)
