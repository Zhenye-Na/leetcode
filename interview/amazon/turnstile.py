from collections import deque

def getTimes(numCustomers, arrTime, direction):

    entrance_queue = deque([])
    exit_queue = deque([])

    curr_time, last_state = 0, None


    for i in range(len(arrTime)):
        if direction[i] == 1:
            exit_queue.append([arrTime[i], i])
        else:
            entrance_queue.append([arrTime[i], i])


    res = [0 for _ in range(len(arrTime))]
    while len(entrance_queue) > 0 or len(exit_queue) > 0:
        if len(exit_queue) > 0 and exit_queue[0][0] <= curr_time and \
            (last_state is None or last_state == 1 or len(entrance_queue) == 0 or \
            (last_state == 0 and entrance_queue[0][0] > curr_time)):

            _, idx = exit_queue.popleft()
            res[idx] = curr_time
            last_state = 1

        elif len(entrance_queue) > 0 and entrance_queue[0][0] <= curr_time:

            _, idx = entrance_queue.popleft()
            res[idx] = curr_time
            last_state = 0

        else:
            last_state = None

        curr_time += 1
    

    print(res)
    return res


testcases = [
    [ [0,0,1,5], [0,1,1,0], [2,0,1,5] ],\
    [[1,2,4], [0,1,1], [1,2,4]],\
    [[1,1], [1,1], [1,2]], \
    [[1,1,3,3,4,5,6,7,7], [1,1,0,0,0,1,1,1,1], [1,2,3,4,5,6,7,8,9]] 
]

passedCounter = 0
for i, test in enumerate(testcases):
    time, direction, expected = test[0], test[1], test[2]
    result = getTimes(0, time, direction)
    if result == expected:
        passedCounter += 1
    else:
        print(" %d Test case failed " %(i+1))
        print("Expected: ", expected)
        print("Got: ", result)

print("%d/%d Test Cased Passed" %(passedCounter, len(testcases)))
