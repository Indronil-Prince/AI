CLASS, time, classtest = list(map(float, input("Enter the value of classes, times, classtests: ").split(" ")))

fclass = [0, 0, 0.20, 0.30]
aclass = [0.20, 0.30, 0.45, 0.55]
hclass = [0.45, 0.55, 0.70, 0.80]
vhclass = [0.70, 0.80, 1, 1]

ltime = [0,0, 0.20, 0.40]
atime = [0.20, 0.40, 0.60, 0.80]
latime = [0.60, 0.80, 1, 1]

vlctest = [0,0,0.15,0.25]
lctest = [0.15, 0.25, 0.35, 0.45]
acltest = [0.35, 0.45, 0.55, 0.65]
hctest = [0.55, 0.65, 0.75, 0.85]
vhctest = [0.75, 0.85,1,1]

val_class = []
val_time = []
val_ctest = []

def calculate_class_val(x):
    if x > fclass[3]:
        val_class.append(0)
    elif x < fclass[0]:
        val_class.append(0)
    elif x>=fclass[0] and x<=fclass[1]:
        temp = (x-fclass[0])/(fclass[1]-fclass[0])
        val_class.append(temp)
    elif x>=fclass[1] and x<=fclass[2]:
        val_class.append(1)
    elif x>=fclass[2] and x<=fclass[3]:
        temp = (fclass[3]-x)/(fclass[3]-fclass[2])
        val_class.append(temp)

    if x > aclass[3]:
        val_class.append(0)
    elif x < aclass[0]:
        val_class.append(0)
    elif x>=aclass[0] and x<=aclass[1]:
        temp = (x-aclass[0])/(aclass[1]-aclass[0])
        val_class.append(temp)
    elif x>=aclass[1] and x<=aclass[2]:
        val_class.append(1)
    elif x>=aclass[2] and x<=aclass[3]:
        temp = (aclass[3]-x)/(aclass[3]-aclass[2])
        val_class.append(temp)

    if x > hclass[3]:
        val_class.append(0)
    elif x < hclass[0]:
        val_class.append(0)
    elif x>=hclass[0] and x<=hclass[1]:
        temp = (x-hclass[0])/(hclass[1]-hclass[0])
        val_class.append(temp)
    elif x>=hclass[1] and x<=hclass[2]:
        val_class.append(1)
    elif x>=hclass[2] and x<=hclass[3]:
        temp = (hclass[3]-x)/(hclass[3]-hclass[2])
        val_class.append(temp)

    if x > vhclass[3]:
        val_class.append(0)
    elif x < vhclass[0]:
        val_class.append(0)
    elif x>=vhclass[0] and x<=vhclass[1]:
        temp = (x-vhclass[0])/(vhclass[1]-vhclass[0])
        val_class.append(temp)
    elif x>=vhclass[1] and x<=vhclass[2]:
        val_class.append(1)
    elif x>=vhclass[2] and x<=vhclass[3]:
        temp = (vhclass[3]-x)/(vhclass[3]-vhclass[2])
        val_class.append(temp)


def calculate_time_val(x):
    if x > ltime[3]:
        val_time.append(0)
    elif x < ltime[0]:
        val_time.append(0)
    elif x >= ltime[0] and x <= ltime[1]:
        temp = (x - ltime[0]) / (ltime[1] - ltime[0])
        val_time.append(temp)
    elif x >= ltime[1] and x <= ltime[2]:
        val_time.append(1)
    elif x >= ltime[2] and x <= ltime[3]:
        temp = (ltime[3] - x) / (ltime[3] - ltime[2])
        val_time.append(temp)

    if x > atime[3]:
        val_time.append(0)
    elif x < atime[0]:
        val_time.append(0)
    elif x >= atime[0] and x <= atime[1]:
        temp = (x - atime[0]) / (atime[1] - atime[0])
        val_time.append(temp)
    elif x >= atime[1] and x <= atime[2]:
        val_time.append(1)
    elif x >= atime[2] and x <= atime[3]:
        temp = (atime[3] - x) / (atime[3] - atime[2])
        val_time.append(temp)

    if x > latime[3]:
        val_time.append(0)
    elif x < latime[0]:
        val_time.append(0)
    elif x >= latime[0] and x <= latime[1]:
        temp = (x - latime[0]) / (latime[1] - latime[0])
        val_time.append(temp)
    elif x >= latime[1] and x <= latime[2]:
        val_time.append(1)
    elif x >= latime[2] and x <= latime[3]:
        temp = (latime[3] - x) / (latime[3] - latime[2])
        val_time.append(temp)


