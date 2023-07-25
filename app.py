from flask import Flask, render_template, request
from recommend import recommend
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    username = request.form['username']
    recommendations = recommend(username)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)