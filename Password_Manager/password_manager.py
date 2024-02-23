from cryptography.fernet import Fernet

# create cyper key to encript password
'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file  = open("key.key","rb")
    key = file.read()
    file.close()
    return key
def view(fer):
    with open('password.txt','r') as f:
        for line in f.readlines():
            date = line.rstrip()
            user,pwd = date.split("|")
            print("User Name: "+ user+"\n"+"Password: "+fer.decrypt(pwd.encode()).decode())
def add(fer):
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")




key = load_key()
fer = Fernet(key)


while True:
    mode = input("Would you like to add new password or view existing onces (view/add/q [for quit]): \n => ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view(fer)
        
    elif mode == "add":
        add(fer)
        
    else:
        print("Invalid Mode! ")
