#alt+z:limite l'ecriture selon la largeur du ligne de VsCode
#input():fct qui demande une entree user,"""alt+shift+a""" et retourne la valeur comme un str
nbr1=int(input("Entrez le premier nombre: "))#casting c'est le conversion de la valeur d'une chaine de caractere a un entier
nbr2=int(input("Entrez le deuxieme nombre: "))
sum=nbr1+nbr2
print("La somme est: "+str(sum)) #a la place de +str() on peut mettre , qui est la sollution la plus optimale
#chaines formatees f-string:
print(f"La somme est: {sum}")