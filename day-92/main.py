from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image
from collections import Counter
import io

app = Flask(__name__)

def get_top_colors(image_path, num_colors=10):
    # Open the image
    img = Image.open(image_path)
    # Convert image to NumPy array
    img_array = np.array(img)
    # Flatten the array to a list of RGB values
    pixels = img_array.reshape((-1, 3))
    # Get the most common colors
    color_counts = Counter(map(tuple, pixels))
    top_colors = color_counts.most_common(num_colors)
    # Convert colors to a serializable format (Python list)
    top_colors_serializable = [([int(channel) for channel in color], count) for color, count in top_colors]
    return top_colors_serializable

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return 'No image uploaded'

    image = request.files['image']
    if image.filename == '':
        return 'No image selected'

    try:
        top_colors = get_top_colors(image)
        top_colors = reversed(top_colors)
        return render_template('index.html', colors=top_colors)
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
