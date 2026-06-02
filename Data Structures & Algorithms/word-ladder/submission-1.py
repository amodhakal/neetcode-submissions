class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        listmap = {}
        listmap[beginWord] = []

        for word in wordList:
            for wordkey in listmap.keys():
                diffcount = 0

                for i in range(len(word)):
                    if word[i] != wordkey[i]:
                        diffcount += 1

                if diffcount != 1:
                    continue

                current = listmap[wordkey]
                current.append(word)
                listmap[wordkey] = current
            listmap[word] = []
        print(listmap)

        def bfs(word, depth):
            # Matched
            if word == endWord:
                return depth + 1

            found = listmap[word]
            depths = [1000]
            for items in found:
                result = bfs(items, depth + 1)
                depths.append(result)
            return min(depths)

        result = bfs(beginWord, 0)
        if result == 1000:
            return 0

        return result