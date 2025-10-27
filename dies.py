import random

#print('\u245cF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')
#┌ ─ ┐ │ └ ┘ 

'┌───────────┐'
'│           │'
'│           │'
'│           │'
'└───────────┘'
dice_art = {
    1: ('┌───────────┐',
        '│           │',
        '│     .     │',
        '│           │',
        '└───────────┘'    
    ),
    2: ('┌───────────┐',
        '│  .        │',
        '│           │',
        '│        .  │',
        '└───────────┘'    
    ),
    3: ('┌───────────┐',
        '│  .        │',
        '│     .     │',
        '│        .  │',
        '└───────────┘'    
    ),
    4: ('┌───────────┐',
        '│  .     .  │',
        '│           │',
        '│  .     .  │',
        '└───────────┘'    
    ),
    5: ('┌───────────┐',
        '│  .     .  │',
        '│     .     │',
        '│  .     .  │',
        '└───────────┘'    
    ),
    6: ('┌───────────┐',
        '│  .     .  │',
        '│  .     .  │',
        '│  .     .  │',
        '└───────────┘'    
    )   
}
dice = []
total = 0
dice_num = int(input('How many dice?: '))

for die in range(dice_num):
    dice.append(random.randint(1,6))

for die in range(dice_num):
    for line in dice_art.get(dice[die]):
        print(line)
      
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end='')
    print()
 
for die in dice:
    total += die
print(f'total: {total}')