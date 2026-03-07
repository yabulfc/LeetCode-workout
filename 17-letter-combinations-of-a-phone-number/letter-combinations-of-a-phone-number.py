class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        

        if not digits:
            print([])
        
        else:
            mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
            }
    

            results = [""]
    
            for digit in digits:
                temp_list = []
    
                for combination in results:
                    for letter in mapping[digit]:
                        temp_list.append(combination + letter)

                results = temp_list

        return results