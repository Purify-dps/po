from flask import Flask, render_template, jsonify
app = Flask(__name__)


people = [
    {'id': 0,
     'name': 'UStefanie Friesen',
     'about': 'Product Manager',
     'image': 'templates/stefanie.png'},
    {'id': 1,
     'name': 'Hamza Imam Amjad',
     'about': 'Artificial Intelligence (AI) engineer',
     'image': 'templates/pic.jpg'},
    {'id': 2,
     'name': 'Amir',
     'about': 'Interaction Designer',
     'image': 'templates/amir.png'},
     {'id': 3,
     'name': 'Usitha',
     'about': 'Software engineer',
     'image': 'templates/ushita.png'},
     {'id': 4,
     'name': 'Bhanuja Aggarwal',
     'about': 'Software engineer',
     'image': 'templates/bhanuja.png'},
]


@app.route("/", methods=['GET'])
def home():
    return jsonify(people)


if __name__ == '__main__':
    app.run(debug=True)
