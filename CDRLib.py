import collections
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure


from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    pass

from collections import Counter


def readCSV(name):
    with open(name,"r") as f:
        read = csv.reader(f)
        myList = [i for i in read]
        myList.remove(myList[0])
    return myList


class call:

    def __init__(self,id_pk,start_time,end_time,duration,cid,caller,callee,callee_country,callee_prefix_level,is_forwarded,disposition,ring_time,answer_time,error_code,p_crt,p_dlm,p_ras,trunk_id,call_dir,src_ip,src_port,dest_ip,dest_port,caller_indicator_id,callee_indicator_id,caller_group_id,callee_group_id,diverted_from,call_state):

        self.id_pk = id_pk
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.cid = cid
        self.caller = caller
        self.callee = callee
        self.callee_country = callee_country
        self.callee_prefix_level = callee_prefix_level
        self.is_forwarded = is_forwarded
        self.disposition = disposition
        self.ring_time = ring_time
        self.answer_time = answer_time
        self.error_code = error_code
        self.p_crt = p_crt
        self.p_dlm = p_dlm
        self.p_ras = p_ras
        self.trunk_id = trunk_id
        self.call_dir = call_dir
        self.src_ip = src_ip
        self.src_port = src_port
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.caller_indicator_id = caller_indicator_id
        self.callee_indicator_id = callee_indicator_id
        self.caller_group_id = caller_group_id
        self.callee_group_id = callee_group_id
        self.diverted_from = diverted_from
        self.call_state = call_state
        
        
        

    def getid_pk(self):
        return self.id_pk
    def getstart_time(self):
        return self.start_time
    def getend_time(self):
        return self.end_time
    def getduration(self):
        return self.duration
    def getcid(self):
        return self.cid
    def getcaller(self):
        return self.caller
    def getcallee(self):
        return self.callee
    def getcallee_country(self):
        return self.callee_country
    def getcallee_prefix_level(self):
        return self.callee_prefix_level
    def getis_forwarded(self):
        return self.is_forwarded
    def getdisposition(self):
        return self.disposition
    def getring_time(self):
        return self.ring_time
    def getanswer_time(self):
        return str(self.answer_time)[11:13]
    def geterror_code(self):
        return self.error_code
    def getp_crt(self):
        return self.p_crt
    def getp_dlm(self):
        return self.p_dlm
    def getp_ras(self):
        return self.p_ras
    def gettrunk_id(self):
        return self.trunk_id
    def getcall_dir(self):
        return self.call_dir
    def getsrc_ip(self):
        return self.src_ip
    def getsrc_port(self):
        return self.src_port
    def getdest_ip(self):
        return self.dest_ip
    def getdest_port(self):
        return self.dest_port
    def getcaller_indicator_id(self):
        return self.caller_indicator_id
    def getcallee_indicator_id(self):
        return self.callee_indicator_id
    def getcaller_group_id(self):
        return self.caller_group_id
    def getcallee_group_id(self):
        return self.callee_group_id
    def getdiverted_from(self):
        return self.diverted_from
    def getcall_state(self):
        return self.call_state
    
    def getTIMEZONE(self):
        if 6<=int(str(self.answer_time)[11:13])<15:
            return 'Day'
        elif 15<=int(str(self.answer_time)[11:13])<23:
            return 'Evening'
        else:
            return 'Night'  
             
        
        
#############################################


def makecall(a):
    return call(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26],a[27],a[28])



