import customtkinter
import hashlib
import os
from cryptography.fernet import Fernet


def Encryptor_AES(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password)
    string_encrypted = str(encrypted_password, encoding='utf-8')
    return string_encrypted

def Decryptor(textToDecrypt, key):
    key = key.encode('utf-8')
    cipher_suite = Fernet(key)
    decryptedText = cipher_suite.decrypt(textToDecrypt)
    string_decrypted = str(decryptedText, encoding='utf-8')
    return string_decrypted

def generate_key():
    key = Fernet.generate_key()
    return key

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x500")


#fucntion of a button that encrypts inputted text with an inputed AES key-----------------WIP adding a hash encryption function
count = 1
def encrypt_button_event():
    global count
    user_input = entry.get()
    aes_key = entry_key.get()
    user_input_bytes = bytes(user_input, encoding='utf-8')
    aes_key_bytes = bytes(aes_key, encoding='utf-8')
    result = Encryptor_AES(user_input_bytes, aes_key_bytes)
    username = entry3.get()
    website = entry4.get()
    print(result)
    f = open('Passowrds.txt', 'a')
    #f.write(str(count))
    #f.write('\n')
    f.write("--------------------------------")
    f.write('\n')
    f.write("Website: " + website)
    f.write('\n')
    f.write("Username: " + username)
    f.write('\n')
    f.write(result)
    f.write('\n')
    f.write("--------------------------------")
    f.close()
    #count = count + 1
    #print(count)
    entry.delete(0, 'end')
    entry4.delete(0, 'end')
    entry3.delete(0, 'end')
encrypt_button = customtkinter.CTkButton(app, text="Encrypt", command=encrypt_button_event)
encrypt_button.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
    

#entry where the key gets generated to
entry2 = customtkinter.CTkEntry(app, placeholder_text="CTkEntry", state='readonly')
entry2.place(relx = 0.1, rely = 0.7, anchor=customtkinter.CENTER)


#fucntion of a button that generates a key
def keygen_button_event():
    entry2.configure(state='normal')
    entry2.delete(0)
    entry2.insert(0, generate_key())
    entry2.configure(state='readonly')
keygen_button = customtkinter.CTkButton(app, text="Generate key", command=keygen_button_event)
keygen_button.place(relx=0.1, rely=0.6, anchor=customtkinter.CENTER)


#function of a button that copies the generated key
def copy_key_button_event():
    text_to_copy = entry2.get()
    app.clipboard_clear()
    app.clipboard_append(text_to_copy)
copy_key_button = customtkinter.CTkButton(app, text="Copy Key", command=copy_key_button_event, height=10, width=50)
copy_key_button.place(relx=0.1, rely=0.8, anchor=customtkinter.CENTER)


#fucntion of a button that decrypts using an encrypted text and a proper AES key
def decrypt_button_event():
    result = Decryptor(entry_encrypted.get(), entry_key.get())
    print(result)
decrypt_button = customtkinter.CTkButton(app, text="Decrypt", command=decrypt_button_event)
decrypt_button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)    


#entry to input an AES key
entry_key = customtkinter.CTkEntry(app, placeholder_text="AES key", width=350)
entry_key.place(relx = 0.5, rely = 0.3, anchor=customtkinter.CENTER)


#entry to input a password
entry = customtkinter.CTkEntry(app, placeholder_text="Password")
entry.place(relx = 0.5, rely = 0.2, anchor=customtkinter.CENTER)

#entry to input username
entry3 = customtkinter.CTkEntry(app, placeholder_text="Username")
entry3.place(relx = 0.3, rely = 0.2, anchor=customtkinter.CENTER)

#entry to put website
entry4 = customtkinter.CTkEntry(app, placeholder_text="Website")
entry4.place(relx = 0.7, rely = 0.2, anchor=customtkinter.CENTER)




#entry to input encrypted text
entry_encrypted = customtkinter.CTkEntry(app, placeholder_text="Encrypted text", width=350)
entry_encrypted.place(relx = 0.5, rely = 0.8, anchor=customtkinter.CENTER)



label = customtkinter.CTkLabel(app, text="Password Manager (Early build)", fg_color="transparent", font=('Arial', 25))
label.place(relx = 0.5, rely = 0.05, anchor=customtkinter.CENTER)

app.mainloop()