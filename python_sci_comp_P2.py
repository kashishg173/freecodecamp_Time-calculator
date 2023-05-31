days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
def search(day):
  day=day.lower()
  for i in range(len(days)):
    if(days[i].lower()==day.lower()):
      return i
  return -1
  
def add_time(start, duration,day='hash'):
  hour_time_s=start.split(':')[0]
  hour_time=int(hour_time_s)
  second=start.split(':')[1]
  min_time_s=second.split()[0]
  min_time=int(min_time_s)
  mn=second.split()[1]
  
  dur_hs_time=duration.split(':')[0]
  dur_h_time=int(dur_hs_time)
  dur_ms_time=duration.split(':')[1]
  dur_m_time=int(dur_ms_time)

  hour_add=hour_time+dur_h_time
  min_add=min_time+dur_m_time

  n=int(dur_h_time/12)
  rem=dur_h_time%12
  
  
  if(min_add<60):
    n1=n+1 if hour_time+rem>=12 else n
    #ampm
    ampm=mn
    i=1
    while i<=n1:
      ampm=ampm if hour_add<12*n1 else ('AM' if ampm=='PM' else 'PM')
      i+=1

    #hour
    hours='1' if hour_time+rem==13 else (hour_time+rem if hour_time+rem<=12 else dur_h_time-(12*n1-hour_time))
   

    #mins
    min=min_add
    
    #nex
    if(day=='hash'):
      string1=' (next day)'
      string2=' ('+str(int(n1/2)+1)+' days later)' if (n1%2!=0 and mn=='PM') else ' ('+str(int(n1/2))+' days later)'
      nex=string1 if ((n1==1 and mn=='PM' and ampm=='AM') or n1==2 or (n1==3 and mn=='AM')) else (string2 if n1>2 else '')
      #final_time
      time=str(hours)+':'+str(min_add).rjust(2,'0')+' '+ampm+nex
    else:
      days_later=int(n1/2)+1 if (n1%2!=0 and mn=='PM') else int(n1/2)
      day=day[0].upper()+day[1:].lower()
      day=day if (n1==0 or (n1==1 and mn=='AM' and ampm=='PM')) else days[(search(day)+days_later)%7]
      nex=''
      if(days_later>0):
        string1=' (next day)'
        string2=' ('+str(int(n1/2)+1)+' days later)' if (n1%2!=0 and mn=='PM') else ' ('+str(int(n1/2))+' days later)'
        nex=string1 if ((n1==1 and mn=='PM' and ampm=='AM') or n1==2 or (n1==3 and mn=='AM')) else (string2 if n1>2 else '')
      #final_time
      time=str(hours)+':'+str(min_add).rjust(2,'0')+' '+ampm+', '+day+nex

  else:
    n1=n+1 if hour_time+rem+1>=12 else n
    #ampm
    ampm=mn
    i=1
    while i<=n1:
      ampm=ampm if hour_add+1<12*n1 else ('AM' if ampm=='PM' else 'PM')
      i+=1
    
    #hour
    hours='1' if hour_time+rem+1==13 else (hour_time+rem+1 if hour_time+rem+1<=12*n1 else (hour_add+1)-12*n1)

    #mins
    min='00' if min_add==60 else str(min_add-60).rjust(2,'0')

    #nex
    if(day=='hash'):
      string1=' (next day)'
      string2=' ('+str(int(n1/2)+1)+' days later)' if (n1%2!=0 and mn=='PM') else ' ('+str(int(n1/2))+' days later)'
      nex=string1 if ((n1==1 and mn=='PM' and ampm=='AM') or n1==2 or (n1==3 and mn=='AM')) else (string2 if n1>2 else '')
      #final_time
      time=str(hours)+':'+str(min)+' '+ampm+nex
    else:
      days_later=int(n1/2)+1 if (n1%2!=0 and mn=='PM') else int(n1/2)
      day=day[0].upper()+day[1:].lower()
      day=day if (n1==0 or (n1==1 and mn=='AM' and ampm=='PM')) else days[(search(day)+days_later)%7]
      nex=''
      if(days_later>0):
        string1=' (next day)'
        string2=' ('+str(int(n1/2)+1)+' days later)' if (n1%2!=0 and mn=='PM') else ' ('+str(int(n1/2))+' days later)'
        nex=string1 if ((n1==1 and mn=='PM' and ampm=='AM') or n1==2 or (n1==3 and mn=='AM')) else (string2 if n1>2 else '')
      #final_time
      time=str(hours)+':'+str(min)+' '+ampm+', '+day+nex
      
  print(time)
add_time("8:16 PM", "4:00","Monday")
