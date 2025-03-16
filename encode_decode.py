print("Welcome to Encrypt & Decrypt App ! \nwhat do you want to do ? \n\t1) Encrypt\n\t2) Decrypt")
encrypt_decrypt = int(input("please choose your option (1 or 2) :"))
cryptography_method = int(input("what method do you want ? \n\t1) Caesar-cipher\n\t2) Base-64\n\t3) Rot-13\nplease enter your choice (1,3) : "))
input_text = input("now please enter your Text :\n\t")

def encrypt():
    if cryptography_method == 1 :
        encrypted_text = ""
        shift_value = int(input("please enter shift value you want : ").strip())
        for c in input_text :
            print(ord(c))
            encrypted_text += chr((ord(c)+shift_value)%26)
        print(encrypted_text)


if encrypt_decrypt == 1 :
    encrypt()