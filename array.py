a = [[20, 18], [20, 19], [21, 18], [21, 19], [33, 15], [32, 16], [34, 16], [31, 17], [35, 17], [36, 17], [31, 18], [31, 19], [32, 20], [35, 18], [35, 19], [34, 20], [36, 20], [33, 21], [37, 18], [37, 19], [37, 20], [38, 18], [38, 19], [38, 21], [
    39, 19], [39, 21], [40, 20], [43, 17], [43, 18], [43, 22], [43, 23], [44, 17], [44, 19], [44, 21], [44, 23], [45, 18], [45, 19], [45, 20], [45, 21], [45, 22], [46, 19], [46, 20], [46, 21], [47, 20], [54, 20], [54, 21], [55, 20], [55, 21]]


result = map(lambda x: [x[0]+20, x[1]], a)
print(list(result))