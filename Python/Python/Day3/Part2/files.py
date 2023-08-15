read_cars = open("Python/Day3/Part2/car_sales.csv", "r")

read_file = read_cars.readlines()
print(read_file)
companies = [] 
sales = []

# to_list=read_file.
for x in read_file:
    my_lists=x.split(",")
    print(my_lists)
#     if x == "Jan" or "Feb":
#         companies.append(x)
#         print (companies)
