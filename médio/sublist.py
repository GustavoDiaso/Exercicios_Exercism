"""
Given any two lists A and B, determine if:

List A is equal to list B; or
List A contains list B (A is a superlist of B); or
List A is contained by list B (A is a sublist of B); or
None of the above is true, thus lists A and B are unequal

Specifically, list A is equal to list B if both lists have the same values in the same order.

List A is a superlist of B if A contains a contiguous sub-sequence of values equal to B.

List A is a sublist of B if B contains a contiguous sub-sequence of values equal to A.

"""

def compare_lists(list_a: list, list_b: list) -> str:

    def first_in_second(l1: list, l2: list) -> bool:
        if len(l1) and len(l2) != 0:
            if l2[l2.index(l1[0]):l2.index(l1[0]) + len(l1)] == l1:
                return True
            else:
                return False
        else:
            if len(l1) == 0:
                return True
            else:
                return False


    if list_a == list_b:
        return 'A equals to B'

    elif first_in_second(list_a, list_b):
        return 'A is a sublist of B'

    elif first_in_second(list_b, list_a):
        return  'A is a superlist of B'

    else:
        return  'A and B are unequal'



print(compare_lists([1, 3, 2], [1, 3, 2]))















