# DICIONÁRIO: armazena os dados principais do moto clube
moto_clube = {
    "nome": "Asfalto de Ferro",
    "fundacao": 2000,
    "cidade": "São Paulo - SP"
}

# LISTA: armazena as categorias de motos aceitas 
categorias_motos = ["Custom", "Chopper", "Bobber", "Cafe Racer", "Sport"]
 
# Lista de dicionários avançada
lineup_bandas = [
    {
        "nome": "Iron Maiden",
        "genero": "Heavy Metal",
        "integrantes": ["Bruce Dickinson", "Steve Harris", "Nicko McBrain"],
        "cache": 150000.00,
        "confirmada": True
    },
    {
        "nome": "AC/DC",
        "genero": "Hard Rock",
        "integrantes": ["Angus Young", "Brian Johnson", "Cliff Williams"],
        "cache": 180000.00,
        "confirmada": True
    },
    {
        "nome": "Metallica",
        "genero": "Thrash Metal",
        "integrantes": ["James Hetfield", "Lars Ulrich", "Kirk Hammett"],
        "cache": 200000.00,
        "confirmada": False
    }
]
 
 
# Puxa o valor da chave "nome" do dicionário moto_clube
# O método upper() transforma o texto em letras maiúsculas
def exibir_cabecalho():
    nome_formatado = moto_clube["nome"].upper()
    print("-" * 50)

    # Imprime o nome do sistema usando a variável nome_formatado
    # Essa variável recebeu o nome armazenado em moto_clube["nome"]
    print(f"SISTEMA DE GESTÃO: {nome_formatado}")

    # Puxa a cidade da chave "cidade" do dicionário moto_clube
    # Puxa o ano da chave "fundacao" e converte para texto com str()
    print("Sede: " + moto_clube["cidade"] +
          " | Desde: " + str(moto_clube["fundacao"]))
    print("-" * 50)
 
def listar_categorias_motos():
# Imprime um título fixo, escrito diretamente no código
    print("\nCATEGORIAS DE MOTOS ACEITAS NO ENCONTRO:")

    # Percorre a lista categorias_motos
    # A variável categoria recebe um item da lista a cada repetição
    # A variável i recebe a numeração iniciada em 1
    for i, categoria in enumerate(categorias_motos, start=1):
        # Imprime o número i e o nome da categoria atual
        # Os dados vêm do enumerate() e da lista categorias_motos
        print(f"  {i}. {categoria}")
 
 
def exibir_detalhes_banda(banda):
    """Exibe os detalhes de uma única banda."""
    # Verifica a chave "confirmada" do dicionário da banda
    # Se for True, utiliza "CONFIRMADA"; caso contrário, usa o outro texto
    status = "CONFIRMADA" if banda["confirmada"] else "AGUARDANDO CONFIRMAÇÃO"
    # Os valores de nome e genero vêm do dicionário banda
    print(f"\nBanda: {banda['nome']} | Gênero: [{banda['genero']}]")
    # O status exibido vem da variável status, calculada acima
    print(f"Status: {status}")
    # O valor do cachê vem da chave "cache" do dicionário banda
    # :,.2f formata o número com separador de milhar e duas casas decimais
    print(f"Cachê: R$ {banda['cache']:,.2f}")
    # Os integrantes vêm da lista armazenada na chave "integrantes"
    # join() reúne os nomes, separando-os por vírgula
    print(f"Integrantes: {', '.join(banda['integrantes'])}")
 
 
def listar_todas_bandas():
    # Texto fixo: não vem de uma lista nem de um dicionário
    print("\nLINEUP COMPLETO DO ROCK FESTIVAL:")
    # Verifica se a lista lineup_bandas está vazia
    if not lineup_bandas:
        # Imprime a mensagem caso não existam bandas cadastradas
        print("Nenhuma banda cadastrada no momento.")
        return
    # Percorre cada dicionário existente na lista lineup_bandas
    for banda in lineup_bandas:
        # Envia o dicionário da banda atual para a função de exibição
        # Os prints dos detalhes buscarão os valores nesse dicionário
        exibir_detalhes_banda(banda)
 
 
