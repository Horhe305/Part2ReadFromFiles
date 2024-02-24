"""File paths"""
# ./ syntax
with open('./content/something.txt', 'r') as result:
    print(result.read())

# ../ syntax
# with open('../content/something.txt', 'r') as result1:  # ../ means look at 1 level outside the current path
#     print(result1.read())
