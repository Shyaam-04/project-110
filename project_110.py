import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
#print(data)
pop_mean = statistics.mean(data)

pop_sd = statistics.stdev(data)

dataset = []
sample_data = []
for j in range(0,100):
    for i in range(0,30):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    sample_data.append(mean)

sample_data_mean = statistics.mean(sample_data)
sample_data_sd = statistics.stdev(sample_data)


print("population mean = "+str(pop_mean))
print("Sampling Mean = "+str(sample_data_mean))

fig = ff.create_distplot([sample_data],["Means of sample data"],show_hist = False)
fig.show()



