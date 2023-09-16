# This is an exercise with the guest_book.txt file
user_data_file = "guest_book.txt"

new_users = ""

with open(user_data_file, 'r') as user_file:
    lines = user_file.readlines()

while True:
    username = input("Kindly enter your name(Enter 'q' if you want to stop): ")
    if username == 'q':
        break
    else:
        print(f"Hello {username}, you are welcome to guest_book.txt")
        for line in lines:
            print(f"{username.title()} met {line.strip().strip()} in guest_book.txt")
        new_users += f"{username}\n"


with open(user_data_file, 'a') as user_file:
    user_file.write(new_users)
