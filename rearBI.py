from collections import deque

with open("rosalind_rear.txt", "r") as f:
    content = [line.strip() for line in f if line.strip()]

def neighbors(perm):
    n = len(perm)
    for i in range(n):
        for j in range(i + 2, n + 1):
            yield perm[:i] + perm[i:j][::-1] + perm[j:]

def reversal_dist(start, target):
    start = tuple(start)
    target = tuple(target)

    if start == target:
        return 0

    front = {start}
    back = {target}

    dist_front = {start: 0}
    dist_back = {target: 0}

    while front and back:
        # 永远扩展较小的一边
        if len(front) > len(back):
            front, back = back, front
            dist_front, dist_back = dist_back, dist_front

        new_front = set()

        for current in front:
            for nxt in neighbors(current):
                if nxt in dist_front:
                    continue

                if nxt in dist_back:
                    return dist_front[current] + 1 + dist_back[nxt]

                dist_front[nxt] = dist_front[current] + 1
                new_front.add(nxt)

        front = new_front

answers = []

for i in range(0, len(content), 2):
    original = list(map(int, content[i].split()))
    target = list(map(int, content[i + 1].split()))
    answers.append(str(reversal_dist(original, target)))

print(" ".join(answers))