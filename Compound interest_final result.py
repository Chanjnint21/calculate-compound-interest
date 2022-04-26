def funtion():
  #Ask user to type the amount of Deposite, interest rate, months
  A = float(input("Enter Deposite Amount:"))
  W = float(input("Enter interest Rate:"))
  t = int(input("Enter month:"))
  
  #Arange the position of value and string
  print ("\n{:<7} {:<10} {:<17} {:<25} {:<25} {:<25}".format('Month','Deposite','total Deposite', "This Month's interest", 'Total-interest Earned', 'Total-value to-Date'))
  print('─' * 110) #create line
  int0 = 0
  for i in range(t):
    month = i+1 
    total_dep = (A*month) #total_dep = Total deposite
    F = A*((1+W/1200)**month)
    month_int = F - A #month_int = month interest
    total_int = int0 + month_int #int0 = last month interest rate  
    int0 += month_int
    total_value_date = total_int + total_dep  
    
    # Use format to express the vlue to have only 4 decimal places
    deposite    = "{:.2f}".format(A)
    total_dep   = "{:.2f}".format(total_dep)
    month_int   = "{:.2f}".format(month_int)
    total_int   = "{:.2f}".format(total_int)
    total_value = "{:.2f}".format(total_value_date)
    print ("{:<7} {:<12} {:<18} {:<27} {:<28} {:<28}".format( month, deposite, total_dep, month_int, total_int, total_value))
    print('─' * 110)
funtion()

# Ask the user if they want to redo the compound interest
while True:
  if input("\nDo you want to calulate again? (y/n):") == "y":
    print('--' * 20)
    funtion()
  else:
    print("Thank You!")
    break 