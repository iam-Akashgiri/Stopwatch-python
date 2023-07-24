import time
import os

t=int(input('Enter the time in sec: '))
print("="*70,"=>")
for i in range(t,0, -1):
    seconds= i % 60
    minutes= int(i / 60) % 60
    hours= int(i/3600) % 60
    print(f' {" "*80} {hours:02}:{minutes:02}:{seconds:02}')
    # os.system('cls')
    time.sleep(1)


print("Time's out...!")
print()
print()
