
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

# method to get the total
def get_total(rows):
    total = 0
    # for each row
    for row in rows:
        # add profit/loss in this row to the total 
        profit_loss = int(row.split(",")[1])
        total += profit_loss
    return total

# method to find the average change
def get_average_change(rows):
    total_change = 0
    for i in range(len(rows) - 1):
        row = rows[i]
        next_row = rows[i+1]
        profit_loss_1 = int(row.split(",")[1])
        profit_loss_2 = int(next_row.split(",")[1])
        total_change += (profit_loss_2 - profit_loss_1)
    return total_change/(len(rows) - 1)

# get the greatest increase of profits
def get_greatest_increase_profits(rows):
    greatest_increase = 0
    # current_profit = 0
    month = ""
    for row in rows:
        profit_loss = int(row.split(",")[1])
        if profit_loss>0 and profit_loss>greatest_increase:
            greatest_increase = profit_loss
            month = row.split(",")[0]
        # current_profit += profit_loss
        # if current_profit > greatest_increase:
        #     greatest_increase = current_profit
        #     month = row.split(",")[0]
        # if profit_loss>0:
        #     current_profit += profit_loss
        #     if current_profit > greatest_increase:
        #         greatest_increase = current_profit
        #         month = row.split(",")[0]
        # else:
        #     current_profit = 0
    return month,greatest_increase

# get the greatest decrease of profits
def get_greatest_decrease_profits(rows):
    greatest_decrease = 0
    month = ""
    for row in rows:
        profit_loss = int(row.split(",")[1])
        if profit_loss<0 and profit_loss<greatest_decrease:
            greatest_decrease = profit_loss
            month = row.split(",")[0]
    return month,greatest_decrease


# the main method
def main():
    # read rows
    header_row, rows = read_csv("Resources/budget_data.csv")
    # print(rows)

    # print total months
    print("Total Months:",len(rows))
    # print total
    print(f"Total : ${get_total(rows)}")
    # print average change
    print(f"Average Change: ${format(get_average_change(rows),'.2f')}")
    # print greatest increase
    month_greatest_increase,greatest_increase = get_greatest_increase_profits(rows)
    print(f"Greatest Increase in Profits : {month_greatest_increase} (${greatest_increase})")
    # print greatest decrease
    month_greatest_decrease,greatest_decrease = get_greatest_decrease_profits(rows)
    print(f"Greatest Decrease in Profits : {month_greatest_decrease} (${greatest_decrease})")


    # file to print the results 
    with open('results.txt', "w") as f:
        # print the details  one by one 
        f.write(f"Total Months: {len(rows)}\n")
        f.write(f"Total : ${get_total(rows)}\n")
        f.write(f"Average Change: ${format(get_average_change(rows),'.2f')}\n")
        f.write(f"Greatest Increase in Profits : {month_greatest_increase} (${greatest_increase})\n")
        f.write(f"Greatest Decrease in Profits : {month_greatest_decrease} (${greatest_decrease})\n")

# run the main
main()