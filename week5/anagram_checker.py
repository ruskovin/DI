class AnagramChecker():
    def __init__(self):
        with open('week5/words.txt', 'r') as f:
            self.word_list = [ i.strip() for i in f.readlines()]

    def is_valid_word(self,word):
        if word.upper() in self.word_list:
            return True
        print("Your word is not VALID")
        return False
    
    def is_anagram(self, word1, word2):
        wd1 = list(word1)
        wd2 = list(word2)
        if sorted(wd1) == sorted(wd2) and wd1 != wd2:
            return True
        return False


    def get_anagrams(self,word):
        anagrams = []
        for wd in self.word_list:
            if self.is_anagram(word.upper(), wd):
                anagrams.append(wd)
        anagrams_str = " ".join(anagrams)
        if anagrams_str == '':
            return False
        return anagrams_str



    