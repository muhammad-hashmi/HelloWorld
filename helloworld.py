import sys

if len(sys.argv) != 2:
    print("Usage: python helloworld.py [name]")
else:
    name = sys.argv[1]
    print(f"Hello, {name}!")
