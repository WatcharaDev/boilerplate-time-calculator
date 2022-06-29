
days =  ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday']

day_map = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}

def parse_time(t):
    [hm, am] = t.split()
    [h, m] = map(lambda s: int(s), hm.split(":"))
    #To 24H
    if am != 'AM':
        h += 12
    return [h, m]

def add_time(t, add, start_day =""):

  [h, m] = parse_time(t)
  [ah, am] = map(lambda s: int(s), add.split(":"))

  #Add Time
  h += ah
  m += am

  #Min to Hr
  if m > 60: 
    m %= 60
    h += 1
    
  #Hr To n days
  n = h // 24
  if h > 24:
    h %= 24

  
  #AM or PM
  ampm = "AM"
  if h > 12:
    h %= 12
    ampm = "PM"

  if h == 12:
    ampm = "PM"

  if h == 0:
    h = 12
    ampm = "AM"

  #Display Day?
  if start_day == "":
    if n == 0:
      return f"{h}:{m:02d} {ampm}"
    if n == 1:
      return f"{h}:{m:02d} {ampm} (next day)"

    return f"{h}:{m:02d} {ampm} ({n} days later)"
  
  else:
    start_day = start_day.lower()
    start_day = start_day[0].upper() + start_day[1:]
    end_day = days[(day_map[start_day] + n) % 7]
    if n == 0:
      return f"{h}:{m:02d} {ampm}, {end_day}"
    if n == 1:
      return f"{h}:{m:02d} {ampm}, {end_day} (next day)"

    return f"{h}:{m:02d} {ampm}, {end_day} ({n} days later)"
