#dicrete random variable example
student_scores = [10,20,30,40,50]
print("total students")
print(len(student_scores))
#continous random variable example
#heights of students in a centimeters
heights = [150.5, 160.2, 170.8, 180.1, 190.7]
print("Student Heights:")
print(heights)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#set the probability of sucess for the Bernolli distribution
p=0.3
#probability of succes(1)
#generate Bernolli data
data=np.random.binomial(1,p,1000)
sns.histplot(data,stat="density",discrete=True)
plt.title("Bernoulli Distribution(p={p})")
plt.xlabel("Outcome(0=failure,1=success)")
plt.ylabel("Density")
plt.xticks([0,1])
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#set the probability of success for the Bernoulli distribution
n=10
p=0.5
data=np.random.binomial(n,p,1000)
sns.histplot(data,kde=True,stat="density",bins=n+1)
plt.title("Binomial Distribution(n={n},p={p})")
plt.xlabel("Number of Successes")
plt.ylabel("Density")   
plt.show()