from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Meine Freunde haben Krebs'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
