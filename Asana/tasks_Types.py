def tasksTypes(deadlines, day):
  label = list()
  upcoming = 0
  later = 0
  count = 0
  task = 0

  for i in range(len(deadlines)):
    if deadlines[i] <= day:
       task += 1 
    if deadlines[i] > day and deadlines[i] <= day + 7:
       upcoming += 1
    if deadlines[i] > day + 7:
       later += 1

  label.append(task)
  label.append(upcoming)
  label.append(later)
  return label
    
    
