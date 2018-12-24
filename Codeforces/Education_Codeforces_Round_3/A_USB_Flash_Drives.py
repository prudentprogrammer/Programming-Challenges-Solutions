import sys

def find_minimum_number_of_flash_drives(storage_sizes, filesize):
    n = len(storage_sizes)
    storage_sizes.sort(reverse=True)
    counter = 0
    for size in storage_sizes:
        filesize -= size
        counter += 1
        if filesize <= 0:
            break

    return counter



number_of_flash_drives = int(sys.stdin.readline().strip())
filesize = int(sys.stdin.readline().strip())

storage_sizes = []
for _ in range(number_of_flash_drives):
    storage_sizes.append(int(sys.stdin.readline().strip()))

sys.stdout.write(str(find_minimum_number_of_flash_drives(storage_sizes, filesize)) + '\n')
