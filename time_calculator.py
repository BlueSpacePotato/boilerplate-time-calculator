def add_time(start, duration, starting_day=None):
  """
  a start time in the 12-hour clock format (ending in AM or PM)
  a duration time that indicates the number of hours and minutes
  (optional) a starting day of the week, case insensitive
  """
  # define empty return value
  new_time = 0

  # values for day calc
  day_overflow = 0
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
  # load start time and reformat into 24h
  start_time = start.split()
  s_h, s_m = start_time[0].split(':')
  s_h = int(s_h)
  s_m = int(s_m)
  if start_time[1] == 'PM':
    s_h += 12

  # load duration and reformat into 24h
  d_h, d_m = duration.split(':')
  d_h = int(d_h)
  d_m = int(d_m)

  # add times
  n_h = s_h + d_h
  n_m = s_m + d_m

  # calc min overflow
  n_h += int(n_m/60)
  n_m = n_m % 60

  # calc day overflow
  day_overflow = int(n_h / 24) 
  n_h = n_h % 24

  if day_overflow == 1:
    next_day = '(next day)'
  elif day_overflow > 1:
    next_day = f'({day_overflow} days later)'

  if n_h > 12:
    new_time = f'{n_h - 12}:{n_m:02d} PM'
  elif n_h == 12:
    new_time = f'{n_h}:{n_m:02d} PM'
  elif n_h == 0:
    new_time = f'{n_h + 12}:{n_m:02d} AM'
  else:
    new_time = f'{n_h}:{n_m:02d} AM'

  if starting_day is not None:
    ending_day = starting_day.title()
    if day_overflow > 0:
      idx = days.index(ending_day) + day_overflow
      ending_day = days[idx%7]

    
  # return strings
  if day_overflow > 0 and starting_day is not None:
    return f'{new_time}, {ending_day} {next_day}'
  elif day_overflow > 0:
    return f'{new_time} {next_day}'
  elif starting_day is not None:
    return f'{new_time}, {ending_day}'
  return f'{new_time}'