def calculate_classtest_val(x):
    if x > vlctest[3]:
        val_ctest.append(0)
    elif x < vlctest[0]:
        val_ctest.append(0)
    elif x >= vlctest[0] and x <= vlctest[1]:
        temp = (x - vlctest[0]) / (vlctest[1] - vlctest[0])
        val_ctest.append(temp)
    elif x >= vlctest[1] and x <= vlctest[2]:
        val_ctest.append(1)
    elif x >= vlctest[2] and x <= vlctest[3]:
        temp = (vlctest[3] - x) / (vlctest[3] - vlctest[2])
        val_ctest.append(temp)

    if x > lctest[3]:
        val_ctest.append(0)
    elif x < lctest[0]:
        val_ctest.append(0)
    elif x >= lctest[0] and x <= lctest[1]:
        temp = (x - lctest[0]) / (lctest[1] - lctest[0])
        val_ctest.append(temp)
    elif x >= lctest[1] and x <= lctest[2]:
        val_ctest.append(1)
    elif x >= lctest[2] and x <= lctest[3]:
        temp = (lctest[3] - x) / (lctest[3] - lctest[2])
        val_ctest.append(temp)

    if x > acltest[3]:
        val_ctest.append(0)
    elif x < acltest[0]:
        val_ctest.append(0)
    elif x >= acltest[0] and x <= acltest[1]:
        temp = (x - acltest[0]) / (acltest[1] - acltest[0])
        val_ctest.append(temp)
    elif x >= acltest[1] and x <= acltest[2]:
        val_ctest.append(1)
    elif x >= acltest[2] and x <= acltest[3]:
        temp = (acltest[3] - x) / (acltest[3] - acltest[2])
        val_ctest.append(temp)

    if x > hctest[3]:
        val_ctest.append(0)
    elif x < hctest[0]:
        val_ctest.append(0)
    elif x >= hctest[0] and x <= hctest[1]:
        temp = (x - hctest[0]) / (hctest[1] - hctest[0])
        val_ctest.append(temp)
    elif x >= hctest[1] and x <= hctest[2]:
        val_ctest.append(1)
    elif x >= hctest[2] and x <= hctest[3]:
        temp = (hctest[3] - x) / (hctest[3] - hctest[2])
        val_ctest.append(temp)

    if x > vhctest[3]:
        val_ctest.append(0)
    elif x < vhctest[0]:
        val_ctest.append(0)
    elif x >= vhctest[0] and x <= vhctest[1]:
        temp = (x - vhctest[0]) / (vhctest[1] - vhctest[0])
        val_ctest.append(temp)
    elif x >= vhctest[1] and x <= vhctest[2]:
        val_ctest.append(1)
    elif x >= vhctest[2] and x <= vhctest[3]:
        temp = (vhctest[3] - x) / (vhctest[3] - vhctest[2])
        val_ctest.append(temp)


calculate_class_val(CLASS)
calculate_time_val(time)
calculate_classtest_val(classtest)

vl = []
l = []
a = []
h = []
vh = []

vl.append(min(val_class[0],min(val_time[0],val_ctest[0])))
vl.append(min(val_class[0],min(val_time[0],val_ctest[1])))
vl.append(min(val_class[0],min(val_time[0],val_ctest[2])))
l.append(min(val_class[0],min(val_time[0],val_ctest[3])))
l.append(min(val_class[0],min(val_time[0],val_ctest[4])))
vl.append(min(val_class[0],min(val_time[1],val_ctest[0])))
vl.append(min(val_class[0],min(val_time[1],val_ctest[1])))
l.append(min(val_class[0],min(val_time[1],val_ctest[2])))
a.append(min(val_class[0],min(val_time[1],val_ctest[3])))
h.append(min(val_class[0],min(val_time[1],val_ctest[4])))
vl.append(min(val_class[0],min(val_time[2],val_ctest[0])))
vl.append(min(val_class[0],min(val_time[2],val_ctest[1])))
l.append(min(val_class[0],min(val_time[2],val_ctest[2])))
a.append(min(val_class[0],min(val_time[2],val_ctest[3])))
h.append(min(val_class[0],min(val_time[2],val_ctest[4])))


