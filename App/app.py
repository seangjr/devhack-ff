from flask import Flask, request, jsonify

app = Flask(__name__)
#example to make routes
#youtube tutorial link if needed further understanding
#YT link :https://www.youtube.com/watch?v=zsYIw6RXjfM&t=638s
#note! flash installer is in the resume miner installation file
@app.route('/')
def index():
    return "hello world"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data={
        "user_id": user_id,
        "name": "John",
        "email": "john@email.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)