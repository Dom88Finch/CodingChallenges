import unittest
from final_find_words import WordFinder


class WordMatcher(unittest.TestCase):
    '''
    Use the following class to run unit test on our `WordMatcher`
    '''

    def test_word_finder_func_1(self):
        print("Test 1 Called ...")

        result = ['cat sees me', 'mary likes trees']
        path = 'test_scripts/sample_text_1.txt'        
        matches_found  = WordFinder(path).apply_pattern_matching()
        self.assertListEqual(matches_found, result)

    def test_word_finder_func_2(self):
        print("Test 2 Called ...")  
        result = ['to get very', 'by her sister']
        path = 'test_scripts/sample_text_2.txt'
        matches_found  = WordFinder(path).apply_pattern_matching()
        self.assertListEqual(matches_found, result)

    def test_word_finder_func_3(self):
        print("Test 3 Called ...")

        result = ['this is another', 'this is one']
        path = 'test_scripts/sample_text_3.txt'        
        matches_found  = WordFinder(path).apply_pattern_matching()
        self.assertListEqual(matches_found, result)

    def test_word_finder_func_4(self):
        print("Test 4 Called ...")
 
        result = []
        path = 'test_scripts/sample_text_4.txt'
        matches_found  = WordFinder(path).apply_pattern_matching()
        self.assertListEqual(matches_found, result)

    def test_word_finder_func_5(self):
        print("Test 5 Called ...")
          
        result = ['fsasrm', 'efwonoi asrm']
        path = 'test_scripts/sample_text_5.txt'
        matches_found  = WordFinder(path).apply_pattern_matching()
        self.assertListEqual(matches_found, result)

    def test_word_finder_func_6(self):
        print("Test 6 Called ...")
        #   
        result = []
        path = 'test_scripts/sample_text_6.txt'
        matches_found  = WordFinder(path).apply_pattern_matching() 
        self.assertListEqual(matches_found, result)
    
    def test_word_finder_func_7(self):
        print("Test 7 Called ...")

        result = []
        path = 'test_scripts/sample_text_7.txt' 
        matches_found  = WordFinder(path).apply_pattern_matching()
        self.assertListEqual(matches_found, result)


if __name__ == "__main__":
    unittest.main()
    
