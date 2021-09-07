def minimum_waiting_time(queries_list):
    queries_list.sort()
    waiting_time=0
    for idx,duration in enumerate(queries_list):
        queries_let=(len(queries_list) -(idx+1))
        waiting_time += duration * queries_let
    return waiting_time

queries_list=[3,2,1,2,6]
print(minimum_waiting_time(queries_list))

