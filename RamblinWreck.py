
#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#This line will open the file:
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
rec_lib = [0,0,0]
rec_list = []
for line in record_file:
    line_split = line.strip("\n").split(",")
    rec_list.append(line_split)
del rec_list[0]

for game in rec_list:
    
    if game[2] == "Home":
        if int(game[3]) > int(game[4]):
            rec_lib[0] += 1
        elif int(game[3]) < int(game[4]):
            rec_lib[1] += 1
        elif int(game[3]) == int(game[4]):
            rec_lib[2] += 1
record_file.close()
print(rec_lib)       
        
     
record_file.close()

    



#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.





