class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return "" if it is an empty string list
        if not str:
            return ""

        # start with the first string as the prefix
        prefix = strs[0]

        # compare the prefix with each string in the list of string
        for string in strs[1:]:
            # update the prefix by trimming it down to the common part
            while not string.startswith(prefix):
                # trimming the last characters if it is not match the prefix till
                # it match the prefix, and then it will return the prefix
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix