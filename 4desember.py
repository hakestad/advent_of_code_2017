# --- Day 4: High-Entropy Passphrases ---

# A new system policy has been put in place that requires all
# accounts to use a passphrase instead of simply a password.
# A passphrase consists of a series of words (lowercase letters)
# separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.

# The system's full passphrase list is available as your puzzle input.
# How many passphrases are valid?

num_valid = 0
with open("puzzle_4.txt") as puzzle:
    for line in puzzle:
        words = [i for i in line.split()]
        # Use set() to remove duplicates, then compare length of lists
        isDuplicateFree = len(words) == len(set(words))
        # Pythons 'ternary operator'
        num_valid += (1 if isDuplicateFree else 0)
print("Valid passphrases:", num_valid)

# --- Part Two ---

# For added security, yet another system policy has been put in place.
# Now, a valid passphrase must contain no two words that are anagrams of
# each other - that is, a passphrase is invalid if any word's letters can
# be rearranged to form any other word in the passphrase.

# For example:

# abcde fghij is a valid passphrase.
# abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
# a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
# iiii oiii ooii oooi oooo is valid.
# oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
# Under this new system policy, how many passphrases are valid?

def is_anagram(phrase, tests):
    for test in tests:
        if (sorted(test) == sorted(phrase)):
            return True
    return False

num_valid = 0
with open("puzzle_4.txt") as puzzle:
    for line in puzzle:
        words = [i for i in line.split()]
        found_anagram = False

        for word in words:
            # Only check for anagram with the other items in this passphrase, not itself
            words_copy = words[:]
            idx = words.index(word)
            del words_copy[idx]

            if (is_anagram(word, words_copy)):
                found_anagram = True
                break

        num_valid += 0 if found_anagram else 1

print("Valid passphrases with added security:", num_valid)
