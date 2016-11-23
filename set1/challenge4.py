import helper
bestValue = 0
bestString = ""
with open("4.txt", "rb") as f:
    for line in f:
        result = helper.getMostProbableEnglishString(line.strip())
        if(result[1] > bestValue):
            bestValue = result[1]
            bestString = result[0]


print bestString.strip()
