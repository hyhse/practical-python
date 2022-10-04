# bounce.py
#
# Exercise 1.5

bounce = 1
height = 100
while bounce <= 10:
    height = height * 0.6
    print(bounce, round(height,4))
    bounce += 1