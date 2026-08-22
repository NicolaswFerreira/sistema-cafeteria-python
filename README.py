# ==========================================
# SISTEMA DE GERENCIAMENTO - CAFETERIA
# ==========================================


# ==========================================
# 1. PRODUTOS
# ==========================================

lista_produtos = [
    {
        "codigo": "P001",
        "nome": "Café Espresso Pequeno",
        "preco": 4.00,
        "estoque": 20,
        "ingredientes": {
            "cafe_pó": 1,
            "acucar": 1
        }
    },
    {
        "codigo": "P002",
        "nome": "Café Espresso Médio",
        "preco": 5.00,
        "estoque": 20,
        "ingredientes": {
            "cafe_pó": 1,
            "acucar": 1,
            "leite": 1
        }
    },
    {
        "codigo": "P003",
        "nome": "Café Espresso Grande",
        "preco": 6.00,
        "estoque": 20,
        "ingredientes": {
            "cafe_pó": 2,
            "acucar": 1,
            "leite": 1
        }
    },
    {
        "codigo": "P004",
        "nome": "Brownie",
        "preco": 7.00,
        "estoque": 10,
        "ingredientes": {
            "chocolate": 1,
            "massa": 1
        }
    },
    {
        "codigo": "P005",
        "nome": "Pão de Queijo",
        "preco": 5.00,
        "estoque": 30,
        "ingredientes": {
            "pao": 1,
            "queijo": 1
        }
    },
    {
        "codigo": "P006",
        "nome": "Misto",
        "preco": 8.00,
        "estoque": 15,
        "ingredientes": {
            "pao": 1,
            "queijo": 1,
            "presunto": 1
        }
    },
    {
        "codigo": "P007",
        "nome": "Água com Gás",
        "preco": 4.00,
        "estoque": 20,
        "ingredientes": {}
    },
    {
        "codigo": "P008",
        "nome": "Refrigerante",
        "preco": 6.00,
        "estoque": 15,
        "ingredientes": {}
    },
    {
        "codigo": "P009",
        "nome": "Suco",
        "preco": 7.00,
        "estoque": 15,
        "ingredientes": {
            "frutas": 1
        }
    },
    {
        "codigo": "P010",
        "nome": "Panqueca",
        "preco": 10.00,
        "estoque": 10,
        "ingredientes": {
            "massa": 1,
            "leite": 1
        }
    },
    {
        "codigo": "P011",
        "nome": "Tapioca",
        "preco": 9.00,
        "estoque": 10,
        "ingredientes": {
            "massa": 1
        }
    },
    {
        "codigo": "P012",
        "nome": "Sanduíche Natural",
        "preco": 10.00,
        "estoque": 10,
        "ingredientes": {
            "pao": 1,
            "frango": 1
        }
    },
    {
        "codigo": "P013",
        "nome": "Sorvete",
        "preco": 7.00,
        "estoque": 15,
        "ingredientes": {
            "leite": 1
        }
    }
]


# ==========================================
# 2. CLIENTES
# ==========================================

lista_clientes = [
    {
        "codigo": "C001",
        "nome": "Nicolas Ferreira",
        "pontos": 0
    },
    {
        "codigo": "C002",
        "nome": "João Silva",
        "pontos": 3
    },
    {
        "codigo": "C003",
        "nome": "Maria Santos",
        "pontos": 4
    }
]


# ==========================================
# 3. INGREDIENTES
# ==========================================

lista_ingredientes = [
    {
        "codigo": "I001",
        "nome": "cafe_pó",
        "quantidade": 50
    },
    {
        "codigo": "I002",
        "nome": "acucar",
        "quantidade": 100
    },
    {
        "codigo": "I003",
        "nome": "leite",
        "quantidade": 30
    },
    {
        "codigo": "I004",
        "nome": "pao",
        "quantidade": 40
    },
    {
        "codigo": "I005",
        "nome": "queijo",
        "quantidade": 30
    },
    {
        "codigo": "I006",
        "nome": "presunto",
        "quantidade": 30
    },
    {
        "codigo": "I007",
        "nome": "frango",
        "quantidade": 20
    },
    {
        "codigo": "I008",
        "nome": "chocolate",
        "quantidade": 20
    },
    {
        "codigo": "I009",
        "nome": "massa",
        "quantidade": 30
    },
    {
        "codigo": "I010",
        "nome": "frutas",
        "quantidade": 30
    }
]


# ==========================================
# 4. VENDAS
# ==========================================

lista_vendas = []

contador_venda = 1


# ==========================================
# 5. FUNÇÕES AUXILIARES
# ==========================================

