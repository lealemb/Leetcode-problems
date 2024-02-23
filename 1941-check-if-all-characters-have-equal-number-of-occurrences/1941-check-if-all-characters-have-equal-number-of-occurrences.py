class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s)
        return len(set(counts.values())) == 1