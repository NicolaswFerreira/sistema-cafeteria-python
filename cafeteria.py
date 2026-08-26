# ==========================================
# SISTEMA DE GERENCIAMENTO - CAFETERIA
# Versão com funções, validações e arquivos CSV
# ==========================================

import csv
import os

ARQUIVO_CLIENTES = "clientes.csv"
ARQUIVO_PRODUTOS = "produtos.csv"
ARQUIVO_INGREDIENTES = "ingredientes.csv"
ARQUIVO_VENDAS = "vendas.csv"
ARQUIVO_ITENS_VENDA = "itens_venda.csv"

PONTOS_PARA_CAFE_GRATIS = 5


# ==========================================
# DADOS INICIAIS
# ==========================================

PRODUTOS_INICIAIS = [
    {"codigo":"P001","nome":"Café Espresso Pequeno","preco":4.00,"estoque":20,"ingredientes":{"cafe_pó":1,"acucar":1}},
    {"codigo":"P002","nome":"Café Espresso Médio","preco":5.00,"estoque":20,"ingredientes":{"cafe_pó":1,"acucar":1,"leite":1}},
    {"codigo":"P003","nome":"Café Espresso Grande","preco":6.00,"estoque":20,"ingredientes":{"cafe_pó":2,"acucar":1,"leite":1}},
    {"codigo":"P004","nome":"Brownie","preco":7.00,"estoque":10,"ingredientes":{"chocolate":1,"massa":1}},
    {"codigo":"P005","nome":"Pão de Queijo","preco":5.00,"estoque":30,"ingredientes":{"pao":1,"queijo":1}},
    {"codigo":"P006","nome":"Misto","preco":8.00,"estoque":15,"ingredientes":{"pao":1,"queijo":1,"presunto":1}},
    {"codigo":"P007","nome":"Água com Gás","preco":4.00,"estoque":20,"ingredientes":{}},
    {"codigo":"P008","nome":"Refrigerante","preco":6.00,"estoque":15,"ingredientes":{}},
    {"codigo":"P009","nome":"Suco","preco":7.00,"estoque":15,"ingredientes":{"frutas":1}},
    {"codigo":"P010","nome":"Panqueca","preco":10.00,"estoque":10,"ingredientes":{"massa":1,"leite":1}},
    {"codigo":"P011","nome":"Tapioca","preco":9.00,"estoque":10,"ingredientes":{"massa":1}},
    {"codigo":"P012","nome":"Sanduíche Natural","preco":10.00,"estoque":10,"ingredientes":{"pao":1,"frango":1}},
    {"codigo":"P013","nome":"Sorvete","preco":7.00,"estoque":15,"ingredientes":{"leite":1}}
]

CLIENTES_INICIAIS = [
    {"codigo":"C001","nome":"Nicolas Ferreira","pontos":0,"cafes_gratis":0},
    {"codigo":"C002","nome":"João Silva","pontos":3,"cafes_gratis":0},
    {"codigo":"C003","nome":"Maria Santos","pontos":4,"cafes_gratis":0}
]

INGREDIENTES_INICIAIS = [
    {"codigo":"I001","nome":"cafe_pó","quantidade":50},
    {"codigo":"I002","nome":"acucar","quantidade":100},
    {"codigo":"I003","nome":"leite","quantidade":30},
    {"codigo":"I004","nome":"pao","quantidade":40},
    {"codigo":"I005","nome":"queijo","quantidade":30},
    {"codigo":"I006","nome":"presunto","quantidade":30},
    {"codigo":"I007","nome":"frango","quantidade":20},
    {"codigo":"I008","nome":"chocolate","quantidade":20},
    {"codigo":"I009","nome":"massa","quantidade":30},
    {"codigo":"I010","nome":"frutas","quantidade":30}
]

lista_produtos = []
lista_clientes = []
lista_ingredientes = []
lista_vendas = []


# ==========================================
# ENTRADA E VALIDAÇÃO
# ==========================================

