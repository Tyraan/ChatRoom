from app import app
@app.route('/')
@app.route('/home')
def home():
    return "Hello , it's home"