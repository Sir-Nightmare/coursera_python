import json
from functools import wraps


def to_json(fun):
    @wraps(fun)
    def wrapper(*args, **kwds):
        data = fun(*args, **kwds)
        return json.dumps(data)

    return wrapper


@to_json
def get_data():
    return ['data', 42]


if __name__ == '__main__':
    print(type(get_data()), get_data())
