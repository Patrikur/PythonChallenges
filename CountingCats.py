mystery_string = "my cat your cat"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Add some code below that will count and print how many
# times the character sequence "cat" appears in mystery_string.
# For example, for the string above, it would print 2.
#
# This one is tricky! Think carefully about for-each loops,
# conditionals, and booleans. How can you track what character
# you're currently looking for? We expect you'll use a loop
# and a single big conditional, but there are other approaches
# as well. Try to stick with the topics we've covered so far.


# Add your code here!
counter = 0
for character in mystery_string:
    if character == "c":
        let_1 = True
    if character == "a" and let_1:
        let_2 = True
    if character == "t" and let_1 and let_2:
        counter += 1
print(counter)
