class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo")
    
with AlgumaCoisa() as ola:
    print("Estou no meio")

# class MinhaClasse:
#     def __init__(self):
#         self.nome = nome
    
#     def imprimir_self(self):
#         print(self)

# # Criando duas instâncias da classe
# objeto1 = MinhaClasse("objeto1")
# objeto2 = MinhaClasse("objeto2")

# # Chamando o método imprimir_self() em cada instância
# objeto1.imprimir_self()
# objeto2.imprimir_self()