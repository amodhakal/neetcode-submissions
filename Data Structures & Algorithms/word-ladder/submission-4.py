class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return False

        adjlist = defaultdict(list)
        for word in wordList:
            adjlist[word] = []

        print(adjlist)