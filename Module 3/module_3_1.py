calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    new_tuple = (len(string),string.upper(),string.lower())
    return new_tuple

def is_contains(string, list):
    count_calls()
    for i in range(len(list)):
        if string.lower() == list[i].lower():
            result = True
            break
        else:
            result = False
    return result


print(string_info('Day'))
print(string_info('Google'))
print(string_info('Python project'))
print(is_contains('Car', ['Kar','CAR','card']))
print(is_contains('Or', ['Vendor','TOR','tea or coffee']))
print(calls)