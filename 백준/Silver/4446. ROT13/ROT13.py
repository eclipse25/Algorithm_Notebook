vowels = ['a','i','y','e','o','u']
consonants = ['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f']

while (True):
  try:
    sentence = input()
      
    new_sentence = []
    for i in range(len(sentence)):
      isupper = 0
      lowerchar = sentence[i]
      if sentence[i].isupper() == True:
        isupper = 1
        lowerchar = sentence[i].lower()
        
      if lowerchar in vowels:
        iv = (vowels.index(lowerchar) + 3) % 6
        if isupper == 1:
          new_sentence.append(vowels[iv].upper())
        else:
          new_sentence.append(vowels[iv])
      elif lowerchar in consonants:
        ic = (consonants.index(lowerchar) + 10) % 20
        if isupper == 1:
          new_sentence.append(consonants[ic].upper())
        else:
          new_sentence.append(consonants[ic])
      else:
        new_sentence.append(sentence[i])
  
    print(''.join(new_sentence))
  except:
    break
  