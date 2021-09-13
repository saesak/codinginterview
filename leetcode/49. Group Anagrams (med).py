'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


https://leetcode.com/problems/group-anagrams/

'''



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictlist = []
        final = []
        
        for ele in strs:
            dicto = dict()
            for letter in ele:
                if letter in dicto:
                    dicto[letter] = dicto[letter] + 1
                else:
                    dicto[letter] = 1
            if dicto not in dictlist:
                dictlist.append(dicto)
                final.append([])
                final[-1].append(ele)
            else:
                indx = dictlist.index(dicto)
                final[indx].append(ele)
                
        return final