def make_index_object_from_dict(path_till_here: str, input: dict, output: dict):
    for key, value in input.items():
        make_index_object_from_any(path_till_here + '/' + key, value, output)

def make_index_object_from_list(path_till_here: str, input: list, output: dict):
    for i in range(len(input) - 1):
       make_index_object_from_any(path_till_here + '/' + str(i), input[i], output) 

def make_index_object_from_any(path_till_here: str, input: any, output: dict):
    if type(input) is list:
        make_index_object_from_list(path_till_here, input, output)
        return

    if type(input) is dict:
        make_index_object_from_dict(path_till_here, input, output)
        return

    output[path_till_here] = input

def make_index_object(input: any) -> dict:
    result = dict()
    make_index_object_from_any('root', input, result)
    return result