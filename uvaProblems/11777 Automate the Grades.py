# Link: https://uva.onlinejudge.org/external/117/11777.pdf

def get_letter_for_scores(curr_scores):
    scores = {}
    curr_scores = [int(x) for x in curr_scores]
    for score, curr_range in [
                    ('F', range(0, 60)), 
                    ('D', range(60, 70)), 
                    ('C', range(70, 80)), 
                    ('B', range(80, 90)), 
                    ('A', range(90, 201))
                    ]:
        for i in curr_range:
            scores[i] = score
    return scores[sum(curr_scores[:4]) + sum(sorted(curr_scores[-3:], reverse=True)[:2]) // 2]

for test_case in range(1, int(input())+1):
    try:
        print('Case {}: {}'.format(test_case, get_letter_for_scores(input().split())))
    except EOFError:
        break
