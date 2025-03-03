from flask import Flask, render_template

app = Flask(__name__)  # 🔥 이 줄이 반드시 있어야 함!

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

