from math import*
phrase ="hello world"
number =5
print(phrase.count("l"))
print(phrase.index("l"))
print(phrase[2].upper().isupper())#lower/islower
print(phrase.index("l"))
print(phrase.replace("hello", "hi"))
print(pow(number, 2))
print(abs(number))
print(max(3, 6))#min
print(round(3.5))
print(floor(3.7))#ceil is the oposite of floor (dont forget from math import*)
print(sqrt(36))
num1 = input("enter the first number: ")#REMARAQUE num1 et num2 sont sous formes de chaines de caracteres on doit d'abord les convertir sous forme de float
num2 = input("enter the second number: ")
#WE CAN ALSO DO num2 = float(input("enter the second number: "))
result = float(num1)+float(num2)
print(result)
#LISTS
numbers = [1, 2, 5, -1, 3]
freinds = ["osmane", "boukara", "berbeche", "rouji", "ifriki"]
freinds[4] = "yacine"#remplacer la case 4 par yacine
freinds.append("ned")# ajouter une valeur a la liste
freinds.insert(2, "mojito")#ajouter une valeur dans une case precise
freinds.remove("rouji")#supprimer
print(freinds[0:4])#selectionner uniquement les variable entre 0 et <4 // si on mets exp 2: on selectionne tout les variables apres 2eme
print(freinds[4])
print(freinds)
freinds.sort()#par ordre alphabetique ou numerique
print(freinds)
freinds.extend(numbers)#ajouter une liste a une autre liste
freinds.reverse()#renverser l'ordre
print(freinds)
lists = freinds.copy()# copier une liste
print(lists)
tuple = (1, 2, 5)# la diff entre lists et tuple c que tuple ne peut pas etre modifier apres exp: tuple[1]="berbeche"// ()au lieu de []
coordinate = [(1, 2), (3, 4), (5, 6)]# we can use tuples inside a list
#FUNTIONS
def identity(name, age):
    print("hello ,my name is "+name +" ,I am "+age)#Or we can use str(age) and remove "" from age

identity("osmane", "23")
#RETURN FUNCTION
def cube(nbr):
     result=nbr* nbr* nbr
     return print(result)
cube(4)

#we can also do :(first oen better!)
#def cube(nbr):
    #return nbr*nbr*nbr
#result=cube(4)
#print(result)

#IF STATEMENT
male= True
tall= False

if male and tall:# there's also OR operator
    print("u are a  tall male")
elif tall and not(male):
    print("u are a tall female")
elif not (tall) and male:
    print("u are a short male")
else:
    print("u are a short female")




def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #!= not equal / ==equal /
        print("the highest number is "+str(num1))
    elif num2 >= num1 and num2 >= num3:
        print("the highest number is "+str(num2))
    else:
        print("the highest number is "+str(num3))
max_num(12, 24, 8 )

#dictioners
mounth_conversions = {
    1 :"january",
    2 : "february",
    3 : "march",
}

print(mounth_conversions[3]) #ou [] ou get() c la meme chose
print(mounth_conversions.get(3))
print(mounth_conversions.get(5, "may"))#pour une valeur non reconnu par le dictionnaire on peut lui donner une valeur ou un commentaire bien precie


# while loops
i = 1
while i <= 10:
    print(i)
    i += 1

print("done with this loop")

#for loops
for freind in freinds:
    print(freind)

for index in range(3, 6):
    print(index)
names = ["osmane", "fady", "maha", "nazli"]
for nbr_freinds in range(len(names)):#regarde le programem attentivement et tu comprendras XD
    print(names[nbr_freinds])

#exponent loop
def raise_topower(nbr, pow_nbr):
    result=1
    for index in range(pow_nbr):#la longeur est de 3 la
        result = result * nbr# fro loop execute le probleme 3 fois donc 1*5 ensuite 5*5 ensuite 25*5 etc..
    return result
print(raise_topower(5, 3))

# 2D list and nest loop(for inside for loop)
number_grid=[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

for i in number_grid:
        print(i)#pour i appartenant a nbr_grid pour lindex 0 puis pour 1 puis 2
        for j in i:
            print(j)#pour j appartenant i pour lindex 0 puis pour 1 puis 2


#try except (le but de ca est de trouver une erreur bien specifique)
try:
    number=int(input("enter your number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

#reading files:
files_2020 = open("scratch.txt", "r")# "r"=read "w"=write  "r+"=read and write "a"=appened
      print(files_2020.readable())# voir si le fichier peut etre lu
      print(files_2020.readline())#lire just la premiere ligne
      print(files_2020.readlines())# lire toute les lignes et els mettre dans une lists
      print(files_2020.readlines()[])#lire une ligne specifique
files_2020.write("\nberbeche in the air"))#ajouter dans une nouvelle ligne au fichier
files_2020.close()#fermer le fichier

#writing files
files_2020 = open("new_file.txt", "a")#si on met "a" on ajoute au fichier parcontre "r" on ecrase le fichier et on ecrit a nouveau
files_2020.write("berbeche in the air")#voir si le fichier peut etre lu
files_2020.close()# fermer le fichier
#on peut aussi creer

#modules and pip
#modules is a python files which we can import to our python file


#class and object
class berbeche:
    def __init__(self, name, age, matricule):
        self.name = name
        self.age = age
        self.matricule = matricule

from exercice import berbeche
exo1 = berbeche("osmane", 23, 1)
exo2 = berbeche("rouji", 22, 2)
print(exo1.age)
print(exo2.name)


#inheritence
from exercice import exerrcice
class exo1(exercice): #heritage
    ##rq si on veut modifier une fonction de lheritage alors on la reformule

   #skfnodghosdfbinfib











