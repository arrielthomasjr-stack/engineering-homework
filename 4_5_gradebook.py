#Lets the user enter student names and scores, saving each to gradebook.txt in Name,Score format
from unicodedata import name


def initial_entry():
    with open("gradebook.txt", "w") as f:
        while True:
            name = input("\nEnter student name (or 'done' to stop): ")
            if name.lower() == "done":
                break
            score = input("Enter student score: ")
            f.write(f"{name},{score}\n")
            print(f"  {name} saved!")
    print("\nGradebook created successfully.")
    		

# Has a "read" mode that opens gradebook.txt, reads all entries, and prints: the full list, the class average, the highest and lowest scores

def read_mode():
    try:
           with open("gradebook.txt", "r") as f:
            lines = f.readlines()
            
            if not lines:
                print("\nGradebook is empty.")
                return
            
            print("\nGradebook")
            scores = []
            for line in lines:
                name, score = line.strip().split(",")
                scores.append(int(score))
                print(f"  {name}: {score}")     
        	
            print(f"\n  Total Students : {len(scores)}")
            print(f"  Average Score  : {sum(scores) / len(scores):.2f}")
            print(f"  Highest Score  : {max(scores)}")
            print(f"  Lowest Score   : {min(scores)}")

    except FileNotFoundError:
        	print("\nNo gradebook found. Please add a student first.")


# Has an "add" mode that appends a new student without erasing existing data

def _add():
	name = input("\nEnter student name: ")
	score = input("Enter student score: ")
	with open("gradebook.txt", "a") as f:
   	 	f.write(f"{name},{score}\n")
    
print(f"\n{name} appended to gradebook.txt")

def main():
    while True:
        
        print("\n  Student Grade Book ")
        print("=" *38)
        print(" 1. Initial Entry     ")
        print(" 2. Display Scores ")
        print(" 3. Apend a new student ")
        print(" 4. Quit              ")
        print("=" * 38)


        # Input validation: while loop rejects choices outside 1–4
        choice = ""
        while choice not in ("1", "2", "3", "4"):
            choice = input("  Enter choice (1-4): ").strip()
            if choice not in ("1", "2", "3", "4"):
                print("  Invalid choice. Please enter 1, 2, 3, or 4.")

        if   choice == "1": initial_entry()
        elif choice == "2": read_mode()
        elif choice == "3": _add()
        elif choice == "4":
            print("\n  Goodbye!\n")
            break

main()	