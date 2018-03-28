# 5-line fuzzer below is from Charlie Miller's 'Babysitting an Army of Monkeys'
# Part 1 = http://wwww.youtube.com/watch?v=Xnwodi2CBws
# Part 2 = http://wwww.youtube.com/watch?v=lK5fgCvS2N4


# List of files to use as initial seed

file_list = [
    "Cracking the Coding Interview (4th edition) .pdf",
    "Resume_Stromsland_Nest.pdf",
    "HowToBuildaCareerinTech.pdf",
    "Charlie_Miller_(security_researcher).pdf"
    ]

# List of applications to test

apps = [
    "../../../../../usr/bin/okular",
    "../../../../../usr/bin/atril"
    ]



fuzz_output = "fuzz.pdf"

FuzzFactor = 250
num_tests = 10000

############# end configuration ######################

import math
import random
import string
import subprocess
import time

log = []
count = 0

for i in range(num_tests):
    file_choice = random.choice(file_list)
    app = random.choice(apps)
    found = False
    index = 0
    for j in range(len(file_list)):
        if file_choice == file_list[j]:
            index = j
            break
    if len(log) > 0:
        for k in log:
            if k[0] == index:
                k[1] += 1
                if app == apps[0]:
                    k[2] += 1
                else:
                    k[3] += 1
                found = True
                break
            elif k[0] == index:
                k[1] += 1
                if app == apps[0]:
                    k[2] += 1
                else:
                    k[3] += 1
                found = True
                break
            elif k[0] == index:
                k[1] += 1
                if app == apps[0]:
                    k[2] += 1
                else:
                    k[3] += 1
                found = True
                break
            elif k[0] == index:
                k[1] += 1
                if app == apps[0]:
                    k[2] += 1
                else:
                    k[3] += 1
                found = True
                break
    if found == False or len(log) == 0:
        tmp = []
        if index == 0:
            tmp.append(0)
            tmp.append(1)
            if app == apps[0]:
                tmp.append(1)
                tmp.append(0)
            else:
                tmp.append(0)
                tmp.append(1)
        elif index == 1:
            tmp.append(1)
            tmp.append(1)
            if app == apps[0]:
                tmp.append(1)
                tmp.append(0)
            else:
                tmp.append(0)
                tmp.append(1)
        elif index == 2:
            tmp.append(2)
            tmp.append(1)
            if app == apps[0]:
                tmp.append(1)
                tmp.append(0)
            else:
                tmp.append(0)
                tmp.append(1)
        elif index == 3:
            tmp.append(3)
            tmp.append(1)
            if app == apps[0]:
                tmp.append(1)
                tmp.append(0)
            else:
                tmp.append(0)
                tmp.append(1)
        log.append(tmp)


    buf = bytearray(open(file_choice, 'rb').read())

    # start Charlie Miller code
    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1

    for i in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)

    # end Charlie Miller code

    open(fuzz_output, 'wb').write(buf)

    process = subprocess.Popen([app, fuzz_output])

    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()
    count += 1
    print('\n!!!!!!!!!!!!!!!!TEST ' + str(count) + ' END ' + file_choice + ', ' + app + '!!!!!!!!!!!!!!!!!!!!!!\n')

print('\n')

for i in range(len(log)):
    if log[i][0] == 0:
        print(file_list[0] + ' runs: ' + str(log[i][1]) + ', okular: ' + str(log[i][2]) + ', atril: ' + str(log[i][3]))
    if log[i][0] == 1:
        print(file_list[1] + ' runs: ' + str(log[i][1]) + ', okular: ' + str(log[i][2]) + ', atril: ' + str(log[i][3]))
    if log[i][0] == 2:
      print(file_list[2] + ' runs: ' + str(log[i][1]) + ', okular: ' + str(log[i][2]) + ', atril: ' + str(log[i][3]))
    if log[i][0] == 3:
        print(file_list[3] + ' runs: ' + str(log[i][1]) + ', okular: ' + str(log[i][2]) + ', atril: ' + str(log[i][3]))
