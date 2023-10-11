class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(x) for x in strs])
        common = ""
        for i in range(min_len):
            l = strs[0][i]
            flag = True
            for word in strs:
                if word[i] != l:
                    flag = False
                    break
            if flag:
                common += l
            else:
                break
        return common