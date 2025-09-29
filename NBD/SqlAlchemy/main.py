from models import Base, Pedido, ItemPedido
from database import engine
from control import PedidoControl

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    control = PedidoControl()

    pedido = Pedido(cliente='Ana Paula')
    pedido.itens = [
        ItemPedido(produto='Smartphone', quantidade=1, preco=1500.00, categoria='Eletrônicos'),
        ItemPedido(produto='Capinha', quantidade=1, preco=50.00, categoria='Acessórios')
    ]

    control.salvar_pedido(pedido)
    pedidos = control.listar_pedidos_com_itens()

    # Inserção
    novo_pedido = Pedido(cliente='Carlos Silva')
    novo_pedido.itens = [
        ItemPedido(produto='Notebook', quantidade=1, preco=3500.00, categoria='Eletrônicos')
    ]
    control.salvar_pedido(novo_pedido)

    # Atualização
    pedido_atualizar = pedidos[0]
    pedido_atualizar.cliente = 'Ana Paula Souza'
    control.salvar_pedido(pedido_atualizar)

    # Listagem
    pedidos_atualizados = control.listar_pedidos_com_itens()
    for p in pedidos_atualizados:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}\n")

    # Deleção Sempre deleta o último pedido da lista (Carlos Silva)
    if pedidos_atualizados:
        control.deletar_pedido(pedidos_atualizados[-1].id)
    control.fechar()


