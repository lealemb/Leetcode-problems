class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        uniqueCounts = set(counts.values())
        return len(counts) == len(uniqueCounts)