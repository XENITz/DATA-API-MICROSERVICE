
class Logic:
    def __init__(self):
        pass
    
    def analyze_text(self, text):
        '''
        FUNCTION TO THAT ANALYZE TEXT(STR) AND RETURN
        A DICTIONARY WITH 3 KEYS: WORD COUNT, CHARACTER COUNT
        AVERAGE WORD LENGTH
        '''
        character_count = len(text)
        word_count = len(text.split())
        average_word_length = round(float(character_count / word_count) if word_count > 0 else 0 , 2)
        
        return {
            "word_count": word_count,
            "character_count": character_count,
            "average_word_length": average_word_length
        }
        
        
            



if __name__ == "__main__":
    #STRING = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?' So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    STRING = ""
    logic = Logic()
    print(logic.analyze_text(STRING))
    
