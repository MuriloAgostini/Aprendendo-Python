import random
print ('Para começar o sorteio, voce vai precisar informar individualmente o nome de cada um dos quatro alunos abaixo ')
al1 = input('Informe o nome do primeiro aluno' )
al2 = input('Informe o nome do segundo aluno' )
al3 = input('Informe o nome do terceiro aluno' )
al4 = input('Informe o nome do quarto aluno' )
alunos = (al1, al2, al3, al4)
random.shuffle(alunos)
print (alunos)