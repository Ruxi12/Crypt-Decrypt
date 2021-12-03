def decrypt(cheie, fisierout):
    with open(fisierout) as f:
        text = f.read()
        ascii_text = "".join([chr(int(binary, 2)) for binary in text.split()])
        len_key = len(key)
        cipherAscii = ""
        for i in range(len(ascii_text)):
            j = i % len_key
            xor = ord(ascii_text[i]) ^ ord(key[j])
            cipherAscii = cipherAscii + chr(xor)
        g.write(cipherAscii)


key = input()
g = open("input_recuperat.txt","w")
decrypt(key,"output.txt")
g.close()

