import sys


# function to determine whether a one-to-one character mapping exists from string s1 to string s2
def is_mapping(s1, s2):
    # if the lengths of two strings are not equal, no 1-1 mapping exists
    if len(s1) != len(s2):
        return False
    dict = {}
    for i in range(len(s1)):
        # if the same character in s1 maps to different character in s2, no 1-1 mapping exists
        if s1[i] in dict and dict[s1[i]] != s2[i]:
            return False
        else:
            # update char mapping between s1 and s2
            dict[s1[i]] = s2[i]
    return True


def main():
    # check number of input arguments
    if len(sys.argv) != 3:
        print("Please provide TWO strings as function input.")
        return
    if is_mapping(sys.argv[1], sys.argv[2]):
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()
