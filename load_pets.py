import sqlite3
import os

# Connect to pets.db in the same folder as this script
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pets.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the person table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
''')

# Create the pet table
# "dead" is 1 if the pet has passed away, 0 if still alive
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    )
''')

# Create the person_pet table (links people to their pets)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER,
        pet_id INTEGER
    )
''')

# Insert people
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]
cursor.executemany('INSERT INTO person VALUES (?, ?, ?, ?)', people)

# Insert pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'AlaskanMalamute', 3, 0),
    (3, 'Max', 'CockerSpaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'CockerSpaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]
cursor.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pets)

# Insert person-pet relationships
person_pets = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]
cursor.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pets)

# Save changes and close
conn.commit()
conn.close()

print("Data loaded into pets.db successfully!")
