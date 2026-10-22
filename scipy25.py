import numpy as np
import pandas as pd
from scipy import stats

data = {
    "age": [22, 25, 28, 30, 32, 35, 38, 40, 42, 45],
    "salary": [20000, 25000, 28000, 32000, 35000,
               40000, 45000, 48000, 52000, 58000],
    "experience": [1, 2, 4, 5, 7, 9, 11, 13, 15, 18],
    "performance": [60, 65, 68, 72, 75, 78, 82, 85, 88, 92]
}

df = pd.DataFrame(data)

print("employee data")
print(df)


print("\ncorrelation matrix")
print(df.corr().round(3))

r,p = stats.pearsonr(df["experience"],df["salary"])

print("\nexperience vs salary: ")
print("correlation: ",round(r,3))

print("p-vlaue: ",p)

if p < 0.05:
    print("the relationship is statistically significant")
else: 
    print("the relationship is not statistically significant")

r2,p2 = stats.pearsonr(df["experience"],df["performance"])
print("\nexperience vs performance: ")

print("correlation: ",round(r2,3))
print("p-value: ",p2)

low_exp = df[df["experience"] <= 5]["performance"]
high_exp = df[df["experience"] > 5]["performance"]

t_stat,t_p = stats.ttest_ind(high_exp,low_exp)
print("\nttest: performance")

print("t-statistic: ",round(t_stat,3))
print("p-value: ",t_p)

slope,intercept,r_value,p_value,std_err = stats.linregress(
    df["experience"],df["salary"]
)
print("\nlinear regression: ")
print("slope: ",round(slope,2))
print("intercept: ",round(intercept,2))
print("r-squared: ",round(r_value ** 2,3))
print("p-value: ",p_value)



years = 10
predicted_salary = intercept + slope * years


print("predicted salary for 10 years experience: ",
      round(predicted_salary,2))

print("\nCONCLUSIONS")

if r > 0 and p < 0.05:
    print("- Experience and salary have a significant positive relationship.")

if r2 > 0 and p2 < 0.05:
    print("- Experience and performance have a significant positive relationship.")

if t_p < 0.05:
    print("- Performance differs significantly between the experience groups.")
else:
    print("- No statistically significant performance difference was found.")

if p_value < 0.05:
    print("- Experience is a statistically significant predictor of salary.")
else:
    print("- Experience is not a statistically significant predictor of salary.")
