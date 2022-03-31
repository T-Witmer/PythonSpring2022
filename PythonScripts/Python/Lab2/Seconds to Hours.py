# Troy Witmer
seconds = int(input('please type time in seconds: '))

hours = seconds // 3600
minutes = seconds % 3600 // 60
seconds2 = seconds % 60

print(seconds,'seconds =',hours,'hours', minutes,'minutes', seconds2, 'seconds')

