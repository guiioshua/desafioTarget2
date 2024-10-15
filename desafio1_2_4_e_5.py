#1)
def desafio1():
    i = 13
    soma = 0
    k = 0
    while k < i:
        k = k+1
        soma = soma + k
    return soma
print(desafio1())

#2)
def findFibo(n):
  fiboList = [1, 1]
  fibo = 0
  while fibo <= n:
    fibo = fiboList[-1] + fiboList[-2]
    fiboList.append(fibo)
  return print(f'{n} pertence a sequência de fibonacci.') if n in fiboList else print(f'{n} não pertence à sequencia de fibonacci.')

findFibo(int(input('Digite n: ')))

#4)
def findPercentual():
###        TRATAMENTO DA ENTRADA DOS DADOS DOS ESTADOS          ### 
  incomeRaw = '''
    • SP – R$67.836,43
    • RJ – R$36.678,66
    • MG – R$29.229,88
    • ES – R$27.165,48
    • Outros – R$19.849,53
    '''.strip()
  incomeList = incomeRaw.splitlines()
  incomePerState = {}
  for state in incomeList:
    state = state.strip(' •')
    state, income = state.split(' – ')
    income = float(income.replace('R$', '').replace('.','').replace(',','.'))
    incomePerState[state] = income
### FIM DO TRATAMENTO, armazenei as informações em um dicionário ###
  amount = sum(incomePerState.values())
  percentualPerState = {state: round(income/amount*100,2) for state, income in incomePerState.items()}

  return percentualPerState
percentualPerState = findPercentual()
for state in percentualPerState:
  print(f' Estado: {state} - Participação no total: {percentualPerState[state]}%')

#5) JEITO FÁCIL
def stringInverterEasy(string):
  return string[::-1]

#5) JEITO DIFÍCIL
def stringInverterHard(string):
  invertedString = ''
  for i in range(len(string)):
    invertedString += string[len(string)-i-1]
  return invertedString

stringInput = input('Digite a string: ')
print(stringInverterEasy(stringInput))
print(stringInverterHard(stringInput))