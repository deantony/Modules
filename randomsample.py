import random

def normal_sample(sample_size, sample_mean = 100, sample_sd = 15):
    indv = 1
    sample = []
    while indv <= sample_size:
        x = random.randint(1, 10000)
        if 1 <= x <= 3413: # 0 <= Z <= 1   34.13%
            sample.append(random.randint(sample_mean, sample_mean + sample_sd))
        elif 3414 <= x <= 6826: # -1 <= Z <= 0   34.13% 
            sample.append(random.randint(sample_mean - sample_sd, sample_mean))
        elif 6827 <= x <= 8185: # 1 <= Z <= 2   13.59%
            sample.append(random.randint(sample_mean + sample_sd, sample_mean + (2 * sample_sd)))
        elif 8186 <= x <= 9544: # -2 <= Z <= -1   13.59%
            sample.append(random.randint(sample_mean - (2 * sample_sd), sample_mean - sample_sd))
        elif 9545 <= x <= 9759: # 2 <= z <= 3   2.15%
            sample.append(random.randint(sample_mean + (2 * sample_sd), sample_mean + (3 * sample_sd)))
        elif 9760 <= x <= 999974: # -3 <= Z <= -2   2.15%
            sample.append(random.randint(sample_mean - (3 * sample_sd), sample_mean - (2 * sample_sd)))
        elif 9975 <= x <= 9987: # 3 <= Z <= 5   .13% beyond Z = 3
            sample.append(random.randint(sample_mean + (3 * sample_sd), sample_mean + (5 * sample_sd)))
        elif 9988 <= x <= 10000: # -5 <= Z <= -3   .13% beyond Z = 3
            sample.append(random.randint(sample_mean - (5 * sample_sd), sample_mean - (3 * sample_sd)))
        
        indv += 1
    return sample

