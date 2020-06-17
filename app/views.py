from app import app


@app.route('/')
def home():
    return 'Home'


@app.route('/timer')
def profile():
    return 'Timer'
