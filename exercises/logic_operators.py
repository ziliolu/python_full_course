temp = int(input("What is the temperature outside? "))

if not(temp >= 0 and temp <= 0):
    print("The temperature is extreme today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today! Go outside!")
   