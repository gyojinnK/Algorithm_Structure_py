def dailyTemperatures(temperatures):
    tem = temperatures
    res = [0] * len(tem)
    stack = []
    for i, t in enumerate(tem):
        while stack and t > tem[stack[-1]]:
            target = stack.pop()
            res[target] = i - target
        stack.append(i)

    return print(res)

dailyTemperatures([73,74,75,71,69,72,76,73])