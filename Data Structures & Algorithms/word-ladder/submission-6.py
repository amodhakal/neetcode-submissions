import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjlist = defaultdict(list)
        for word in wordList + [beginWord]:
            adjlist[word] = []

        for word in wordList + [beginWord]:
            for chidx in range(0, len(word)):
                for ch in list(string.ascii_lowercase):
                    new_word = list(word)
                    new_word[chidx] = ch
                    new_word = "".join(new_word)

                    if new_word in adjlist:
                        adjlist[word].append(new_word)

        visited = set()
        q = collections.deque()
        q.append((beginWord, 0))

        while q:
            curr, depth = q.popleft()
            if curr == endWord:
                return depth + 1

            visited.add(curr)
            for outgoing in adjlist[curr]:
                if outgoing in visited:
                    continue
                q.append((outgoing, depth + 1))

        return 0
