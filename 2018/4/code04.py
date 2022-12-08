import re

data = []
with open('data04.txt') as f:
    for line in f:
        date = re.search(r'\d{2}-\d{2}\s', line).group()
        time = re.search(r'\d{2}:\d{2}', line).group()
        action = re.search(r'begins|falls|wakes', line).group()
        if 'begins' in action:
            id = re.search(r'#\d+', line).group()[1:]
        else:
            id = '0'
        entry = {'date':date, 'time':time, 'id':id, 'action':action}
        data.append(entry)

#sort by time then date
data = sorted(data, key=lambda t: t['time'])
data = sorted(data, key=lambda t: t['date'])

#check if data is correct
prev_action = 'begins'
for entry in data:
    action = entry['action']
    time = entry['time']
    if action == 'wakes' and  time[:2] == '23':
        print('Something wrong ', entry)
    prev_action = action

# calculate time asleep for each guard
guards = []
guards_time_asleep = {}
for entry in data:
    if entry['action'] == 'begins':
        id = entry['id']
        guards.append(id)
    if entry['action'] == 'falls':
        start = int(entry['time'][3:5])
    if entry['action'] == 'wakes':
        end = int(entry['time'][3:5])
        duration = end-start
        try:
            guards_time_asleep[id] += duration
        except:
            guards_time_asleep[id] = duration
    
# find the most sleepy guard
max_time = 0
for guard in guards_time_asleep:
    time_asleep = guards_time_asleep[guard]
    if time_asleep > max_time:
        max_time = time_asleep
        sleepiest_guard = guard
print('Most sleepy guard is', sleepiest_guard, 'with', max_time, 'minutes')

# find the minute this guard has been most often asleep on
guards_minutes_count = {}
for guard_id in guards:
    guards_minutes_count[guard_id] = {}
    same_guard = False
    minutes = {}
    for entry in data:
        if entry['action'] == 'begins':
            if entry['id'] == guard_id:
                same_guard = True
            else:
                same_guard = False
        if entry['action'] == 'falls' and same_guard:
            start = int(entry['time'][3:5])
        if entry['action'] == 'wakes' and same_guard:
            end = int(entry['time'][3:5])
            for minute in range(start, end):
                try:
                    guards_minutes_count[guard_id][minute] += 1
                except:
                    guards_minutes_count[guard_id][minute] = 1

# make a dict containing key - guard, value[0] - minute, value[1] - count
most_freq_minutes = {}
for guard_id in guards:
    most_freq_minutes[guard_id] = [0, 0]
    max_minute = 0
    freq = 0
    for minute in guards_minutes_count[guard_id]:
        if guards_minutes_count[guard_id][minute] > freq:
            max_minute = minute
            freq = guards_minutes_count[guard_id][minute]
    most_freq_minutes[guard_id][0] = max_minute
    most_freq_minutes[guard_id][1] = freq 

# find the best minute and print the result
max_freq = 0
for guard in most_freq_minutes:
    if most_freq_minutes[guard][1] > max_freq:
        sleepiest_guard_2 = guard
        max_freq = most_freq_minutes[guard][1]
        best_minute = most_freq_minutes[guard][0]
print('Guard', sleepiest_guard_2, 'has been most often asleep at minute',
        best_minute)
print('Part 2:', int(sleepiest_guard_2)*best_minute)

# remainings from part 1
same_guard = False
minutes = {}
for entry in data:
    if entry['action'] == 'begins':
        if entry['id'] == sleepiest_guard:
            same_guard = True
        else:
            same_guard = False
    if entry['action'] == 'falls' and same_guard:
        start = int(entry['time'][3:5])
    if entry['action'] == 'wakes' and same_guard:
        end = int(entry['time'][3:5])
        for minute in range(start, end):
            try:
                minutes[minute] += 1
            except:
                minutes[minute] = 1

most_freq_times_asleep = 0
for minute in minutes:
    if minutes[minute] > most_freq_times_asleep:
        most_freq_minute = minute
        most_freq_times_asleep = minutes[minute]
print('The minute the guard has been most asleep at:', most_freq_minute)

print('Part 1:', most_freq_minute * int(sleepiest_guard))

# find which guard is the most frequently asleep on the same minute
