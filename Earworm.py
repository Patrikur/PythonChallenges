
lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 3

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Recall the Earworm problem (3.3.5 Coding Exercise 2). The
# first time, you would still finish printing the entire list
# of lyrics after lines_of_sanity was exceeded.
#
# Revise that code so that you always stop when lines_of_sanity
# is reached. If lines_of_sanity is 6, you would print 6 lines,
# no matter how many lines are in the list. If there are fewer
# than 6 lines in the list, then you'd repeat the list until
# the number of lines is reached.
#
# For example, with the values above, you'd print:
# I wanna be your endgame
# I wanna be your first string
# I wanna be your A-Team
# I wanna be your endgame, endgame
# I wanna be your endgame
# I wanna be your first string
# MAKE IT STOP
#
# That's 6 lines: the entire list once, then the first two lines
# again to reach 6. As before, print MAKE IT STOP when you're
# done.
#
# HINT: There are multiple ways to do this: some involve a small
# change to our earlier answer, others involve a more wholesale
# rewrite. If you're stuck on one, try to think of a totally
# different way!


# Add your code here! Using the initial inputs from above, this
# should print 7 lines: all 4 lines of the list, then the first
# two lines again, then MAKE IT STOP
lines_heard = 0
verses = len(lyrics)
while lines_heard < lines_of_sanity and lines_heard < verses and lines_of_sanity < verses:
    for i in range(0, lines_of_sanity):
        print(lyrics[i])
        lines_heard += lines_of_sanity

while lines_heard < lines_of_sanity and lines_heard < verses and not lines_of_sanity < verses:
    for line in lyrics:
        lines_heard += 1
        print(line)

while lines_heard < lines_of_sanity and (lines_of_sanity - lines_heard) >= verses:
    for line in lyrics:
        lines_heard += 1
        print(line)

while lines_heard < lines_of_sanity and (lines_of_sanity - lines_heard) < verses and (lines_of_sanity - lines_heard) > 0:
    extra = lines_of_sanity - lines_heard
    for i in range(0, extra):
        print(lyrics[i])
    lines_heard += extra

print("MAKE IT STOP")
