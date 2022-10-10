'''
Calculating Damage

Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.

Examples
damage(40, 5, "second") ➞ 200
damage(100, 1, "minute") ➞ 6000
damage(2, 100, "hour") ➞ 720000

Notes
Return "invalid" if damage or speed is negative.
'''

def damage(damage_cnt, speed, time):
    if damage_cnt < 0 or speed < 0:
        return "Invalid"
    else:
        if time == "second":
            return damage_cnt * speed
        elif time == "minute":
            return damage_cnt * speed * 60
        elif time == "hour":
            return damage_cnt * speed * 3600

print(damage(40, 5, "second"))
print(damage(100, 1, "minute"))
print(damage(2, 100, "hour"))


'''
Sample Code:

def damage(damage, speed, time):
    secs = {'second':1, 'minute':60, 'hour':3600}
    ans = damage*speed*secs[time]
    return ans if ans > 0 and speed > 0 else 'invalid'
'''