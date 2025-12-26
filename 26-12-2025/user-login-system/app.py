from flask import Flask, render_template
from database import init_db, close_db, get_db
from auth import auth_bp

app = Flask(__name__)
app.secret_key = 'change_this_to_a_random_secret'  # Required for sessions
app.teardown_appcontext(close_db)

app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return render_template('login.html')  # Default to login page

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)
