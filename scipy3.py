from scipy import stats

exam1 = [75, 80, 85, 70, 90, 78, 88, 82]
exam2 = [65, 72, 68, 75, 70, 66, 74, 69]

t_stat,p_value = stats.ttest_ind(exam1,exam2)

print("t_statitics: ",t_stat)
print("p_value: ",p_value)

if p_value < 0.05:
    print("the means are significantly different")
else:
    print("the means are not significantly different")