vl.append(min(val_class[1],min(val_time[0],val_ctest[0])))
vl.append(min(val_class[1],min(val_time[0],val_ctest[1])))
l.append(min(val_class[1],min(val_time[0],val_ctest[2])))
a.append(min(val_class[1],min(val_time[0],val_ctest[3])))
h.append(min(val_class[1],min(val_time[0],val_ctest[4])))
vl.append(min(val_class[1],min(val_time[1],val_ctest[0])))
vl.append(min(val_class[1],min(val_time[1],val_ctest[1])))
l.append(min(val_class[1],min(val_time[1],val_ctest[2])))
a.append(min(val_class[1],min(val_time[1],val_ctest[3])))
h.append(min(val_class[1],min(val_time[1],val_ctest[4])))
vl.append(min(val_class[1],min(val_time[2],val_ctest[0])))
vl.append(min(val_class[1],min(val_time[2],val_ctest[1])))
l.append(min(val_class[1],min(val_time[2],val_ctest[2])))
a.append(min(val_class[1],min(val_time[2],val_ctest[3])))
h.append(min(val_class[1],min(val_time[2],val_ctest[4])))


vl.append(min(val_class[2],min(val_time[0],val_ctest[0])))
l.append(min(val_class[2],min(val_time[0],val_ctest[1])))
a.append(min(val_class[2],min(val_time[0],val_ctest[2])))
h.append(min(val_class[2],min(val_time[0],val_ctest[3])))
vh.append(min(val_class[2],min(val_time[0],val_ctest[4])))
vl.append(min(val_class[2],min(val_time[1],val_ctest[0])))
l.append(min(val_class[2],min(val_time[1],val_ctest[1])))
a.append(min(val_class[2],min(val_time[1],val_ctest[2])))
h.append(min(val_class[2],min(val_time[1],val_ctest[3])))
vh.append(min(val_class[2],min(val_time[1],val_ctest[4])))
vl.append(min(val_class[2],min(val_time[2],val_ctest[0])))
l.append(min(val_class[2],min(val_time[2],val_ctest[1])))
a.append(min(val_class[2],min(val_time[2],val_ctest[2])))
h.append(min(val_class[2],min(val_time[2],val_ctest[3])))
vh.append(min(val_class[2],min(val_time[2],val_ctest[4])))


l.append(min(val_class[3],min(val_time[0],val_ctest[0])))
a.append(min(val_class[3],min(val_time[0],val_ctest[1])))
h.append(min(val_class[3],min(val_time[0],val_ctest[2])))
h.append(min(val_class[3],min(val_time[0],val_ctest[3])))
vh.append(min(val_class[3],min(val_time[0],val_ctest[4])))
l.append(min(val_class[3],min(val_time[1],val_ctest[0])))
a.append(min(val_class[3],min(val_time[1],val_ctest[1])))
h.append(min(val_class[3],min(val_time[1],val_ctest[2])))
h.append(min(val_class[3],min(val_time[1],val_ctest[3])))
vh.append(min(val_class[3],min(val_time[1],val_ctest[4])))
l.append(min(val_class[3],min(val_time[2],val_ctest[0])))
a.append(min(val_class[3],min(val_time[2],val_ctest[1])))
h.append(min(val_class[3],min(val_time[2],val_ctest[2])))
vh.append(min(val_class[3],min(val_time[2],val_ctest[3])))
vh.append(min(val_class[3],min(val_time[2],val_ctest[4])))


max_vl = max(vl)
max_l = max(l)
max_a = max(a)
max_h = max(h)
max_vh = max(vh)

cog = max_vl*(0.0+0.05+0.1+0.15+0.2)
cog+= max_l*(0.25+0.3+0.35+0.4)
cog+= max_a*(0.45+0.5+0.55+0.6)
cog+= max_h*(0.65+0.70+0.75+0.8)
cog+= max_vh*(0.85+0.9+0.95+1)

cog/= ((max_vl*5)+(max_l*4)+(max_a*4)+(max_h*4)+(max_vh*4))
print(cog)


