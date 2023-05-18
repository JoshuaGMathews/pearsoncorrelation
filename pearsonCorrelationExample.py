# Pearson correlation example

import math
# pearson correlation between two dictionaries
def pearsonD(userratings1, userratings2):
    sumpq = 0
    sump = 0
    sumq = 0
    sump2 = 0
    sumq2 = 0
    n = 0

    for item in userratings1.keys():
        if item in userratings2.keys():
            # calculate the pearson correlation using the computationally efficient form
            p = userratings1[item]
            q = userratings2[item]
            
            sumpq += p * q
            sump += p
            sumq += q
            sump2 += p**2
            sumq2 += q**2
            n = n + 1
    # pearson correlation coefficient
    nr = (sumpq - (sump *sumq) / n)
    dr = (math.sqrt(sump2 - sump**2 / n) * math.sqrt(sumq2 - sumq**2 / n))
    r = nr/dr
    
    return r
      
# establish the dictionaries of ratings      
UserPRatings = {'Apple':1, 'Samsung':5, 'Nokia':7, 'Motorola':8, 'LG':5, 'Sony':1, 'Blackberry':7 }
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

# run and print
pC = pearsonD (UserPRatings, UserQRatings)
print("P ratings:", UserPRatings)
print("Q ratings:", UserQRatings)
print("Pearson Correlation =", round(pC,4))