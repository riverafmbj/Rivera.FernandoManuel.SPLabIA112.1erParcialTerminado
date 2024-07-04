from random import randint

def get_path_actual(nombre_archivo):
  """
  Obtiene el path del archivo que le pasemos

  Args:
      nombre_archivo(str): el nombre del archivo

  Returns:
      el directorio donde se encuentra el archivo
  """  
  
  import os
  directorio_actual = os.path.dirname(__file__)
  return os.path.join(directorio_actual, nombre_archivo)

def menu()->str:
  """
  Imprime el menú en pantalla

  Returns:
      input: para seleccionar la opción que querramos
  """
  
  print(f"{'Menú de opciones':^50}")
  print("1 - Cargar archivo .CSV")
  print("2 - Imprimir lista de películas")
  print("3 - Asignar rating")
  print("4 - Asignar género")
  print("5 - Filtrar por género")
  print("6 - Ordenar películas")
  print("7 - Informar Mejor Rating")
  print("8 - Guardar películas")
  print("9 - Salir")

  return input("Ingrese opción: ")

def cargar_archivo_csv(nombre_archivo:str)->list:
  """
  Carga los datos de un archivo en una lista

  Args:
      nombre_archivo(str): el nombre del archivo

  Returns:
      lista_peliculas(list): la lista con los datos cargados
  """
  with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
    lista_peliculas = []
    encabezado = archivo.readline().strip("\n").split(",")
    

    for linea in archivo.readlines(): #o for linea in archivo.readlines():
      pelicula = {}
      linea = linea.strip("\n").split(",")
      
      id, titulo, genero, rating = linea
      pelicula["id"] = id
      pelicula["titulo"] = titulo
      pelicula["genero"] = genero
      pelicula["rating"] = rating
      lista_peliculas.append(pelicula)
  
    return lista_peliculas
  
def mostrar_peliculas(lista_peliculas:list)->None:
  """
  Imprime en pantalla la lista de películas

  Args:
      lista_peliculas(list): la lista con los datos cargados
  """
  tam = len(lista_peliculas)
  print("                 ***Listado de peliculas***")
  print("ID                  Título                 Género      Rating")
  print("---------------------------------------------------------------")

  for i in range(tam):
    mostrar_pelicula_item(lista_peliculas[i])

def mostrar_pelicula_item(pelicula: dict)->None:
  """
  Imprime en pantalla una película

  Args:
      pelicula(dict): el diccionario con los datos de la pelicula
  """
  print(f"{pelicula['id']:>3} {pelicula['titulo']:>30} {pelicula['genero']:>15} {pelicula['rating']:>10}")

def asignar_rating()->float:
  """
  Asigna un número de rating random

  Return:
      rating(float): un número float random
  """
  rating = float(randint(1, 10))
  return rating

def mapear_titulos_rating(lista_peliculas)->list:
   """
   Mapea la lista de películas con los ratings

   Args:
      lista_películas(list): la lista con las películas

   Returns:
      lista_mapeada(list): la lista con los ratings mapeados
   """
   lista_mapeada = []
   for pelicula in lista_peliculas:
     pelicula["rating"] = asignar_rating()
     lista_mapeada.append({pelicula["titulo"], pelicula["rating"]})
   return lista_mapeada

def asignar_generos():
  """
  Asigna un número de genero random

  Return:
      rating(int): un número entero random
  """
  numero = randint(1, 4)
  return numero


def mapear_generos(lista_peliculas)->list:
   """
    Mapea la lista de películas con los generos

    Args:
          lista_películas(list): la lista con las películas

    Returns:
          lista_mapeada(list): la lista con los generos mapeados
   """
   lista_mapeada = []
   for pelicula in lista_peliculas:
     numero = asignar_generos()
     if numero == 1:
       pelicula["genero"] = "drama"
     elif numero == 2:
       pelicula["genero"] = "comedia"
     elif numero == 3:
       pelicula["genero"] = "accion"
     elif numero == 4:
       pelicula["genero"] = "terror"
     lista_mapeada.append({pelicula["titulo"], pelicula["genero"]})
   return lista_mapeada

def filtrar_por_genero(lista_peliculas:list, genero:str)->None:
  """
   Filtra a la lista de películas por género y crea un archivo .csv con las películas de ese género

   Args:
      lista_películas(list): la lista con las películas
      genero(str): la clave "genero" de los diccionarios de las películas

   Returns:
      None
   """
  peliculas_filtradas = []

  for pelicula in lista_peliculas:
      if genero == pelicula["genero"]:
          peliculas_filtradas.append(pelicula)
  

  with open(get_path_actual(f"{genero}.csv"), "w", encoding="utf-8") as archivo:
        values = list(lista_peliculas[0].keys())
        encabezado = ",".join(values) + "\n" #lo uno con comas y le agrego el \n
        archivo.write(encabezado)
        for pelicula in peliculas_filtradas:
          values = list(pelicula.values())
          l = []
          for value in values:
              if isinstance(value, int):
                  l.append(str(value))
              elif isinstance(value, float):
                  l.append(str(value))
              else:
                  l.append(value)
          linea = ",".join(l) + "\n"
          archivo.write(linea)

def ordenar_clave_criterio(lista_peliculas:list, clave:str, clave2:str)->None:
  """
   Ordena la lista por 2 criterios

   Args:
      lista_películas(list): la lista con las películas
      clave(str): la clave del diccionario que será el primer criterio de ordenamiento
      clave2(str): la clave del diccionario que será el segundo criterio de ordenamiento

   Returns:
      None
   """
  
  tam = len(lista_peliculas)
  for i in range(len(lista_peliculas)):
    for j in range (i + 1, tam):
        if lista_peliculas[i][clave] > lista_peliculas[j][clave] or \
        (lista_peliculas[i][clave] == lista_peliculas[j][clave] and lista_peliculas[i][clave2] < lista_peliculas[j][clave2]):
          aux = lista_peliculas[i]
          lista_peliculas[i] = lista_peliculas[j]
          lista_peliculas[j] = aux

def filtrar_mejores_ratings(lista_peliculas:list, lista_vacia:list)->None:
  """
   Filtra a las películas con mejor rating en una lista vacía

   Args:
      lista_peliculas(list): la lista con las películas
      lista_vacia(list): la lista vacía a la cual irán las películas con mejor rating

   Returns:
      None
   """
  rating_max = 0
  flag_rating = False

  for pelicula in lista_peliculas:
    
    rating = pelicula["rating"]
    if flag_rating == False or rating > rating_max:
      rating_max = rating
      flag_rating = True

  if flag_rating == True:
    for pelicula in lista_peliculas:
      rating = pelicula["rating"]
      if rating == rating_max:
        lista_vacia.append(pelicula)


def guardar_en_json(lista_peliculas:list)->None:
  """
   Crea un archivo .json y allí guarda el listado de películas

   Args:
      lista_peliculas(list): la lista con las películas

   Returns:
      None
   """
  import json 
  with open(get_path_actual("peliculas_mejor_rating.json"), "w", encoding="utf-8") as archivo:
      json.dump(lista_peliculas, archivo, indent=4) 




