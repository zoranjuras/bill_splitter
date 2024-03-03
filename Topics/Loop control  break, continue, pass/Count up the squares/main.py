def print_numbers(n):
    for x in range(1, n + 1):
        if x % 15 == 0:
            break
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

def main():

    n = int(input())
    print_numbers(n)


if __name__ == "__main__":
    main()