def current_beat():
    beat = [1,2,3,4]
    while True:
        for x in beat:
            yield x

    # position = 0
    # while True:
    #     if position < len(beat):
    #         yield beat[position]
    #         position +=1
    #     else:
    #         position = 0

my_beat = current_beat()
for x in range (25):
    i = next(my_beat)
    if i == 1 or i == 2:
        print("BOOM")
    elif i == 3:
        print("chaaa")
    else:
        print("kuh")




# def count_up_to(max):
# 	count = 1
# 	while count<max
# 		yield count
# 		count += 1
          
# print(count_up_to(10))