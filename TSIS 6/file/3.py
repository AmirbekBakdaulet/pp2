import os

def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)   
        print(f"Directory portion: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")
path=input("path:")
test_path(path)