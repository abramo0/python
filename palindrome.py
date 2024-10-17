#a simple program that asks the user to enter a word, it tells the user whether the entered word is a palindrome or not

def palindrome():
    word=input("Write the word: ")
    word=word.lower()
    word_reverse = word[::-1]
    
    if word==word_reverse:
        print("The word is palindrome")
    else:
        print("The word is NOT palindrome")


def main():
    palindrome()


if __name__=="__main__":
    main()