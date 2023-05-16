from agenda import Agenda

def main():
    lista = Agenda()
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar contato")
        print("2. Visualizar contato")
        print("3. Atualizar contato")
        print("4. Sair")
        
        opcao = input("Opção: ")
        if opcao == "1":
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            nascimento = input("Data de Nascimento: ")
            email = input("Email: ")
            lista.adicionar(nome, sobrenome, telefone, nascimento, email)
            print("Contato adicionado com sucesso!")
        
        elif opcao == "2":
            lista.visualizar()
        
        elif opcao == "3":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")         
            lista.atualizar(nome, telefone, email)    
        
        elif opcao =="4": 
            print("4. Sair") 
            break   
        
        else:
            print("Opção inválida!")
            
        
        
    
if __name__== "__main__":
    main()
    
    