def disposition(alist):
    errorcounter,NAcounter,cancelcounter,byecounter,releaseErrcounter,total = 0, 0, 0, 0, 0, 0
    for i in alist:
        total +=1
        if i.getdisposition()== 'ERROR' :
            errorcounter += 1
        elif i.getdisposition()== 'NA' :
            NAcounter += 1
        elif i.getdisposition()== 'BYE' :
            byecounter += 1
        elif i.getdisposition()== 'CANCEL' :
            cancelcounter += 1
        else:
            releaseErrcounter +=1
            
            
            
    print("The amount of error  are {}.".format(errorcounter))
    print("The amount of NA  are {}.".format(NAcounter))
    print("The amount of BYE  are {}.".format(byecounter))
    print("The amount of cancel  are {}.".format(cancelcounter))
    print("The amount of realese errors  are {}.".format(releaseErrcounter))


    print("Total calls are {}.".format(total))
  
    
    labels = 'ERROR', 'NA', 'BYE', 'CANCEL', 'Realese Error'
    sizes  = [errorcounter,NAcounter,byecounter,cancelcounter,releaseErrcounter]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'red','yellow']
    explode = (0.1, 0.1, 0.1, 0.1, 0.1)
        
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()


def ERRbyzone(alist):
    
   
    print("This is ERROR analysis by TIMEZONE")
    DayERR,EveningERR,NightERR,total = 0,0,0,0
    for i in alist:
        total +=1
        if i.getdisposition()== 'ERROR' :
            if i.getTIMEZONE() == "Day":
                DayERR += 1
            elif i.getTIMEZONE() == "Evening":
                EveningERR += 1
            else:
                NightERR += 1

    
    L1 = "Time_zone  Counts  Rate"
    L2 = "{2:^9}  {0:^6}  {1:^4.1%}".format(DayERR,DayERR/total,"Day")
    L3 = "{2:^9}  {0:^6}  {1:^4.1%}".format(EveningERR,EveningERR/total,"Evening")
    L4 = "{2:^9}  {0:^6}  {1:^4.1%}".format(NightERR,NightERR/ total,"Night")
    table = [L1,L2,L3,L4]
   
    for i in table:
            print(i)
            
def call_by_time(data):
    daycall,eveningcall,nightcall = 0,0,0
    for i in data:
        if i.getTIMEZONE() == 'Day':
            daycall += 1
        elif i.getTIMEZONE() == 'Evening':
            eveningcall += 1
        else:
            nightcall += 1
    print('Call times')
    print('There are {} day time calls'.format(daycall))
    print('There are {} evening time calls'.format(eveningcall))
    print('There are {} night time calls'.format(nightcall))
    print('********************')

    
    labels = 'Day', 'Evening', 'Night'
    sizes = [daycall,eveningcall,nightcall]
    colors = ['yellowgreen', 'gold', 'lightskyblue']
    explode = (0.1, 0.1, 0.1) 

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
    
def call_by_day(data):    
    MONtotalCALLTIME=0
    TUEtotalCALLTIME=0
    WEDtotalCALLTIME=0
    THUtotalCALLTIME=0
    FRItotalCALLTIME=0
    SATtotalCALLTIME=0
    SUNtotalCALLTIME=0

    for i in data:

       
        if i.getstart_time()[8:10] == '18':
          TUEtotalCALLTIME += 1
        elif i.getstart_time()[8:10] == '19' :
          WEDtotalCALLTIME += 1
        elif i.getstart_time()[8:10] == '20':
          THUtotalCALLTIME += 1
        elif i.getstart_time()[8:10] == '21':
          FRItotalCALLTIME += 1
        elif i.getstart_time()[8:10] == '22':
          SATtotalCALLTIME += 1
        elif i.getstart_time()[8:10] == '23':
          SUNtotalCALLTIME += 1
        elif i.getstart_time()[8:10] == '24' or '17' :
          MONtotalCALLTIME += 1  
      
    print("Calls by day")
    print('MON time {}'.format(MONtotalCALLTIME))
    print('TUE time {}'.format(TUEtotalCALLTIME))
    print('WED time {}'.format(WEDtotalCALLTIME))
    print('THU time {}'.format(THUtotalCALLTIME))
    print('FRI time {}'.format(FRItotalCALLTIME))
    print('SAT time {}'.format(SATtotalCALLTIME))
    print('SUN time {}'.format(SUNtotalCALLTIME))

    labels = 'Mon', 'TUE','WED','THU','FRI','SAT','SUN'
    sizes = [MONtotalCALLTIME,TUEtotalCALLTIME,WEDtotalCALLTIME,THUtotalCALLTIME,FRItotalCALLTIME,SATtotalCALLTIME,SUNtotalCALLTIME]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue','green']
    explode = (0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1)  
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    plt.show()

