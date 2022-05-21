from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "contact": '9658236578',
        "name": 'Raju',
        "done": False,
        "id": 1
    },
    {
        "contact": '5823695872',
        "name": 'Rahul',
        "done": False,
        "id": 2
    },
    {
        "contact": '9586236502',
        "name": 'Khush',
        "done": False,
        "id": 3
    }
]

@app.route("/add-data",methods = ["POST"])

def add_data():
    if not request.json:
        return jsonify({"status": "error", "message": "Please give a data."}, 400)
    else:
        contact = {
            "id": data[-1]["id"] + 1,
            "contact":  request.json.get("contact",""),
            "name": request.json["name"],
            "done": False
        }

        data.append(contact)

        return jsonify({"status": "success","message": "Data added successfully."})


@app.route("/get-data")

def get_data():
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(debug = True)