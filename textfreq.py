class myClass(object):
    def __init__(self,myfile=""):
        f = open("demofile.txt","r")
        myContent = f.read()
        mySentences = myContent.split(".")
        self.myWords = []
        for sentence in mySentences:
            Words_In_The_Sentence = sentence.split(" ")
            for word_1 in Words_In_The_Sentence:
                self.myWords.append(word_1)
    def frekans1(self):
        frekans = {}
        for word in self.myWords:
            if(word in frekans):
                frekans[word] = frekans[word] + 1
            else:
                frekans[word] = 1
        return frekans
    def frekans2(self):
        ikilidizi = []
        frekans = {}
        for i in range(len(self.myWords)-1):
            ikilidizi.append(self.myWords[i] + " " +self.myWords[i+1])
        for word in ikilidizi:
            if (word in frekans):
                frekans[word] = frekans[word] + 1
            else:
                frekans[word] = 1
        return frekans

class1 = myClass()

print(class1.frekans1())
print(class1.frekans2())


