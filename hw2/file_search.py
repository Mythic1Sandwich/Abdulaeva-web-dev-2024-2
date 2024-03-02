import os

def search_file(filename, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        if filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r') as file:
                for _ in range(5):
                    print(file.readline())
            return True
    return False

if __name__ == '__main__':
    filename = input()
    if not search_file(filename, os.path.dirname(os.path.realpath(__file__))):
        print(f"File {filename} not found")
