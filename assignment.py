#print "hello_username"
def hello_name(user_name):
    print("hell0" +" "+ user_name.title()+ "!")
hello_name("satwik")

#To print the odd numbers 1_100
def first_odds():
    for n in range (1,100+1):
        if n % 2!= 0:
            print(n)
a=first_odds()
print(a) 

#To print maxium number in the list

def max_num_in_list(a_list):
	a_list.sort()
	print("maximum value is", a_list[-1])
max_num_in_list([29,78,986,54,69])	

#to return given year is leap year
def is_leap_year(a_year):
     if (a_year %400 == 0)or(a_year %4 == 0 and a_year % 100!=0):
          return True
     return False
print(is_leap_year(2023))

#To check all the numbers in the list are consecutive
def is_consucative(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
         return True
    return False
print(is_consucative([2,3,6,5,4]))

