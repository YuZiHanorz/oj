class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        while i < len(words):
            st = i
            minlen = curlen = len(words[i])
            cnt = 1
            if i == len(words) - 1:
                i += 1
            for j in range(i+1, len(words)):
                if minlen + 1 + len(words[j]) <= maxWidth:
                    cnt += 1
                    minlen += 1 + len(words[j])
                    curlen += len(words[j])
                    if j == len(words) - 1:
                        i = j + 1
                else:
                    i = j
                    break
            slen = maxWidth - curlen
            if cnt == 1:
                tmp = words[st] + ' ' * (maxWidth - curlen)
            elif i == len(words):
                tmp = words[st]
                for j in range(st+1, st+cnt):
                    tmp += ' ' + words[j]
                tmp += ' ' * (maxWidth - minlen)
            else:
                s = slen // (cnt - 1)
                r = slen % (cnt - 1)
                tmp = words[st]
                for j in range(st+1, st+cnt):
                    if r > 0:
                        tmp += ' '*(s+1) + words[j]
                        r -= 1
                    else:
                        tmp += ' '*s + words[j]
            res.append(tmp)
        
        return res