def mostrar_produtos():

    print("\n========== PRODUTOS ==========")

    print(
        f"{'Código':<8}"
        f"{'Nome':<30}"
        f"{'Preço':>10}"
        f"{'Estoque':>10}"
    )

    print("-" * 58)

    for produto in lista_produtos:

        print(
            f"{produto['codigo']:<8}"
            f"{produto['nome']:<30}"
            f"R$ {produto['preco']:>7.2f}"
            f"{produto['estoque']:>10}"
        )


def buscar_produto(codigo):

    for produto in lista_produtos:

        if produto["codigo"] == codigo:
            return produto

    return None


def buscar_cliente(codigo):

    for cliente in lista_clientes:

        if cliente["codigo"] == codigo:
            return cliente

    return None


def buscar_venda(codigo):

    for venda in lista_vendas:

        if venda["codigo"] == codigo:
            return venda

    return None


def buscar_ingrediente(nome):

    for ingrediente in lista_ingredientes:

        if ingrediente["nome"] == nome:
            return ingrediente

    return None


# ==========================================
# 6. SISTEMA PRINCIPAL
# ==========================================

sistema_funcionando = True

while sistema_funcionando:

    print("\n====================================")
    print("       SISTEMA DA CAFETERIA")
    print("====================================")

    print("1 - Iniciar venda")
    print("2 - Buscar venda")
    print("3 - Cadastrar cliente")
    print("4 - Buscar cliente")
    print("5 - Consultas")
    print("0 - Encerrar sistema")

    opcao = input("\nDigite uma opção: ")


    # ==========================================
    # 1 - INICIAR VENDA
    # ==========================================

    if opcao == "1":

        # ------------------------------
        # IDENTIFICAR CLIENTE
        # ------------------------------

        codigo_cliente = input(
            "\nDigite o código do cliente: "
        )

        cliente = buscar_cliente(codigo_cliente)

        if cliente is None:

            print("\nCliente não encontrado.")

            cadastrar = input(
                "Deseja cadastrar este cliente? "
                "1 - Sim / 2 - Não: "
            )

            if cadastrar == "1":

                nome_cliente = input(
                    "Digite o nome completo do cliente: "
                )

                codigo_cliente = (
                    f"C{len(lista_clientes) + 1:03d}"
                )

                cliente = {
                    "codigo": codigo_cliente,
                    "nome": nome_cliente,
                    "pontos": 0
                }

                lista_clientes.append(cliente)

                print(
                    "\nCliente cadastrado com sucesso!"
                )

                print(
                    f"Código do cliente: {codigo_cliente}"
                )

            else:

                print("Venda cancelada.")
                continue


        # ------------------------------
        # CRIAR PEDIDO
        # ------------------------------

        pedido = []
        adicionar_produtos = True

        while adicionar_produtos:

            mostrar_produtos()

            codigo_produto = input(
                "\nDigite o código do produto: "
            )

            produto = buscar_produto(codigo_produto)

            if produto is None:

                print("\nProduto não encontrado.")

                continuar = input(
                    "Deseja tentar novamente? "
                    "1 - Sim / 2 - Não: "
                )

                if continuar == "1":
                    continue

                else:
                    adicionar_produtos = False
                    pedido = []

            else:

                print(
                    f"\nProduto selecionado: "
                    f"{produto['nome']}"
                )

                print(
                    f"Preço: R$ {produto['preco']:.2f}"
                )

                quantidade = int(
                    input("Digite a quantidade: ")
                )

                if quantidade <= 0:

                    print("Quantidade inválida.")

                elif quantidade > produto["estoque"]:

                    print(
                        "Quantidade maior que o estoque disponível."
                    )

                else:

                    subtotal = (
                        produto["preco"]
                        * quantidade
                    )

                    item = {
                        "produto": produto["codigo"],
                        "nome": produto["nome"],
                        "quantidade": quantidade,
                        "preco": produto["preco"],
                        "subtotal": subtotal
                    }

                    pedido.append(item)

                    print(
                        "\nProduto adicionado ao pedido."
                    )

                print(
                    "\nDeseja adicionar outro produto?"
                )

                print("1 - Sim")
                print("2 - Não")

                continuar = input(
                    "Digite uma opção: "
                )

                if continuar == "1":

                    adicionar_produtos = True

                else:

                    adicionar_produtos = False


        # ------------------------------
        # VERIFICAR PEDIDO
        # ------------------------------

        if len(pedido) == 0:

            print(
                "\nNenhum produto foi adicionado."
            )

            print("Venda cancelada.")

            continue


        # ------------------------------
        # CALCULAR TOTAL
        # ------------------------------

        valor_total = 0

        for item in pedido:

            valor_total = (
                valor_total
                + item["subtotal"]
            )


        # ------------------------------
        # RESUMO
        # ------------------------------

        print(
            "\n========== RESUMO DO PEDIDO =========="
        )

        print(
            f"Cliente: {cliente['nome']}"
        )

        print(
            f"Código: {cliente['codigo']}"
        )

        print("-" * 70)

        print(
            f"{'Código':<8}"
            f"{'Produto':<30}"
            f"{'Qtd.':>8}"
            f"{'Preço':>12}"
            f"{'Subtotal':>12}"
        )

        print("-" * 70)

        for item in pedido:

            print(
                f"{item['produto']:<8}"
                f"{item['nome']:<30}"
                f"{item['quantidade']:>8}"
                f"R$ {item['preco']:>8.2f}"
                f"R$ {item['subtotal']:>8.2f}"
            )

        print("-" * 70)

        print(
            f"TOTAL: R$ {valor_total:.2f}"
        )


        # ------------------------------
        # CONFIRMAR OU CANCELAR
        # ------------------------------

        print("\nDeseja confirmar a venda?")
        print("1 - Confirmar")
        print("2 - Cancelar")

        confirmacao = input(
            "Digite uma opção: "
        )

        if confirmacao != "1":

            print("\nVenda cancelada.")

            continue


        # ==========================================
        # VENDA CONFIRMADA
        # ==========================================


        # ------------------------------
        # BAIXAR ESTOQUE DOS PRODUTOS
        # ------------------------------

        for item in pedido:

            produto = buscar_produto(
                item["produto"]
            )

            produto["estoque"] = (
                produto["estoque"]
                - item["quantidade"]
            )


        # ------------------------------
        # BAIXAR ESTOQUE DOS INGREDIENTES
        # ------------------------------

        for item in pedido:

            produto = buscar_produto(
                item["produto"]
            )

            for nome_ingrediente in produto["ingredientes"]:

                quantidade_por_produto = (
                    produto["ingredientes"]
                    [nome_ingrediente]
                )

                quantidade_utilizada = (
                    quantidade_por_produto
                    * item["quantidade"]
                )

                ingrediente = buscar_ingrediente(
                    nome_ingrediente
                )

                if ingrediente:

                    ingrediente["quantidade"] = (
                        ingrediente["quantidade"]
                        - quantidade_utilizada
                    )


        # ------------------------------
        # ATUALIZAR PONTOS
        # ------------------------------

        cliente["pontos"] = (
            cliente["pontos"] + 1
        )

        # 5 pontos = Espresso grátis

        if cliente["pontos"] == 5:

            print(
                "\n🎉 Cliente ganhou um Espresso grátis!"
            )

            cliente["pontos"] = 0

            print(
                "Pontos restantes: 0"
            )


        # ------------------------------
        # GERAR CÓDIGO DA VENDA
        # ------------------------------

        codigo_venda = (
            f"V{contador_venda:03d}"
        )

        contador_venda = (
            contador_venda + 1
        )


        # ------------------------------
        # REGISTRAR VENDA
        # ------------------------------

        venda = {
            "codigo": codigo_venda,
            "cliente": cliente["codigo"],
            "produtos": pedido,
            "valor_total": valor_total
        }

        lista_vendas.append(venda)


        # ------------------------------
        # CONFIRMAÇÃO
        # ------------------------------

        print(
            "\n===================================="
        )

        print(
            "          VENDA CONCLUÍDA!"
        )

        print(
            "===================================="
        )

        print(
            f"Código da venda: {codigo_venda}"
        )

        print(
            f"Cliente: {cliente['nome']}"
        )

        print(
            f"Valor total: R$ {valor_total:.2f}"
        )

        print(
            f"Pontos atuais: {cliente['pontos']}"
        )


    # ==========================================
    # 2 - BUSCAR VENDA
    # ==========================================

    elif opcao == "2":

        codigo_busca = input(
            "\nDigite o código da venda: "
        )

        venda = buscar_venda(codigo_busca)

        if venda:

            print(
                "\n========== VENDA ENCONTRADA =========="
            )

            print(
                f"Código: {venda['codigo']}"
            )

            print(
                f"Cliente: {venda['cliente']}"
            )

            print(
                f"Valor Total: "
                f"R$ {venda['valor_total']:.2f}"
            )

            print("\nProdutos:")

            for item in venda["produtos"]:

                print(
                    f"{item['nome']} "
                    f"x {item['quantidade']} "
                    f"- R$ {item['subtotal']:.2f}"
                )

        else:

            print(
                "\nVenda não encontrada."
            )


    # ==========================================
    # 3 - CADASTRAR CLIENTE
    # ==========================================

    elif opcao == "3":

        nome_cliente = input(
            "\nDigite o nome completo do cliente: "
        )

        codigo_cliente = (
            f"C{len(lista_clientes) + 1:03d}"
        )

        novo_cliente = {
            "codigo": codigo_cliente,
            "nome": nome_cliente,
            "pontos": 0
        }

        lista_clientes.append(
            novo_cliente
        )

        print(
            "\nCliente cadastrado com sucesso!"
        )

        print(
            f"Código: {codigo_cliente}"
        )


    # ==========================================
    # 4 - BUSCAR CLIENTE
    # ==========================================

    elif opcao == "4":

        codigo_cliente = input(
            "\nDigite o código do cliente: "
        )

        cliente = buscar_cliente(
            codigo_cliente
        )

        if cliente:

            print(
                "\n========== CLIENTE =========="
            )

            print(
                f"Código: {cliente['codigo']}"
            )

            print(
                f"Nome: {cliente['nome']}"
            )

            print(
                f"Pontos: {cliente['pontos']}"
            )

            if cliente["pontos"] == 5:

                print(
                    "🎉 Cliente ganhou um Espresso grátis!"
                )

        else:

            print(
                "\nCliente não encontrado."
            )


    # ==========================================
    # 5 - CONSULTAS
    # ==========================================

    elif opcao == "5":

        print(
            "\n========== CONSULTAS =========="
        )

        print("1 - Estoque de produtos")
        print("2 - Estoque de ingredientes")
        print("3 - Vendas")
        print("4 - Clientes")
        print("0 - Voltar")

        consulta = input(
            "\nDigite uma opção: "
        )


        # ------------------------------------------
        # 1 - ESTOQUE DE PRODUTOS
        # ------------------------------------------

        if consulta == "1":

            mostrar_produtos()


        # ------------------------------------------
        # 2 - ESTOQUE DE INGREDIENTES
        # ------------------------------------------

        elif consulta == "2":

            print(
                "\n========== INGREDIENTES =========="
            )

            print(
                f"{'Código':<8}"
                f"{'Ingrediente':<25}"
                f"{'Quantidade':>12}"
            )

            print("-" * 45)

            for ingrediente in lista_ingredientes:

                print(
                    f"{ingrediente['codigo']:<8}"
                    f"{ingrediente['nome']:<25}"
                    f"{ingrediente['quantidade']:>12}"
                )


        # ------------------------------------------
        # 3 - VENDAS
        # ------------------------------------------

        elif consulta == "3":

            print(
                "\n========== VENDAS =========="
            )

            print(
                f"{'Código':<10}"
                f"{'Cliente':<15}"
                f"{'Valor Total':>15}"
            )

            print("-" * 40)

            faturamento_total = 0

            for venda in lista_vendas:

                print(
                    f"{venda['codigo']:<10}"
                    f"{venda['cliente']:<15}"
                    f"R$ {venda['valor_total']:>11.2f}"
                )

                faturamento_total = (
                    faturamento_total
                    + venda["valor_total"]
                )

            print("-" * 40)

            print(
                f"Total de vendas: "
                f"{len(lista_vendas)}"
            )

            print(
                f"Faturamento total: "
                f"R$ {faturamento_total:.2f}"
            )


        # ------------------------------------------
        # 4 - CLIENTES
        # ------------------------------------------

        elif consulta == "4":

            print(
                "\n========== CLIENTES =========="
            )

            print(
                f"{'Código':<8}"
                f"{'Nome':<25}"
                f"{'Pontos':>10}"
            )

            print("-" * 43)

            for cliente in lista_clientes:

                print(
                    f"{cliente['codigo']:<8}"
                    f"{cliente['nome']:<25}"
                    f"{cliente['pontos']:>10}"
                )


        # ------------------------------------------
        # 0 - VOLTAR
        # ------------------------------------------

        elif consulta == "0":

            print(
                "Voltando ao menu principal..."
            )


        else:

            print(
                "Opção de consulta inválida."
            )


    # ==========================================
    # 0 - ENCERRAR SISTEMA
    # ==========================================

    elif opcao == "0":

        sistema_funcionando = False

        print(
            "\nSistema encerrado."
        )


    # ==========================================
    # OPÇÃO INVÁLIDA
    # ==========================================

    else:

        print(
            "\nOp
