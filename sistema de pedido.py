# Sistema de Gerenciamento de Pedidos para Restaurante

def main():
    # Inicialização das estruturas de dados
    itens_menu = []  # Lista de itens do cardápio
    pedidos = []     # Lista de todos os pedidos
    fila_pendentes = []  # Fila de pedidos pendentes
    fila_aceitos = []    # Fila de pedidos aceitos
    fila_prontos = []    # Fila de pedidos prontos
    
    # Contadores para IDs automáticos
    proximo_id_item = 1
    proximo_id_pedido = 1
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GERENCIAMENTO DE RESTAURANTE")
        print("="*50)
        print("1. Gerenciar Menu de Itens")
        print("2. Gerenciar Pedidos")
        print("3. Consultar Pedidos")
        print("4. Relatório Diário")
        print("5. Sair")
        print("-"*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Submenu de Gerenciamento de Itens
            while True:
                print("\n--- GERENCIAR MENU DE ITENS ---")
                print("1. Cadastrar Novo Item")
                print("2. Atualizar Item")
                print("3. Consultar Todos os Itens")
                print("4. Voltar ao Menu Principal")
                
                sub_opcao = input("Escolha uma opção: ")
                
                if sub_opcao == "1":
                    # Cadastrar novo item
                    print("\n--- CADASTRAR NOVO ITEM ---")
                    nome = input("Nome do item: ")
                    descricao = input("Descrição: ")
                    
                    # Validação do preço
                    while True:
                        try:
                            preco = float(input("Preço: R$ "))
                            if preco <= 0:
                                print("O preço deve ser maior que zero!")
                                continue
                            break
                        except ValueError:
                            print("Digite um valor numérico válido!")
                    
                    # Validação do estoque
                    while True:
                        try:
                            estoque = int(input("Quantidade em estoque: "))
                            if estoque < 0:
                                print("O estoque não pode ser negativo!")
                                continue
                            break
                        except ValueError:
                            print("Digite um número inteiro válido!")
                    
                    # Criar novo item
                    novo_item = {
                        'codigo': proximo_id_item,
                        'nome': nome,
                        'descricao': descricao,
                        'preco': preco,
                        'estoque': estoque
                    }
                    
                    itens_menu.append(novo_item)
                    proximo_id_item += 1
                    print(f"Item '{nome}' cadastrado com sucesso! Código: {novo_item['codigo']}")
                
                elif sub_opcao == "2":
                    # Atualizar item
                    if not itens_menu:
                        print("Nenhum item cadastrado!")
                        continue
                    
                    print("\n--- ATUALIZAR ITEM ---")
                    codigo = int(input("Código do item a ser atualizado: "))
                    
                    item_encontrado = None
                    for item in itens_menu:
                        if item['codigo'] == codigo:
                            item_encontrado = item
                            break
                    
                    if not item_encontrado:
                        print("Item não encontrado!")
                        continue
                    
                    print(f"Editando item: {item_encontrado['nome']}")
                    novo_nome = input(f"Novo nome ({item_encontrado['nome']}): ") or item_encontrado['nome']
                    nova_desc = input(f"Nova descrição ({item_encontrado['descricao']}): ") or item_encontrado['descricao']
                    
                    # Validação do novo preço
                    while True:
                        try:
                            novo_preco = input(f"Novo preço (R$ {item_encontrado['preco']}): ")
                            if novo_preco == "":
                                novo_preco = item_encontrado['preco']
                                break
                            novo_preco = float(novo_preco)
                            if novo_preco <= 0:
                                print("O preço deve ser maior que zero!")
                                continue
                            break
                        except ValueError:
                            print("Digite um valor numérico válido!")
                    
                    # Validação do novo estoque
                    while True:
                        try:
                            novo_estoque = input(f"Novo estoque ({item_encontrado['estoque']}): ")
                            if novo_estoque == "":
                                novo_estoque = item_encontrado['estoque']
                                break
                            novo_estoque = int(novo_estoque)
                            if novo_estoque < 0:
                                print("O estoque não pode ser negativo!")
                                continue
                            break
                        except ValueError:
                            print("Digite um número inteiro válido!")
                    
                    # Atualizar item
                    item_encontrado['nome'] = novo_nome
                    item_encontrado['descricao'] = nova_desc
                    item_encontrado['preco'] = novo_preco
                    item_encontrado['estoque'] = novo_estoque
                    
                    print("Item atualizado com sucesso!")
                
                elif sub_opcao == "3":
                    # Consultar todos os itens
                    if not itens_menu:
                        print("Nenhum item cadastrado!")
                        continue
                    
                    print("\n--- TODOS OS ITENS DO CARDÁPIO ---")
                    for item in itens_menu:
                        print(f"Código: {item['codigo']}")
                        print(f"Nome: {item['nome']}")
                        print(f"Descrição: {item['descricao']}")
                        print(f"Preço: R$ {item['preco']:.2f}")
                        print(f"Estoque: {item['estoque']} unidades")
                        print("-" * 30)
                
                elif sub_opcao == "4":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao == "2":
            # Submenu de Gerenciamento de Pedidos
            while True:
                print("\n--- GERENCIAR PEDIDOS ---")
                print("1. Criar Novo Pedido")
                print("2. Processar Pedidos Pendentes")
                print("3. Atualizar Status de Pedido")
                print("4. Cancelar Pedido")
                print("5. Voltar ao Menu Principal")
                
                sub_opcao = input("Escolha uma opção: ")
                
                if sub_opcao == "1":
                    # Criar novo pedido
                    if not itens_menu:
                        print("Nenhum item disponível no cardápio!")
                        continue
                    
                    print("\n--- CRIAR NOVO PEDIDO ---")
                    
                    # Mostrar itens disponíveis
                    print("Itens disponíveis:")
                    for item in itens_menu:
                        if item['estoque'] > 0:
                            print(f"{item['codigo']} - {item['nome']} (R$ {item['preco']:.2f}) - Estoque: {item['estoque']}")
                    
                    itens_pedido = []
                    total = 0.0
                    
                    while True:
                        try:
                            codigo_item = int(input("Digite o código do item (0 para finalizar): "))
                            if codigo_item == 0:
                                break
                            
                            item_encontrado = None
                            for item in itens_menu:
                                if item['codigo'] == codigo_item:
                                    item_encontrado = item
                                    break
                            
                            if not item_encontrado:
                                print("Item não encontrado!")
                                continue
                            
                            if item_encontrado['estoque'] <= 0:
                                print("Item sem estoque disponível!")
                                continue
                            
                            quantidade = int(input(f"Quantidade de '{item_encontrado['nome']}': "))
                            
                            if quantidade <= 0:
                                print("Quantidade deve ser maior que zero!")
                                continue
                            
                            if quantidade > item_encontrado['estoque']:
                                print(f"Estoque insuficiente! Disponível: {item_encontrado['estoque']}")
                                continue
                            
                            # Adicionar item ao pedido
                            itens_pedido.append({
                                'codigo': item_encontrado['codigo'],
                                'nome': item_encontrado['nome'],
                                'preco': item_encontrado['preco'],
                                'quantidade': quantidade,
                                'subtotal': item_encontrado['preco'] * quantidade
                            })
                            
                            total += item_encontrado['preco'] * quantidade
                            print(f"Item adicionado! Subtotal: R$ {item_encontrado['preco'] * quantidade:.2f}")
                            
                        except ValueError:
                            print("Digite um valor numérico válido!")
                    
                    if not itens_pedido:
                        print("Pedido vazio! Cancelando operação.")
                        continue
                    
                    # Aplicar cupom de desconto
                    cupom = input("Digite o cupom de desconto (ou Enter para pular): ")
                    desconto = 0.0
                    
                    if cupom.upper() == "DESCONTO10":
                        desconto = total * 0.1
                        print(f"Desconto de 10% aplicado! Valor: R$ {desconto:.2f}")
                    elif cupom:
                        print("Cupom inválido ou inexistente!")
                    
                    total_final = total - desconto
                    
                    # Confirmar pedido
                    print(f"\nResumo do Pedido:")
                    for item in itens_pedido:
                        print(f"{item['quantidade']}x {item['nome']} - R$ {item['subtotal']:.2f}")
                    print(f"Total: R$ {total:.2f}")
                    print(f"Desconto: R$ {desconto:.2f}")
                    print(f"Total Final: R$ {total_final:.2f}")
                    
                    confirmar = input("Confirmar pedido? (S/N): ").upper()
                    
                    if confirmar == "S":
                        # Criar pedido
                        novo_pedido = {
                            'numero': proximo_id_pedido,
                            'itens': itens_pedido,
                            'status': 'AGUARDANDO APROVACAO',
                            'total': total,
                            'desconto': desconto,
                            'total_final': total_final,
                            'timestamp': '2024-01-01 12:00:00'  # Simulado
                        }
                        
                        # Atualizar estoque
                        for item_pedido in itens_pedido:
                            for item_menu in itens_menu:
                                if item_menu['codigo'] == item_pedido['codigo']:
                                    item_menu['estoque'] -= item_pedido['quantidade']
                                    break
                        
                        pedidos.append(novo_pedido)
                        fila_pendentes.append(novo_pedido)
                        proximo_id_pedido += 1
                        
                        print(f"Pedido #{novo_pedido['numero']} criado com sucesso!")
                    else:
                        print("Pedido cancelado!")
                
                elif sub_opcao == "2":
                    # Processar pedidos pendentes
                    if not fila_pendentes:
                        print("Nenhum pedido pendente para processar!")
                        continue
                    
                    print("\n--- PROCESSAR PEDIDOS PENDENTES ---")
                    
                    pedido_atual = fila_pendentes[0]
                    print(f"Pedido #{pedido_atual['numero']}")
                    print("Itens:")
                    for item in pedido_atual['itens']:
                        print(f"  {item['quantidade']}x {item['nome']} - R$ {item['subtotal']:.2f}")
                    print(f"Total: R$ {pedido_atual['total_final']:.2f}")
                    
                    decisao = input("Aceitar pedido? (S/N): ").upper()
                    
                    if decisao == "S":
                        pedido_atual['status'] = 'ACEITO'
                        fila_aceitos.append(pedido_atual)
                        fila_pendentes.pop(0)
                        print("Pedido aceito e movido para preparo!")
                    else:
                        pedido_atual['status'] = 'REJEITADO'
                        # Devolver itens ao estoque
                        for item_pedido in pedido_atual['itens']:
                            for item_menu in itens_menu:
                                if item_menu['codigo'] == item_pedido['codigo']:
                                    item_menu['estoque'] += item_pedido['quantidade']
                                    break
                        fila_pendentes.pop(0)
                        print("Pedido rejeitado!")
                
                elif sub_opcao == "3":
                    # Atualizar status do pedido
                    if not pedidos:
                        print("Nenhum pedido cadastrado!")
                        continue
                    
                    print("\n--- ATUALIZAR STATUS DO PEDIDO ---")
                    numero_pedido = int(input("Número do pedido: "))
                    
                    pedido_encontrado = None
                    for pedido in pedidos:
                        if pedido['numero'] == numero_pedido:
                            pedido_encontrado = pedido
                            break
                    
                    if not pedido_encontrado:
                        print("Pedido não encontrado!")
                        continue
                    
                    print(f"Pedido #{pedido_encontrado['numero']} - Status atual: {pedido_encontrado['status']}")
                    print("Status disponíveis:")
                    
                    if pedido_encontrado['status'] == 'AGUARDANDO APROVACAO':
                        print("1. ACEITO")
                        print("2. REJEITADO")
                        print("3. CANCELADO")
                    elif pedido_encontrado['status'] == 'ACEITO':
                        print("1. FAZENDO")
                        print("2. CANCELADO")
                    elif pedido_encontrado['status'] == 'FAZENDO':
                        print("1. FEITO")
                    elif pedido_encontrado['status'] == 'FEITO':
                        print("1. ESPERANDO ENTREGADOR")
                    elif pedido_encontrado['status'] == 'ESPERANDO ENTREGADOR':
                        print("1. SAIU PARA ENTREGA")
                    elif pedido_encontrado['status'] == 'SAIU PARA ENTREGA':
                        print("1. ENTREGUE")
                    
                    novo_status = input("Novo status: ").upper()
                    
                    # Validar transição de status
                    status_validos = {
                        'AGUARDANDO APROVACAO': ['ACEITO', 'REJEITADO', 'CANCELADO'],
                        'ACEITO': ['FAZENDO', 'CANCELADO'],
                        'FAZENDO': ['FEITO'],
                        'FEITO': ['ESPERANDO ENTREGADOR'],
                        'ESPERANDO ENTREGADOR': ['SAIU PARA ENTREGA'],
                        'SAIU PARA ENTREGA': ['ENTREGUE']
                    }
                    
                    if novo_status in status_validos.get(pedido_encontrado['status'], []):
                        pedido_encontrado['status'] = novo_status
                        
                        # Atualizar filas
                        if novo_status == 'ACEITO':
                            if pedido_encontrado in fila_pendentes:
                                fila_pendentes.remove(pedido_encontrado)
                            fila_aceitos.append(pedido_encontrado)
                        elif novo_status == 'FEITO':
                            if pedido_encontrado in fila_aceitos:
                                fila_aceitos.remove(pedido_encontrado)
                            fila_prontos.append(pedido_encontrado)
                        elif novo_status in ['REJEITADO', 'CANCELADO']:
                            # Devolver itens ao estoque se cancelado
                            if novo_status == 'CANCELADO':
                                for item_pedido in pedido_encontrado['itens']:
                                    for item_menu in itens_menu:
                                        if item_menu['codigo'] == item_pedido['codigo']:
                                            item_menu['estoque'] += item_pedido['quantidade']
                                            break
                            # Remover de todas as filas
                            if pedido_encontrado in fila_pendentes:
                                fila_pendentes.remove(pedido_encontrado)
                            if pedido_encontrado in fila_aceitos:
                                fila_aceitos.remove(pedido_encontrado)
                            if pedido_encontrado in fila_prontos:
                                fila_prontos.remove(pedido_encontrado)
                        
                        print("Status atualizado com sucesso!")
                    else:
                        print("Transição de status inválida!")
                
                elif sub_opcao == "4":
                    # Cancelar pedido
                    if not pedidos:
                        print("Nenhum pedido cadastrado!")
                        continue
                    
                    print("\n--- CANCELAR PEDIDO ---")
                    numero_pedido = int(input("Número do pedido: "))
                    
                    pedido_encontrado = None
                    for pedido in pedidos:
                        if pedido['numero'] == numero_pedido:
                            pedido_encontrado = pedido
                            break
                    
                    if not pedido_encontrado:
                        print("Pedido não encontrado!")
                        continue
                    
                    if pedido_encontrado['status'] not in ['AGUARDANDO APROVACAO', 'ACEITO']:
                        print("Pedido não pode ser cancelado (já em preparação ou finalizado)!")
                        continue
                    
                    confirmar = input(f"Confirmar cancelamento do pedido #{numero_pedido}? (S/N): ").upper()
                    
                    if confirmar == "S":
                        pedido_encontrado['status'] = 'CANCELADO'
                        
                        # Devolver itens ao estoque
                        for item_pedido in pedido_encontrado['itens']:
                            for item_menu in itens_menu:
                                if item_menu['codigo'] == item_pedido['codigo']:
                                    item_menu['estoque'] += item_pedido['quantidade']
                                    break
                        
                        # Remover de todas as filas
                        if pedido_encontrado in fila_pendentes:
                            fila_pendentes.remove(pedido_encontrado)
                        if pedido_encontrado in fila_aceitos:
                            fila_aceitos.remove(pedido_encontrado)
                        
                        print("Pedido cancelado com sucesso!")
                    else:
                        print("Cancelamento abortado!")
                
                elif sub_opcao == "5":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao == "3":
            # Consultar pedidos
            if not pedidos:
                print("Nenhum pedido cadastrado!")
                continue
            
            print("\n--- CONSULTAR PEDIDOS ---")
            print("1. Todos os pedidos")
            print("2. Filtrar por status")
            
            sub_opcao = input("Escolha uma opção: ")
            
            if sub_opcao == "1":
                print("\n--- TODOS OS PEDIDOS ---")
                for pedido in pedidos:
                    print(f"Pedido #{pedido['numero']}")
                    print(f"Status: {pedido['status']}")
                    print(f"Total: R$ {pedido['total_final']:.2f}")
                    print("-" * 30)
            
            elif sub_opcao == "2":
                status_filtro = input("Digite o status para filtrar: ").upper()
                print(f"\n--- PEDIDOS COM STATUS: {status_filtro} ---")
                
                encontrados = False
                for pedido in pedidos:
                    if pedido['status'] == status_filtro:
                        print(f"Pedido #{pedido['numero']}")
                        print("Itens:")
                        for item in pedido['itens']:
                            print(f"  {item['quantidade']}x {item['nome']} - R$ {item['subtotal']:.2f}")
                        print(f"Total: R$ {pedido['total_final']:.2f}")
                        print("-" * 30)
                        encontrados = True
                
                if not encontrados:
                    print(f"Nenhum pedido com status '{status_filtro}' encontrado!")
            
            else:
                print("Opção inválida!")
        
        elif opcao == "4":
            # Relatório diário
            print("\n--- RELATÓRIO DIÁRIO ---")
            
            total_vendas = 0.0
            pedidos_entregues = 0
            pedidos_cancelados = 0
            
            for pedido in pedidos:
                if pedido['status'] == 'ENTREGUE':
                    total_vendas += pedido['total_final']
                    pedidos_entregues += 1
                elif pedido['status'] in ['CANCELADO', 'REJEITADO']:
                    pedidos_cancelados += 1
            
            print(f"Total de pedidos: {len(pedidos)}")
            print(f"Pedidos entregues: {pedidos_entregues}")
            print(f"Pedidos cancelados/rejeitados: {pedidos_cancelados}")
            print(f"Valor total em vendas: R$ {total_vendas:.2f}")
            
            # Itens mais vendidos
            if pedidos_entregues > 0:
                print("\n--- ITENS MAIS VENDIDOS ---")
                vendas_por_item = []
                
                for item_menu in itens_menu:
                    quantidade_vendida = 0
                    for pedido in pedidos:
                        if pedido['status'] == 'ENTREGUE':
                            for item_pedido in pedido['itens']:
                                if item_pedido['codigo'] == item_menu['codigo']:
                                    quantidade_vendida += item_pedido['quantidade']
                    
                    if quantidade_vendida > 0:
                        vendas_por_item.append((item_menu['nome'], quantidade_vendida))
                
                # Ordenar por quantidade vendida (decrescente)
                for i in range(len(vendas_por_item)):
                    for j in range(i + 1, len(vendas_por_item)):
                        if vendas_por_item[j][1] > vendas_por_item[i][1]:
                            vendas_por_item[i], vendas_por_item[j] = vendas_por_item[j], vendas_por_item[i]
                
                for nome, quantidade in vendas_por_item[:5]:  # Top 5
                    print(f"{nome}: {quantidade} unidades")
        
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
