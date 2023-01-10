c_h = float(input())
r_h = float(input())
s_h = float(input())

total_cal = c_h * 200 + r_h * 475 + s_h * 275

pounds = total_cal // 3500
left_cal = total_cal% 3500

print("Total pound is", pounds, "and", round(left_cal, 2), "calories left")