def adicionar_banda():
# Texto fixo que identifica a operação
    print("\nADICIONAR NOVA BANDA")
    # O usuário digita o nome da banda
    nome = input("Nome da banda: ").strip()
    genero = input("Gênero musical: ").strip()
    # A variável cache recebe o valor digitado e convertido para número
    # Se o valor for inválido ou negativo, uma mensagem será exibida
    try:
        cache = float(input("Valor do cachê (R$): ").replace(",", "."))
        if cache < 0:
            print("O cachê não pode ser negativo. Definido como R$ 0,00.")
            cache = 0.00
    except ValueError:
        print("Valor inválido! Definido como R$ 0,00.")
        cache = 0.00
    # Os integrantes digitados são separados por vírgulas
    # O resultado é armazenado na lista lista_integrantes
    integrantes_input = input("Integrantes (separados por vírgula): ")
    lista_integrantes = [
        i.strip() for i in integrantes_input.split(",") if i.strip()
    ]
    # Cria um novo dicionário com os dados coletados
    nova_banda = {
        "nome": nome,
        "genero": genero,
        "integrantes": lista_integrantes,
        "cache": cache,
        "confirmada": True
    }
    # Adiciona o novo dicionário à lista principal lineup_bandas
    lineup_bandas.append(nova_banda)
    # O print utiliza o valor digitado e armazenado na variável nome
    print(f"\n{nome} adicionada ao lineup com sucesso!")
 
 
def remover_banda():
    print("\nREMOVER BANDA DO LINEUP")
 
    if not lineup_bandas:
        print("Nenhuma banda disponível para remover.")
        return
 
    for indice, banda in enumerate(lineup_bandas, start=1):
        print(f"  [{indice}] - {banda['nome']}")
 
    try:
        escolha = int(input("\nDigite o número da banda que deseja remover: "))
        indice_real = escolha - 1
 
        if 0 <= indice_real < len(lineup_bandas):
            banda_removida = lineup_bandas.pop(indice_real)
            print(f"\n{banda_removida['nome']} foi removida do festival!")
        else:
            print("\nNúmero inválido! Nenhuma banda foi removida.")
 
    except ValueError:
        print("\nEntrada inválida! Digite apenas números.")
 
 
def listar_bandas_por_categoria():
    print("\nLISTAR BANDAS POR CATEGORIA (GÊNERO)")
    categoria_busca = input("Digite o gênero musical que procura: ").strip().lower()
    encontrou = False
 
    for banda in lineup_bandas:
        if categoria_busca in banda["genero"].lower():
            exibir_detalhes_banda(banda)
            encontrou = True
 
    if not encontrou:
        print(f"\nNenhuma banda encontrada na categoria '{categoria_busca}'.")
 
 
# --- NOVA FUNÇÃO: DOAÇÕES VOLUNTÁRIAS ---
 
def realizar_doacao():
    print("\n" + "=" * 50)
    print(" APOIE O ASFALTO DE FERRO ROCK FESTIVAL! ")
    print("=" * 50)
    print("O rock une gerações, acelera corações e fortalece amizades!")
    print("Se desejar, você pode contribuir voluntariamente para ajudar")
    print("na organização do evento e manter viva a paixão pelo rock.")
 
    resposta = input("\nDeseja fazer uma doação? (sim/não): ").strip().lower()
 
    if resposta in ["sim", "s", "ss"]:
        try:
            valor = float(input("Digite o valor da sua doação (R$): ").replace(",", "."))
 
            if valor <= 0:
                print("\nO valor precisa ser maior que zero.")
                print("Não se preocupe: sua presença já fortalece nosso evento!")
                return
 
            print("\n DOAÇÃO REGISTRADA NESTA SESSÃO! ")
            print(f"Valor informado: R$ {valor:,.2f}")
            print("Muito obrigado por fortalecer essa corrente do rock!")
            print("Sua contribuição voluntária ajuda a manter a estrada aberta,")
            print("os motores roncando e as guitarras falando mais alto!")
            print("Você faz parte dessa história! ")
 
        except ValueError:
            print("\nValor inválido! Digite um número, como 25.00 ou 25,00.")
            print("Nenhuma doação foi registrada.")
 
    elif resposta in ["não", "nao", "n"]:
        print("\nSem problemas! Sua participação já é muito importante.")
        print("O que vale é a união da galera, o respeito e o amor pelo rock!")
        print("Esperamos você na frente do palco! ")
 
    else:
        print("\nResposta não reconhecida. Você pode participar sem doar!")
        print("O importante é curtir o festival com responsabilidade.")
 
 
# --- NOVA FUNÇÃO: CENTRAL DE DÚVIDAS SOBRE O SHOW ---
 
