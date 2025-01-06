
item_structure = []

def calculate_structure_sum(data_structure):

    if (isinstance(data_structure, int)
            or isinstance(data_structure, float)):
        item_structure.append(data_structure)

    if isinstance(data_structure, str):
        item_structure.append(len(data_structure))

    if (isinstance(data_structure, list)
            or isinstance(data_structure, tuple)
            or isinstance(data_structure, set)):
        for item in data_structure:
            calculate_structure_sum(item)

    if isinstance(data_structure, dict):
        for item_key, item_value in data_structure.items():
            calculate_structure_sum(item_key)
            calculate_structure_sum(item_value)

    return sum(item_structure)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure_2 = [
  [1, 2, {'a': (17,18,19,20), 'b': {3,4,5,6,7}}],
  {'c': 8, 'd': 9, 'e': [10,11,12]},
  (13, {'f': 14, 'g': 15}, 16),
    ("H", {"k", 'l', 'm', 'n'})
]

print(calculate_structure_sum(data_structure))