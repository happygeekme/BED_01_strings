# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_one + ' ' + str(goal_0) + ', ' + player_two + ' ' + str(goal_1)

report = f'{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute'
print(report)

player = "Ronald Koeman"
first_name = player[0:6]
'Ronald' in player

'Koeman' in player
last_name = player[7:13]
last_name_len = len(last_name)

first_character = player[0:1]
name_short = first_character + ". " + last_name

scream = first_name + '! '
times = len(first_name)
to_chant = scream * times
chant = to_chant[0:47]
length_chant = len(chant)
last_character = chant[length_chant - 1]
good_chant = last_character != " "


