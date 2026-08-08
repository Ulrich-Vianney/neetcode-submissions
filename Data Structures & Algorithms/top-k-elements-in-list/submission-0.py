class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            dico={}
            for i in nums:
                if i not in dico:
                    dico[i]=0
                dico[i]+=1
            freq={}
            for i,freq_i in dico.items():
                if freq_i not in freq:
                    freq[freq_i]=[]
                freq[freq_i].append(i)
            res=[]
            for j in sorted(freq):
                res+=freq[j]
            return res[-k:]