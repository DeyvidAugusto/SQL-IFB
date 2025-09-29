from database import Database
from models import Pedido, ItemPedido
from control import PedidoControl

if __name__ == "__main__":
    db = Database(host='127.0.0.1', user='root', password='root', database='db_pedidos')
    control = PedidoControl(db)
    # pedido = Pedido(cliente="Claudio Ulisse")
    #
    # control.salvar_pedido(pedido)
    # control.atualizar_pedido(pedido)
    #
    # pedidos = control.listar_pedidos_com_itens()
    # for p in pedidos:
    #     print(f"Pedido {p.id} - Cliente: {p.cliente}")
    #     for i in p.itens:
    #         print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")

    # Inserção
    novo_pedido = Pedido(cliente="Maria Silva")
    print(f"Pedido inserido: {novo_pedido.id} - Cliente: {novo_pedido.cliente}")

    novo_pedido.add_item(ItemPedido("Produto X", 2, 19.9, "Eletrônicos"))
    novo_pedido.add_item(ItemPedido("Produto Y", 1, 29.9, "Livros"))
    control.salvar_pedido(novo_pedido)

    outro_pedido = Pedido(cliente="João Souza")
    print(f"Pedido inserido: {outro_pedido.id} - Cliente: {outro_pedido.cliente}")

    outro_pedido.add_item(ItemPedido("Produto Z", 3, 15.5, "Brinquedos"))
    outro_pedido.add_item(ItemPedido("Produto W", 2, 25.0, "Casa"))
    control.salvar_pedido(outro_pedido)

    # Atualização
    novo_pedido.cliente = "Maria Silva Atualizado"
    control.atualizar_pedido(novo_pedido)
    print(f"Pedido atualizado: {novo_pedido.id} - Cliente: {novo_pedido.cliente}")

    # Listagem
    pedidos = control.listar_pedidos_com_itens()
    print("Listagem de pedidos:")
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria={i.categoria}\n")

    # Deleção
    control.deletar_pedido(novo_pedido.id)
    print(f"Pedido deletado: {novo_pedido.id}")

    db.close()
