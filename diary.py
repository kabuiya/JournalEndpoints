from flask import Flask, jsonify, request

from models import Entries

app = Flask(__name__)

# storing elements in memory
entr = Entries()


@app.route("/api/v1/entries", methods=['GET'])
def entries():
    all_entries = entr.get_entries()
    return jsonify(all_entries)


@app.route("/api/v1/add", methods=['POST'])
def add_new_entries():
    data = request.get_json()
    if "content" in data:
        return jsonify(entr.add_entries(data)), 201
    else:
        return jsonify({"error": "content  is missing"}), 400


@app.route("/api/v1/entry/<int:entry_id>", methods=['GET'])
def entry(entry_id):
    an_entry = entr.get_entry(entry_id)
    if an_entry:
        return jsonify(an_entry)
    else:
        return jsonify({"error": "Entry not found"}), 404


@app.route("/api/v1/update/<int:entry_id>", methods=['PUT'])
def update_entry(entry_id):
    update_with = request.get_json()
    new_ent = entr.update_entry(entry_id, update_with)
    if new_ent:
        return jsonify(new_ent)
    else:
        return jsonify({"error": "Entry not found"}), 400


@app.route("/api/v1/delete/<int:entry_id>", methods=['DELETE'])
def del_entry(entry_id):
    new_ent = entr.delete_entry(entry_id)
    if new_ent:
        return jsonify(new_ent)
    else:
        return jsonify({"error": "Entry not found"}), 400

# run
if __name__ == '__main__':
    app.run(debug=True)
