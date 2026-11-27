from flask import Flask, render_template

app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/')
# def ban_ve():
#     return render_template('employees_banve.html')

# @app.route('/')
# def ban_ve():
#     return render_template('customers_datve.html')

# @app.route('/')
# def admin():
#      return render_template('admin_xembieudo.html')

# @app.route('/')
# def admin():
#      return render_template('admin_quanlychuyenbay.html')

# @app.route('/')
# def admin():
#      return render_template('admin_quanlytuyenbay.html')

# @app.route('/')
# def admin():
#      return render_template('login.html')

# @app.route('/')
# def admin():
#      return render_template('customers.html')

@app.route('/')
def ban_ve():
    return render_template('login_tracuuve.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)