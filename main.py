"""I/O input and output"""
result = open('text.txt')
# print(result)
# print(result.read())
# print(result.read())
#
# # seek method
# result.seek(0)
# print(result.read())
# result.seek(3)
# print(result.read())

# readline method
print(result.readline())

# readlines method
result.seek(0)
print(result.readlines())

# close
result.close()
