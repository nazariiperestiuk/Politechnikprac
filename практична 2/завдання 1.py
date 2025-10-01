score = int(input("write your score:"))
if score > 90:
 grade = 'відмінно'
elif score > 50:
 grade = 'задовільно'
else:
 grade = 'незадовільно'
print(f'IF: Ви набрали {score} балів, оцінка - {grade}.')
grade = 'відмінно' if score > 90 else 'задовільно' if score > 50 else 'незадовільно'
print(f'TERN: Ви набрали {score} балів, оцінка - {grade}.')