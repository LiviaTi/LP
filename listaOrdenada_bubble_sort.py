#Bubble sort compara o numero vizinho e troca de lugar
def executar_bubble_sort(lista):
  n = len(lista)

  for i in range(n - 1):
    for j in range(n - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  return lista


lista = [10, 9, 8, 5, 11, -1, 2]
executar_bubble_sort(lista)
print(lista)
