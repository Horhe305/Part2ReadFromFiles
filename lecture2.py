"""Write to a file"""
# with open('text.txt', 'r') as result:
#     print(result.read())
#
# with open('text.txt', 'w') as result:
#     result.write('How are you')

with open('text.txt', 'r+') as result:
    result.write('Hello')
