## The DES encryption scheme
## Developed by Adam Burke, Riya Gupta, Kathryn Furman, and Joe Hirsch for MATH4575, Fall 2023
import copy

## CONSTANTS ##  ## TODO add actual values
(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16) = None
S_BOXES = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16]
IP = None
IP_INV = None
E = None
P = None
PC1 = None
PC2 = None

###################################################################################
# DES encryption functions
###################################################################################
g_round_states = [] ## stores data of the form [RoundData] for 0 <= i <= 16 and with K0 = K, see def(RoundData) below


def encrypt(plaintext, key):
    return None

def decrypt(ciphertext, key):
    return None

def keySchedule(key):
    return None

def next_CD(C, D, round_idx):
    shifts = v(round_idx)
    return (circular_left_shift(C, shifts), circular_left_shift(D, shifts))

def u0(plaintext):
    return perm_matrix_mul(PC1, plaintext)

def next_u(prev_L, prev_R, curr_K):
    return g(prev_R, prev_R, curr_K)

def g(prev_L, prev_R, curr_K):
    return (prev_R, f(prev_R, curr_K) + prev_L)

def f(A, J):
    C = perm_matrix_mul(E, A) + J
    return perm_matrix_mul(P, C)

def v(i):
    return 1 if i in [1,2,9,16] else 2










###################################################################################
# Matrix algebra functions
###################################################################################
# for each aij in m1 and bkl in m2, assigns bkl <- aij in order
def perm_matrix_mul(m1, m2):
    m = [] ## the result
    for i in range(len(m1)):
        m.append(m2[m1[i]])
    return m


# For an (m x n) matrix m with even n, returns a (m x n/2) matrix of the values in the left half
def left_matrix(m):
    return None

# For an (m x n) matrix m with even n, returns a (m x n/2) matrix of the values in the right half
def right_matrix(m):
    return None

# Writes a valid DES key to a 8x8 matrix
def key_to_matrix(key):
    return None

# Applies S-box S to 6-bit vector B, returns 4-bit vector
def apply_S_box(S, B):
    return None

# returns the element at (row, col) 1-indexed logical coordinate of m
def getElement(m, row, col):
    return None

# performs a circular left shift of vector v by n places
def circular_left_shift(v, n):
    w = copy.deepcopy(v)
    for i in range(n):
        w = w[1:] + [w[0]]
    return w


###################################################################################
# classes and data
###################################################################################
class RoundData:
    def __init__(self, B, C, D, L, K, R): ## data tracked in a round, constructed alphabetically by variable
        self.B = B
        self.C = C
        self.D = D
        self.L = L
        self.K = K
        self.R = R
