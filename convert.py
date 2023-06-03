import docx2txt

# replace following line with location of your .docx file
MY_TEXT = docx2txt.process("FAKTA-ILMIAH-KEHARAMAN-BABI-denata.docx")


with open("Output.txt", "w") as text_file:
    print(MY_TEXT, file=text_file)