# ─────────────────────────────────────────
# COP1035C  Chapter 3 Project: Grade Manager
# Student: _______________  Date: __________
# ─────────────────────────────────────────

students = [
    ("Alice",   [88, 92, 79, 95]),
    ("Bob",     [72, 68, 75, 80]),
    ("Carol",   [95, 98, 91, 99]),
    ("David",   [55, 60, 58, 62]),
    ("Eva",     [83, 79, 85, 88]),
    ("Frank",   [65, 70, 72, 68]),
]

def get_grade(avg):
    if avg >= 90:   return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else:           return "F"


# ── Stage 1: Full Report ──────────────────
def full_report():
    print(f"{'Student':<12} {'Avg':>7} {'Grade':>6} {'Status':>7}")
    print("=" * 38)
    class_avgs = []
    for name, scores in students:
        avg = sum(scores) / len(scores)
        class_avgs.append(avg)
        grade = get_grade(avg)
        status = "PASS" if avg >= 60 else "FAIL"
        print(f"{name:<12} {avg:>7.1f} {grade:>6} {status:>7}")
    print("=" * 38)
    print(f"{'Class Average:':<20} {sum(class_avgs)/len(class_avgs):.1f}")
    print(f"{'Highest:':<20} {max(class_avgs):.1f}")
    print(f"{'Lowest:':<20} {min(class_avgs):.1f}")

# ── Stage 2: Interactive Mode ─────────────
def student_lookup():
    name_input = input("\nEnter student name: ")
    found = False
    for name, scores in students:
        if name.lower() == name_input.lower():
            found = True
            avg = sum(scores) / len(scores)
            grade = get_grade(avg)
            status = "PASS" if avg >= 60 else "FAIL"
            print(f"\n  Student : {name}")
            print(f"  Scores  : {scores}")
            print(f"  Average : {avg:.1f}")
            print(f"  Grade   : {grade}")
            print(f"  Status  : {'PASS' if avg >= 60 else 'FAIL'}")
            break
    if not found:
        print(f"  Student '{name_input}' not found.")

def class_statistics():
    class_avgs = []
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for name, scores in students:
        avg = sum(scores) / len(scores)
        class_avgs.append(avg)
        grade_counts[get_grade(avg)] += 1

    print(f"\n  Class Average : {sum(class_avgs)/len(class_avgs):.1f}")
    print(f"  Highest       : {max(class_avgs):.1f}")
    print(f"  Lowest        : {min(class_avgs):.1f}")
    print(f"  # Passing     : {sum(1 for a in class_avgs if a >= 60)}")
    print(f"  # Failing     : {sum(1 for a in class_avgs if a < 60)}")

    print("\n  Grade Histogram:")
    print("  " + "-" * 20)
    for grade in ["A", "B", "C", "D", "F"]:
        bar = "*" * grade_counts[grade]
        print(f"  {grade} | {bar:<10} ({grade_counts[grade]})")
    print("  " + "-" * 20)

# ── Main Program ─────────────────────────
def main():
    while True:
        
        print("\n  Grade Manager  Menu ")
        print("=" * 38)
        print(" 1. Full report       ")
        print(" 2. Look up a student ")
        print(" 3. Class statistics  ")
        print(" 4. Quit              ")
        print("=" * 38)


        # Input validation: while loop rejects choices outside 1–4
        choice = ""
        while choice not in ("1", "2", "3", "4"):
            choice = input("  Enter choice (1-4): ").strip()
            if choice not in ("1", "2", "3", "4"):
                print("  Invalid choice. Please enter 1, 2, 3, or 4.")

        if   choice == "1": full_report()
        elif choice == "2": student_lookup()
        elif choice == "3": class_statistics()
        elif choice == "4":
            print("\n  Goodbye!\n")
            break

main()