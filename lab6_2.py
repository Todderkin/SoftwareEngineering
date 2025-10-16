from pprint import pprint

my_dict = {'first': 'so easy'}

def add_to_dict(**kwargs):
    my_dict.update(kwargs)

add_to_dict(a1=1, a2=20, a3=54, a4=13)
add_to_dict(name='Михаил', age=31, weight=70, eye_color='blue')

pprint(my_dict)