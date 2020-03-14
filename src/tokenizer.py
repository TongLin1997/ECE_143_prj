import nltk

class DataTokens:
    def __init__(self):
        self.token_counts = {}
        self.token_locations = {}

    def __len__(self):
        return len(self.token_counts.keys())

    def desc2token(self,description,class_name):
        '''
        :param description: description string of a class
        :return: description broken up into tokens
        '''
        assert(isinstance(description,str))
        tokens = nltk.word_tokenize(description)
        for el in tokens:
            el = el.lower()
            if el not in self.token_counts.keys():
                self.token_counts[el] = 1
                self.token_locations[el] = [class_name]
            else:
                self.token_counts[el] = self.token_counts[el] + 1
                self.token_locations[el].append(class_name)

    def get_num_occurs(self,token):
        assert(token in self.token_counts)
        return self.token_counts[token]

    def get_locs(self,token):
        assert(token in self.token_locations)
        return self.token_locations[token]
'''
    def return_reverse(self):
        return {nums: els for els, nums in self.token_counts.items()}

    def return_prereq(self,desc):
        assert(isinstance(desc,str))
        desc = desc.lower()
        if "prerequisite" not in desc and "prerequisites" not in desc and "corequisite" not in desc:
            return None
        else:
            if "corequisite" in desc:
                return desc.split("corequisite:")[1]
            elif "prerequisites" in desc:
                return desc.split("prerequisites:")[1]
            else:
                return desc.split("prerequisite:")[1]
'''