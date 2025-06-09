from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for w1, w2 in zip(words, words[1:]):
        for a, b in zip(w1, w2):
            if a != b:
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""

    q = deque([c for c in indegree if indegree[c] == 0])
    res = []

    while q:
        c = q.popleft()
        res.append(c)
        for n in graph[c]:
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)

    return "".join(res) if len(res) == len(indegree) else ""

# Test Case
words = ["wrt", "wrf", "er", "ett", "rftt"]
print("Alien Order:", alien_order(words))
