from datetime import datetime

now = datetime.now()
line = now.strftime("%Y-%m-%d %H:%M:%S (%A)")

print(line)

with open("datetime_log.txt", "a") as f:
    f.write(line + "\n")
