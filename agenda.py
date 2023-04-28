from contato import Contato

class Agenda:
    def __init__(self):
        self.primeiro_contato = None
        self.ultimo_contato = None
        self.quantidade_contatos = 0
           
    def adicionar(self, nome, sobrenome, telefone, data_de_nascimento, email):
        novo_contato = Contato(nome, sobrenome, telefone, data_de_nascimento, email)
        if self.primeiro_contato is None:
            self.primeiro_contato = novo_contato
            self.ultimo_contato = novo_contato
        else:
            self.ultimo_contato.proximo = novo_contato
            self.ultimo_contato = novo_contato
        self.quantidade_contatos += 1        
        
       
    def visualizar(self):
        atual = self.primeiro_contato
        while atual!= None:
            print("-----------------------------")
            print(atual.nome)
            print(atual.sobrenome)
            print(atual.telefone)
            print(atual.data_de_nascimento)
            print(atual.email)
            print(self.quantidade_contatos)
            atual = atual.proximo
            print("-----------------------------")
            
    def atualizar(self, nome,  telefone, email):
        atual = self.primeiro_contato;
        while atual != None:
            if atual.nome == nome:
                atual.telefone = telefone
                atual.email = email
            atual = atual.proximo
                
    def remover(self):
        return None

#Métodos adicionais
   
    def ordenar(self):
        return None
    def merge_sort(self):
        return None