from flask import Flask, request, jsonify
import string

app = Flask(__name__)

@app.route('/endpoint', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        data = request.get_json()
        status = "Success"
        user_id = data.get('user_id')
        college_email = data.get('college_email')
        college_roll_number = data.get('college_roll_number')
        array_numbers = data.get('array_numbers')
        array_alphabets = data.get('array_alphabets')

        # Logic to find the highest lowercase alphabet
        highest_lowercase = max([char for char in array_alphabets if char in string.ascii_lowercase], default=None)

        response = {
            "status": status,
            "user_id": user_id,
            "college_email": college_email,
            "college_roll_number": college_roll_number,
            "array_numbers": array_numbers,
            "array_alphabets": array_alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        return jsonify(response)

    elif request.method == 'GET':
        operation_code = "12345"  # You can set any code you want
        return jsonify({"operation_code": operation_code})

if __name__ == '__main__':
    app.run(debug=True)
