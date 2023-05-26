from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'  # Replace with your OpenAI API key

@app.route('/fashion-combination', methods=['POST'])
def get_fashion_combination():
    # Get customer details and inventory data from the request
    customer_details = request.json.get('customer_details')
    inventory_data = request.json.get('inventory_data')
    inventory_data = str(inventory_data)

    # Create a prompt using customer details and inventory data
    prompt = f"Generate fashion combinations for user with details {customer_details} from the available inventory options which is {inventory_data}"

    # Generate a fashion combination using OpenAI ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,  # Number of responses to generate
        stop=None,  # Stop generating responses at specified token
        temperature=0.7  # Controls the randomness of the generated text
    )

    # Extract the suggested fashion combination from the response
    fashion_combination = response.choices[0].text.strip()

    # Return the fashion combination as JSON response
    return jsonify({'fashion_combination': fashion_combination})

if __name__ == '__main__':
    app.run(debug=True)
