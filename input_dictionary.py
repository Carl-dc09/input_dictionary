# Create a dictionary to store the information
def input_dictionary():
    input_num_ranges = {
        "1 - 10": [],
        "11 - 20": [],
        "21 - 30": [],
        "31 - 40": [],
        "41 - 50": []
    }

# Create an infinite loop input that breaks when the number is lower than 1 and greater than 50
    while True:
        try:
            input_number = int(input("Enter a number (between 1 and 50): "))
            if input_number < 1 or input_number > 50:
                break

            # Store the number that's been inputted in the dictionary
            elif 1 <= input_number <= 10:
                input_num_ranges["1 - 10"].append(input_number)
            elif 11 <= input_number <= 20:
                input_num_ranges["11 - 20"].append(input_number)
            elif 21 <= input_number <= 30:
                input_num_ranges["21 - 30"].append(input_number)
            elif 31 <= input_number <= 40:
                input_num_ranges["31 - 40"].append(input_number)
            elif 41 <= input_number <= 50:
                input_num_ranges["41 - 50"].append(input_number)

        # Print error if the input is invalid
        except:
            print("Error: Invalid input. Please enter a number.")

# Print the result
    print("\nInput summary:")
    for range_key, input_numbers in input_num_ranges.items():
        input_count = len(input_numbers)
        print(f"\n{range_key} = {input_count} \nValues: {input_numbers}")