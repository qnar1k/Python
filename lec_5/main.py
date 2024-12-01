def sum_of_elements(numbers, exclude_negative=False):    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]    return sum(numbers)

def main():    user_input = input("Enter a list of numbers separated by spaces: ")
        try:
        numbers = list(map(int, user_input.split()))    except ValueError:
        print("Error: Please enter valid numbers.")        return
    exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
    exclude_negative = exclude_negative_input == 'yes'
    total_sum = sum_of_elements(numbers, exclude_negative=exclude_negative)
    print(f"The sum of the elements is: {total_sum}")
main()
