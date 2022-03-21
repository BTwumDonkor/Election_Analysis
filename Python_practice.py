print ("hello world")

counties = ["Arapahoe", "Denver", "Jefferson"]

print (counties)


print (counties[0])

print (counties[0:2])

if counties[1] == "Denver":
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
elif temperature <= 80:
    print("Open the windows.")

x = 0
while x <= 5:
    print(x)
    x = x + 1