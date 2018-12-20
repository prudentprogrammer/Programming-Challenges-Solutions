
def handle_numeric_chunks(chunk, A, B):
    if not chunk:
        B.append(chunk)
    elif chunk[0] == '0':
        if len(chunk) > 1:
            B.append(chunk)   
        else:
            A.append(chunk)
    elif chunk.isdigit():
        A.append(chunk) 
    else:
        B.append(chunk)

    return A, B


def extract_numbers(s):
    A = []
    B = []
    chunk = ''
    for i, letter in enumerate(s):
        if letter in ',;':
            A, B = handle_numeric_chunks(chunk, A, B)
            chunk = ''
        else:
            chunk += letter

    A, B = handle_numeric_chunks(chunk, A, B)
    return A, B 

def format_output(l):
    if not l:
        return "-"
    else:
        temp = ['\"']
        for x in l:
            temp.append(x)
            temp.append(',')
        temp[-1] = '\"'
        return ''.join(temp)

s = input()
A, B = extract_numbers(s)
print(format_output(A))
print(format_output(B))
