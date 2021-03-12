# Optimize Memory Usage / Amazon Prime Air Route

# https://aonecode.com/amazon-online-assessment-oa2-optimize-memory-usage


def optimizeMemoryUsage(foregroundTasks, backgroundTasks, K):
    """
    :type foregroundTasks: List[int]
    :type backgroundTasks: List[int]
    :type K: int
    :rtype: List[List[int]]
    """
    res = []
    curr_max = 0

    if len(foregroundTasks) == 0:
        for j in range(len(backgroundTasks)):
            add_result(backgroundTasks[j], K, curr_max, res, j, 1)


    if len(backgroundTasks) == 0:
        for i in range(len(foregroundTasks)):
            add_result(foregroundTasks[i], K, curr_max, res, i, 0)

    for i in range(len(foregroundTasks)):
        for j in range(len(backgroundTasks)):
            curr_usage = foregroundTasks[i] + backgroundTasks[j]
            if curr_usage > K:
                add_result(foregroundTasks[i], K, curr_max, res, i, 0)
                add_result(backgroundTasks[j], K, curr_max, res, j, 1)

            if curr_usage > curr_max and curr_usage <= K:
                res = [[i, j]]
                curr_max = curr_usage
            elif curr_usage == curr_max:
                res.append([i, j])
    
    return res if len(res) > 0 else [[-1, -1]]


def add_result(num, K, curr_max, res, idx, position):
    if num <= K:
        if num > curr_max:
            res = [[-1, idx]] if position == 1 else [[idx, -1]]
            curr_max = num
        elif num == curr_max:
            tmp = [-1, idx] if position == 1 else [idx, -1]
            if tmp not in res:
                res.append(tmp)

    
print(optimizeMemoryUsage([1],[], 0))