# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

''' Hallo David, wat super fijn dat jullie de opdrachten ook nakijken. Bij FED gaat dat anders.
Ik vond het al zo'n gekke opdracht, maar nu het generiek is vind ik hem een stuk logischer.
Bedankt voor je tijd en uitleg, ik begrijp het nu beter. Hopelijk is het nu wel goed.
Groetjes, Jitske'''

player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_one + ' ' + str(goal_0) + ', ' + player_two + ' ' + str(goal_1)

report = f'{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute'
print(report)

player = "Ronald Koeman"
index_space = player.find(" ")
first_name = player[:index_space]
last_name = player[(index_space + 1):len(player)]
last_name_len = len(last_name)
name_short = player[0:1] + ". " + last_name
chant = ((first_name + "! ") * len(first_name))[:-1]
good_chant = chant[-1] != " "