def total_call_duration(data):
    groupOne,groupTwo,groupThree,groupFour, groupFive = 0,0,0,0,0
    for i in data:
        if 0 <= float(i.getduration()) <1:
            groupOne +=1
        elif 1 <= float(i.getduration()) <10:
            groupTwo +=1
        elif 10 <= float(i.getduration()) <30:
            groupThree += 1
        elif 30 <= float(i.getduration()) <60:
            groupFour +=1
        else:
            groupFive +=1
            
    print('There are {} calls which lasted less than 1 seconds'.format(groupOne))
    print('There are {} calls which lasted between 1-10 seconds'.format(groupTwo))
    print('There are {} calls which lasted between 10-30 seconds'.format(groupThree))
    print('There are {} calls which lasted between 30-60 seconds'.format(groupFour))
    print('There are {} calls which lasted more than 60 seconds'.format(groupFive))
        
    
    types = ["less than one second", "1-10 seconds", "10-30 seconds", "more than 30 seconds"]
    durations = [groupOne, groupTwo, groupThree, groupFour]
   
    plt.plot(types, durations, color='g')
    plt.xlabel('types')
    plt.ylabel('durations')
    plt.title('Call durations in seconds')
    plt.show()
   
def errcode(data):
     code200,code486,code503,code480,code484,total,code404,code408,code487,code504,code603,code604,code0  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
     for i in data:
            total +=1
            if i.geterror_code()== '200' :
                code200 += 1
            elif i.geterror_code()== '486' :
                code486 += 1
            elif i.geterror_code()== '503' :
                code503 += 1
            elif i.geterror_code()== '480' :
                code480 += 1
            elif i.geterror_code()== '484' :
                code484 += 1  
            elif i.geterror_code()== '404' :
                code404 += 1 
            elif i.geterror_code()== '408' :
                code408 += 1
            elif i.geterror_code()== '487' :
                code487 += 1
            elif i.geterror_code()== '504' :
                code504 += 1 
            elif i.geterror_code()== '603' :
                code603 += 1
            elif i.geterror_code()== '604' :
                code604 += 1               
            elif i.geterror_code()== '0' :
                code0 += 1 

     
     A = ["code200","code486","code503","code480","code484","code404","code408","code487","code504","code603","code604","code0"]
     B = [code200,code486,code503,code480,code484,code404,code408,code487,code504,code603,code604,code0]

     plt.plot(A, B, color='g')
   

     plt.xticks(rotation=90)   
     plt.ylabel('amounts')
     plt.xlabel('errorcodes')
     plt.title('Amounts of different error codes')
     plt.show()



#####
def callmonth(data):
    jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec=0,0,0,0,0,0,0,0,0,0,0,0
    
    for i in data:

        if i.getstart_time()[5:7] == '01' :
          jan +=1
        elif i.getstart_time()[5:7] == '02' :
          feb +=1
        elif i.getstart_time()[5:7] == '03' :
          mar +=1
        elif i.getstart_time()[5:7] == '04' :
          apr +=1
        elif i.getstart_time()[5:7] == '05' :
          may +=1
        elif i.getstart_time()[5:7] == '06' :
          jun +=1
        elif i.getstart_time()[5:7] == '07' :
          jul +=1
        elif i.getstart_time()[5:7] == '08' :
          aug +=1
        elif i.getstart_time()[5:7] == '09' :
          sep +=1
        elif i.getstart_time()[5:7] == '10' :
          octo +=1
        elif i.getstart_time()[5:7] == '11' :
          nov +=1
        elif i.getstart_time()[5:7] == '12' :
          dec +=1
          
    print("Call months")      
    print('January: {}'.format(jan))
    print('February: {}'.format(feb))
    print('March: {}'.format(mar))
    print('April: {}'.format(apr))
    print('May: {}'.format(may))
    print('June: {}'.format(jun))
    print('July: {}'.format(jul))
    print('August: {}'.format(aug))
    print('September: {}'.format(sep))
    print('October: {}'.format(octo))
    print('November: {}'.format(nov))  
    print('December: {}'.format(dec))

    

