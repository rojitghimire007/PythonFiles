person = {"name": "Rojit", "Age":21, "isCute": True}
print(person["Age"])

'''for i in person.items():
	print(i)
'''

''' print("name" in person)
print("Rojit" in person.values())
person2 = person.copy().values()
print(person2)
'''



'''game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", 
"enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
initial_game_state = {}.fromkeys(game_properties,0)
print(initial_game_state)
print(initial_game_state.pop("high_score"))
'''

'''playlist = {
"title": "patagonia bus",
"author": "rojit Dai",
"songs": [
{"songname": "TUHIDASDE", "Singer": ["micky Singh"], "songLength": 3.33, "AddedTime": 2017},
{"songname": "TUHIE", "Singer": ["micky Sinsdsgh"], "songLength": 3.33, "AddedTime": 2019},
{"songname": "ASDE", "Singer": ["mingh"], "songLength": 3.33, "AddedTime": 2020}
]
}

totalLength = 0
for i in playlist["songs"]:
	 totalLength += i['songLength']
print(totalLength)
'''

'''person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {i[0]:i[1] for i in person}
print(answer)
'''

list1 = ["a","e","i","o","u"]
answer = {list1[i]:0 for i in range(0,5)}
print(answer)
