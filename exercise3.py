user_list = []


def input_list_helper():
    for i in range(5):
        user_list.append(int(input("Enter a number: ")))
    return user_list


def input_list(user_list):
    sum = 0
    for i in range(len(user_list)):
        sum += user_list[i]
    user_list.append(sum)
    return user_list


""" the user_list() function
    collects numbers from user input,
    calculate their sum and return it as a list
		(We recommend creating a helper function named
		input_list_helper for collecting the user input
    :return: list of numbers that were given
    by the user, the last object is the sum of all the others
    """

# print(input_list_helper())
# print(input_list(user_list))


def check_monotonic_sequence(sequence):
    """ get a sequence (list) of numbers and determine its
    monotonicity type

    :return: list of 4 booleans that represent 4 different
             monotonicity characters
        """

    mono_up = True
    mono_upstrong = True
    mono_down = True
    mono_downstrong = True
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i+1]:
            mono_up = False
        if sequence[i] >= sequence[i+1]:
            mono_upstrong = False
        if sequence[i] < sequence[i+1]:
            mono_down = False
        if sequence[i] <= sequence[i+1]:
            mono_downstrong = False
    return [mono_up, mono_upstrong, mono_down, mono_downstrong]

# print(check_monotonic_sequence([1, 2, 2, 3]))


def check_monotonic_sequence_inverse(def_bool):

    mono_up = False
    mono_upstrong = False
    mono_down = False
    mono_downstrong = False
    if def_bool[0] == True:
        mono_up = True
    if def_bool[1] == True:
        mono_upstrong = True
    if def_bool[2] == True:
        mono_down = True
    if def_bool[3] == True:
        mono_downstrong = True
    if mono_up == True and mono_upstrong == True and mono_down == True and mono_downstrong == True:
        return [100]
    elif mono_up == True and mono_upstrong == True:
        return [1, 2, 3, 5]
    elif mono_up == True and mono_down == True:
        return [1, 1, 1, 1]
    elif mono_up == True and mono_downstrong == False:
        return [1, 2, 2, 4]
    elif mono_down == True and mono_downstrong == True:
        return [5, 4, 3, 1]
    elif mono_down == True and mono_upstrong == False:
        return [4, 3, 3, 1]
    elif mono_up == False and mono_upstrong == False and mono_down == False and mono_downstrong == False:
        return [1, 0, -1, 1]
    else:
        return None


""" The function that gets a boolean list, and checks if it
	  matches any of the valid monotonicity cases, if it does,
    it will return a matching list,
		else (if such doesn't exist such a sequence),
		it will return None

    :param def_bool: a list of 4 booleans
    :return: matching sequence to the booleans
						 monotonicity_inverse value
    """

# print(check_monotonic_sequence_inverse([True, False, False, True]))
# print(len(check_monotonic_sequence_inverse([False, True, True, True])))


# def primes_generator(n):
#     prime_list = []
#     for i in range(2, n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             prime_list.append(i)
#     return prime_list


""" the functions find and return a list of prime numbers
            with n primes in it.

    :param n: number of primes the function needs to return
    :return: list that contains the amount of n prime numbers.
    """


def primes_generator(n):
    prime_list = []
    i = 2
    while len(prime_list) < n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
        i += 1
    return prime_list


# print(primes_generator(5))

def is_empty_vector(vec_lst):
    for i in vec_lst:
        if len(str(i)) > 0:
            return False
    return True


"""
    being called by vectors_list_sum()
		to check if a vector list is empty

    :param vec_lst: a list with lists inside of it,
					 each sublist     is a vector

    :return: True when empty and False when not.
    """


def vectors_list_sum(vec_lst):
    sum_vec = []
    if len(vec_lst) == 3:
        for i in range(0, len(vec_lst)-2):
            for j in range(0, len(vec_lst[i])):
                sum_vec.append(vec_lst[0][j] + vec_lst[1][j] + vec_lst[2][j])
    else:
        for i in range(len(vec_lst)-1):
            for j in range(len(vec_lst[i])):
                sum_vec.append(vec_lst[i][j] + vec_lst[i+1][j])
    return sum_vec


""" get a list of vectors, add them to each other
    and returns a vector of their sum.

    :param vec_lst: a list with lists inside of it,
					each sublist is a vector

    :return: list of the total vectors sum.
    """

# print(vectors_list_sum([[1, 1, 1], [1, 0, 0], [0, 0, 100]]))
# vec_lst = [[1, 1, 1], [1, 0, 0], [0, 0, 100]]
# print((vec_lst[2]))


def calc_the_inner_product(vec_1, vec_2):
    inner_product = 0
    if is_empty_vector(vec_1) == True and is_empty_vector(vec_2) == True:
        return inner_product
    elif is_empty_vector(vec_1) == True or is_empty_vector(vec_2) == True:
        return None
    else:
        for i in range(len(vec_1)):
            inner_product += vec_1[i] * vec_2[i]
        return inner_product

# print(calc_the_inner_product([], []))


""" gets two list, calculates their inner
        product and returns it

    :param vec_1: list of numbers
    :param vec_2: list of numbers
    :return: the inner product of the two lists.
    """


def orthogonal_number(vectors):
    orth_pairs = 0
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            if calc_the_inner_product(vectors[i], vectors[j]) == 0:
                orth_pairs += 1
    return orth_pairs


""" get a list of vectors, and check how many pairs in
    the list are orthogonal
		 then it returns the amount of pairs as int.
     You should use the calc_the_inner_product() helper function
		 for calculations.

    :param vectors: list of lists, with numbers in it
    :return: number (float), of the amount of orthogonal pairs
    """
