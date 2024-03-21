from datetime import datetime
print(datetime)

current_datetime = datetime.now()

print(current_datetime) # show the local time. and is more precises with the float at the miliseconds.

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #formats time layout.

