# Write your methods here after you've created your tests
#A python program to illustrate Caesar Cipher Technique 

def login():    
    user = raw_input("Username: ")
    passw = raw_input("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print "Login successful!"
            return True
    print "Wrong username/password"
    return False

def menu():
    #here's a menu that the user can access if he logged in.

def main():
    global True
    while True:
        True = True
        log = login()
        if log == True:
             menu()
             True = False


main()

def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  

def decrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Decrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65) 
  
        # Decrypt lowercase characters 
        else: 
            result += chr((ord(char) - s - 97) % 26 + 97) 
  
    return result 
  
