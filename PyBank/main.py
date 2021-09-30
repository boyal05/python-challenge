import csv

with open("Resources/budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    # store the header
    header_row = next(csvreader)

    # to store the total of profits/loss
    total = 0

    # to store total number of rows
    num_rows = 0

    # to store greatest increase
    greatest_increase = 0
    greatest_increase_month = ""

    # to store greatest decrease
    greatest_decrease = 0
    greatest_decrease_month = ""

    previous_row = None
    total_change = 0
    for row in csvreader:
        # add profit/loss in this row to the total 
        profit_loss = int(row[1])
        total += profit_loss
        num_rows += 1

        # update greatest increase
        if profit_loss>0 and profit_loss>greatest_increase:
            greatest_increase = profit_loss
            greatest_increase_month = row[0]

        # update greatest decrease
        if profit_loss<0 and profit_loss<greatest_decrease:
            greatest_decrease = profit_loss
            greatest_decrease_month = row[0]

        if previous_row == None:
            previous_row = row
        else:
            profit_loss_1 = int(previous_row[1])
            profit_loss_2 = int(row[1])
            total_change += (profit_loss_2 - profit_loss_1)
            previous_row = row

    avg_change = total_change/(num_rows - 1)

    # print total months
    print("Total Months:",num_rows)
    # print total
    print(f"Total : ${total}")
    # print average change
    print(f"Average Change: ${format(avg_change,'.2f')}")
    # print greatest increase
    print(f"Greatest Increase in Profits : {greatest_increase_month} (${greatest_increase})")
    # print greatest decrease
    print(f"Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_decrease})")

    with open('results.txt', "w") as f:
        # print the details  one by one 
        f.write(f"Total Months: {num_rows}\n")
        f.write(f"Total : ${total}\n")
        f.write(f"Average Change: ${format(avg_change,'.2f')}\n")
        f.write(f"Greatest Increase in Profits : {greatest_increase_month} (${greatest_increase})\n")
        f.write(f"Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_decrease})\n")
