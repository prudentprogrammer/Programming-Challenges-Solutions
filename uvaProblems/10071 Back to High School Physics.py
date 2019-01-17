# Link: https://uva.onlinejudge.org/external/100/10071.pdf

while True:
    try:
        velocity, time = [int(x) for x in input().split()]
        print(velocity * time * 2)
    except:
        break # End of input
