# Exception handling in Python

a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

try:
    print(a/b)

except Exception as e:
    print("An error occurred:", e)

finally:
    print("This block always executes, regardless of an error.")

# Retry with a new value for B
a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

try:
    print(a/b)

except Exception as e:
    print("An error occurred:", e) 
    print("Please enter valid numbers.") 
    b = int(input("Enter B value: ")) 
    print(a/b)

finally:
    print("This block always executes, regardless of an error.")


# Exception handling with else and finally blocks
a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

try:
    print(a/b)

except Exception as e:
    print("An error occurred:", e)

else:
    print("No errors occurred.") 

finally:
    print("This block always executes, regardless of an error.")


# Exception handling with custom exception
try:
    boy = input("who do you like? : ")
    if boy.lower() == "nobody":
        raise Exception("You should like someone!")
    
except Exception as e:
    print("An error occurred:", e)

else:
    print(f"You like {boy}!")