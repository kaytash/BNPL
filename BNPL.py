budget = int(input("Enter your BNPL Budget: $ "))
credit = int(input("Enter the credit you set for customers: $ "))
repayment_Cycle = int(input("Enter the repayment service cycle(month): "))
interest_Rate = int(input("Enter the interest rate for each user/service: % "))

first_Users = int(budget / credit)
users = [0]
users[0] = first_Users

lst = [0, 0, 0, 0]

lst.insert(0, first_Users * credit / repayment_Cycle)

for i in range(11):
    sum_lst = sum(lst[0:4])
    new_users = int(sum_lst / credit)
    users.append(new_users)
    new_balance = int(sum_lst / repayment_Cycle)
    lst.insert(0, new_balance)

#print(lst)
#print(users)
sum_users = sum(users[:])
print("Your total BNPL sell is: " , sum_users)
print("Your BNPL ROI is: % ", (sum_users * interest_Rate * credit) / budget)
