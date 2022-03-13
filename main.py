import sys

def redirect_to_file(text):
    sys.stdout = open('redirect.txt', 'w')
    print(text)

"""
    after this script is run:
    - existing content will be removed completely.
    - only "hello world 4" will be kept in the .txt file.
"""



redirect_to_file("hello world 1")
redirect_to_file("hello world 2")
redirect_to_file("hello world 3")
redirect_to_file("hello world 4")  #only "hello world 4" will be kept in the .txt file.
