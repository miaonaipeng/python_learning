'''
    邀请人共进晚餐
'''
names = ['Amy', 'Jack', 'Tom', 'Laura']
for name in names:
    print("Would you have dinner with me, " + name + "?")
# Jack缺席，邀请Jenny
absent = 'Jack'
names.remove(absent)
print(absent+" will be absent!")
names.append("Jenny")
for name in names:
    print("Would you have dinner with me, " + name + "?\n")
# 找到一张更大的桌子，把嘉宾Kate添加到名单开头
print("I find a lager desk!\n")
names.insert(0, "Kate")
for name in names:
    print("Would you have dinner with me, " + name + "?")


