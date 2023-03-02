def find_msg_generator(binary_file):
    binary_byte = binary_file.read(1)
    integer = int.from_bytes(binary_byte, byteorder='big')
    while binary_byte:
        current_msg = ""

        if ord('z') >= integer >= ord('a'):
            current_msg = binary_byte.decode('ascii')
            binary_byte = binary_file.read(1)
            integer = int.from_bytes(binary_byte, byteorder='big')
            while ord('z') >= integer >= ord('a'):
                current_msg = current_msg+(binary_byte.decode('ascii'))
                binary_byte = binary_file.read(1)
                integer = int.from_bytes(binary_byte, byteorder='big')

        if len(current_msg) >= 5 and integer == ord('!'):
            yield current_msg+"\n"

        binary_byte = binary_file.read(1)
        integer = int.from_bytes(binary_byte, byteorder='big')


with open("logo.jpg", 'rb') as binary_file:
    # Loop through the file byte by byte
    for item in find_msg_generator(binary_file):
        print(item, end="")
