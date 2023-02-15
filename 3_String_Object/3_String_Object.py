a = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
  '''
print('BEFORE:\n\n', a)

sentences = a.split('.')  # split text on sentences using dot separator
final_sentences = []  # create empty list
# last_words = '' # create new empty string (v.1)
last_words = []  # create empty list (v.2)
for sentence in sentences:  # run loop for each sentence
    sentence = sentence.strip()  # remove whitespaces
    if not sentence:  # if not a sentence - continue
        continue
    sentence = sentence.capitalize()  # capitalize text for each sentence
    final_sentences.append(sentence)  # add each sentence to final list
    word = sentence.split()[-1]  # split each sentence by words and take the last word from string
    last_words.append(word)  # add to list all last words of all sentences (v.2)
last_words = ' '.join(last_words)  # convert list to string with whitespaces (v.2)
    # if last_words == '': # (v.1)
    #     last_words = last_words + word  # (v.1)
    # else:  # (v.1)
    #     last_words = last_words + ' ' + word  # concatinate all last words from each sentence  # (v.1)
# last_words = last_words + '.' # add dot for new sentence
last_words = last_words.capitalize()  # capitalize new sentence
final_sentences.insert(3, last_words)  # insert new sentence after appropriate paragraph
#print(last_words)
final_text = '. '.join(final_sentences)  # join sentences from list to string with dot+space
final_text = final_text + '.'  # add dot at the end of the text
final_text = final_text.replace('Iz', 'Is')  # replace from Iz to Is
final_text = final_text.replace(' iz ', ' is ')  # replace from iz to is with whitespaces
final_text = final_text.replace(' iz.', ' is.')  # replace from iz. to is.
final_text = final_text.replace('Homework:', 'Homework:\t')  # replace with new line
final_text = final_text.replace('variable.', 'variable.\n')  # replace with new line
final_text = final_text.replace('view.', 'view.\n')  # replace with new line
final_text = final_text.replace('paragraph.', 'paragraph.\n')  # replace with new line
final_text = final_text.replace('87.', '87.\n')  # replace with new line
final_text = final_text.replace('here.', 'here.\n')  # replace with new line
final_text = final_text.replace('mistake.', 'mistake.\n')  # replace with new line
final_text = final_text.replace('text.', 'text.\n')  # replace with new line
final_text = final_text.replace('whitespaces.', 'whitespaces.\n')  # replace with new line

print('AFTER:\n\n', final_text)  # see the result

string = '''
  homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

counter = 0  # set counter as 0
for i in string:  # run loop for each element of text
    if i == ' ' or i == '\n' or i == '\r' or i == '\f' or i == '\t':  # if i has whitespaces
        counter += 1  # add it to counter
print('Count of all whitespaces:', counter)  # result



