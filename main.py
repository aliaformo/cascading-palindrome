class CascadingPalindrome:
    def __init__(self, parameter):
        if not self._is_valid_input(parameter):
            raise ValueError("Invalid input. Please provide a valid parameter.")
        self.parameter = parameter

    @staticmethod
    def _is_valid_input(parameter):
        if not isinstance(parameter, str) or parameter == "":
            return False
        return all(item.strip().isalnum() for item in parameter.split())

    @staticmethod
    def _is_palindrome(s):
        return s == s[::-1]

    def find_cascading_palindrome(self):
        palindrome_parts = []

        for item in self.parameter.split():
            if self._is_palindrome(item):
                palindrome_parts.append(item)

        return ' '.join(palindrome_parts)