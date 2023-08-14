# -*- encoding: UTF-8 -*-
import numpy as np
from scipy.stats import skew, kurtosis

class Evaluate:
    def __init__(self,values):
        self.mean = np.mean(values,axis=0)
        self.skews = skew(values, axis=0)
        self.kurt = kurtosis(values, axis=0)
    
    
    def calculate_weighted_score(self,mean_score, kurtosis_score, skewness_score):
        """
        Calculate the weighted score based on mean, kurtosis, and skewness scores.

        :param mean_score: Score based on mean of probabilities
        :param kurtosis_score: Score based on kurtosis of probabilities distribution
        :param skewness_score: Score based on skewness of probabilities distribution
        :param weights: Dictionary containing weights for each measure (mean, kurtosis, skewness)
        :return: Weighted score
        """
        weights = {
            'mean':0.3,
            'kurtosis':0.4,
            'skewness':0.3
        }
        weighted_mean = mean_score * weights['mean']
        weighted_kurtosis = kurtosis_score * weights['kurtosis']
        weighted_skewness = skewness_score * weights['skewness']

        weighted_score = weighted_mean + weighted_kurtosis + weighted_skewness
        return weighted_score
    
    def final_score(self):
        i,j,k = [self.mean,self.kurt,self.skews]
        score = self.calculate_weighted_score(i,j,k)
        inicio = score[0:3]
        fim = score[3:]
        final = fim.sum() - inicio.sum()
        print(final)
        return final
        
        
        