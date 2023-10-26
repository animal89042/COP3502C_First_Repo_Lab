# Author: Brody Michaels
# Date: 10/25/23
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(password):
    global new_pass
    for i in password:
        new_pass += str((int(i)+3))
    return new_pass

def decoder(password):
    pass

new_pass = ''
decoder_run = True
run_it = True

while __name__ == '__main__':
    while run_it:
        print_menu()
        while decoder_run:
            menu_choice = input("Please enter an option: ")
            if menu_choice == '1':
                pass_to_enc = input("Please enter your password to encode:")
                encoded_pass = encoder(pass_to_enc)
                print("Your password has been encoded and stored!")
            if menu_choice == '2':
                decoded_pass = decoder(encoded_pass)
                print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}')
            if menu_choice == '3':
                decoder_run = False
                run_it = False


