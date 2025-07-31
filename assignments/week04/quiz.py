
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("jimmy", 20, "chonburi", "thai")  # name, age, city, country
    hobbies = []
    
    # Your code here
    while True:
        print("\n1. Display into")
        print("2. add hobby")
        print("3. Remove hobby")
        print("4. Edit age")
        print("5. exit")
        choice = input("What do you want to do?: ")

        if choice == "1":
            print("Name:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hoppies:", person[0])
        
        elif choice == "2":
            hobby = input("Insert new hoppy: ")
            hobbies.append(hoppy)

        elif choice == "3":
            del hobbies[0] 


        age = int(input("Insert new age: "))
        person_list = list(person)
        person_list[1] = age
        person = tuple(person_list)


    if __name__ == "__main__":
        personal_info_manager()


"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = # Your code here
    odd_numbers = # Your code here
    
    # Calculate average
    average = # Your code here
    
    # Numbers greater than average
    above_average = # Your code here
    
    # Display results
    # Your code here

if __name__ == "__main__":
    number_operations()