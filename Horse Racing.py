
# coding: utf-8

# In[2]:

print('Copy and paste pool data from TVG, starting with POOLS')
rawData = input()


# In[3]:


rawData1 = rawData.split('\t') #break up raw data into list, still need to separate $ and numbers


# In[4]:


rawData0 = rawData.replace('\t'," ") #remove tabs
rawData01 = rawData0.replace('$', "") #remove $
rawData02 = rawData01.replace(',', '') #remove , from dollar amounts
rawdata03 = rawData02.replace('\n1','')
rawdata04 = rawdata03.replace('\n',' ')
#print(rawdata04)

# In[5]:


rawListStr = rawdata04.split(' ')
#%%
if 'Pools' in rawListStr:
    rawListStr.remove('Pools')
if 'Win' in rawListStr:
    rawListStr.remove('Win')
if 'Place' in rawListStr:
    rawListStr.remove('Place')
if 'Show' in rawListStr:
    rawListStr.remove('Show')
if 'All' in rawListStr:
    rawListStr.remove('All')

#%%
raw = list(map(float, rawListStr))
#print(raw)

# In[6]:


totPools = raw[:3] #total pools for the race
#print(totPools)
noHorses=int(((len(raw)-2)/4)) #number of horses in race
horsePools = raw[3:] #pools for each horse
#print(horsePools)
#print(len(raw))

# In[7]:


#try creating dictionary
#h={}
#for x in range(1,(noHorses+1)):
    #st = x*4
    #fi = x*4+3
    #h["H{0}".format(x)]=raw[st:fi]


# In[8]:


#Create variables for each horse's pool
for x in range(1,(noHorses+1)):
    Wox = 0


# In[9]:


#find win odds using dictionary ABANDONED
#Wo = {} #dictionary of win odds
#for x in range(1,(noHorses+1)):
    #Wo[x] = horsePools[0]/h['H1'][0]
#print(Wo)


# In[10]:


#individual horse pools as list
horse = [raw[(4*i):4*i+3]for i in range(1,(noHorses+1))]
#print(horse)
#print(horse[0][0])


# In[11]:


#win place and show pools as lists
#for i in range(noHorses):
   # win1 = [horsePools[1+4*i]]
win = horsePools[0::4]
place = horsePools[1::4]
show = horsePools[2::4]


# In[12]:


# win place show odds
counter = 0

#for index in range(len(win)):
   # print (win[index])
win_odds = []
place_odds = []
show_odds = []
for index in win:
    if not index:
        win_odds.append(0)
    else:
        win_odds.append(1/(index / totPools[0]))
for index in place:
    if not index:
        place_odds.append(0)
    else:
        place_odds.append(1/(index / totPools[1]))
for index in show:
    if not index:
        show_odds.append(0)
    else:
        show_odds.append(1/(index / totPools[2]))


# In[32]:


print('Odds for each horse w/p/s')
for x in range(noHorses):
    print('Horse',x+1,[round(win_odds[x],2), round(place_odds[x],2),round(show_odds[x],2)])
#%%
#if the place odds are less than win, place is a good bet
place_diff = []
print(' ')
for x in range(noHorses):
    if (win_odds[x]-place_odds[x]) > 0:
        place_diff.append(win_odds[x]-place_odds[x])
    else:
        place_diff.append(0)
for x in range(noHorses):
    print('Horse',x+1, [round(place_diff[x],2)])