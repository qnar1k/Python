def classify_numbers(numbers):    even_numbers = []
    odd_numbers = []
    for num in numbers:        if num % 2 == 0:
            even_numbers.append(num)        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers
def main():
    user_input = input("Enter a list of numbers separated by spaces: ")    
    try:        numbers = list(map(int, user_input.split()))
    except ValueError:        print("Error: Please enter valid numbers.")
        return
    evens, odds = classify_numbers(numbers)
    print("Even numbers:", evens)
    print("Odd numbers:", odds)
main()
