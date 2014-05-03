import random

def addQuote():
    #print "addQuote: Line 4"
    quoteLength = random.randint(1, 20)
    quoteCount = 0
    quote = " \"Hodor"

    while quoteCount < quoteLength:
        tmp = random.randint(1, 20)
        if tmp < 4:
            quote += " Hodor"
        else:
            quote += " hodor"
        quoteCount += 1
    tmp3 = random.randint(0, 100)
    if tmp3 <= 10:
        quote += "?\""
    elif tmp3 <= 20:
        quote += "!\""
    else:
        quote += ".\""

    tmp = random.randint(0,2)
    for i in range (0, tmp):
        tmp2 = random.randint(1,2)
        if tmp2 < 2:
            quote += " Hodor"
        else:
            quote += " hodor"
    return quote
    #print "Quote! Line 18"

def addHodor(sentence):
    #print "Pre addHodor: " + sentence
    #print "addHodor"
    capital = random.randint(1, 10)
    if capital < 4:
        sentence +=" Hodor"
    else:
        sentence +=" hodor"
    #print "Post addHodor: " + sentence
    return sentence

def main():
    wordCount = 0
    sentenceCount = 0
    sentenceLength = 0

    while wordCount < 4000: #Until chapter is full
        sentencesPerParagraph = random.randint(4, 10) #Create random length for paragraph
        sentenceCount = 0
        print ""

        while sentenceCount < sentencesPerParagraph: #Generate a sentence while less than number per paragraph
            #Create clean sentence
            wordsPerSentence = random.randint(12, 40) #Create random length for sentence
            sentence = "Hodor"
            sentenceLength = 1
            wordCount += 1

            while sentenceLength < wordsPerSentence: #Create number of Hodors
                sentence = addHodor(sentence)
                sentenceLength += 1
                wordCount += 1
                tmp = random.randint(1,10)
                if tmp < 4:
                    sentence += addQuote()
            sentence += ". " #End sentence
            sentenceCount += 1 #Increment number of sentences
            print sentence

if __name__ == "__main__":
    main()
