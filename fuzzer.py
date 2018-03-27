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
log_file = "log.txt"

FuzzFactor = 250
# num_tests = 10000
num_tests = 1
############# end configuration ######################

import math
import random
import string
import subprocess
import time

for i in range(num_tests):
    file_choice = random.choice(file_list)
    app = random.choice(apps)

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

    print(process)
    # open(log_file, 'w').write(process)
    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()

    print('\n!!!!!!!!!!!!!!!!TEST END ' + file_choice + ', ' + app + '!!!!!!!!!!!!!!!!!!!!!!\n')
