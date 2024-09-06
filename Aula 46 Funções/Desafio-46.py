# Temos duas funções, não trabalham ao mesmo tempo mas estão conectadas para seguir um fluxo
############
def PerguntarDados(primeiroNome, apelido):
  primeiroNome = input("Digite seu nome para o registro: ")
  apelido = input("Digite seu apelido: ")
  return (f"Obrigado!, os dados informados foram: {primeiroNome} {apelido}")
resultado = PerguntarDados("" , "") 

def confirmarDados(resultado):
  while True:
        resposta = input("Deseja confirmar os dados? s/n: ").lower()
        if resposta == "s":
            print(resultado)
            break  
        elif resposta == "n":
            print("Pronto, o sistema atualizou os dados.")
            break  
        else:
            print("Resposta inválida. Por favor, digite 's' ou 'n'.")

confirmarDados(resultado)
     