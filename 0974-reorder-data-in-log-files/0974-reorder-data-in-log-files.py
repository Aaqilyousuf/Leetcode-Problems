class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_logs = []
        let_logs = []
        for log in logs:
            if log[-1].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log)

        # lexicographical order 
        let_logs.sort(key = lambda x: (x.split()[1:], x.split()[0]))

        res = let_logs + dig_logs

        return res