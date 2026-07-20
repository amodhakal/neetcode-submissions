import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        wordset.add(beginWord)
        WORD_LEN = len(beginWord)

        if endWord not in wordset:
            return 0

        patterntowordmap = defaultdict(set)
        for word in wordset:
            for idx in range(WORD_LEN):
                pattern = list(word)
                pattern[idx] = "*"
                pattern = "".join(pattern)
                patterntowordmap[pattern].add(word)

        visited = set()
        q = collections.deque()
        q.append((beginWord, 0))

        while q:
            curr, depth = q.popleft()
            if curr == endWord:
                return depth + 1

            for idx in range(WORD_LEN):
                pattern = curr[:idx] + "*" + curr[idx+1:]
                for word in patterntowordmap[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append((word, depth + 1))

        return 0
