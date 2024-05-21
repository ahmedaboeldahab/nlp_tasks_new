import nltk
def text_tokenization(text):
    return nltk.word_tokenize(text)
def sentence_tokenization(text):
    return nltk.sent_tokenize(text)
def main():
    user_input=input('enter the text')
    print('enter the number between 1 to 3')
    print('1.word toknize')
    print('2.sent toknize')
    print('3.split text')
    choice=int(input('enter(1/2/3)'))
    if choice==1:
     print(text_tokenization(user_input))
    elif choice==2:
        print(sentence_tokenization(user_input))
    elif choice==3:
        print(user_input.split())
if __name__ == "__main__":
    main()