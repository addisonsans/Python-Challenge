import os
import csv

# set path
pollpath = os.path.join('election_data.csv')

# tally total votes
total_votes = 0

with open(pollpath) as csvfile:
    pollreader = csv.reader(csvfile)
    if csv.Sniffer().has_header: #skip the header
        next(pollreader)
    for row in pollreader:
        total_votes += 1

print(total_votes)

# create list of names
full_list = []

with open(pollpath) as csvfile:
    pollreader = csv.reader(csvfile)
    if csv.Sniffer().has_header: #skip the header
        next(pollreader)
    for row in pollreader:
        full_list.append(row[2])

# find unique names in list
set_list = set(full_list)
print(set_list)

# count instances of names per list
khan_count = full_list.count('Khan')
cor_count = full_list.count('Correy')
tool_count = full_list.count("O'Tooley")
li_count = full_list.count('Li')

# find percentage of votes per candidate
khan_percent = (khan_count / total_votes) * 100
cor_percent = (cor_count / total_votes) * 100
tool_percent = (tool_count / total_votes) * 100
li_percent = (li_count / total_votes) * 100

# tag winner
winner = "Khan"

# set write path
PollOut = open('PyPoll Output')

# write to txt
PollOut.write(f"Polling Data\n")
PollOut.write(f'----------------------------------------------\n')
PollOut.write(f"O'Tooley: {tool_count},  {tool_percent}\n")
PollOut.write(f'Correy: {cor_count}, "  " {cor_percent}\n')
PollOut.write(f'Khan: {khan_count}, "  "  {khan_percent}\n')
PollOut.write(f'Li: {li_count}, "  " {li_percent}\n')
PollOut.write('----------------------------------------------\n')
PollOut.write(f'The winner is: {winner}\n')

# write to terminal
print(f"Polling Data")
print(f'---------------------------------------------')
print(f"O'Tooley: {tool_count},  {tool_percent}")
print(f'Correy: {cor_count}, "  " {cor_percent}')
print(f'Khan: {khan_count}, "  "  {khan_percent}')
print(f'Li: {li_count}, "  " {li_percent}')
print(f'----------------------------------------------')
print(f'The winner is: {winner}')