bill_thickness = 0.11 * 0.001
sears_height = 420
num_bills = 1
day = 1
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)

"""
if 条件1:
    情况1
elif 条件2:
    情况2
else~~ 条件3~~:
    情况3
"""