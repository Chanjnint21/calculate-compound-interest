def Funtion():
  A=float(input("Enter Deposite: "))
  W=float(input("Enter Interest rate: "))
  T=int(input("Enter month:"))
  print("\n{:<10} {:<15} {:<20} {:<25} {:<25} {:<30}".format("Month", "Deposit", "Total Deposit", "This Month's interest", "Total-interest Earned", "Total-value to Date"))  #Arange the position of string
  print('=' * 120)
  def calculate():
    int0 = 0 # for first time start putting the money interest suppose to be 0 cuz last month you are not doing it
    for t in range(T):
      month = t + 1 
      total_dep = (A*month)
      F = A*(pow((1+W/1200),month))
      month_int = F - A
      total_int = int0 + month_int   
      int0 += month_int #int0 = Last interest rate
      total_value_to_date = total_int + total_dep  
      print("{:3}".format(month), #Arange the position of value and only 2 decimal point
            "{:13.2f}".format(A),
            "{:16.2f}".format(total_dep),
            "{:22.2f}".format(month_int),
            "{:27.2f}".format(total_int),
            "{:26.2f}".format(total_value_to_date)) 
      print('─' * 120)
  calculate()
  Answer = (input("\nDo you want to calulate again?(y/n):")) # Ask the user if they want to redo the compound interest
  if Answer =="y": 
    print('─' * 40)
    Funtion()
  else:
    print("Bye....")
Funtion()