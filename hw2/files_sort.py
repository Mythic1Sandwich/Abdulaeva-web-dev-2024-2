import os

def sort_files(directory):
    files = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_name, file_ext = os.path.splitext(file)
            if file_ext in files:
                files[file_ext].append(file_name)
            else:
                files[file_ext] = [file_name]
    
    sorted_files = []
    for ext in sorted(files.keys()):
        for file_name in sorted(files[ext]):
            sorted_files.append(f"{file_name}{ext}")
    
    return sorted_files

if __name__ == '__main__':
    directory_path = input("Введите путь до директории: ")
    files_list = sort_files(directory_path)
    
    for file_name in files_list:
        print(file_name)
