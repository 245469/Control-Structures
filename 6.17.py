time_24 = input("Enter time (24-hour format): ")
hour, minute = time_24.split(":")
hour = int(hour)

if hour == 0:
    hour_12 = 12
    print(f"Time in 12-hour format: {hour_12}:{minute}am")
elif hour < 12:
    hour_12 = hour
    print(f"Time in 12-hour format: {hour_12}:{minute}am")
elif hour == 12:
    hour_12 = 12
    print(f"Time in 12-hour format: {hour_12}:{minute}pm")
else:
    hour_12 = hour - 12
    print(f"Time in 12-hour format: {hour_12}:{minute}pm")