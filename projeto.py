# Classe Produto que representa um produto no estoque
class Produto:
    def _init_(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def _str_(self):
        return f"{self.id}. {self.nome} - R${self.preco:.2f}"

# Função para exibir o estoque
def exibir_estoque(estoque):
    print("\nProdutos disponíveis:")
    for produto in estoque:
        print(produto)

# Função para adicionar um item ao carrinho
def adicionar_ao_carrinho(estoque, carrinho):
    try:
        produto_id = int(input("\nDigite o ID do produto que deseja adicionar ao carrinho: "))
        quantidade = int(input("Digite a quantidade: "))

        # Verifica se o produto existe no estoque
        produto = next((p for p in estoque if p.id == produto_id), None)
        if produto:
            carrinho.append((produto, quantidade))
            print(f"{quantidade}x {produto.nome} adicionados ao carrinho.")
        else:
            print("Produto não encontrado!")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# Função para exibir o carrinho de compras
def exibir_carrinho(carrinho):
    if not carrinho:
        print("\nSeu carrinho está vazio!")
        return
    print("\nCarrinho de Compras:")
    for produto, quantidade in carrinho:
        print(f"{quantidade}x {produto.nome} - R${produto.preco * quantidade:.2f}")
        
# Função para calcular o total da compra
def calcular_total(carrinho):
    total = sum(produto.preco * quantidade for produto, quantidade in carrinho)
    return total

# Função principal que controla o fluxo do programa
def main():
    # Criando o estoque do supermercado
    estoque = [
        Produto(1, "Arroz", 20.50),
        Produto(2, "Feijão", 10.30),
        Produto(3, "Carne", 30.99),
        Produto(4, "Leite", 3.50),
        Produto(5, "Pão", 1.99),
    ]

    carrinho = []

    while True:
        print("\n** Supermercado Simples **")
        print("1. Ver Estoque")
        print("2. Adicionar Produto ao Carrinho")
        print("3. Ver Carrinho")
        print("4. Finalizar Compra")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            exibir_estoque(estoque)
        elif opcao == "2":
            adicionar_ao_carrinho(estoque, carrinho)
        elif opcao == "3":
            exibir_carrinho(carrinho)
        elif opcao == "4":
            total = calcular_total(carrinho)
            print(f"\nTotal da compra: R${total:.2f}")
            print("Obrigado por comprar no Supermercado!")
            break
        elif opcao == "5":
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

# Rodar o programa
if _name_ == "_main_":
    main()