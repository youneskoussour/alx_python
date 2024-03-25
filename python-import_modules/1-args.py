import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  

    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} argument{'s' if num_arguments > 1 else ''}:")
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")