def ler_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).strip()
        if valor in opcoes:
            return valor
        print("Opção inválida. Tente novamente.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue

            return valor

        except ValueError:
            print("Digite um número inteiro válido.")


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()

        if nome:
            return nome

        print("O nome não pode ficar vazio.")


# ==========================================
# BUSCAS
# ==========================================

def buscar_produto(codigo):
    for produto in lista_produtos:
        if produto["codigo"].upper() == codigo.upper():
            return produto
    return None


def buscar_cliente(codigo):
    for cliente in lista_clientes:
        if cliente["codigo"].upper() == codigo.upper():
            return cliente
    return None


def buscar_venda(codigo):
    for venda in lista_vendas:
        if venda["codigo"].upper() == codigo.upper():
            return venda
    return None


def buscar_ingrediente(nome):
    for ingrediente in lista_ingredientes:
        if ingrediente["nome"] == nome:
            return ingrediente
    return None


def proximo_codigo(lista, prefixo):
    maior = 0

    for item in lista:
        try:
            numero = int(item["codigo"][1:])
            if numero > maior:
                maior = numero
        except (ValueError, KeyError):
            pass

    return f"{prefixo}{maior + 1:03d}"


# ==========================================
# EXIBIÇÃO
# ==========================================

def mostrar_produtos():
    print("\n========== PRODUTOS ==========")
    print(f"{'Código':<8}{'Nome':<30}{'Preço':>10}{'Estoque':>10}")
    print("-" * 58)

    for produto in lista_produtos:
        print(
            f"{produto['codigo']:<8}"
            f"{produto['nome']:<30}"
            f"R$ {produto['preco']:>7.2f}"
            f"{produto['estoque']:>10}"
        )


def mostrar_ingredientes():
    print("\n========== INGREDIENTES ==========")
    print(f"{'Código':<8}{'Ingrediente':<25}{'Quantidade':>12}")
    print("-" * 45)

    for ingrediente in lista_ingredientes:
        print(
            f"{ingrediente['codigo']:<8}"
            f"{ingrediente['nome']:<25}"
            f"{ingrediente['quantidade']:>12}"
        )


def mostrar_clientes():
    print("\n========== CLIENTES ==========")
    print(
        f"{'Código':<8}"
        f"{'Nome':<25}"
        f"{'Pontos':>10}"
        f"{'Cafés grátis':>15}"
    )
    print("-" * 58)

    for cliente in lista_clientes:
        print(
            f"{cliente['codigo']:<8}"
            f"{cliente['nome']:<25}"
            f"{cliente['pontos']:>10}"
            f"{cliente['cafes_gratis']:>15}"
        )


def mostrar_vendas():
    print("\n========== VENDAS ==========")
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

        faturamento_total += venda["valor_total"]

    print("-" * 40)
    print(f"Total de vendas: {len(lista_vendas)}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")


# ==========================================
# ARQUIVOS CSV
# ==========================================

def salvar_clientes():
    with open(
        ARQUIVO_CLIENTES,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo, delimiter=";")

        writer.writerow([
            "codigo",
            "nome",
            "pontos",
            "cafes_gratis"
        ])

        for cliente in lista_clientes:
            writer.writerow([
                cliente["codigo"],
                cliente["nome"],
                cliente["pontos"],
                cliente["cafes_gratis"]
            ])


def carregar_clientes():
    if not os.path.exists(ARQUIVO_CLIENTES):
        lista_clientes.extend(CLIENTES_INICIAIS)
        salvar_clientes()
        return

    with open(
        ARQUIVO_CLIENTES,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        reader = csv.DictReader(arquivo, delimiter=";")

        for linha in reader:
            lista_clientes.append({
                "codigo": linha["codigo"],
                "nome": linha["nome"],
                "pontos": int(linha["pontos"]),
                "cafes_gratis": int(
                    linha.get("cafes_gratis", 0)
                )
            })


def salvar_produtos():
    with open(
        ARQUIVO_PRODUTOS,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo, delimiter=";")

        writer.writerow([
            "codigo",
            "nome",
            "preco",
            "estoque"
        ])

        for produto in lista_produtos:
            writer.writerow([
                produto["codigo"],
                produto["nome"],
                produto["preco"],
                produto["estoque"]
            ])


def carregar_produtos():
    if not os.path.exists(ARQUIVO_PRODUTOS):
        lista_produtos.extend(PRODUTOS_INICIAIS)
        salvar_produtos()
        return

    with open(
        ARQUIVO_PRODUTOS,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        reader = csv.DictReader(arquivo, delimiter=";")

        for linha in reader:

            ingredientes = {}

            for produto_inicial in PRODUTOS_INICIAIS:

                if produto_inicial["codigo"] == linha["codigo"]:
                    ingredientes = (
                        produto_inicial["ingredientes"].copy()
                    )
                    break

            lista_produtos.append({
                "codigo": linha["codigo"],
                "nome": linha["nome"],
                "preco": float(linha["preco"]),
                "estoque": int(linha["estoque"]),
                "ingredientes": ingredientes
            })


def salvar_ingredientes():
    with open(
        ARQUIVO_INGREDIENTES,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo, delimiter=";")

        writer.writerow([
            "codigo",
            "nome",
            "quantidade"
        ])

        for ingrediente in lista_ingredientes:
            writer.writerow([
                ingrediente["codigo"],
                ingrediente["nome"],
                ingrediente["quantidade"]
            ])


def carregar_ingredientes():
    if not os.path.exists(ARQUIVO_INGREDIENTES):
        lista_ingredientes.extend(INGREDIENTES_INICIAIS)
        salvar_ingredientes()
        return

    with open(
        ARQUIVO_INGREDIENTES,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        reader = csv.DictReader(arquivo, delimiter=";")

        for linha in reader:
            lista_ingredientes.append({
                "codigo": linha["codigo"],
                "nome": linha["nome"],
                "quantidade": int(linha["quantidade"])
            })


def salvar_vendas():
    with open(
        ARQUIVO_VENDAS,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo, delimiter=";")

        writer.writerow([
            "codigo",
            "cliente",
            "valor_total"
        ])

        for venda in lista_vendas:
            writer.writerow([
                venda["codigo"],
                venda["cliente"],
                venda["valor_total"]
            ])

    with open(
        ARQUIVO_ITENS_VENDA,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo, delimiter=";")

        writer.writerow([
            "venda",
            "produto",
            "nome",
            "quantidade",
            "preco",
            "subtotal"
        ])

        for venda in lista_vendas:

            for item in venda["produtos"]:

                writer.writerow([
                    venda["codigo"],
                    item["produto"],
                    item["nome"],
                    item["quantidade"],
                    item["preco"],
                    item["subtotal"]
                ])


def carregar_vendas():
    if not os.path.exists(ARQUIVO_VENDAS):
        return

    with open(
        ARQUIVO_VENDAS,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        reader = csv.DictReader(arquivo, delimiter=";")

        for linha in reader:
            lista_vendas.append({
                "codigo": linha["codigo"],
                "cliente": linha["cliente"],
                "produtos": [],
                "valor_total": float(linha["valor_total"])
            })

    if not os.path.exists(ARQUIVO_ITENS_VENDA):
        return

    with open(
        ARQUIVO_ITENS_VENDA,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        reader = csv.DictReader(arquivo, delimiter=";")

        for linha in reader:

            venda = buscar_venda(linha["venda"])

            if venda:
                venda["produtos"].append({
                    "produto": linha["produto"],
                    "nome": linha["nome"],
                    "quantidade": int(linha["quantidade"]),
                    "preco": float(linha["preco"]),
                    "subtotal": float(linha["subtotal"])
                })


def salvar_dados():
    salvar_clientes()
    salvar_produtos()
    salvar_ingredientes()
    salvar_vendas()


def carregar_dados():
    carregar_clientes()
    carregar_produtos()
    carregar_ingredientes()
    carregar_vendas()


# ==========================================
# ESTOQUE
# ==========================================

def verificar_ingredientes_disponiveis(
    produto,
    quantidade
):
    for nome, quantidade_por_produto in (
        produto["ingredientes"].items()
    ):

        ingrediente = buscar_ingrediente(nome)

        if ingrediente is None:
            return (
                False,
                f"Ingrediente {nome} não cadastrado."
            )

        necessario = (
            quantidade_por_produto
            * quantidade
        )

        if ingrediente["quantidade"] < necessario:
            return (
                False,
                f"Estoque insuficiente de {nome}. "
                f"Necessário: {necessario}. "
                f"Disponível: "
                f"{ingrediente['quantidade']}."
            )

    return True, ""


def verificar_estoque_pedido(pedido):
    consumo_produtos = {}
    consumo_ingredientes = {}

    for item in pedido:

        codigo = item["produto"]

        consumo_produtos[codigo] = (
            consumo_produtos.get(codigo, 0)
            + item["quantidade"]
        )

        produto = buscar_produto(codigo)

        for (
            nome,
            quantidade_por_produto
        ) in produto["ingredientes"].items():

            consumo_ingredientes[nome] = (
                consumo_ingredientes.get(nome, 0)
                + quantidade_por_produto
                * item["quantidade"]
            )

    for codigo, quantidade in (
        consumo_produtos.items()
    ):

        produto = buscar_produto(codigo)

        if quantidade > produto["estoque"]:
            return (
                False,
                f"Estoque insuficiente de "
                f"{produto['nome']}. "
                f"Necessário: {quantidade}. "
                f"Disponível: {produto['estoque']}."
            )

    for nome, quantidade in (
        consumo_ingredientes.items()
    ):

        ingrediente = buscar_ingrediente(nome)

        if ingrediente is None:
            return (
                False,
                f"Ingrediente {nome} não cadastrado."
            )

        if quantidade > ingrediente["quantidade"]:
            return (
                False,
                f"Estoque insuficiente de {nome}. "
                f"Necessário: {quantidade}. "
                f"Disponível: "
                f"{ingrediente['quantidade']}."
            )

    return True, ""


def baixar_estoques(pedido):
    for item in pedido:

        produto = buscar_produto(
            item["produto"]
        )

        produto["estoque"] -= (
            item["quantidade"]
        )

        for (
            nome,
            quantidade_por_produto
        ) in produto["ingredientes"].items():

            ingrediente = buscar_ingrediente(nome)

            if ingrediente:
                ingrediente["quantidade"] -= (
                    quantidade_por_produto
                    * item["quantidade"]
                )


# ==========================================
# VENDA
# ==========================================

def criar_item_pedido(
    produto,
    quantidade,
    gratis=False
):
    preco = (
        0.00
        if gratis
        else produto["preco"]
    )

    return {
        "produto": produto["codigo"],
        "nome": produto["nome"],
        "quantidade": quantidade,
        "preco": preco,
        "subtotal": preco * quantidade
    }


def mostrar_resumo_pedido(
    pedido,
    cliente
):
    valor_total = sum(
        item["subtotal"]
        for item in pedido
    )

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

    return valor_total


def iniciar_venda():

    codigo_cliente = input(
        "\nDigite o código do cliente: "
    ).strip()

    cliente = buscar_cliente(
        codigo_cliente
    )

    if cliente is None:

        print("\nCliente não encontrado.")

        cadastrar = ler_opcao(
            "Deseja cadastrar este cliente? "
            "1 - Sim / 2 - Não: ",
            ["1", "2"]
        )

        if cadastrar == "2":
            print("Venda cancelada.")
            return

        nome_cliente = ler_nome(
            "Digite o nome completo do cliente: "
        )

        codigo_cliente = proximo_codigo(
            lista_clientes,
            "C"
        )

        cliente = {
            "codigo": codigo_cliente,
            "nome": nome_cliente,
            "pontos": 0,
            "cafes_gratis": 0
        }

        lista_clientes.append(cliente)

        print(
            "\nCliente cadastrado com sucesso!"
        )

        print(
            f"Código do cliente: "
            f"{codigo_cliente}"
        )

    pedido = []

    while True:

        mostrar_produtos()

        codigo_produto = input(
            "\nDigite o código do produto "
            "(ou 0 para cancelar): "
        ).strip()

        if codigo_produto == "0":
            print("\nVenda cancelada.")
            return

        produto = buscar_produto(
            codigo_produto
        )

        if produto is None:
            print("Produto não encontrado.")
            continue

        quantidade = ler_inteiro(
            "Digite a quantidade: ",
            minimo=1
        )

        if quantidade > produto["estoque"]:
            print(
                "Quantidade maior que o "
                "estoque disponível."
            )
            continue

        disponivel, mensagem = (
            verificar_ingredientes_disponiveis(
                produto,
                quantidade
            )
        )

        if not disponivel:
            print(mensagem)
            continue

        usar_cafe_gratis = False

        if (
            produto["codigo"] == "P001"
            and cliente["cafes_gratis"] > 0
            and quantidade == 1
        ):

            usar = ler_opcao(
                f"Cliente possui "
                f"{cliente['cafes_gratis']} café(s) grátis. "
                "Usar nesta compra? "
                "1 - Sim / 2 - Não: ",
                ["1", "2"]
            )

            if usar == "1":
                usar_cafe_gratis = True
                cliente["cafes_gratis"] -= 1

        elif (
            produto["codigo"] == "P001"
            and cliente["cafes_gratis"] > 0
            and quantidade > 1
        ):

            print(
                "O café grátis pode ser usado "
                "apenas para 1 espresso por vez."
            )

        item = criar_item_pedido(
            produto,
            quantidade,
            gratis=usar_cafe_gratis
        )

        pedido.append(item)

        if usar_cafe_gratis:
            print(
                "\nCafé grátis aplicado."
            )
        else:
            print(
                "\nProduto adicionado ao pedido."
            )

        continuar = ler_opcao(
            "\nDeseja adicionar outro produto? "
            "1 - Sim / 2 - Não: ",
            ["1", "2"]
        )

        if continuar == "2":
            break

    if not pedido:

        print(
            "\nNenhum produto foi adicionado."
        )

        print(
            "Venda cancelada."
        )

        return

    disponivel, mensagem = (
        verificar_estoque_pedido(
            pedido
        )
    )

    if not disponivel:

        for item in pedido:

            if (
                item["produto"] == "P001"
                and item["preco"] == 0
            ):
                cliente["cafes_gratis"] += 1

        print(
            f"\nNão foi possível concluir "
            f"a venda: {mensagem}"
        )

        print(
            "Venda cancelada."
        )

        return

    valor_total = mostrar_resumo_pedido(
        pedido,
        cliente
    )

    confirmacao = ler_opcao(
        "\nDeseja confirmar a venda? "
        "1 - Confirmar / 2 - Cancelar: ",
        ["1", "2"]
    )

    if confirmacao == "2":

        for item in pedido:

            if (
                item["produto"] == "P001"
                and item["preco"] == 0
            ):
                cliente["cafes_gratis"] += 1

        print(
            "\nVenda cancelada."
        )

        return

    baixar_estoques(
        pedido
    )

    cliente["pontos"] += 1

    if cliente["pontos"] >= (
        PONTOS_PARA_CAFE_GRATIS
    ):

        cliente["pontos"] -= (
            PONTOS_PARA_CAFE_GRATIS
        )

        cliente["cafes_gratis"] += 1

        print(
            "\n🎉 Cliente atingiu 5 pontos "
            "e ganhou 1 café grátis!"
        )

    codigo_venda = proximo_codigo(
        lista_vendas,
        "V"
    )

    venda = {
        "codigo": codigo_venda,
        "cliente": cliente["codigo"],
        "produtos": pedido,
        "valor_total": valor_total
    }

    lista_vendas.append(venda)

    salvar_dados()

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
        f"Valor total: R$ "
        f"{valor_total:.2f}"
    )

    print(
        f"Pontos atuais: "
        f"{cliente['pontos']}"
    )

    print(
        f"Cafés grátis disponíveis: "
        f"{cliente['cafes_gratis']}"
    )


# ==========================================
# CLIENTES E VENDAS
# ==========================================

def buscar_venda_menu():

    codigo = input(
        "\nDigite o código da venda: "
    ).strip()

    venda = buscar_venda(
        codigo
    )

    if not venda:

        print(
            "\nVenda não encontrada."
        )

        return

    cliente = buscar_cliente(
        venda["cliente"]
    )

    print(
        "\n========== VENDA ENCONTRADA =========="
    )

    print(
        f"Código: {venda['codigo']}"
    )

    if cliente:
        print(
            f"Cliente: {cliente['nome']}"
        )
    else:
        print(
            f"Cliente: {venda['cliente']}"
        )

    print(
        f"Valor total: "
        f"R$ {venda['valor_total']:.2f}"
    )

    print("\nProdutos:")

    for item in venda["produtos"]:

        print(
            f"- {item['nome']} | "
            f"Qtd.: {item['quantidade']} | "
            f"R$ {item['subtotal']:.2f}"
        )


def cadastrar_cliente():

    nome = ler_nome(
        "\nDigite o nome completo do cliente: "
    )

    codigo = proximo_codigo(
        lista_clientes,
        "C"
    )

    cliente = {
        "codigo": codigo,
        "nome": nome,
        "pontos": 0,
        "cafes_gratis": 0
    }

    lista_clientes.append(
        cliente
    )

    salvar_clientes()

    print(
        "\nCliente cadastrado com sucesso!"
    )

    print(
        f"Código: {codigo}"
    )


def buscar_cliente_menu():

    codigo = input(
        "\nDigite o código do cliente: "
    ).strip()

    cliente = buscar_cliente(
        codigo
    )

    if not cliente:

        print(
            "\nCliente não encontrado."
        )

        return

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

    print(
        f"Cafés grátis: "
        f"{cliente['cafes_gratis']}"
    )


# ==========================================
# CONSULTAS
# ==========================================

def consultas():

    while True:

        print(
            "\n========== CONSULTAS =========="
        )

        print(
            "1 - Estoque de produtos"
        )

        print(
            "2 - Estoque de ingredientes"
        )

        print(
            "3 - Vendas"
        )

        print(
            "4 - Clientes"
        )

        print(
            "0 - Voltar"
        )

        opcao = ler_opcao(
            "\nDigite uma opção: ",
            ["0", "1", "2", "3", "4"]
        )

        if opcao == "1":
            mostrar_produtos()

        elif opcao == "2":
            mostrar_ingredientes()

        elif opcao == "3":
            mostrar_vendas()

        elif opcao == "4":
            mostrar_clientes()

        elif opcao == "0":

            print(
                "Voltando ao menu principal..."
            )

            return


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu_principal():

    sistema_funcionando = True

    while sistema_funcionando:

        print(
            "\n===================================="
        )

        print(
            "       SISTEMA DA CAFETERIA"
        )

        print(
            "===================================="
        )

        print(
            "1 - Iniciar venda"
        )

        print(
            "2 - Buscar venda"
        )

        print(
            "3 - Cadastrar cliente"
        )

        print(
            "4 - Buscar cliente"
        )

        print(
            "5 - Consultas"
        )

        print(
            "0 - Encerrar sistema"
        )

        opcao = ler_opcao(
            "\nDigite uma opção: ",
            ["0", "1", "2", "3", "4", "5"]
        )

        if opcao == "1":
            iniciar_venda()

        elif opcao == "2":
            buscar_venda_menu()

        elif opcao == "3":
            cadastrar_cliente()

        elif opcao == "4":
            buscar_cliente_menu()

        elif opcao == "5":
            consultas()

        elif opcao == "0":

            sistema_funcionando = False

            salvar_dados()

            print(
                "\nSistema encerrado."
            )


# ==========================================
# INICIALIZAÇÃO
# ==========================================

carregar_dados()
menu_principal()
