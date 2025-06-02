import os

# File search (Linear search)
def file_search(name, directory):
    found = False
    for dirpath, dirname, filename in os.walk(directory):
        if name in filename:
            print("File Found")
            print(f"Full Path: {os.path.join(dirpath, name)}")
            found = True
            break
    if not found:
        print("File Not Found")

# Rename a file or folder
def rename(old, new, path):
    original_wd = os.getcwd()
    try:
        os.chdir(path)
        os.rename(old, new)
        if new in os.listdir():
            print("Renamed Successfully")
        else:
            print("Error Occurred: Rename failed")
    except OSError as e:
        print(f"Error Occurred: {e}")
    finally:
        os.chdir(original_wd)

# Create a folder
def create_folder(path, name):
    try:
        full_path = os.path.join(path, name)
        os.makedirs(full_path, exist_ok=True)
        if name in os.listdir(path):
            print("Folder Created Successfully")
        else:
            print("Error Occurred: Folder was not created")
    except OSError as e:
        print(f"Error Occurred: {e}")

# Create a File
def create_file(path, name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        fd = os.open(name, os.O_CREAT)
        os.close(fd)
        if os.path.exists(name):
            print("File Created Successfully")
        else:
            print("Error Occurred: File was not created")
    except OSError as e:
        print(f"Error Occurred: {e}")
    finally:
        os.chdir(original_path)

# Tells the details about File
def stats(path):
    try:
        stat_info = os.stat(path)
        print(f"File Stats for {path}:")
        print(f"  Size: {stat_info.st_size} bytes")
        print(f"  Last Modified: {stat_info.st_mtime}")
        print(f"  Last Accessed: {stat_info.st_atime}")
        print(f"  Permissions: {oct(stat_info.st_mode & 0o777)}")
    except OSError as e:
        print(f"Error Occurred: {e}")

# Brute File Generator
def brute_create(path, name_of_file, count):
    base, ext = os.path.splitext(name_of_file)
    original_path = os.getcwd()
    try:
        os.chdir(path)
        for i in range(count):
            name = f"{base}{i}{ext}"
            fd = os.open(name, os.O_CREAT)
            os.close(fd)
            if os.path.exists(name):
                print(f"File '{name}' Created Successfully")
            else:
                print(f"Error Occurred: File '{name}' was not created")
    except OSError as e:
        print(f"Error Occurred: {e}")
    finally:
        os.chdir(original_path)

# Delete a File
def delete(path):
    try:
        os.remove(path)
        if os.path.exists(path):
            print("Error Occurred: File Not Deleted")
        else:
            print("File Deleted")
    except OSError as e:
        print(f"Error Occurred: {e}")

# Path verification
def pathverify(path):
    return os.path.exists(path)

# Main program
print("File Handler\nOperations:\n1) File search - file_search\n2) Create a Folder - folder_create\n3) Create a File - file_create\n4) Rename File or Folder - rename\n5) File stats - file_stats\n6) Delete File - delete\n7) Brute File Generator - brute_gen\n8) Exit - exit")
while True:
    user_operation = input("Enter the operation: ").strip().lower()
    if user_operation == "exit":
        print("Exiting File Handler")
        break
    if not user_operation.isnumeric():
        match user_operation:
            case "file_search":
                path = input("Enter the directory path to search in: ")
                if pathverify(path):
                    name = input("Enter the name of the file to search: ")
                    file_search(name, path)
                else:
                    print("Enter a Valid Directory Path")
            case "folder_create":
                path = input("Enter the directory path: ")
                if pathverify(path):
                    name = input("Enter the name of the folder to create: ")
                    create_folder(path, name)
                else:
                    print("Enter a Valid Directory Path")
            case "file_create":
                path = input("Enter the directory path: ")
                if pathverify(path):
                    name = input("Enter the name of the file to create: ")
                    create_file(path, name)
                else:
                    print("Enter a Valid Directory Path")
            case "file_stats":
                path = input("Enter the full path to the file or folder: ")
                if pathverify(path):
                    stats(path)
                else:
                    print("Enter a Valid Path (full path to file or folder)")
            case "rename":
                path = input("Enter the directory path of the file/folder: ")
                if pathverify(path):
                    old = input("Enter the old name: ")
                    new = input("Enter the new name: ")
                    rename(old, new, path)
                else:
                    print("Enter a Valid Directory Path")
            case "delete":
                path = input("Enter the full path to the file to delete: ")
                if pathverify(path):
                    delete(path)
                else:
                    print("Enter a Valid File Path")
            case "brute_gen":
                path = input("Enter the directory path: ")
                if pathverify(path):
                    name = input("Enter the base name of the files: ")
                    count = int(input("Enter the number of files to create: "))
                    brute_create(path, name, count)
                else:
                    print("Enter a Valid Directory Path")
            case _:
                print("Invalid operation. Please choose from the listed options.")
    else:
        print("Please enter a valid operation name (e.g., 'file_search')")