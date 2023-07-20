from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.s = None

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.backtracking(0, [])
        return self.result

    def backtracking(self, idx: int, ips: List[str]):
        if len(ips) > 4:
            return
        elif len(ips) == 4 and idx == len(self.s):
            IP = '.'.join(ips)
            self.result.append(IP)
            print(idx)
            return

        for end_idx in range(idx, min(idx + 3, len(self.s))):
            sub_ip = self.s[idx:end_idx + 1]
            if self.validIP(sub_ip):
                ips.append(sub_ip)
                self.backtracking(idx + len(sub_ip), ips)
                ips.pop()
        return

    def validIP(self, sub_ip: str) -> bool:
        if len(sub_ip) == 1:
            return True
        if sub_ip[0] == '0':
            return False
        if 255 < int(sub_ip):
            return False

        return True


if __name__ == "__main__":
    obj = Solution()
    s = "25525511135"
    print(obj.restoreIpAddresses(s))
