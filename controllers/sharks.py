from werkzeug.exceptions import BadRequest

sharks = [
    {
        'id': 1,
        'name': 'Bob',
        'species': 'Great White'
    },
    {
        'id': 2,
        'name': 'Mike',
        'species': 'Tiger Shark'
    },
    {
        'id': 3,
        'name': 'John',
        'species': 'Hammerhead Shark'
    },
    {
        'id': 4,
        'name': 'Luke',
        'species': 'Basking Shark'
    },
]


def find_by_id(id):
    try:
        return next(shark for shark in sharks if shark['id'] == id)
    except:
        raise BadRequest(f"We don't have that shark with id {id}!")

def index(request):
    return [shark for shark in sharks], 200

def show(req, id):
    return find_by_id(id), 200

def create(req):
    new_shark = req.get_json()
    new_shark['id'] = sorted([shark['id'] for shark in sharks])[-1] + 1
    sharks.append(new_shark)
    return new_shark, 201

def update(req, id):
    shark = find_by_id(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        shark[key] = val
    return shark, 200

def destroy(req, id):
    shark = find_by_id(id)
    sharks.remove(shark)
    return shark, 204
