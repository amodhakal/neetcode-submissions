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
                patternmap[word].add(pattern)
        
        tried = set()
        for word1 in wordset:
            for word2 in wordset:
                if (word1, word2) in tried:
                    continue

                if word1 == word2:
                    continue

                tried.add((word1, word2))

                intersect = patternmap[word1].intersection(patternmap[word2])
                if len(intersect) != 1:
                    continue

                adjlist[word1].add(word2)
                adjlist[word2].add(word1)

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
