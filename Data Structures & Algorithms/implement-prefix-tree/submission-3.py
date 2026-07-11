from dataclasses import dataclass, field

@dataclass(slots=True)
class PrefixNode:
    children: dict[str, "PrefixNode"] = field(default_factory=dict)
    is_end: bool = False


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            curr = curr.children.setdefault(ch, PrefixNode())
        curr.is_end = True

    def _find(self, s: str) -> PrefixNode | None:
        curr = self.root
        for ch in s:
            curr = curr.children.get(ch)
            if curr is None:
                return None
        return curr

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None