intervals = {
    'b': 4,
    'h': 2,
    'q': 1,
    'e': 0.5,
    's': 0.25,
    't': 0.125
}

line = raw_input().split(' ')
tempo = int(line[0])
number_pads = int(line[1])

tempo = (60*1000) / tempo
line = raw_input().split(' ')
while line[0] == '--':
    line = raw_input().split(' ')
for i in xrange(1, len(line)):
    if int(line[i]) > 0:
        print 'p{0} 1;'.format(i),
while True:
    try:
        line = raw_input().split(' ')
        while line[0] == '--':
            line = raw_input().split(' ')
        for i in xrange(1, len(line)):
            if int(line[i]) > 0:
                print 'p{0} 1;'.format(i),
        print '\n{0}'.format(tempo * intervals[line[0]]),
    except:
        print ''
        break
