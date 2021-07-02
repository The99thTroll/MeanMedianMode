from collections import Counter
import dataFetcher, meanCalculator, medianCalculator, modeCalculator

data = dataFetcher.main()

mean = meanCalculator.calculate(data)
median = medianCalculator.calculate(data)
mode = modeCalculator.calculate(data)

print("The mean is " + str(mean))
print("The median is " + str(median))
print("The mode is " + str(mode))