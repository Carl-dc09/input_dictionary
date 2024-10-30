# Create a dictionary to store the information
def input_dictionary():
    ranges = {
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
# Print