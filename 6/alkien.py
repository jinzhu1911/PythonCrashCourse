alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 先创建一个空字典
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
# 删除键-值对
del alien_1['points']
print(alien_1)