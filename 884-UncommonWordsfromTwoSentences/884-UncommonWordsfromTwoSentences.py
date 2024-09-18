class Solution:
    def uncommonFromSentences(self, s1, s2):
       
        #split the sentences into words
        words_s1 = s1.split()
        words_s2 = s2.split()

        #Combine all words
        all_words = words_s1 + words_s2
        print(all_words)

        #check the frequency of each word
        words_dict = {}
        for word in all_words:
            #if word exists already in dict
            if word in words_dict:
                 words_dict [word] +=1

            #if seen for first time in dict
            else:
                words_dict[word] = 1

        #find words whose frequency = 1
        return(word for word in all_words if words_dict[word] == 1)

        