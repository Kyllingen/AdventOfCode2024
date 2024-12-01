import pandas

test_file = pandas.read_table("input.txt", sep="\s+", header=None, names=["1", "2"])

#sort and then find range between two values
sorted_file = test_file.apply(lambda x: x.sort_values().values)
sorted_file["diff"] = abs(sorted_file["1"] - sorted_file["2"])
total = sorted_file["diff"].sum()
print(total)

#find similarity score between left and right column
sum = 0
for item in sorted_file["1"]:
    count = len(sorted_file[sorted_file["2"] == item])
    sum += count * item

print(sum)