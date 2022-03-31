# Troy Witmer
weight = int(input('please type your weight (lb) '))
height = int(input('please type you height (in) '))
age = int(input('please type your age (years) '))

BMR_female = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
bars_female = round(BMR_female / 214, 2)

print(round(BMR_female, 2))

BMR_male = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
bars_male = round(BMR_male / 214, 2)

print(round(BMR_male, 2))

print('If you are female you need to eat ', bars_female, 'chocolate bars a day. '
'If you are male you need to eat ', bars_male, 'chocolate bars a day')

# 66 height
# 200 weight
# 25 age
# results, female 1770.8 8.03, male 1975.2 9.23