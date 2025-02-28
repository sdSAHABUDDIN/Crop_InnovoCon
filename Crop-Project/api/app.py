from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/cropDetails', methods=['POST'])
def create():
    # The crop details dictionary
    my_dict = {
        "Rice": {
            "Selection of Rice Variety": {
                1: "Choose a variety suited to your region, soil type, and water availability."
            },
            "Field Preparation": {
                1: "Plough the field 2-3 times to loosen the soil for better aeration and water retention."
            },
            "Seed Selection and Treatment": {
                1: "Use about 25-30 kg of seeds per hectare for transplanted rice."
            }
        }
    }
    
    # Get the crop name from the request body
    data = request.get_json()
    crop_name = data.get("cropName")  # Extract 'cropName' from the POST request body
    
    # Check if the crop exists in the dictionary
    if crop_name in my_dict:
        return jsonify({crop_name: my_dict[crop_name]})
    else:
        return jsonify({"error": "Crop not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)