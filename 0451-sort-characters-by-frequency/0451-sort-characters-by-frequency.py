class Solution:
    def frequencySort(self, s: str) -> str:
        map = defaultdict(int)
        for i in s:
            map[i] += 1
        freq_list = []
        for k, v in map.items():
            freq_list.append((k, v))
        sorted_freq = sorted(freq_list, key=lambda item:item[1], reverse=True)
        res = ""
        for char, freq in sorted_freq:
            res += char*freq
        return res