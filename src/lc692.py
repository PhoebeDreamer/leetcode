class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words).most_common()
        pq = []
        for word, freq in counter:
            heapq.heappush(pq, (-freq, word))
        
        ans = []
        for i in range(k):
            freq, word = heapq.heappop(pq)
            ans.append(word)
        
        return ans