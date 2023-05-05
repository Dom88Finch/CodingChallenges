import numpy as np 
import re 
import os
import glob

## class used to search text and find a given word
class WordFinder:
    def __init__(self, path):
        ## define our path
        self.path = path 

    def pre_process_checks(self):
        '''
        Function below is used to check our file and identify potential common errors that could occur in our file
        '''
        try:
            with open(self.path, 'r') as f: #open the file
                contents = f.readlines() #put the lines to a variable (list).
                ## by looping through and removing empty linews from our list, we ensure that we are are not searching on empty lists
                contents = [j for j in contents if j != '\n']
                ## obtain the source text
                source_text = contents[:-1] 
                ## obtain the search term
                search_term = contents[-1].strip().split(' ')
                # print(len(search_term))
                try:
                    if len(search_term) == 1 and len(source_text) > 0:
                        # print('The search term has more than 1 item')
                        return source_text, search_term[0]
                    # else:
                    #     print('The search term has more than 1 item. Please review the format of document')
                except IndexError:
                    print("Length of source term is insufficient. there can only be 1 search term.")
                    return
            
        except IOError:    #This means that the file does not exist (or some other IOError)
            print(f"Oops, no file found in path:  {self.path}.")

        
        except IndexError:
                ## catch source text that is less that 
                print("Length of source text is insufficient. source text must be greater than 0.")
       
                    
    def pattern_word_matcher(self, source_text, search_term):
        '''
        Function used to pattern match our source text and search term as a list []
        '''
        # will be used to store our matched words/sentences 
        all_matches = []
        pattern = re.compile("^[a-zA-Z]+$")
        for line in  source_text:
            ## apply search to identify if item is found in string or not 
            if re.search(search_term, line):
                ## replace strings that are not in alphabet with space and then 
                ## apply strip to remove trailing spaces.
                match = re.sub(r'[^a-zA-Z]+', ' ', line).strip()
                ## append the processed line to our list `all_matches` 
                all_matches.append(match)                                         
        # print(all_matches)
        return all_matches

    def apply_pattern_matching(self):
        ''' 
        function call both our `pre_process_checks` function and `pattern_word_matcher` and returns our result as a list []
        '''
        try:
            source_text, search_term  = self.pre_process_checks()
            # print(source_text)
            result = self.pattern_word_matcher(source_text, search_term)
            # print(result)
            return result
        except TypeError:
            print('No search term found. Please review the format of document')
            return []

## to run code, replace path with desired file path and run this below by replacing the path and uncomment the code   
# path = 'test_scripts/sample_text_1.txt'
# finder  = WordFinder(path)
# matched_list = finder.apply_pattern_matching()
# print(matched_list)

