import os
from itertools import permutations
from math import factorial

os.system('cls' if os.name == 'nt' else 'clear')

# cool ascii art
ascii_art = """
 _       ______  ____  ____  __  ______   ______   
| |     / / __ \/ __ \/ __ \/  |/  /   | / ____/   
| | /| / / / / / /_/ / / / / /|_/ / /| |/ /        
| |/ |/ / /_/ / _, _/ /_/ / /  / / ___ / /___      
|__/|__/\____/_/ |_/_____/_/  /_/_/  |_\____/      
"""

print(ascii_art)
print(" " * 27 + "\033[42m By Electrifyied \033[0m")

print("\n" * 2)

#prompt for option
print("Choose an option:")
print("\033[42m 1. \033[0m Default") # normal
print("\033[42m 2. \033[0m Omni") # multi directional
choice = input("").strip()

file_name = input("\nEnter the name for the output file (without extension): ").strip() + ".lst"

if choice == '1':
    #fixed length
    words = input("Enter words separated by spaces: ").split()
    total_permutations = factorial(len(words))


    estimated_size_bytes = total_permutations * sum(len(''.join(perm)) for perm in permutations(words)) / total_permutations
    estimated_size_kb = estimated_size_bytes / 1024
    estimated_size_mb = estimated_size_kb / 1024

    print(f"\nTotal number of permutations: {total_permutations}")
    print(f"Estimated file size: {estimated_size_kb:.2f} KB ({estimated_size_mb:.2f} MB)")
    print(f"List is gonna be created in {file_name}")

    proceed = input("Do you want to proceed with the action? [N/y]: ").lower()
    
    #fuck this shit
    if proceed == 'y':
        with open(file_name, "w") as f:
            for perm in permutations(words):
                f.write(''.join(perm) + '\n')
        
        print(f"Combinations have been written to {file_name}")
    else:
        print("Action aborted. No file was created.")

elif choice == '2':
    words = input("Enter words separated by spaces: ").split()
    #thanks for gpt for fixing my mistake below
    total_permutations = sum(factorial(len(words)) // factorial(len(words) - r) for r in range(1, len(words) + 1))

    average_length = sum(len(''.join(perm)) for r in range(1, len(words) + 1) for perm in permutations(words, r)) / total_permutations
    estimated_size_bytes = total_permutations * (average_length + 1)
    estimated_size_kb = estimated_size_bytes / 1024
    estimated_size_mb = estimated_size_kb / 1024

    print(f"\nTotal number of lines/words to be generated: {total_permutations}")
    print(f"Estimated file size: {estimated_size_kb:.2f} KB ({estimated_size_mb:.2f} MB)")
    print(f"List is gonna be created in {file_name}")

    proceed = input("Do you want to proceed with the action? [N/y]: ").lower()

    if proceed == 'y':
        #write all perm
        with open(file_name, "w") as f:
            for r in range(1, len(words) + 1):
                perms = permutations(words, r)
                for perm in perms:
                    f.write(''.join(perm) + '\n')
        
        print(f"Combinations have been written to {file_name}")
    else:
        print("Action aborted. No file was created.")
else:
    print("Invalid choice. Exiting.")
