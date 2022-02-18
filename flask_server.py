from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/<uuid>', methods=['GET', 'POST'])
def update(uuid):
    content = request.json
    print(content)

    return jsonify({'data': 'some json'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
