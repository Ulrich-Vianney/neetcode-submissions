class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return "[]"
        res_total = ""
        for i in range(n):
            s = strs[i]
            res = f"{i}--{len(s)}--"
            dico = {}
            for j, ch in enumerate(s):
                dico.setdefault(ch, []).append(j)
            for ch in sorted(dico):
                positions = dico[ch]
                res += ch + "{{" + str(len(positions)) + "{{"
                for u in positions:
                    res += str(u) + "{{"
            res_total += res
        return res_total

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j:j+2] != "--":
                j += 1
            j += 2 
            k = j
            while s[k:k+2] != "--":
                k += 1
            length = int(s[j:k])
            k += 2
            chars = [""] * length
            placed = 0
            while placed < length:
                ch = s[k]          
                k += 1
                k += 2 
                m = k
                while s[m:m+2] != "{{":
                    m += 1
                count = int(s[k:m])
                k = m + 2
                for _ in range(count):
                    m = k
                    while s[m:m+2] != "{{":
                        m += 1
                    pos = int(s[k:m])
                    chars[pos] = ch
                    k = m + 2
                    placed += 1
            res.append("".join(chars))
            i = k
        return res