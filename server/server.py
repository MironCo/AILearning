from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import PIL
import PIL.Image
import imagecreator
import ai

number_image = PIL.Image.new(mode="RGB", size=(28, 28))

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the Svelte frontend

@app.route('/predict', methods=['POST'])
def receive_pixels():
    data = request.json
    pixels = data.get('pixels') # type: ignore
    if pixels is None:
        return jsonify({'error': 'No pixels provided'}), 400

    # Process the pixel data as needed
    if all([ v == 0 for v in pixels ]) :
        return jsonify("?"), 200
    else:
        image = imagecreator.create_image(pixels=pixels)
        predicted_item = ai.predict_image_server(image)

        return jsonify(predicted_item), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
