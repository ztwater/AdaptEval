def frequency_sample_std_dev(X, n):
    """
    Sample standard deviation for X and n,
    where X[i] is the quantity each person in group i has,
    and n[i] is the number of people in group i.
    See Equation 6.4 of:
    Montgomery, Douglas, C. and George C. Runger. Applied Statistics 
     and Probability for Engineers, Enhanced eText. Available from: 
      WileyPLUS, (7th Edition). Wiley Global Education US, 2018.
    """
    n_groups = len(n)
    n_people = sum(n)
    lhs_numerator = sum([ni*Xi**2 for Xi, ni in zip(X, n)])
    rhs_numerator = sum([Xi*ni for Xi, ni in zip(X,n)])**2/n_people
    denominator = n_people-1
    var = (lhs_numerator - rhs_numerator) / denominator
    std = sqrt(var)
    return std
