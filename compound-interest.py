print("F = A[(1+W/1200) + (1+W/1200)**2 + (1+W/1200)**3 + (1+W/1200)**4 + (1+W/1200)**5)]")
def funtion01():
  A = float(input("Enter Deposite:"))
  W = float(input("Enter interest Rate per year:"))
  x = float(input("Enter Deposite in month:"))
  #Total Deposite
  A1 = A
  A2 = A*2
  A3 = A*3
  A4 = A*4
  A5 = A*5
  #This month interest
  
  #Total interest earn
  
  #Total-value to-Date
  F1 = A*(1+W/1200)
  F2 = A*((1+W/1200) + (1+W/1200)**2)
  F3 = A*((1+W/1200) + (1+W/1200)**2 + (1+W/1200)**3)
  F4 = A*((1+W/1200) + (1+W/1200)**2 + (1+W/1200)**3 + (1+W/1200)**4)
  F5 = A*((1+W/1200) + (1+W/1200)**2 + (1+W/1200)**3 + (1+W/1200)**4 + (1+W/1200)**5)
  d = [ ["1", A, A1, 1.00,  1.00, F1],
       ["2", A, A2, 2.01, 3.01, F2],
       ["3", A, A3, 3.03,  6.04 , F3],
       ["4",A, A4, 4.06, 10.10, F4],
       ["5",A, A5, 5.10, 15.20, F5]]
       
  print ("{:<7} {:<10} {:<17} {:25} {:<25} {:<25}".format('Month','Deposite','total Deposite', "This Month's interest", 'Total-interest Earned', 'Total-value to-Date'))
  for x in d:
      mon, dep, tdep, monint, totalearn, totalvalue = x
      print ("{:<9} {:<14} {:<20} {:<25} {:<25} {:<25}".format( mon, dep, tdep, monint, totalearn, totalvalue))
funtion01()

#Question03
while True:
  if input("Want to calulate again? (y/n):") == "y":
    print("")
    funtion01()
  else:
    print("Thank You")
    break 