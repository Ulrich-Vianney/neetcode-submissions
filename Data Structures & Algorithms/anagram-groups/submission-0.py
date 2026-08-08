class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            if len(strs)==0:
                return [[""]]
            else:
                if len(strs)==1:
                    return [strs]
                else:
                    dico={}
                    for i in range(len(strs)):
                        key=tuple(sorted(strs[i]))
                        if key not in dico:
                            dico[key]=[]
                        dico[key].append(strs[i])
                    return [it for _,it in dico.items()]