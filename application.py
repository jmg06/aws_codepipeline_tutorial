import funtions as f
from flask import Flask, jsonify, abort

application = Flask(__name__)
data = f.load_file('./heroes.csv')

@application.route("/")
def get_all_heroes():
    return jsonify(data)

@application.route("/<string:id_hero>")
def get_hero_by_id(id_hero):
    if id_hero not in data:
        abort(404, description="Hero not found!")
    return jsonify(data[id_hero])

if __name__ == "__main__":
    application.run(port = 5000, debug = True)