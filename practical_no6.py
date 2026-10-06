SIZE = 10
table = [None] * SIZE


# Hash function
def hash_function(key):
    return key % SIZE


# Insert
def insert(key):
    index = hash_function(key)
    start = index

    while table[index] is not None:
        index = (index + 1) % SIZE

        # Hash table is full
        if index == start:
            print("Hash table is full!")
            return

    table[index] = key
    print("Key inserted at index", index)


# Search
def search(key):
    index = hash_function(key)
    start = index

    while table[index] is not None:
        if table[index] == key:
            print("Key found at index", index)
            return index

        index = (index + 1) % SIZE

        # We have checked all possible positions
        if index == start:
            break

    print("Key not found")
    return -1


# Delete
def delete(key):
    index = hash_function(key)
    start = index

    while table[index] is not None:
        if table[index] == key:
            table[index] = None
            print("Key deleted from index", index)
            return

        index = (index + 1) % SIZE

        if index == start:
            break

    print("Key not found")


# Display
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", table[i])


# Menu
while True:
    print("\n===== HASH TABLE MENU =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
