import sqlite3
import os

# Connect to pets.db in the same folder as this script
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pets.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Welcome to the Pet Lookup System!")
print("Enter -1 to quit.\n")

while True:
    # Ask user for a person ID
    user_input = input("Enter a person's ID: ")

    # Exit if the user types -1
    if user_input == '-1':
        print("Goodbye!")
        break

    # Make sure the input is actually a number
    if not user_input.isdigit():
        print("Please enter a valid number.\n")
        continue

    person_id = int(user_input)

    # Look up the person by ID
    cursor.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()

    # If no person found, print error
    if person is None:
        print("No person found with that ID.\n")
        continue

    # Print person info
    person_id_val, first_name, last_name, age = person
    print(f"\n{first_name} {last_name}, {age} years old")

    # Get all pets for this person using the person_pet link table
    cursor.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    ''', (person_id_val,))

    pets = cursor.fetchall()

    # Print each pet's info
    if pets:
        for pet in pets:
            pet_name, breed, pet_age, dead = pet
            status = "deceased" if dead == 1 else str(pet_age) + " years old"
            print(f"  - {first_name} {last_name} owned {pet_name}, a {breed}, that was {status}")
    else:
        print("  This person has no pets.")

    print()

# Close the connection when done
conn.close()
