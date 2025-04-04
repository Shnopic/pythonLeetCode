#Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = set(sentence)
        return len(seen) == 26