def callcountry(data):
         dom,inter = 0,0 
         for i in data:
             if i.getcallee_country() == 'DOMESTIC':
                 dom +=1
             else:
                 inter +=1
    
         print('Number of domestic calls {}'.format(dom))
         print('Number of international calls {}'.format(inter))
         
         
         labels = 'Domestic', 'International'
         sizes  = [dom,inter]
         colors = ['yellowgreen', 'gold']
         explode = (0.1, 0.1)
            
         plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
         plt.axis('equal')
         plt.show()
         
##

def country(data):
    N = []
    y = []
    z = []
    
   
    for i in data:
          N.append(i.getcallee_country())
        

    
    A = collections.Counter(N)
 

    for key, value in A.items():
        print("Number of calls to " + key, value)
        y.append(key)
        z.append(value)
        
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xticks(rotation=90)    
    plt.bar(y,z)
    plt.show()

def dispositionsInAday(data):
    DayERRcode,EveningERRcode,NightERRcode,total = 0,0,0,0
    DayNAcode,EveningNAcode,NightNAcode, total1 = 0,0,0,0
    DayBYEcode,EveningBYEcode,NightBYEcode, total2= 0,0,0,0
    DayCANCELcode,EveningCANCELcode,NightCANCELcode, total3= 0,0,0,0
    DayRBYEcode,EveningRBYEcode,NightRBYEcode,total4 = 0,0,0,0
    for i in data:
        
        if i.getdisposition()== 'ERROR' :
            total +=1
            if i.getTIMEZONE() == "Day":
                DayERRcode += 1
            elif i.getTIMEZONE() == "Evening":
                EveningERRcode += 1
            else:
                NightERRcode += 1
                
        elif i.getdisposition()== 'NA' :
            total1 +=1
            if i.getTIMEZONE() == "Day":
                DayNAcode += 1
            elif i.getTIMEZONE() == "Evening":
                EveningNAcode += 1
            else:
                NightNAcode += 1
                
        elif i.getdisposition()== 'BYE' :
            total2 +=1

            if i.getTIMEZONE() == "Day":
                DayBYEcode += 1
            elif i.getTIMEZONE() == "Evening":
                EveningBYEcode += 1
            else:
                NightBYEcode += 1
                
        elif i.getdisposition()== 'CANCEL' :
            total3 +=1
            if i.getTIMEZONE() == "Day":
                DayCANCELcode += 1
            elif i.getTIMEZONE() == "Evening":
                EveningCANCELcode += 1
            else:
                NightCANCELcode += 1
        else:
             total4 +=1
             if i.getTIMEZONE() == "Day":
                DayRBYEcode += 1
             elif i.getTIMEZONE() == "Evening":
                EveningRBYEcode += 1
             else:
                NightRBYEcode += 1
    print('Dispositions in a day')            
    print("{} number of Error".format(total))
    print("{} number of NA".format(total1))
    print("{} number of BYE".format(total2))
    print("{} number of CANCEL".format(total3))
    print("{} number of Release Bye".format(total4))


    barWidth = 0.15
    
     
    bars1 = [DayERRcode, DayNAcode, DayBYEcode, DayCANCELcode,DayRBYEcode]
    bars2 = [EveningERRcode, EveningNAcode, EveningBYEcode, EveningCANCELcode,EveningRBYEcode]
    bars3 = [NightERRcode, NightNAcode, NightBYEcode, NightCANCELcode,NightRBYEcode]
   

    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
 
     
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='day')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='evening')
    plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='night')

    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['ERROR', 'NA', 'BYE', 'CANCEL', 'Release Bye'])
     
    plt.legend()
    plt.show()
    ####
   
