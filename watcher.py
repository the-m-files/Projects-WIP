import time

with open(r"Foundations\noaiprojects\Saved_time.txt", "r") as last_time:
    last_time = last_time.read()
    time_elapsed = (time.time() - float(last_time))

days = int(time_elapsed // 86400)
hours = int((time_elapsed % 86400) // 3600)
minutes = int((time_elapsed % 3600) // 60)
seconds = int(time_elapsed % 60)

print(f"it has been {days} days, {hours}:{minutes}:{seconds} since you last opened this file")

with open(r"Foundations\noaiprojects\Saved_time.txt", "w") as new_last_time:
    new_last_time.write(str(time.time()))
    print("Updated")

