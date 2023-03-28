## 5.
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a simple API endpoint
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    message = f'Hello, {name}!'
    return jsonify({'message': message})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
