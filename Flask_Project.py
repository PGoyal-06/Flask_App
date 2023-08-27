from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [{
    "data": [
        {
            "Contact": 9987644546,
            "Name": "Raju",
            "done": False,
            "id": 1
        },
        {
            "Contact": 9876543222,
            "Name": "Rahul",
            "done": False,
            "id": 2
        }
    ]
}]

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide all data"
        },400)
    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        'status': "success",
        'message': "Data added successfully"
    })

@app.route("/get-data")

def get_tasks():
    return jsonify({
        'data': contacts
    })

if __name__ == '__main__':
    app.run(debug=True)