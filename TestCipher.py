'''
  File: TestCipher.py

  Description: first assignment

  Student's Name: Shimin Zhang

  Student's UT EID: sz6939

  Course Name: CS 313E

  Unique Number: 51350

  Date Created: 9/8/2018

  Date Last Modified: 9/9/2018
'''

# takes a single string as input parameter and returns a string
def substitution_encode ( strng ):
  cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
  newStrng=''
  for i in strng:
      if 97<=ord(i)<=122:
        idx = ord(i) - ord('a')
        newStrng=newStrng+cipher[idx]
      else:
        newStrng = newStrng + i
  return(newStrng)


# takes a single string as input parameter and returns a string
def substitution_decode ( strng ):
    cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm',
              'i', 'k', 'o', 'l', 'p']
    alphabet = []
    for letter in range(97, 123):
        alphabet.append(chr(letter))#create a list of alphabet

    newStrng = ''
    for i in strng:
        try:
            idx= cipher.index(i)
            newStrng=newStrng+alphabet[idx]
        except:
            newStrng = newStrng + i #when punctuation marks, digits and spaces appear
    return(newStrng)


# takes two strings as input parameter and returns a string
def vigenere_encode ( strng, passwd ):
    alphabet = []
    for letter in range(97, 123):
        alphabet.append(chr(letter))

    newStrng = ''
    listIdx = 0
    for i in strng:
        if 97 <= ord(i) <= 122:
            strngIdx = alphabet.index(i)#convert letters in the plain text to the index in alphabet

            if (listIdx+1)%len(passwd)==0:#if this is No.X letter in the plain text and X is divisible by the length of
                # the password, this letter in the plain text should be matched with the last letter in the pass phrase
                passwdIdx=alphabet.index(passwd[-1])# convert the last letter in the pass phrase to the index in alphabet

            else:#if X is not divisible by the length of the password, this letter in the plain text should be matched
                # with the NO.remainder letter in the pass phrase
                passwdIdx=alphabet.index(passwd[(listIdx+1)%len(passwd)-1])#convert the NO.remainder letter in the pass
                # phrase to the index in alphabet

            # add the two indexes to get the final index and convert it to the final letter
            if strngIdx+passwdIdx<=25:#
                newStrng = newStrng + alphabet[strngIdx+passwdIdx]
            else:
                newStrng = newStrng + alphabet[strngIdx+passwdIdx-26]
            listIdx+=1
        else:
            newStrng = newStrng + i #when punctuation marks, digits and spaces appear

    return (newStrng)

# takes two strings as input parameter and returns a string
def vigenere_decode ( strng, passwd ):
    alphabet = []
    newStrng = ''
    for letter in range(97, 123):
        alphabet.append(chr(letter))

    listIdx = 0
    for i in strng:
        if 97 <= ord(i) <= 122:
            strngIdx = alphabet.index(i)
            if (listIdx + 1) % len(passwd) == 0:
                passwdIdx = alphabet.index(passwd[-1])
            else:
                passwdIdx = alphabet.index(passwd[(listIdx + 1) % len(passwd) - 1])

            # subtract passwdIdx from strngIdx to get the final index and convert it to the final letter
            newStrng = newStrng + alphabet[strngIdx - passwdIdx]

            listIdx += 1

        else:
            newStrng = newStrng + i

    return (newStrng)


def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

 # read line to be decoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
