ORIG = "A_PROD_LIST.txt"
MAURILIO = "MAURILIO.txt"

# check that everything in ORIG is in MAURILIO

maurilio_set = set()

with open(MAURILIO) as maurilio:
    for line in maurilio:
        maurilio_set.add(line.strip())

with open(ORIG) as orig:
    for line in orig:
        if line.strip() not in maurilio_set:
            print(line)

            
