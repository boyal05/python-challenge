# method to read the records
def read_csv(filename):
    with open(filename,'r') as f:
        rows = f.readlines()
        for i in range(len(rows)):
            rows[i] = rows[i][:-1]
        # separate the header row
        header_row = rows[0]
        # remove the header row from the set of rows
        rows.pop(0)
        # return header and data
        return header_row,rows 

# the method to get all the candidates
def get_candidates(rows):
    # the list of all candidates to return
    candidates = []
    # for each data row
    for row in rows:
        # get the candidate in this row
        candidate = row.split(",")[2]
        # if this candidate not in our list of candidates, add to list of candidates
        if candidate not in candidates:
            candidates.append(candidate)
    return candidates

# method to get the votes for this candidate
def get_votes(rows, candidate):
    votes = 0
    for row in rows:
        # get the voted candidate in this row
        voted_candidate = row.split(",")[2]
        # increment the votes by 1 if the voted candidate matches the given candidate 
        if voted_candidate == candidate:
            votes += 1
    return votes


# method to get the winner
def get_winner(candidates, votes):
    winner = candidates[0]
    max_votes = votes[0]
    for i in range(1, len(candidates)):
        if votes[i] > max_votes:
            max_votes = votes[i]
            winner = candidates[i]
    return winner

# the main method 
def main():
    # read rows
    header_row, rows = read_csv("Resources/election_data.csv")
    # get candidates
    candidates = get_candidates(rows)
    # print(candidates)

    # print header
    print("Election Results")
    print("-------------------------")
    # print the total votes
    total_votes = len(rows)
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    # find votes for each candidate
    votes = []
    for candidate in candidates:
        votes.append(get_votes(rows,candidate))
    # print(votes)

    # print percentage of each candidate
    for i in range(len(candidates)):
        percentage_votes = (votes[i]*100)/total_votes
        print(f"{candidates[i]}: {format(percentage_votes, '.3f')}% ({votes[i]})")

    # print winner
    print("-------------------------")
    print(f"Winner : {get_winner(candidates, votes)}")    
    print("-------------------------")

    # print to file 
    with open('results.txt', "w") as f:
        # print the details  one by one 
        f.write("Election Results\n")
        f.write("-------------------------\n")
        # print the total votes
        f.write(f"Total Votes: {total_votes}\n")
        f.write("-------------------------\n")

        # print percentage of each candidate
        for i in range(len(candidates)):
            percentage_votes = (votes[i]*100)/total_votes
            f.write(f"{candidates[i]}: {format(percentage_votes, '.3f')}% ({votes[i]})\n")

        # print winner
        f.write("-------------------------\n")
        f.write(f"Winner : {get_winner(candidates, votes)}\n")    
        f.write("-------------------------\n")

# run the main
main()

