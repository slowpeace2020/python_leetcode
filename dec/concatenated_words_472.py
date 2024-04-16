from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self,words:List[str])->List[str]:
        word_set = set(words)
        result = []

        for word in words:
            sz = len(word)
            flags = [False] * (sz+1)
            flags[0] = True
            word_set.remove(word)

            for i in range(sz):
                if not flags[i]:
                    continue

                for k in range(i+1,sz+1):
                    if k-i < sz and word[i:k] in word_set:
                        flags[k] = True

                if flags[sz]:
                    result.append(word)
                    break
            word_set.add(word)

        return result
