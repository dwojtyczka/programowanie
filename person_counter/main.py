from flask import Flask, request, jsonify
import requests
import os
from detector import PersonDetector

app = Flask(__name__)
detector = PersonDetector('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')


@app.route('/count_local', methods=['GET'])
def count_local():
    image_path = request.args.get('image_path', 'test.jpg')
    wynik = detector.policz_osoby(image_path)
    return jsonify({'persons_detected': wynik})


@app.route('/count_url', methods=['GET'])
def count_url():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Brak url'}), 400

    temp_file = "temp_web_image.jpg"
    try:
        response = requests.get(url, timeout=10)
        with open(temp_file, 'wb') as f:
            f.write(response.content)

        wynik = detector.policz_osoby(temp_file)
        return jsonify({'persons_detected': wynik})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)