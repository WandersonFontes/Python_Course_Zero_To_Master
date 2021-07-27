'''
i = 0
while i < 10:
    print('wanderson')
    i = i+1
print(i)

for item in [1,2,3]:
    print(item)
    pass
print(100*'+')
i = 0
while i < len([1,2,3]):
    i += 1
    break
print(i)
'''

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

i = 0
# for pic in picture:
#     while i < len(pic):
#         if pic[i] == 1:
#             print('*')
#         else:
#             print('')
#         i+=1
fill = '*'
empty = ''
for row in picture:
    for pix in row:
        if pix == 1:
            print(fill, end='')
        else:
            print(empty , end='')
    print('')