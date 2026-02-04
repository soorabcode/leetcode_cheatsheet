# Day 51 
# Compare Version Numbers
# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        len1 = len(revisions1)
        len2 = len(revisions2)
        max_len = max(len1 , len2)
        for i in range(max_len):
            r1 = int(revisions1[i]) if i < len1 else 0 
            r12 = int(revisions2[i]) if i < len2 else 0 
            if r1 < r2 : 
                return -1 
            else:
                return 1
        return 0