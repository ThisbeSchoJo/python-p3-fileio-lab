def write_file(file_name, file_content):
    # writes content to a .txt file, overwriting any existing content
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # appends content to an existing .txt file
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    # reads and returns the content of a .txt file
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
