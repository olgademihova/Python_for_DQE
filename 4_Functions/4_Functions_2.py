import re  # import regular expression module

string = '''
  homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


def count_whitespaces():
    result = (len(re.findall(r'\s', string)))
    return result


sentences = count_whitespaces()
print('Count of all whitespaces:', sentences)  # result


def split_sentences():
    split = (re.split(r'([.!?]\s*)', string))
    return split



#print(sentences)  # result


def correct_style_text(sentences):
    final_sentences = []  # create empty list
    for sentence in sentences:  # run loop for each sentence
        sentence = sentence.strip()  # remove whitespaces
        if not sentence:  # if not a sentence - continue
            continue
        sentence = sentence.capitalize()  # capitalize text for each sentence
        final_sentences.append(sentence)  # add each sentence to final list
    return final_sentences



#print(sentences)  # result



def last_words(final_sentences, position):
    last_words = []  # create empty list (v.2)
    for s in final_sentences:
        #print(s)
        if s != '.':
            word = s.split()[-1]
            last_words.append(word)
            #print(word)
    #word = final_sentences.split()[-1]  # split each sentence by words and take the last word from string
    #last_words.append(word)  # add to list all last words of all sentences (v.2)
    last_words = ' '.join(last_words)  # convert list to string with whitespaces (v.2)
    last_words = last_words.capitalize()  # capitalize new sentence
    final_sentences.insert(position, last_words)
    return final_sentences



#print(sentences)


def final_sent(final_sentences):
    final_text = '. '.join(final_sentences)  # join sentences from list to string with dot+space
    final_text = final_text + '.'  # add dot at the end of the text
    final_text = final_text.replace(' iz ', ' is ')  # replace from iz to is with whitespaces
    final_text = final_text.replace(' iz.', ' is.')  # replace from iz. to is.
    final_text = final_text.replace(' ..', ' ')  # replace from  .. to whitespace
    final_text = final_text.replace('.', '.\n')  # replace from  . to .\n
    final_text = re.sub(' +', ' ', final_text)
    return final_text


sentences = split_sentences()   # call the function split_sentences
sentences = correct_style_text(sentences)  # call the function correct_style_text
sentences = last_words(sentences, 3)  # set position and call the function last_words
sentences = final_sent(sentences)  # call the function final_sent

print(sentences)