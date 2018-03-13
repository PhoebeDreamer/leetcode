class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s).most_common()
        pq = []
        for word, freq in counter:
            heapq.heappush(pq, (-freq, word))

        ans = ""
        while pq:
            freq, word = heapq.heappop(pq)
            ans+=word*(-freq)
        
        return ans