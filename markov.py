import math

def k_tokens(text, k, idx):

    text_circular = text + text[0:k]
    text_circular_plus = text + text[0:k + 1]

    return text_circular[idx:idx + k], text_circular_plus[idx:idx + k + 1]

class Markov:

    def __init__(self,k:int,text:str):
        """
        Constructs a new k-order markov model using provided text
        """
        self._text = text
        self._k = k 
        self._tokens = {}

        for idx,_ in enumerate(text):

            k_string,k_string_plus = k_tokens(self._text,self._k,idx)

            if k_string not in self._tokens:
                self._tokens[k_string] = 0
            self._tokens[k_string] += 1

            if k_string_plus not in self._tokens:
                self._tokens[k_string] = 0
            self._tokens[k_string_plus] += 1

    def log_probability(self, text: str) -> float:
        """
        Retrieves the log, Laplace-smoothed probability of a given string given
        the statistics of the character sequences model by the Markov model. 
        
        """

        # Intializing total likelihoods
        total_likelihood = 0

        S = len(set(text))

        for idx, char in enumerate(text):
            
            k_string,k_string_plus = k_tokens(self._text,self._k,idx)

            if self._tokens.get(k_string):
                N = self._tokens.get(k_string)
            else:
                N = 0

            if self._tokens.get(k_string_plus):
                M = self._tokens.get(k_string_plus)
            else:
                M = 0
            
            total_likelihood += math.log((M + 1) / (N + S))

        return total_likelihood
            





