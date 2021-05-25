import sys

dat_file = sys.argv[1]
with open(dat_file, 'r') as f:
    lines = f.readlines()
    # Skip header
    headers = lines[0].split(',')
    cols = len(headers)
    lines = lines[1:]
    sum_times = [0] * cols
    for line in lines:
        line = line.split(',')
        if (int(line[0]) < 2000):
            for i in range(cols):
                sum_times[i] += int(line[i])
        else: break
    print(list(zip(headers, sum_times)))
