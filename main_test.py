from main import CascadingPalindrome

# Test cases
test_cases = [
    "1230321",
    "1230321 09234 0124210",
    "abcd5dcba 1230321 09234 0124210",
    "abcd5dcba 1230321 @#$%",
    1230321,
    "",
    "runraninarnur",
    1230321592345124210,
    "~!^",
    "somosonosomos",
]

for test_case in test_cases:
    try:
        cascading_palindrome = CascadingPalindrome(test_case)
        result = cascading_palindrome.find_cascading_palindrome()
        print(f"Input: {test_case} => Output: {result}")
    except ValueError as e:
        print(f"Input: {test_case} => Error: {e}")