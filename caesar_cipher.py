'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''
# Import the string module.
import string

choice=input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
choice=choice.lower()

def encode(message, key):
    '''
    This function takes a message and a key and returns the encrypted message.
    '''
    for i in message:
        if i in string.ascii_letters:
            if i.isupper():
                print(chr((ord(i)+key-65)%26+65),end="")
            else:
                print(chr((ord(i)+key-97)%26+97),end="")
        else:
            print(i,end="")


def decode(message, key):
    '''
    This function takes a message and a key and returns the decrypted message.
    '''
    for i in message:
            if i in string.ascii_letters:
                if i.isupper():
                    print(chr((ord(i)-key-65)%26+65),end="")
                else:
                    print(chr((ord(i)-key-97)%26+97),end="")
            else:
                print(i,end="")

if choice=="e":

    input_key=int(input("Please enter the key (0 to 25) to use.\n> "))
    input_message=input("Enter the message to encrypt.\n> ")
    input_message=input_message.upper()

    encode(input_message, input_key)

elif choice=="d":
    
        input_key=int(input("Please enter the key (0 to 26) to use.\n> "))
        input_message=input("Enter the input_message to decrypt.\n> ")
        input_message=input_message.upper()

        decode(input_message, input_key)
        