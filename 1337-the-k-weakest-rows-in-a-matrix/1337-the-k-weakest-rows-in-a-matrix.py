class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_val = len(mat[0]) + 1
        sums = []
        for l in mat:
            sums.append(sum(l))
            
        out = []
        for i in range(k):
            smallest = 0;
            for j in range(len(sums)):
                if sums[j] < sums[smallest]:
                    smallest = j
            
            out.append(smallest)
            sums[smallest] = max_val
            
        return out