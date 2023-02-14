a = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
  '''
print(a.capitalize()) # capitalize text
a = a.capitalize()
print(a.replace('iz', 'is'))
a = a.replace('iz', 'is') # replace from iz to is
print(a.split('.'))
sentences = a.split(('.')) # split text on sentences
final_sentences = [] # create empty list
for sentence in sentences: # run loop for each sentence
    sentence = sentence.strip() #remove whitespaces
    if not sentence: # if not a sentence - continue
        continue
    sentence = sentence.capitalize() # capitalize text for each sentence
    final_sentences.append(sentence) # add each sentence to final list
final_text = '. '.join(final_sentences) # join sentences
final_text = final_text + '.' # add dot at the end of text
print(final_text) # see the result

string = '''
  homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
# counter = 0
# for i in string:
#     if i == ' ' or i == '\n':
#         counter += 1
# print(counter)

# print(len(string.split())-1)

#taking input from the user
string = input("Enter your string: ")
#splitting the string
words = string.split()[-1] # take last word from string
print(words)
# for i in words:
# #slicing the list (negative index means index from the end)
# #-1 means the last element of the list
#print(words[-1])

