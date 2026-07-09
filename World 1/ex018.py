from math import sin, cos, tan , radians
a = int(input('Digite um angulo: '))
r = radians(a)
s = sin (r)
c = cos(r)
t = tan(r)
print('Seno : {:.2f} \n Cosseno : {:.2f} \n Tangente : {:.2f}'.format(s, c , t))