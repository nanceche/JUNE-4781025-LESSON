import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51, 72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47, 48,49,53,61,63,69,75,77,60,83"

data_list=(data.split(","))

data_lists= list(map(int,data_list))

print(min(data_lists))

print(max(data_lists))

sum_data_lists= (sum(data_lists))

average_data_lists= (round((sum_data_lists/len(data_lists)),2))

print(average_data_lists)

print(round(statistics.mean(data_lists),2))

print(round(statistics.median(data_lists)))

final_text= "The mean value is {mean_value}, the minimum value is {minimum_value}, the max value is {max_value}, the average values is {average_value} and the median value is{median_value}"
nancy_text=final_text.format(mean_value=53.18, minimum_value=14,max_value=100,average_value=53.18,median_value=50)
print(nancy_text)
