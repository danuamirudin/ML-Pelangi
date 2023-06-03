# importing SequenceMatcher of difflib module
from difflib import SequenceMatcher

with open('Output.txt', 'rb') as first_file, \
        open('FAKTAILMIAH_TENTANG_KEHARAMAN_BABI_denata.txt', 'rb') as second_file:

    # Reading Both Text Files
    file1 = first_file.read()
    file2 = second_file.read()

    # Comparing Both Text Files
    ab = SequenceMatcher(None, file1, file2).ratio()

    # converting decimal output in integer
    result = int(ab * 100)
    print(f"{result}% Plagiarism Document 1 dengan Document 2 ")

    if result > 50:
        print("Perlu Intervensi")
    elif result == 50:
        print("Baik")
    else:
        print("Lulus")