def central_de_duvidas():
    print("\n" + "=" * 50)
    print(" CENTRAL DE DÚVIDAS DO ROCK FESTIVAL ")
    print("=" * 50)
    print("Ficou com alguma dúvida? Manda ver!")
    print("Escolha um assunto para consultar:\n")
 
    print("1. Quais bandas vão tocar?")
    print("2. O Metallica está confirmado?")
    print("3. Quais motos são aceitas?")
    print("4. Como faço para saber sobre ingressos?")
    print("5. Posso levar minha própria comida e bebida?")
    print("6. Que horas começa o show?")
    print("7. Haverá estacionamento para motos?")
    print("8. Quais são as regras de segurança?")
    print("9. Como entro em contato com a organização?")
    print("10. Voltar ao menu principal")
 
    while True:
        duvida = input("\nDigite o número da sua dúvida: ").strip()
 
        if duvida == "1":
            print("\n LINEUP DO FESTIVAL:")
            if lineup_bandas:
                for banda in lineup_bandas:
                    status = "Confirmada" if banda["confirmada"] else "Aguardando confirmação"
                    print(f"- {banda['nome']} ({banda['genero']}) - {status}")
            else:
                print("O lineup ainda está sendo preparado.")
            print("Prepare o pescoço para o headbang e confira as atualizações!")
 
        elif duvida == "2":
            metallica = next(
                (banda for banda in lineup_bandas
                 if banda["nome"].lower() == "metallica"),
                None
            )
 
            if metallica and metallica["confirmada"]:
                print("\n Sim! O Metallica está confirmado no lineup cadastrado!")
            else:
                print("\n Ainda não! O Metallica está aguardando confirmação.")
                print("Fique ligado nas atualizações oficiais para não perder novidades.")
 
        elif duvida == "3":
            print("\n CATEGORIAS DE MOTOS ACEITAS:")
            for categoria in categorias_motos:
                print(f"- {categoria}")
            print("Sua máquina é bem-vinda se estiver dentro das regras do evento!")
 
        elif duvida == "4":
            print("\n INGRESSOS:")
            print("Consulte os canais oficiais do organizador para verificar")
            print("preços, lotes, disponibilidade e formas de compra.")
            print("Os dados de venda ainda não estão cadastrados neste sistema.")
 
        elif duvida == "5":
            print("\n COMIDA E BEBIDA:")
            print("As regras sobre alimentos, bebidas e itens permitidos")
            print("precisam ser confirmadas com a organização.")
            print("Consulte as orientações oficiais antes de sair de casa.")
 
        elif duvida == "6":
            print("\n HORÁRIO DO SHOW:")
            print("Os horários de abertura dos portões e dos shows")
            print("ainda não estão cadastrados no sistema.")
            print("Acompanhe os anúncios oficiais para planejar sua chegada.")
 
        elif duvida == "7":
            print("\n ESTACIONAMENTO:")
            print("Consulte a organização para confirmar a disponibilidade,")
            print("a localização e as regras de estacionamento para motos.")
            print("Chegue com antecedência e estacione com segurança!")
 
        elif duvida == "8":
            print(
                "\nSEGURANÇA EM PRIMEIRO LUGAR: \n"
                "- Respeite a equipe de segurança e os demais participantes.\n"
                "- Se beber, não pilote.\n"
                "- Use capacete e equipamentos adequados na estrada.\n"
                "- Confira as regras oficiais sobre objetos permitidos.\n"
                "Queremos todo mundo curtindo o rock e voltando bem para casa!"
            )
 
        elif duvida == "9":
            print("\n CONTATO COM A ORGANIZAÇÃO:")
            print("Os contatos oficiais ainda não estão cadastrados aqui.")
            print("Procure os canais oficiais do Asfalto de Ferro m.c.")
            print("Não compartilhe dados pessoais com contatos não verificados.")
 
        elif duvida == "10":
            print("\n Dúvidas encerradas! Agora é acelerar rumo ao rock!")
            break
 
        else:
            print("\nOpção inválida! Escolha um número de 1 a 10.")
 
 
# --- FLUXO PRINCIPAL ---
 
executando = True
 
while executando:
    exibir_cabecalho()
    print("1. Ver Categorias de Motos")
    print("2. Ver Lineup Completo")
    print("3. Adicionar Nova Banda")
    print("4. Remover Banda")
    print("5. Filtrar Bandas por Categoria")
    print("6. Fazer uma Doação")
    print("7. Tirar Dúvidas sobre o Show")
    print("8. Sair do Sistema")
    print("-" * 50)
 
    opcao = input("Escolha uma opção (1-8): ").strip()
 
    match opcao:
        case "1":
            listar_categorias_motos()
        case "2":
            listar_todas_bandas()
        case "3":
            adicionar_banda()
        case "4":
            remover_banda()
        case "5":
            listar_bandas_por_categoria()
        case "6":
            realizar_doacao()
        case "7":
            central_de_duvidas()
        case "8":
            print("\nPé na estrada e rock na veia!")
            print("Obrigado por fazer parte dessa jornada. Até o próximo encontro! ")
            executando = False
        case _:
            print("\nOpção inválida! Tente novamente.")
 
    if executando:
        input("\nPressione ENTER para voltar ao menu...")
        print("\n" * 3)
 