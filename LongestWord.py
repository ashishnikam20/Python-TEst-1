def LongestWord(str):
    str = sorted(str, key = len)

    print(str[-1])

if __name__ == "__main__":

    str =  "It is a longgggggggggg established fact"
    LST = list(str.split(" "))

    LongestWord(str)