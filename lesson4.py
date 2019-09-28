# Practise Functios
# Warmup

def lesser_of_two(a,b):
    '''
    A function that returns the lesser of two given if both numbers are even
    but returns the greater if one or both numbers are odd
    ex:
    lesser_of_two(2,4)
    Returns 2
    lesser_of_two(2,5)
    returns 5
    '''
    # If a and b are even then return min
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two(2,5))
print(lesser_of_two(2,4))

def animal_crackers(text):
    '''
    this function takes a two word string and returns True if the both words start with the same letter
    ex:
    levelheaded llama                 (true)
    crazy kangaroo                    (false)
    '''
    new_List = text.lower().split()
    print(new_List)
    result = (new_List[0][0] == new_List[1][0])
    return result
print(animal_crackers('levelheaded llama'))
print(animal_crackers('crazy Kangeroo'))


def makes_twenty(n1,n2):
    '''
    Given two integers, return True if the sum of the integer is 20 or if 1 of the integer is twenty.
    If not, return false.
    '''
    return(n1 + n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(20, 10))
#return true
print(makes_twenty(12, 8))
#return Ture
print(makes_twenty(2,3))
#return flase


# hard level one

def old_macdonald(name):
    '''
    Write a function that capitalizes the first and fourth letters of a name,
    if the name is less than four is characters, 
    return the name is too short.
    len()
    .capitalize()makes the current character Capital
    '''
    if len(name) < 4:
        return "name is too short!"
    else:
        return name[0:3].capitalize() + name[3:].capitalize()

print(old_macdonald("bob"))
print(old_macdonald("joshua"))


def fake_master_yoda(sentence):
    '''
    Given a sentence return the same sentence with the wrds reversed
    '''
    wordlist = sentence.split(" ")
    return " ".join(wordlist[::-1])
print(fake_master_yoda('I am home'))
# returns I am home
print(fake_master_yoda('We are ready'))
# returns Ready we are



def Real_Master_Yoda(sentence):
    '''
    Given a sentence, put the first two words of the sentence and put it in the end
    '''
    import random

    number_of_words = random.randint(2, 3)
    wordlist = sentence.split()
    if len(wordlist) > 3:
        return " ".join(wordlist[number_of_words:] + wordlist[:number_of_words])
    else:
        return "get yodaed!"
print(Real_Master_Yoda("you will find what you are looking for"))
print(Real_Master_Yoda("d f g"))


def we_are_almost_there(n):
    '''
    Given an intger n, return true if n is within 10 or either 100 or 200
    use abs() takes the absolute value of the object
    '''
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print(we_are_almost_there(90), we_are_almost_there(104), we_are_almost_there(150), we_are_almost_there(209))


def print_big(letter):
    '''
    write a function that takes in the letter and returns a 5x5 representation f the letter
    print_big('a')

    out:              *
                     * *
                    *****
                    *   *
                    *   *
    HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
    For purposes of this exercise, it's ok if your dictionary stops at "E".
    '''
    patterns = {
        1: '  *  ',
        2: ' * * ',
        3: '*   *',
        4: '*****',
        5: '**** ',
        6: '   * ',
        7: ' *   ',
        8: '*  * ',
        9: '*    ',
        0: '    *',
        10:'  ** '
    }
    alphabet = {
        'A': [1,2,4,3,3],
        'B': [5,3,5,3,5],
        'C': [4,9,9,9,4],
        'D': [5,3,3,3,5],
        'E': [4,9,4,9,4],
        'F': [4,9,4,9,9]
    }
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('c')