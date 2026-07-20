import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        wordset.add(beginWord)
        WORD_LEN = len(beginWord)

        if endWord not in wordset:
            return 0

        adjlist = defaultdict(set)
        for word in wordset:
            adjlist[word] = set()

        patternmap = defaultdict(set)
        for word in wordset:
            for idx in range(WORD_LEN):
                pattern = list(word)
                pattern[idx] = "*"
                pattern = "".join(pattern)
                patternmap[pattern].add(word)

        for matches in patternmap.values():
            if len(matches) < 2:
                continue

            for word1 in matches:
                for word2 in matches:
                    if word1 == word2:
                        continue

                    adjlist[word2].add(word1)
                    adjlist[word1].add(word2)


        visited = set()
        q = collections.deque()
        q.append((beginWord, 0))

        while q:
            curr, depth = q.popleft()
            if curr == endWord:
                return depth + 1

            for outgoing in adjlist[curr]:
                if outgoing in visited:
                    continue
                    
                visited.add(curr)
                q.append((outgoing, depth + 1))

        return 0
