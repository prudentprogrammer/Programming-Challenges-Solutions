# Link: https://uva.onlinejudge.org/external/100/10050.pdf
def calculate_working_days(days, hartal_number_for_parties):
    # Pad 0th day for 1-1 index mapping
    buffer = [False] + ([False] * (days))
    
    for hartal in hartal_number_for_parties:
        startPoint = hartal
        # Stride by hartal days and for each of those days,
        # mark the buffer as true.
        while startPoint <= days:
            buffer[startPoint] = True
            startPoint += hartal
    
    return sum(day and ind % 7 != 0 and ind % 7 != 6 
                for ind, day in enumerate(buffer))
            
for _ in range(int(input())):
    days = int(input())
    parties = int(input())
    hartal_number_for_parties = [int(input()) for _ in range(parties)]
    print(calculate_working_days(days, hartal_number_for_parties))
