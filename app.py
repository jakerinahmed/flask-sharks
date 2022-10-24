from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from werkzeug import exceptions
from controllers import sharks

app = Flask(__name__)
CORS(app)


@app.route('/')
def welcome():
    # return jsonify({'message': 'Hello from Flask!'}), 200
    return render_template("home.html"), 200


@app.route('/sharks', methods=["GET", "POST"])
def sharks_handler():
    # fns = {
    #     "GET": sharks.index,
    #     "POST": sharks.create
    # }
    # response, code = fns[request.method](request)
    # print(response)
    # return jsonify(response), code
    if request.method == "GET":
        response, code = sharks.index(request)
        return render_template("shark-list.html", sharks = response)
    else:
        response, code = sharks.create(request)
        print("Hello")
        return render_template("shark-list.html", sharks = jsonify(response))
        # r = request.post("localhost:5000/sharks", jsonify(response))
        # return render_template("shark-list.html")
 


@app.route('/sharks/<int:sharks_id>', methods=["GET", "PATCH", "PUT", "DELETE"])
def sharks_handler_id(sharks_id):
    fns = {
        "GET": sharks.show,
        "PATCH": sharks.update,
        "PUT": sharks.update,
        "DELETE": sharks.destroy
    }
    response, code = fns[request.method](request, sharks_id)
    # return jsonify(response), code
    return render_template("shark-show.html", shark = response)

@app.errorhandler(NotFound)
def handle404(err):
    return jsonify({'message': f'oops{err}'}), 404

@app.errorhandler(BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(InternalServerError)
def handle500(err):
    return jsonify({'message': "It's not you, it's us"}), 500

if __name__ == "__main__":
    app.run(debug=True)
