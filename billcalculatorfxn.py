def calc_tip(bill_amount,tip_percent):
	tip_amount = bill_amount * tip_percent/100
	return tip_amount

def calc_totalbill(tip_amount,bill_amount):
	total_bill = tip_amount + bill_amount
	return total_bill

def split_bill(total_bill,num_people):
	split_amount = total_bill / num_people
	return split_amount

# print calc_totalbill(calc_tip(100,10),100)

# tip_amount = calc_tip(100,10)
# total_bill = calc_totalbill(tip_amount,100)
# print "Each person pays", split_bill(total_bill,5)

def main():
	bill = int(raw_input("How much is the bill? "))
	percenttip = int(raw_input("What percentage would you like to tip? "))
	user_choice = int(raw_input("Enter 1 to calculate tip or 2 to split the bill "))
	if user_choice == 1:
		print "This is the tip amount:",calc_tip(bill,percenttip)
		tip = calc_tip(bill,percenttip)
		print "This is the total bill:",calc_totalbill(tip,bill)
		billtotal = calc_totalbill(tip,bill)
		user_split = str.lower(raw_input("Would you like to split the bill, yes or no? "))
		if user_split == "yes":
			people = int(raw_input("How many people are splitting the bill? "))
			print "Each person pays:",split_bill(billtotal,people)
		else:
			print "Please pay:",billtotal
	elif user_choice == 2:
		tip = calc_tip(bill,percenttip)
		billtotal = calc_totalbill(tip,bill)
		people = int(raw_input("How many people are splitting the bill? "))
		print "Each person pays:",split_bill(billtotal,people)
	else:
		print "Please choose 1 or 2!~!!!!!!"

if __name__ == '__main__':
   main()