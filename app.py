from flask import Flask, request
import database as db
import json
app = Flask(__name__)

json_content = {'content-type': 'text/json'}


@app.route('/', methods=['GET'])
def select_all():
    return json.dumps(db.select_all()), 200


@app.route('/create-new', methods=['POST'])
def create_tables():
    db.create_tables()
    return json.dumps({'msg': 'Created tables'}), 200, json_content


@app.route('/drop-all', methods=['PUT'])
def drop_all():
    db.drop_all()
    return json.dumps({'msg': 'Dropped all tables.'}), 200, json_content


@app.route('/person', methods=['POST', 'GET', 'DELETE'])
def person():
    if request.method == "POST":
        person = json.loads(request.data)
        db_person = db.add_person(person["Name"], person["Priority"])
        return json.dumps(db_person), 201, json_content
    elif request.method == "GET":
        people = db.get_people()
        return json.dumps(people), 200, json_content
    elif request.method == "DELETE":
        person = json.loads(request.data)
        db_person = db.delete_person(person["Name"])
        return json.dumps(db_person), json_content


@app.route('/room', methods=['POST', 'GET', 'DELETE'])
def room():
    if request.method == "POST":
        room = json.loads(request.data)
        db_room = db.add_room(room["House"], room["Room"])
        return json.dumps(db_room), 201, json_content
    elif request.method == "GET":
        rooms = db.get_rooms()
        return json.dumps(rooms), 200, json_content
    elif request.method == "DELETE":
        rooms = json.loads(request.data)
        db_room = db.delete_room(f"{rooms['House']} {rooms['Room']}")
        return json.dumps(db_room), json_content


@app.route('/item', methods=['POST', 'GET', "DELETE"])
def item():
    if request.method == "POST":
        item = json.loads(request.data)
        db_item = db.add_item(
            name=item["ItemName"],
            room=item["Room"],
            owner=item["Owner"],
            value=item["Value"],
            quant=item["Quantity"],
            size=item["Size"],
            priority=item["Priority"],
            fragile=item["Fragile"],
            owned=item["Owned"],
            moved=item["Moved"],
            keeping=item["Keeping"],
            notes=item["Notes"]
        )
        return json.dumps(db_item), 201, json_content
    elif request.method == "GET":
        items = db.get_items()
        return json.dumps(items), 200, json_content
    elif request.methos == "DELETE":
        item = json.loads(request.data)
        db_item = db.delete_item(item["ItemName"])
        return json.dumps(db_item), json_content


@app.route("/available-rooms", methods=["GET"])
def get_availabe_rooms():
    return json.dumps(db.get_person_options()), 200, json_content


@app.route("/availabe-people", methods=["GET"])
def get_available_people():
    return json.dumps(db.get_person_options()), 200, json_content


def main():
    app.run()


if __name__ == "__main__":
    main()
