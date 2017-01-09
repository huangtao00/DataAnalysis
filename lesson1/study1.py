import json,os,sys,random
import matplotlib.pyplot as plt
current_dir=os.path.abspath(".")

filename=[file  for file in os.listdir(current_dir) if ".txt" in file]
fn=filename[0] if len(filename)==1 else ""

if fn: # means we got a valid  filename
    fd=open(fn)
    content=[json.loads(line) for line in fd]
    
else:
    print("no txt file in current directory")
    sys.exit(1)


#deal with the timezone data in all dict data named as tz

#get tz data
allTZdata=[linedcit["tz"] for linedcit in content if "tz" in linedcit]
def get_fre(data):
    counts={}
    for tzd in data:
        if tzd in counts:
            counts[tzd]+=1
        else:
            counts[tzd]=1
    return counts
def getcircledata(datalist):
    key=[]
    value=[]
    for v,k in datalist:
        key.append(k)
        value.append(v)
    total=sum(value)
    vvalue=[]
    for v in value:
        vvalue.append(v/total)
    return key,vvalue



counts=get_fre(allTZdata) #we got the frequencies of different timezones,let us plot it right now

datalist=[]
for key ,value in counts.items():
    if key:
        datalist.append((value,key))
datalist.sort()
datalist=datalist[-10:]
print(datalist)

labels,sizes=getcircledata(datalist)

# The slices will be ordered and plotted counter-clockwise.
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
colors =[random.choice(colors)  for i in range(len(sizes))]

explode = tuple([0 for i in range(len(sizes))])  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()




