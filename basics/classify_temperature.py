"""
It should return:
"Freezing" when the temperature is 32°F or below
"Cold" from 33°F through 50°F
"Mild" from 51°F through 70°F
"Warm" from 71°F through 85°F
"Hot" above 85°F
Test it with 20, 32, 45, 70, 80, and 95.
"""

def classify_temperature(temp_f):
    if temp_f <= 32:
        return "Freezing"
    elif temp_f <= 50:
        return "Cold"
    elif temp_f <= 70:
        return "Mild"
    elif temp_f <= 85:
        return "Warm"
    else:
        return "Hot"
    
for temp in [20, 32, 45, 70, 80, 95]:
    print(temp, classify_temperature(temp))