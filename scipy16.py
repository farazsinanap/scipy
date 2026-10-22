from scipy.stats import chisquare

observed = [20, 30, 25, 25]
expected = [25, 25, 25, 25]

chi_stat,p_value = chisquare(observed,f_exp=expected)
print("chi_square statistic: ",chi_stat)
print("p_vlaue: ",p_value)