"""Error handling: Try - Except block"""
try:
    with open('./content/test.txt', 'r') as result:
        print(result.read())
except FileNotFoundError as err:
    print('File was not found!')
    # raise err
except IOError as err1:
    print('IO Error!')

print('This comes after Try-Except block')

# ImportError
# IndexError
# TypeError

