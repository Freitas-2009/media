
print("-------------------------------------------------------------------------------")
nome = input("Digite seu nome: ")
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3 
print("-------------------------------------------------------------------------------")
print (f"O nome do aluno é: {nome}")
print (f"A média do aluno é: {media}")

if media > 7:
    print("O aluno está APROVADO ✅")

elif media > 4:
    print("O aluno está em RECUPERAÇÃO ⚠️")

else:
    print("O aluno está REPROVADO ❌")

print("-------------------------------------------------------------------------------")
