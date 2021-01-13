def print_art(file_name):
    f = open(file_name, 'r')
    f_content = f.read()
    print(f_content)
    f.close()