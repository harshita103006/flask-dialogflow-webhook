from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req['queryResult']['intent']['displayName']
    
    response_text = "Sorry, I don't know how to answer that yet."

    if intent == 'Weather Forecast':
        response_text = "Weather tomorrow is sunny!"
    elif intent == 'Crop Disease Issues':
        response_text = "Plant disease info coming soon!"
    elif intent == 'Market Prices':
        response_text = "Market price info coming soon!"
    elif intent == 'Soil Information':
        response_text = "Soil info coming soon!"

    return jsonify({'fulfillment_text': response_text})

if __name__ == '__main__':
    app.run(port=5000)
