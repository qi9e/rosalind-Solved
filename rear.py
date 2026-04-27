from collections import deque

with open("rosalind_rear.txt", "r") as f:
    content = [line.strip() for line in f if line.strip()]

def reversal_dist(original, target):
    original = tuple(original)
    target = tuple(target)

    if original == target:
        return 0

    n = len(original)
    result = deque([(original, 0)])
    visited = {original}

    while result:
        current, dist = result.popleft()

        for i in range(n):
            for j in range(i + 2, n + 1):  # meanless reversal of length 1
                new_perm = current[:i] + current[i:j][::-1] + current[j:]

                if new_perm == target:
                    return dist + 1

                if new_perm not in visited:
                    visited.add(new_perm)
                    result.append((new_perm, dist + 1))

            print(f"Processed {i} with distance {dist}, queue size: {len(result)}")

answers = []

for i in range(0, len(content), 2):
    original = list(map(int, content[i].split()))
    target = list(map(int, content[i + 1].split()))
    answers.append(str(reversal_dist(original, target)))

print(" ".join(answers))