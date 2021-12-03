def binary(num, length=8):
    b = bin(num).lstrip("0b")
    b = "0" *(length-len(b)) + b
    return b

def crypt(cheie, fisierin):
  with open(fisierin) as f:
      text = f.read()
      len_key = len(key)
      cipherBin = ""
      for i in range(len(text)):
          j = i % len_key
          xor = ord(text[i]) ^ ord(key[j])
          cipherBin = cipherBin + binary(xor) + " "
      g.write(cipherBin)


key = input ()
g = open("output.txt","w")
crypt(key,"input.txt")
g.close()