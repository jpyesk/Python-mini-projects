from random import randint # Do not delete this line

def displayIntro():
    print('''_______________________________________________
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    _______________________________________________
    _____________________Rules_____________________
    Try to guess the hidden word one letter at a   
    time. The number of dashes are equivalent to   
    the number of letters in the word. If a player 
    suggests a letter that occurs in the word,     
    blank places containing this character will be 
    filled with that letter. If the word does not  
    contain the suggested letter, one new element  
    of a hangman’s gallow is painted. As the game  
    progresses, a segment of a victim is added for 
    every suggested letter not in the word. Goal is
    to guess the word before the man hangs!        
    _______________________________________________'''
          )
def displayEnd(result):
    if result == True:
        print('''
    ________________________________________________________________________
              _                                  _                          
             (_)                                (_)                         
    __      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
     \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
      \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
               | |   (_)    | |                  | (_)                      
            ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
           / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
          | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
           \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
    ________________________________________________________________________''')
    elif result == False:
        print('''
     __     __           _           _   _                                    
     \ \   / /          | |         | | | |                                   
      \ \_/ /__  _   _  | | ___  ___| |_| |                                   
       \   / _ \| | | | | |/ _ \/ __| __| |                                   
        | | (_) | |_| | | | (_) \__ \ |_|_|                                   
        |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
            _______ _                                        _ _          _ _ 
           |__   __| |                                      | (_)        | | |
              | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
              | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
              | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
              |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
    __________________________________________________________________________''')
def displayHangman(state):
    if state == 5:
        print('''
        ._______.   
        |/          
        |           
        |           
        |           
        |           
        |           
    ____|___        
                    ''')
    elif state == 4:
        print('''

        ._______.   
        |/      |   
        |           
        |           
        |           
        |           
        |           
    ____|___        
                    ''')
    elif state == 3:
        print('''

        ._______.   
        |/      |   
        |      (_)  
        |           
        |           
        |           
        |           
    ____|___        
                    ''')
    elif state == 2:
        print('''

        ._______.   
        |/      |   
        |      (_)  
        |       |   
        |       |   
        |           
        |           
    ____|___        
                    ''')
    elif state == 1:
        print('''

        ._______.   
        |/      |   
        |      (_)  
        |      \|/  
        |       |   
        |           
        |           
    ____|___        
                     ''')
    else:
        print('''

        ._______.   
        |/      |   
        |      (_)  
        |      \|/  
        |       |   
        |      / \  
        |           
    ____|___        
                    ''')
def getWord():
    rf = open('hangman-words.txt','r')
    words_to_guess =rf.read()
    words_to_guess = words_to_guess.split()
    random = randint(0, len(words_to_guess) - 1)
    word = words_to_guess[random]
    rf.close()
    return word
def valid(c):
    if len(c) == 1 and 97 <= ord(c) <= 122:
        return True
    return False
def play():
    word = getWord()
    lives = 5# saba _
    guess = str((len(word) * '_'))
    while lives > -1:
        displayHangman(lives)
        print("Guess the Word: " + guess)
        print('Enter the Letter:')
        k = input()
        if not valid(k):
            print("input was not valid, Enter Again")
        elif k in word:
            guess = list(guess)
            for x in range(0, len(word)):
                if k == word[x]:
                    guess[x] = k
            guess = ''.join(guess)
        else:
            lives -= 1
        if lives == -1:
            print("Hidden word was : ", word)
            return False
        if guess == word:
            print("Hidden word was: ", word)
            return True
def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again?(yes/no)")
        answer = input()
        if answer == 'no':
            break
        if answer == 'yes':
            continue
        else:
            exit()

if __name__ == "__main__":
    hangman()

