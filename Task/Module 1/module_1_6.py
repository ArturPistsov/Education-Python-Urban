my_dict = {
    "Black": '#000000',
    'Red': '#000000',
    'Green': '#00FF00'
}
print(my_dict)
my_dict['Red'] = '#FF0000'
my_dict['Blue'] = '#0000FF'
print(my_dict)
my_dict.update({'Yellow': '#FFFF00', 'White': '#FFFFFF'})
print(my_dict)
my_dict.pop('White')
print(my_dict)
print()

my_set = {1, 1, 2, 2.0, '3','3.0'}
print(my_set)
my_set.update([4,'5'])
my_set.remove('3.0')
print(my_set)