dog= {}

dog= {'name':'Goku', 'color':'negro', 'breed':'cocker', 'legs':'4', 'age':'17años'}
student={'name':'elena','last_name': 'aperador','gender':'femenino','age':'16','marital status':'sin novio', 'skill':'karate', 'country':'españa','city':'jerez'}
print(len(student))
print(type(student['skill']))
student['skill'].append("memorizar")
values = student.values()
item = list(student.items())
student.pop('age')
del student