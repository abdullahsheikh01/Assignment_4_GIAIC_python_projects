from hashlib import sha256
gmails_and_passwords : dict[str,str] = {
    "example1@mail.com":"98c1eb4ee93476743763878fcb96a25fbc9a175074d64004779ecb5242f645e6",
    "example2@mail.com":"a631f4488a457da27b4a64dc8f2d85085b50ff568be99125cf6f8f45c759878e",
    "example3@mail.com":"e5679dbecd0e755c68471354c640858d0078b7332c52768290f0d7d336a66f13"
}
def main():
    try:
        for password in ["word","train","tan"]:
            password_score : int = 0
            for _ in gmails_and_passwords:
                if sha256(password.encode()).hexdigest() == gmails_and_passwords[_]:
                    password_score+=1
                    print(f"{password} is a password of {_}")
            if password_score==0:
                print(f"{password} is not a password of any gmail")
        return None
    except:
        print("Unknown Error Occured!")
        return None
if __name__ == '__main__':
    main()