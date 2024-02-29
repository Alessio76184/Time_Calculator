def add_time(start, duration, week=None):

  # Defining Starting time into variables and including then days of the week.
  start_hours = int(start.split(":")[0])
  start_minutes = int(start.split(":")[1].split(" ")[0])
  period = start.split(":")[1].split(" ")[1]
  start_day_index = 0 if week is None else ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(week.capitalize())

  # Defining Duration time into variables that gives it the time to count
  duration_hours = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1].split(" ")[0])

  # Calculating the new time by adding the duration to the start time
  new_hour = int(start_hours) + int(duration_hours)
  new_minutes = int(start_minutes) + int(duration_minutes)
  days_change = 0
  new_period = period

  # Keeping the new minutes within 60 seconds and adding the extra hour
  if int(new_minutes) >= 60:
      new_hour += 1
      new_minutes -= 60

  # Adjusting the number of days if hours exceed 24
  days_change = new_hour // 24
  new_hour = new_hour % 24
  
  # Keeping the hours at a 12-hour format and changing the period. 
  ## It also changes the day index if the period changes in case there is a smaller 
  ## time change from AM to PM
  time_pass = new_hour // 12
  if time_pass % 2 == 0:
    pass
  else:
    if new_period == "AM":
      new_period = "PM"
    else:
      new_period = "AM"
      days_change += 1

  # Converting new hour to 12-hour format
  if new_hour == 0:
      new_hour = 12
  elif new_hour > 12:
      new_hour -= 12

  # Formating the new time to include a 0 if it has only one digit
  new_minutes_str = str(new_minutes).zfill(2)
  
  # Formating the new time without the day of the week
  new_time = str(new_hour) + ":" + new_minutes_str + " " + new_period
  
  # Formating the new time with the day of the week
  if week:
    new_day_index = (start_day_index + days_change) % 7
    new_time += ", " + ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][new_day_index]
  
  # Include the number of days passed in the output
  if days_change == 1:
      new_time += " (next day)"
  elif days_change > 1:
      new_time += " (" + str(days_change) + " days later)"

  return new_time
