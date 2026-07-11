from dataclasses import dataclass

@dataclass
class PrefixNode:
    ch: str
    children: dict
    is_end: bool

    def __str__(self):
        return f"{self.ch} {"DONE" if self.is_end else ""}"

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode("DUMMY", {}, False)

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                new_node = PrefixNode(ch, {}, False)
                curr.children[ch] = new_node

            curr = curr.children[ch]

        curr.is_end = True
        print(self.root)


    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
            if not curr:
                return False

        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            curr = curr.children[ch]
            if not curr:
                return False

        return True
        
        