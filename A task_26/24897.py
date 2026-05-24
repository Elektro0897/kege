with open(r'./files/26_24897.txt') as file:
    n = int(file.readline())
    requests = [list(map(int, i.split())) for i in file]

requests = sorted(requests, key=lambda x: (x[1], x[2], x[0]))
house_num = 0
entrance_num = 0
max_entrances = 0
min_request = 10**10

cnt_entrances = 1
num_start_entrance = requests[0][2]
min_num_request_start_entrance = requests[0][1]

for req_1, req_2 in zip(requests, requests[1:]):
    if req_1[1] != req_2[1] or req_1[2] + 1 != req_2[2]:
        cnt_entrances = 1
        num_start_entrance = req_2[2]
        min_num_request_start_entrance = req_2[0]
        continue
    if req_1[2] == req_2[2]:
        if req_2[2] == num_start_entrance:
            min_num_request_start_entrance = min(min_num_request_start_entrance, req_2[0])
        continue
    if req_1[2] + 1 == req_2[2]:
        cnt_entrances += 1

    if (cnt_entrances > max_entrances or cnt_entrances == max_entrances and
            min_request > min_num_request_start_entrance):
        house_num= req_1[1]
        entrance_num = num_start_entrance
        min_request =min_num_request_start_entrance
        max_entrances = cnt_entrances

print(house_num, entrance_num)