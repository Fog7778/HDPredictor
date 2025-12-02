
#UI
print("What is the Current Day?")
##print(f"Sunday \nMonday \nTuesday \nWednesday \nThursday \nFriday \nSaturday")
current_day_input = input("Enter Day Here: ").lower()
current_day_cleaned = current_day_input.strip()

#Figuring out what day
if (current_day_cleaned == "sunday"):
    print("The Next Day is Monday")
if (current_day_cleaned == "monday"):
    print("The Next Day is Tuesday")
if (current_day_cleaned == "tuesday"):
    print("The Next Day is Wednesday")
if (current_day_cleaned == "wednesday"):
    print("The Next Day is Thursday")
if (current_day_cleaned == "thursday"):
    print("The Next Day is Friday")
if (current_day_cleaned == "friday"):
    print("The Next Day is Saturday")
if (current_day_cleaned == "saturday"):
    print("The Next Day is Sunday")
else:
    (print("Shiiiiiiiii u made a mistake"))
