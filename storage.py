import argparse
import json
import os
import tempfile


def write_dict_to_file(data):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def read_dict_from_file():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            data = json.load(f)
            if data:
                return data
    return {}


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Input key')
    parser.add_argument('--val', default=None, help='Input value to set key-value pair to storage')
    return parser.parse_args()


def print_value(value):
    if value:
        print(value[0], end='')
        if len(value) > 1:
            for item in value[1:]:
                print(',', item, end='')
        print()
    else:
        print('')


if __name__ == '__main__':
    data_dict = read_dict_from_file()
    args = get_args()
    if args.val:
        if data_dict.get(args.key):
            data_dict[args.key].append(args.val)
        else:
            data_dict[args.key] = [args.val]
        write_dict_to_file(data_dict)
    else:
        print_value(data_dict.get(args.key))
