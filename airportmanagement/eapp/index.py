from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ban_ve():
    return render_template('ban_ve.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)