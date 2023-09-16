# Here we are testing how we deal with errors
# And using exceptions to correct them
print("Kindly enter two numbers.")
print("Enter 'q' to quit\n")

while True:
    first_num = input("First Number: ")
    if first_num == 'q':
        break
    second_num = input("Second Number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print(f"You can't add {first_num} to {second_num}\n")
    else:
        print(answer)