# This is a sample Python script.
import string


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def vigenere_encrypt(plaintext, keyword):
    encrypted_nums = []
    for i in range(len(plaintext)):
        encrypted_nums.append((ord(plaintext[i]) - ord('A') - ord(keyword[i % len(keyword)]) - ord('A')) % 26)
    return numbers_to_letters(encrypted_nums)



def letters_to_numbers(input_string):
    # Initialize an empty list to store the numbers
    numbers = []

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            # Convert the letter to a number (0-25) and append it to the list
            number = ord(char) - ord('A')
            numbers.append(number)

    return numbers

def numbers_to_letters(numbers):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each number in the list
    for number in numbers:
        # Check if the number is within the valid range (0-25)
        if 0 <= number <= 25:
            # Convert the number to the corresponding uppercase letter (A-Z) and append it to the result
            letter = chr(number + ord('A'))
            result += letter
        else:
            # If the number is outside the valid range, ignore it
            pass

    return result


## makes a 26x2 matrix of the frequency of each english letter in _s_ in order
## C^N U P^N -> (Z/26Z x N)^26
letters_freq = lambda s: [(chr(i + ord('a')), s.lower().count(chr(i + ord('a')))) for i in range(26)]

## Calculates the index of coincidence of _s_ using english alphabet
## C^N U P^N -> R
Ic = lambda s: (1 / (len(s) * (len(s) - 1))) * sum(fm * (fm - 1) for m, fm in letters_freq(s))

## calculates the first _n_ iterates in the orbit of function _g_ about initial point _x0_
## Lambda[S -> S] x S x N -> S^N, for a set S
orbit = lambda g, x0, n: [x0] + [x0 := g(x0) for i in range(n)]

## calculates the joint probability Pr(_x_,_y_) under probability distn functions
## _prX_ and _prY_ which must be defined for inputs x, y,, resp
## PrY is optional: if not given then defaults to prX.
## X x Y x Lambda[PowerSet(X) -> R] x Lambda[PowerSet(Y) -> R] -> R
joint_prob = lambda x, y, prX, prY: cond_prob(x, y, prX, prX if prY is None else prY) * (prX if prY is None else prY)(y)

## calculates the conditional probability Pr(_x_ | _y_) under probability  distn functions
## _prX_ and _prY_ which must be defined for inputs x, y,, resp
## PrY is optional: if not given then defaults to prX.
## X x Y x Lambda[PowerSet(X) -> R] x Lambda[PowerSet(Y) -> R] -> R
cond_prob = lambda x, y, PrX, prY: 0 # TODO

def perm_matrix_mul(m1, m2):
    m = [] ## the result
    for i in range(len(m1)):
        m.append(m2[m1[i]])
    return m

def as_matrix(m, nrows, ncols):
    matrix = []
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(m[ncols * i + j])
        matrix.append(row)
    return matrix




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # def next_char(z):
    #     return [z[1], z[2], z[3], (z[0] + z[2] +  z[3]) % 2]
    #
    # def h(z):
    #     return next_char(next_char(next_char(next_char(z))))
    PC1 = [57,49,41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]
    K = [1, 0, 0, 0, 1, 0, 0, 1,
         0, 1, 0, 0, 0, 1, 0, 1,
         0, 0, 1, 0, 0, 0, 1, 1,
         0, 0, 0, 1, 0, 0, 1, 1,
         0, 0, 0, 1, 0, 0, 1, 1,
         0, 0, 1, 0, 0, 0, 1, 1,
         0, 1, 0, 0, 0, 1, 0, 1,
         1, 0, 0, 0, 1, 0, 0, 1]

    print(as_matrix(perm_matrix_mul(PC1, K), 8, 7))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
