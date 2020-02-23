'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case will be when the str has a length of less than 2 (can't equal characters 'th' if so)
    if len(word) < 2:
        return 0
    
    # iterate over string. 
    # check at the start of string first
    # if values at index 0 - 2 == 'th' return 1 plus the value returned from calling the function again, 
    # this time passing in the characters from index 1 - the end of the string
    if word[:2] == 'th':
        return 1 + count_th(word[1:])

    # if values at index 0 - 2 != 'th' just return the value returned from calling the function again, 
    # this time passing in the characters from index 1 - the end of the string
    # keep recurring til all characters have been iterated over and base case has been met

    return count_th(word[1:])

# Could also be refactored to cast word to lowercase before counting number of occurences of 'th' if you wanted it to be case insensitive