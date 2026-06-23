class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqmap = dict()

        for val in strs:
            counter = Counter(val)
            counter_list = list(dict(counter).items())
            counter_list.sort()
            counter_key = str(counter_list)

            if freqmap.get(counter_key) is None:
                freqmap[counter_key] = []
            
            freqmap[counter_key].append(val)

        return list(freqmap.values())