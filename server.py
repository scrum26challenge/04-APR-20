from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/webpage', methods=['GET'])
def webpage():
    #insert HTML page in quotes to render it out 
    return render_template('')


if __name__ == '__main__':
    app.run(debug=True)