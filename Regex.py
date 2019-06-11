#A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. 
#Regular expressions are widely used in UNIX world.

# match func
# This function attempts to match RE pattern to string with optional flags.
re.match(pattern, string, flags=0)
# pattern- Regular exp to be matched
# string- String to be searched to match pattern at the beginning of string
# flags- You can specify different flags using bitwise OR (|)

# re.match function returns a match object on success, None on failure.
