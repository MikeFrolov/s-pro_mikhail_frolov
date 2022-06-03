def file_line_editor():

    origin_file = input("Please enter the name of the original file: ")
    try:
        with open(origin_file, 'r') as opened_file:
            count = 1
            file_to_write = input("Please enter a filename to edit: ")
            for line in opened_file:
                with open(file_to_write, 'a') as editable_file:
                    editable_file.write(f"{count}: {line}")
                count += 1
    except FileNotFoundError:
        print("Error: File with this name does not exist!")
