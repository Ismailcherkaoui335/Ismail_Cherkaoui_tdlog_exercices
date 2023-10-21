def solution(str1,str2):
    a = len(str1)
    b = len(str2)
    return str1[slice(a-b,a)] == str2

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)

for test_case in fixed_tests_True:
    input_str, suffix = test_case
    result = solution(input_str, suffix)
    assert result is True, f"Expected True for input {input_str} and suffix {suffix}, but got {result}"

for test_case in fixed_tests_False:
    input_str, suffix = test_case
    result = solution(input_str, suffix)
    assert result is False, f"Expected False for input {input_str} and suffix {suffix}, but got {result}"

print("All tests passed!")

    


"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
