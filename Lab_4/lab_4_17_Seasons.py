input_month = input()
input_day = int(input())

# Spring
if (input_month == 'March') and ((input_day >= 20) and (input_day <= 31)):
    print('Spring')

elif (input_month == 'April') and ((input_day >= 1) and (input_day <= 30)):
    print('Spring')

elif (input_month == 'May') and ((input_day >= 1) and (input_day <= 31)):
    print('Spring')

elif (input_month == 'June') and ((input_day >= 1) and (input_day <= 20)):
    print('Spring')

# Summer
elif (input_month == 'June') and ((input_day >= 21) and (input_day <= 30)):
    print('Summer')

elif ((input_month == 'July') or (input_month == 'August')) and ((input_day >= 1) and (input_day <= 31)):
    print('Summer')

elif (input_month == 'September') and ((input_day >= 1) and (input_day <= 21)):
    print('Summer')

# Autumn
elif (input_month == 'September') and ((input_day >= 22) and (input_day <= 30)):
    print('Autumn')

elif (input_month == 'October') and ((input_day >= 1) and (input_day <= 31)):
    print('Autumn')

elif (input_month == 'November') and ((input_day >= 1) and (input_day <= 30)):
    print('Autumn')

elif (input_month == 'December') and ((input_day >= 1) and (input_day <= 20)):
    print('Autumn')

# Winter
elif (input_month == 'December') and ((input_day >= 21) and (input_day <= 31)):
    print('Winter')

elif (input_month == 'January') and ((input_day >= 1) and (input_day <= 31)):
    print('Winter')

elif (input_month == 'February') and ((input_day >= 1) and (input_day <= 29)):
    print('Winter')

elif (input_month == 'March') and ((input_day >= 1) and (input_day <= 19)):
    print('Winter')

else:
    print('Invalid')
