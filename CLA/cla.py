import sys

if len(sys.argv) == 1:
    print(f"{sys.argv[0]}")

elif len(sys.argv) == 2:
    print(f"program name is {sys.argv[0]} and argv[1] is {sys.argv[1]}")

elif len(sys.argv) == 3:
    argv_2 = int(sys.argv[2])
    for i in range(argv_2):
        print(f"{sys.argv[1]}")

else:
    print("\n\t\t.....Usage information.....\n")
    print("argv[0]: first program name. \nargv[1]: string. \nargv[2]: an int number of string.")