def prefix(data):
        
        N = []
        y = []
        z = []
        
       
        for i in data:
              N.append(i.getcallee_prefix_level())

        
        A = collections.Counter(N)
     
        for key, value in A.items():
            print("Amount and the prefix " + key, value)
            y.append(key)
            z.append(value)
           
        
        figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.y(rotation=90)    
        plt.bar(y,z)
        plt.show()

def trunk(data):
    
    N = []
    y = []
    z = []
    for i in data:
          N.append(i.gettrunk_id())
         
    
    A = collections.Counter(N)

    for key, value in A.items():
        print("trunk_id: {0} and amount: {1}".format(key, value))
        y.append(key)
        z.append(value)
        
       
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'red', 'blue']

    plt.pie(z, labels=y, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()

def src(data):
    N = []
    M = []
    y = []
    z = []
    yy = []
    zz = []
    
    for i in data:
          N.append(i.getsrc_ip())
          M.append(i.getdest_ip())
 
    A = collections.Counter(N)
    B = collections.Counter(M)
    for key, value in A.items():
        print("getsrc_ip and its amount " + key, value)
        y.append(key)
        z.append(value)
    print("")    
    for key, value in B.items():
        print("getdest_ip and its amount " + key, value)
        yy.append(key)
        zz.append(value)
        
        
  
    plt.show()    
    print("") 
    print("") 
    print("Green is getsrc_ip and blue is getdest_ip")    
        
    plt.plot(y, z, color='g')
    plt.plot(yy, zz, color='b')


    plt.xticks(rotation=90)   
    plt.ylabel('amounts')
    plt.title('Call durations in seconds')
    plt.show()
    
def group_id(data):
    
    id1_1, id1_4, id1_7, id4_1, id4_4, id4_7 = 0,0,0,0,0,0
   
    for i in data: 
        if i.getcaller_group_id() == '1' and i.getcallee_group_id() == '1':
            id1_1 += 1
        elif i.getcaller_group_id() == '1' and i.getcallee_group_id() == '4':
            id1_4 += 1
        elif i.getcaller_group_id() == '1' and i.getcallee_group_id() == '7':
            id1_7 += 1
        elif i.getcaller_group_id() == '4' and i.getcallee_group_id() == '1':
            id4_1 += 1
        elif i.getcaller_group_id() == '4' and i.getcallee_group_id() == '4':
            id4_4 += 1
        elif i.getcaller_group_id() == '4' and i.getcallee_group_id() == '7':
            id4_7 += 1
        
        
    caller = ["caller_id1","caller_id4"]
    callee = ["callee_id1","callee_id4","callee_id7"]
    ids = np.array([[id1_1,id1_4,id1_7],
                    [id4_1,id4_4,id4_7],
                    ])
    fig, ax = plt.subplots()
    im = ax.imshow(ids)
        
    ax.set_xticks(np.arange(len(callee)))
    ax.set_yticks(np.arange(len(caller)))
    ax.set_xticklabels(callee)
    ax.set_yticklabels(caller)
        
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")
        
    for i in range(len(callee)):
        for j in range(len(caller)):
                text = ax.text(i, j, ids[j, i],
                               ha="center", va="center", color="w")
        
    ax.set_title("Caller and callee ids")
    fig.tight_layout()
    plt.show()
        
def BYEbyzones(alist):
    y = []
    z = []
    yy = []
    zz = []
    D = []
    E = []
    N = []
    for i in alist:
          if i.getdisposition()== 'BYE' :
              if i.getTIMEZONE() == "Day":
                  D.append(i.getTIMEZONE())
              elif i.getTIMEZONE() == "Evening":
                  E.append(i.getTIMEZONE())
              else:
                  N.append(i.getTIMEZONE())
               
    A = collections.Counter(D)
    B = collections.Counter(E)
    C = collections.Counter(N)
    
    for key, value in A.items():
        print("Bye disposition at " + key, value)
        y.append(key)
        z.append(value)
    for key, value in B.items():
        print("Bye disposition at " + key, value)
        y.append(key)
        z.append(value)
    for key, value in C.items():
        print("Bye disposition at " + key, value)
        y.append(key)
        z.append(value)   
        
    
    D.clear()
    E.clear()
    N.clear()

    for i in alist:
          if i.getdisposition()== 'RELEASE BYE' :
              if i.getTIMEZONE() == "Day":
                  D.append(i.getTIMEZONE())
              elif i.getTIMEZONE() == "Evening":
                  E.append(i.getTIMEZONE())
              else:
                  N.append(i.getTIMEZONE())
               
    A = collections.Counter(D)
    B = collections.Counter(E)
    C = collections.Counter(N)
    
    for key, value in A.items():
        print("Realease Bye disposition at " + key, value)
        yy.append(key)
        zz.append(value)
    for key, value in B.items():
        print("Realease Bye disposition at " + key, value)
        yy.append(key)
        zz.append(value)
    for key, value in C.items():
        print("Realease Bye disposition at " + key, value)
        yy.append(key)
        zz.append(value)     
        
    print("Green line is for Bye, Blue line is for Release Bye")
    plt.plot(y, z, color='g', label='BYE')
    plt.plot(yy, zz, color='b', label='Release Bye')

    
    plt.ylabel('amounts')
    plt.title('Call durations in seconds')
    plt.show()
    
def calldir(data):
    
    mon_I,tue_I,wed_I,thu_I,fri_I,sat_I,sun_I = 0,0,0,0,0,0,0
    mon_O,tue_O,wed_O,thu_O,fri_O,sat_O,sun_O = 0,0,0,0,0,0,0

    
    for i in data:

       if i.getcall_dir() == '1':
        if i.getstart_time()[8:10] == '18':
          tue_I += 1
        elif i.getstart_time()[8:10] == '19' :
          wed_I += 1
        elif i.getstart_time()[8:10] == '20':
          thu_I += 1
        elif i.getstart_time()[8:10] == '21':
          fri_I += 1
        elif i.getstart_time()[8:10] == '22':
          sat_I += 1
        elif i.getstart_time()[8:10] == '23':
          sun_I += 1
        elif i.getstart_time()[8:10] == '24' or '17' :
          mon_I += 1  
       else:
        if i.getstart_time()[8:10] == '18':
          tue_O += 1
        elif i.getstart_time()[8:10] == '19' :
          wed_O += 1
        elif i.getstart_time()[8:10] == '20':
          thu_O += 1
        elif i.getstart_time()[8:10] == '21':
          fri_O += 1
        elif i.getstart_time()[8:10] == '22':
          sat_O += 1
        elif i.getstart_time()[8:10] == '23':
          sun_O += 1
        elif i.getstart_time()[8:10] == '24' or '17' :
          mon_O += 1     
    
    
    inb =  [mon_I,tue_I,wed_I,thu_I,fri_I,sat_I,sun_I]
    outb = [mon_O,tue_O,wed_O,thu_O,fri_O,sat_O,sun_O]
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    
    for i in range(0,7):
        print("{0} inbound calls at {1} ".format(inb[i],days[i]))
    for i in range(0,7):
        print("{0} outbound calls at {1} ".format(outb[i],days[i]))        
   
    print("")
    print("Green is for inbound blue is for outbound calls")
    plt.plot(days, inb, color='g')
    plt.plot(days, outb, color='b')


    plt.xticks(rotation=90) 
    plt.xlabel('Days')
    plt.ylabel('amounts')
    plt.title('Amount of inbound and outbound calls in different days')
    plt.show()
