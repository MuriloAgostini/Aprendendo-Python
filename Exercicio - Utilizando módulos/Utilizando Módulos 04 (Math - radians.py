import math
ang = float(input('informe o angulo '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('Levando em consideração o angulo de {:.03f} graus informado o cosseno é {:.03f}, o seno é {:.03f} e a tangente é {:.03f}' .format(ang, cos, sen , tan))