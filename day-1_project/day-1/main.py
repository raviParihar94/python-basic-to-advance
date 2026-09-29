alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]

directions =input("Enter the direction you want to go (encode/decode): ").lower()
text = input("Enter your message: ").lower()        

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char
    return encrypted_text





def guess_jacpot():
    import random
    jackpot = random.randint(1, 100)
    guess = int(input("Guess the jackpot number between 1 and 100: "))
    while guess != jackpot:
        print("Sorry, that's not the jackpot number. Try again!")
        guess = int(input("Guess the jackpot number between 1 and 100: "))
    print("Congratulations! You guessed the jackpot!")  