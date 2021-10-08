import csv

with open("Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    # store the header
    header_row = next(csvreader)

    # to store the total votes
    total_votes = 0

    # to store total number of rows
    num_rows = 0

    # to store the candidates and their votes
    candidate_votes = {}
    for row in csvreader:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

        num_rows += 1
        total_votes += 1

    
    # print header
    print("Election Results")
    print("-------------------------")
    # print the total votes
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # print percentage of each candidate
    for candidate in candidate_votes:
        percentage_votes = (candidate_votes[candidate] *100)/total_votes
        print(f"{candidate}: {format(percentage_votes, '.3f')}% ({candidate_votes[candidate]})")
    
    # find winner
    winner = next(iter(candidate_votes))
    max_votes = candidate_votes[winner]
    for candidate in candidate_votes:
        if candidate_votes[candidate] > max_votes:
            max_votes = candidate_votes[candidate]
            winner = candidate

    # print winner
    print("-------------------------")
    print(f"Winner : {winner}")    
    print("-------------------------")

    #  print to file 
    with open('results.txt', "w") as f:
        # print the details  one by one 
        f.write("Election Results\n")
        f.write("-------------------------\n")
        # print the total votes
        f.write(f"Total Votes: {total_votes}\n")
        f.write("-------------------------\n")

        # print percentage of each candidate
        for candidate in candidate_votes:
            percentage_votes = (candidate_votes[candidate] *100)/total_votes
            f.write(f"{candidate}: {format(percentage_votes, '.3f')}% ({candidate_votes[candidate]})\n")

        # print winner
        f.write("-------------------------\n")
        f.write(f"Winner : {winner}\n")    
        f.write("-------------------------\n")
