import json

# https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-python-dictionaries-and-lists
def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(md, key):
    jvar = json.loads(md)
    return list(gen_dict_extract(key, jvar))


if __name__ == '__main__':
    myvar, key = input("Enter the key name to get the value\n").split()
    print(find_key(myvar, key))