class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = []
        for char in s:
            if char.isalnum():
                characters.append(char.lower())
        cleaned = "".join(characters)
        return cleaned == cleaned[::-1]