import discord

# Abjuração - spells.py
class Abjuracao:
    def __init__(self):
        pass
    
    #Nome da Magia como função(em minusculo)    
    def Resistencia():
        #atribui uma variavel ao embed criado
        resistencia = discord.Embed(
            #Nome da Magia começando com letra em maiusculo
            title='Resistência',
            #Descrição do efeito da magia 
            description='Você toca uma criatura voluntária. Uma vez, antes da magia acabar, o alvo pode rolar um d4 e adicionar o valor jogado a um teste de resistência de sua escolha.\n Ele pode rolar o dado antes ou depois de realizar o teste de resistência. Então, a magia termina.',
            color=0xFF0000
        ) 
        #Tempo de conjuração da Magia 
        resistencia.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        #Alcance da Magia 
        resistencia.add_field(name='Alcance', value='Toque', inline=False)
        #Componentes da Magia (Se tiver Materiais)
        resistencia.add_field(name='Componentes', value='V S M (um manto em miniatura)', inline=False)
        #Duração da magia 
        resistencia.add_field(name='Duração', value='Concentração, até 1 minuto', inline=False)  
        # O footer vai dizer os efeitos da magia em niveis superiores , se não tiver nenhum efeito ele não vai existir
        resistencia.set_footer(text='Informações adicionais sobre a magia')
        #o return vai retornar a variavel com o embed criado
        return resistencia
    
    def ArmaduraArcana():
        # Atribui uma variável ao embed criado
        armadura_arcana = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Armadura Arcana',
            # Descrição da magia conforme o livro ou fonte
            description='Você toca uma criatura voluntária que não esteja vestindo armadura e uma energia mágica protetora a envolve até a magia acabar. A CA base do alvo se torna 13 + o modificador de Destreza dele. A magia acaba se o alvo colocar uma armadura ou se você dissipá-la usando uma ação.',
            color=0xFF0000  # Cor pode variar conforme preferência
            )
            # Tempo de conjuração da Magia
        armadura_arcana.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        armadura_arcana.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        armadura_arcana.add_field(name='Componentes', value='V S M (um pedaço de couro curado)', inline=False)
        # Duração da magia
        armadura_arcana.add_field(name='Duração', value='8 horas', inline=False)
        # O footer pode descrever informações adicionais sobre a magia
        # Se não houver informações, o footer não será adicionado
        # Exemplo:
        # armadura_arcana.set_footer(text='Efeitos em níveis superiores: ...')

        # O return vai retornar a variável com o embed criado
        return armadura_arcana
    def EscudoArcano():
        # Atribui uma variável ao embed criado
        escudo_arcano = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Escudo Arcano',
            # Descrição da magia conforme o livro ou fonte
            description='Uma barreira de energia invisível aparece e protege você. Até o início do seu próximo turno, você recebe +5 de bônus na CA, incluindo contra o ataque que desencadeou a magia, e você não sofre dano de mísseis mágicos.',
            color=0xFF0000  # Cor pode variar conforme preferência
            )
            # Tempo de conjuração da Magia
        escudo_arcano.add_field(name='Tempo de Conjuração', value='1 reação', inline=False)
        # Alcance da Magia
        escudo_arcano.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        escudo_arcano.add_field(name='Componentes', value='V S M (um pedaço de couro curado)', inline=False)
        # Duração da magia
        escudo_arcano.add_field(name='Duração', value='8 horas', inline=False)
        # O footer pode descrever informações adicionais sobre a magia
        # Se não houver informações, o footer não será adicionado
        # Exemplo:
        # armadura_arcana.set_footer(text='Efeitos em níveis superiores: ...')

        # O return vai retornar a variável com o embed criado
        return escudo_arcano
    def EscudoDaFe():
        # Atribui uma variável ao embed criado com o nome da magia
        escudo_da_fe = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Escudo da Fé (Shield of Faith)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Um campo cintilante aparece ao redor de uma criatura, à sua escolha, dentro do alcance, concedendo +2 de bônus na CA pela duração.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        escudo_da_fe.add_field(name='Tempo de Conjuração', value='1 ação bonus', inline=False)
        # Alcance da Magia
        escudo_da_fe.add_field(name='Alcance', value='60 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        escudo_da_fe.add_field(name='Componentes', value='V S M (um pequeno pergaminho com alguns textos sagrados escritos nele)', inline=False)
        # Duração da magia
        escudo_da_fe.add_field(name='Duração', value='1 minuto', inline=False)
        # O return vai retornar a variável com o embed criado
        return escudo_da_fe
    def ProtecaoContraOBemEMal():
    # Atribui uma variável ao embed criado com o nome da magia
        protecao_bem_mal = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Proteção Contra O Bem E Mal (Protection From Evil And Good)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Até a magia acabar, uma criatura voluntária que você tocar estará protegida contra certos tipos de criaturas: aberrações, celestiais, corruptores, elementais, fadas e mortos-vivos.\n\nA proteção garante diversos benefícios. As criaturas desse tipo tem desvantagem nas jogadas de ataque contra o alvo. O alvo não pode ser enfeitiçado, amedrontado ou possuído por elas. Se o alvo já estiver enfeitiçado, amedrontado ou possuído por uma dessas criaturas, o alvo terá vantagem em qualquer novo teste de resistência contra o efeito relevante.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        protecao_bem_mal.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        protecao_bem_mal.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        protecao_bem_mal.add_field(name='Componentes', value='V S M (água benta ou pó de prata e ferro que a magia consome)', inline=False)
        # Duração da magia
        protecao_bem_mal.add_field(name='Duração', value='Concentração, até 10 minutos', inline=False)
        # O return vai retornar a variável com o embed criado
        return protecao_bem_mal
    def Santuario():
        # Atribui uma variável ao embed criado com o nome da magia
        santuario = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Santuário (Sanctuary)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você protege uma criatura, dentro do alcance, contra ataques. Até a magia acabar, qualquer criatura que tentar atacar ou usar magias que causem dano contra a criatura protegida deve, primeiro, realizar um teste de resistência de Sabedoria. Se falhar na resistência, a criatura deve escolher um novo alvo ou perderá o ataque ou magia. Essa magia não protege a criatura contra efeitos de área, como a explosão de uma bola de fogo.\n\nSe a criatura protegida realizar um ataque ou conjurar uma magia que afete uma criatura inimiga, essa magia acaba.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        santuario.add_field(name='Tempo de Conjuração', value='1 ação bonus', inline=False)
        # Alcance da Magia
        santuario.add_field(name='Alcance', value='30 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        santuario.add_field(name='Componentes', value='V S M (um pequeno espelho de prata)', inline=False)
        # Duração da magia
        santuario.add_field(name='Duração', value='1 minuto', inline=False)
        # O return vai retornar a variável com o embed criado
        return santuario
    def Ajuda():
    # Atribui uma variável ao embed criado com o nome da magia
        ajuda = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Ajuda (Aid)',
            # Descrição da magia sobre o efeito , dano , dados , etc
            description='Sua magia inspira seus aliados com vigor e determinação. Escolha até três criaturas dentro do alcance. '
                        'O máximo de pontos de vida e os pontos de vida atuais de cada alvo aumentam em 5, pela duração.\n\n'
                        ,
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        ajuda.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        ajuda.add_field(name='Alcance', value='30 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        ajuda.add_field(name='Componentes', value='V S M (uma pequena tira de branco)', inline=False)
        # Duração da magia
        ajuda.add_field(name='Duração', value='8 horas', inline=False)
        # Efeitos em níveis superiores
        ajuda.set_footer(text='Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 3° nível ou superior, '
                            'os pontos de vida dos alvos aumentam em 5 pontos adicionais para cada nível do espaço acima do 2°.')
        # O return vai retornar a variável com o embed criado
        return ajuda

    def PassosSemPegadas():
    # Atribui uma variável ao embed criado com o nome da magia
        passos_sem_pegadas = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Passos Sem Pegadas (Pass Without Trace)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Um véu de sombras e silêncio irradia de você, encobrindo você e seus companheiros contra detecção. Pela duração, cada criatura, à sua escolha, a até 9 metros [30 feet] de você (incluindo você) recebe +10 de bônus em testes de Destreza (Furtividade) e não pode ser rastreada, exceto por meios mágicos. Uma criatura que receber esse bônus não deixa quaisquer pegadas ou outros vestígios da sua passagem.',
            color=0xFF0000  # Cor pode variar conforme preferência
    )
        # Tempo de conjuração da Magia
        passos_sem_pegadas.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        passos_sem_pegadas.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        passos_sem_pegadas.add_field(name='Componentes', value='V S M (cinzas de uma folha de visco queimada e um ramo de pinheiro)', inline=False)
        # Duração da magia
        passos_sem_pegadas.add_field(name='Duração', value='Concentração, até 1 hora', inline=False)
        # O return vai retornar a variável com o embed criado
        return passos_sem_pegadas
    def ProtecaoContraVeneno():
    # Atribui uma variável ao embed criado com o nome da magia
        protecao_contra_veneno = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Proteção Contra Veneno (Protection From Poison)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você toca uma criatura. Se ela estiver envenenada, você neutraliza o veneno. Se mais de um veneno estiver afligindo o alvo, você neutraliza um veneno, que você saiba estar presente, ou neutraliza um aleatório. Pela duração, o alvo terá vantagem em testes de resistência para não ser envenenado e terá resistência a dano de veneno.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        protecao_contra_veneno.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        protecao_contra_veneno.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        protecao_contra_veneno.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        protecao_contra_veneno.add_field(name='Duração', value='1 hora', inline=False)
        # O return vai retornar a variável com o embed criado
        return protecao_contra_veneno
    def RestauracaoMenor():
    # Atribui uma variável ao embed criado com o nome da magia
        restauracao_menor = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Restauração Menor (Lesser Restoration)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você toca uma criatura e pode, ou acabar com uma doença ou uma condição que a esteja afligindo. A condição pode ser cega, surda, paralisada ou envenenada.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        restauracao_menor.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        restauracao_menor.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        restauracao_menor.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        restauracao_menor.add_field(name='Duração', value='Instantâneo', inline=False)
        # O return vai retornar a variável com o embed criado
        return restauracao_menor
    def TrancaArcana():
        # Atribui uma variável ao embed criado com o nome da magia
        tranca_arcana = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Tranca Arcana (Arcane Lock)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você toca uma porta, janela, portão, baú ou outra entrada fechada e ela ficará trancada pela duração. '
                        'Você e as criaturas que você designar, quando você conjurar essa magia, podem abrir o objeto normalmente. '
                        'Você também pode definir uma senha que, quando falada a 1,5 metro [5 feet] do objeto, suprime a magia por 1 minuto. '
                        'De outra forma, ele é intransponível até ser quebrado ou a magia seja dissipada ou suprimida. '
                        'Conjurar arrombar no objeto suprime a tranca arcana por 10 minutos.\n\n'
                        'Enquanto estiver sob efeito dessa magia, o objeto é mais difícil de quebrar ou de forçar para abrir; '
                        'a CD para quebrá-lo ou de arrombá-lo aumenta em 10.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        tranca_arcana.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        tranca_arcana.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        tranca_arcana.add_field(name='Componentes', value='V S M (pó de ouro valendo, no mínimo, 25 gp que a magia consome)', inline=False)
        # Duração da magia
        tranca_arcana.add_field(name='Duração', value='Até ser dissipada', inline=False)
        # O return vai retornar a variável com o embed criado
        return tranca_arcana
    def VinculoProtetor():
    # Atribui uma variável ao embed criado com o nome da magia
        vinculo_protetor = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Vínculo Protetor (Warding Bond)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Essa magia protege uma criatura voluntária que você tocar e cria uma conexão mística entre você e o alvo até a magia acabar. '
                        'Enquanto o alvo estiver a até 18 metros [60 feet] de você, ele recebe +1 de bônus na CA, nos testes de resistência e terá resistência a todos os danos. '
                        'No entanto, a cada vez que ele sofrer dano, você sofrerá a mesma quantidade de dano.\n\n'
                        'A magia acaba se você cair a 0 pontos de vida ou se você e o alvo ficarem separados a mais de 18 metros [60 feet]. '
                        'Ela também termina se a magia for conjurada novamente em quaisquer das criaturas conectadas. Você também pode dissipar a magia com uma ação.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        vinculo_protetor.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        vinculo_protetor.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        vinculo_protetor.add_field(name='Componentes', value='V S M (um par de anéis de platina, que você e o alvo deve usar pela duração, valendo, no mínimo, 100 gp)', inline=False)
        # Duração da magia
        vinculo_protetor.add_field(name='Duração', value='1 horas', inline=False)
        # O return vai retornar a variável com o embed criado
        return vinculo_protetor
    def CirculoMagico():
    # Atribui uma variável ao embed criado com o nome da magia
        circulo_magico = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Círculo Mágico (Magic Circle)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você cria um cilindro de energia mágica de 3 metros de raio [10-foot radius] por 6 metros de altura [20-foot-tall], centrado num ponto no solo que você possa ver, dentro do alcance. '
                        'Runas brilhantes aparecem toda vez que o cilindro toca o chão ou outra superfície.\n\n'
                        'Escolha um ou mais dos tipos de criaturas seguintes: celestiais, corruptores, elementais, fadas ou mortos-vivos. O círculo afeta uma criatura do tipo escolhido das seguintes maneiras:\n\n'
                        '1. A criatura não consegue entrar no cilindro voluntariamente por meios não-mágicos. Se a criatura tentar usar teletransporte ou viagem interplanar para fazê-lo, ela deve, primeiro, ser bem sucedida num teste de resistência de Carisma.\n'
                        '2. A criatura tem desvantagem nas jogadas de ataque contra alvos dentro do cilindro.\n'
                        '3. Alvos dentro do cilindro não podem ser enfeitiçados, amedrontados ou possuídos pela criatura.\n\n'
                        'Quando você conjurar essa magia, você pode decidir que a mágica dela opere na direção reversa, prevenindo que uma criatura de um tipo especifico saia do cilindro e protegendo os alvos fora dele.\n\n'
                       ,
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        circulo_magico.add_field(name='Tempo de Conjuração', value='1 minutos', inline=False)
        # Alcance da Magia
        circulo_magico.add_field(name='Alcance', value='10 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        circulo_magico.add_field(name='Componentes', value='V S M (água benta ou pó de prata e ferro valendo, no mínimo, 100 gp que a magia consome)', inline=False)
        # Duração da magia
        circulo_magico.add_field(name='Duração', value='1 horas', inline=False)
        # Efeitos em níveis superiores
        circulo_magico.set_footer(text='Em Níveis Superiores. Quando conjurada com um espaço de magia de 4° nível ou superior, a duração aumenta em 1 hora para cada nível acima do 3°.')
        # O return vai retornar a variável com o embed criado
        return circulo_magico
    def Contramagica():
        # Atribui uma variável ao embed criado com o nome da magia
        contramagica = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Contramágica (Counterspell)',
            # Descrição da magia sobre o efeito , dano , dados , etc
            description='Você tenta interromper uma criatura no processo de conjuração de uma magia. Se a criatura estiver '
                        'conjurando uma magia de 3° nível ou inferior, a magia falha e não gera nenhum efeito. Se ela '
                        'estiver conjurando uma magia de 4° nível ou superior, faça um teste de habilidade usando sua '
                        'habilidade de conjuração. A CD é igual a 10 + o nível da magia. Caso seja bem sucedido, a magia '
                        'da criatura falha e não gera nenhum efeito.\n\n',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        contramagica.add_field(name='Tempo de Conjuração', value='1 reação', inline=False)
        # Alcance da Magia
        contramagica.add_field(name='Alcance', value='60 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        contramagica.add_field(name='Componentes', value='S', inline=False)
        # Duração da magia
        contramagica.add_field(name='Duração', value='instantâneo', inline=False)
        # Efeitos em níveis superiores
        contramagica.set_footer(text='Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 4° '
                                    'nível ou superior, a magia interrompida não vai gerar efeito se o nível dela for '
                                    'menor ou igual ao nível do espaço de magia que você usar.')
        # O return vai retornar a variável com o embed criado
        return contramagica
    def DificultarDetecao():
    # Atribui uma variável ao embed criado com o nome da magia
        dificultar_detecao = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Dificultar Detecção (Nondetection)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Pela duração, você esconde um alvo que você tocar de magias de adivinhação. '
                        'O alvo pode ser uma criatura voluntária, um local ou um objeto com não mais de 3 metros '
                        '[10 feet] em qualquer dimensão. O alvo não pode ser alvo de magias de adivinhação ou '
                        'percebido através de sensores mágicos de vidência.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        dificultar_detecao.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        dificultar_detecao.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        dificultar_detecao.add_field(name='Componentes', value='V S M (polvilhar sobre o alvo um pouco de pó de diamante '
                                                            'valendo, no mínimo, 25 gp que a magia consome)',
                                    inline=False)
        # Duração da magia
        dificultar_detecao.add_field(name='Duração', value='8 horas', inline=False)
        # O return vai retornar a variável com o embed criado
        return dificultar_detecao
    def DissiparMagia():
    # Atribui uma variável ao embed criado com o nome da magia
        dissipar_magia = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Dissipar Magia (Dispel Magic)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Escolha uma criatura, objeto ou efeito mágico dentro do alcance. '
                        'Qualquer magia de 3° nível ou inferior no alvo, termina. Para cada magia de 4° nível '
                        'ou superior no alvo, realize um teste de habilidade usando sua habilidade de conjuração. '
                        'A CD é igual a 10 + o nível da magia. Se obtiver sucesso, a magia termina.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        dissipar_magia.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        dissipar_magia.add_field(name='Alcance', value='120 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        dissipar_magia.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        dissipar_magia.add_field(name='Duração', value='Instantâneo', inline=False)
        # O return vai retornar a variável com o embed criado
        return dissipar_magia
    def MuralhaDeVento():
    # Atribui uma variável ao embed criado com o nome da magia
        muralha_vento = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Muralha de Vento (Wind Wall)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Uma muralha de ventos fortes ergue-se do chão num ponto, à sua escolha, dentro do alcance. '
                        'Você pode fazer a muralha ter até 15 metros de comprimento, 4,5 metros de altura e '
                        '30 centímetros de espessura. Você pode moldar a muralha em qualquer forma que desejar, '
                        'contanto que ela faça um caminho contínuo pelo solo. A muralha permanece pela duração. '
                        'Quando a muralha aparece, cada criatura dentro da área dela deve realizar um teste de '
                        'resistência de Força. Uma criatura sofre 3d8 de dano de concussão se falhar na resistência, '
                        'ou metade desse dano se obtiver sucesso. Os ventos fortes mantêm névoa, fumaça e outros gases '
                        'afastados. Criaturas ou objetos voadores Pequenos ou menores, não podem atravessar a muralha. '
                        'Materiais leves e soltos trazidos para a muralha são arremessados para cima. Flechas, virotes '
                        'e outros projéteis ordinários disparados contra alvos além da muralha são defletidos para cima '
                        'e erram automaticamente. (Pedras arremessadas por gigantes ou armas de cerco e projéteis '
                        'similares, não são afetados.) As criaturas em forma gasosa não podem atravessá-la.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        muralha_vento.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        muralha_vento.add_field(name='Alcance', value='120 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        muralha_vento.add_field(name='Componentes', value='V S M (um leque minúsculo e uma pena de origem exótica)',
                                inline=False)
        # Duração da magia
        muralha_vento.add_field(name='Duração', value='Concentração, até 1 minuto', inline=False)
        # O return vai retornar a variável com o embed criado
        return muralha_vento
    def ProtecaoContraEnergia():
    # Atribui uma variável ao embed criado com o nome da magia
        protecao_energia = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Proteção Contra Energia (Protection From Energy)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Pela duração, a criatura voluntária que você tocar terá resistência a um tipo de dano '
                        'de sua escolha: ácido, elétrico, fogo, frio ou trovejante.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        protecao_energia.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        protecao_energia.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        protecao_energia.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        protecao_energia.add_field(name='Duração', value='Concentração, até 1 minuto', inline=False)
        # O return vai retornar a variável com o embed criado
        return protecao_energia
    def RemoverMaldicao():
    # Atribui uma variável ao embed criado com o nome da magia
        remove_maldicao = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Remover Maldição (Remove Curse)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Ao seu toque, todas as maldições afetando uma criatura ou objeto terminam. '
                        'Se o objeto for um item mágico amaldiçoado, sua maldição persiste, '
                        'mas a magia rompe a sintonia do portador com o objeto, permitindo que ele o remova ou descarte.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        remove_maldicao.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        remove_maldicao.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        remove_maldicao.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        remove_maldicao.add_field(name='Duração', value='Instantâneo', inline=False)
        # O return vai retornar a variável com o embed criado
        return remove_maldicao
    def SinalDeEsperanca():
    # Atribui uma variável ao embed criado com o nome da magia
        sinal_esperanca = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Sinal de Esperança (Beacon of Hope)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Essa magia confere esperança e vitalidade. Escolha qualquer quantidade de criaturas '
                        'dentro do alcance. Pela duração, cada alvo tem vantagem em testes de resistência de '
                        'Sabedoria e testes de resistência contra a morte e recuperam o máximo de pontos de vida '
                        'possível em qualquer cura.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        sinal_esperanca.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        sinal_esperanca.add_field(name='Alcance', value='30 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        sinal_esperanca.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        sinal_esperanca.add_field(name='Duração', value='Concentração, até 1 minutos', inline=False)
        # O return vai retornar a variável com o embed criado
        return sinal_esperanca
    def Banimento():
    # Atribui uma variável ao embed criado com o nome da magia
        banimento = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Banimento (Banishment)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você tenta enviar uma criatura que você pode ver dentro do alcance para outro plano '
                        'de existência. O alvo precisa ser bem sucedido em um teste de resistência de Carisma '
                        'ou será banido.\n\nSe o alvo for nativo do plano de existência que você está, você '
                        'bane o alvo para um semiplano inofensivo. Enquanto estiver lá, a criatura estará '
                        'incapacitada. Ela permanece lá até a magia acabar, a partir desse ponto, o alvo '
                        'reaparece no espaço em que ela deixou ou no espaço desocupado mais próximo, se o '
                        'espaço dela estiver ocupado.\n\nSe o alvo for nativo de um plano de existência '
                        'diferente do que você está, o alvo é banido em um lampejo sutil, retornando para o '
                        'seu plano natal. Se a magia acabar antes de 1 minuto se passar, o alvo reaparece no '
                        'lugar em que estava ou no espaço desocupado mais próximo, se o espaço dela estiver '
                        'ocupado. Do contrário, o alvo não retorna.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        banimento.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        banimento.add_field(name='Alcance', value='60 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        banimento.add_field(name='Componentes', value='V S M (um item desagradável ao alvo)', inline=False)
        # Duração da magia
        banimento.add_field(name='Duração', value='Concentração, até 1 minutos', inline=False)
        # Footer com informações adicionais
        banimento.set_footer(text='Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de '
                                'magia de 5° nível ou superior, você pode afetar uma criatura adicional para '
                                'cada nível do espaço acima do 4°.')
        # O return vai retornar a variável com o embed criado
        return banimento
    def MovimentacaoLivre():
    # Atribui uma variável ao embed criado com o nome da magia
        movimentacao_livre = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Movimentação Livre (Freedom Of Movement)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você toca uma criatura voluntária. Pela duração, os movimentos do alvo não são afetados '
                        'por terreno difícil e magias e outros efeitos mágicos também não podem reduzir o deslocamento '
                        'do alvo ou fazer com que o alvo fique paralisado ou impedido.\n\nO alvo também pode gastar 1,5 '
                        'metro [5 feet] de deslocamento para escapar, automaticamente, de impedimentos não-mágicos, como '
                        'algemas ou o agarrão de uma criatura. Finalmente, estar submerso não impõe penalidades no '
                        'deslocamento ou ataques do alvo.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        movimentacao_livre.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        movimentacao_livre.add_field(name='Alcance', value='toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        movimentacao_livre.add_field(name='Componentes', value='V S M (uma fita de couro, enrolada no braço ou apêndice similar)', inline=False)
        # Duração da magia
        movimentacao_livre.add_field(name='Duração', value='1 horas', inline=False)
        # O return vai retornar a variável com o embed criado
        return movimentacao_livre
    def PeleDePedra():
    # Atribui uma variável ao embed criado com o nome da magia
        pele_de_pedra = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Pele de Pedra (Stoneskin)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Essa magia transforma a pele de uma criatura voluntária que você tocar em rocha sólida. '
                        'Até a magia acabar, o alvo tem resistência a dano de concussão, cortante e perfurante não-mágico.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        pele_de_pedra.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        pele_de_pedra.add_field(name='Alcance', value='toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        pele_de_pedra.add_field(name='Componentes', value='V S M (pó de diamante valendo, no mínimo, 100 gp que a magia consome)', inline=False)
        # Duração da magia
        pele_de_pedra.add_field(name='Duração', value='concentração, até 1 horas', inline=False)
        # O return vai retornar a variável com o embed criado
        return pele_de_pedra
    def ProtecaoContraMorte():
    # Atribui uma variável ao embed criado com o nome da magia
        death_ward = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Proteção Contra a Morte (Death Ward)',
            # Descrição da magia sobre o efeito, dano, dados, etc
            description='Você toca uma criatura e concede a ela uma certa proteção contra a morte.\n\n'
                        'A primeira vez que o alvo cair a 0 pontos de vida, como resultado de ter sofrido dano, '
                        'o alvo, ao invés disso, cai a 1 ponto de vida e a magia termina.\n\n'
                        'Se a magia ainda estiver funcionando quando o alvo for afetado por um efeito que poderia '
                        'matá-lo instantaneamente sem causar dano, o efeito, ao invés disso, não funciona no alvo '
                        'e a magia termina.',
            color=0xFF0000  # Cor pode variar conforme preferência
        )
        # Tempo de conjuração da Magia
        death_ward.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia
        death_ward.add_field(name='Alcance', value='toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        death_ward.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia
        death_ward.add_field(name='Duração', value='8 horas', inline=False)
        # O return vai retornar a variável com o embed criado
        return death_ward
    def Sanctum():
    # Criação do embed
        sanctum = discord.Embed(
            title='Santuário Particular (Private Sanctum)',
            description='Você deixa uma área, dentro do alcance, magicamente segura. '
                        'A área é um cubo que pode ser tão pequeno quanto 1,5 metro [5 feet] ou tão grande quanto '
                        '30 metros [100 feet] de cada lado. A magia permanece pela duração ou até você usar uma ação '
                        'para dissipa-la.\n\nQuando você conjura essa magia, você decide que tipo de segurança ela '
                        'fornecerá, escolhendo qualquer ou todas as propriedades a seguir:',
            color=0xFF0000
        )
        # Adição de campos para detalhes
        sanctum.add_field(name='Tipo de Segurança',
                        value='1. Sons não podem atravessar a barreira na fronteira da área protegida.\n'
                                '2. A barreira da área protegida é escura e nebulosa, impedindo visão '
                                '(inclusive visão no escuro) através dela.\n'
                                '3. Sensores criados por magia de adivinhação não podem aparecer dentro da área '
                                'protegida ou atravessar a barreira no perímetro.\n'
                                '4. As criaturas na área não podem ser alvo de magias de adivinhação.\n'
                                '5. Nada pode se teletransportar para dentro ou para fora da área protegida.\n'
                                '6. Viagem planar está bloqueada para dentro da área protegida.',
                        inline=False)
        sanctum.add_field(name='Conjuração Diária',
                        value='Conjurar essa magia no mesmo lugar, a cada dia, por um ano, torna o efeito permanente.',
                        inline=False)
        # Tempo de conjuração, Alcance, Componentes, Duração
        sanctum.add_field(name='Tempo de Conjuração', value='10 minutos', inline=True)
        sanctum.add_field(name='Alcance', value='120 pés', inline=True)
        sanctum.add_field(name='Componentes', value='V S M (uma folha de chumbo, um pedaço de vidro opaco, '
                                                    'um chumaço de algodão ou pano e pó de crisólita)', inline=True)
        sanctum.add_field(name='Duração', value='24 horas', inline=True)
        # Footer para níveis superiores
        sanctum.set_footer(text='Quando você conjurar essa magia usando um espaço de magia de 5° nível ou superior, '
                                'você pode aumentar o tamanho do cubo em 30 metros [100 feet] de cada lado para cada '
                                'nível do espaço acima do 4°. Então, você poderia proteger um cubo de até 60 metros '
                                '[200 feet] de lado usando um espaço de magia de 5° nível.')

        return sanctum
    def planar_binding():
    # Criação do embed
        binding_embed = discord.Embed(
            title='Âncora Planar (Planar Binding)',
            description='Com essa magia, você tenta obrigar um celestial, corruptor, elemental ou fada a servi-lo. '
                        'A criatura deve estar dentro do alcance durante toda a conjuração da magia.',
            color=0x00ff00  # Cor verde para a borda do embed
        )
        # Adicionando campos para detalhes
        binding_embed.add_field(
            name='Resistência e Obrigatoriedade',
            value='Ao completar a conjuração, o alvo deve realizar um teste de resistência de Carisma. '
                'Se falhar na resistência, ela é obrigada a servir você pela duração.',
            inline=False
        )
        binding_embed.add_field(
            name='Comportamento da Criatura',
            value='Uma criatura obrigada deve seguir suas instruções da melhor forma que puder. '
                'Ela obedecerá ao pé da letra suas instruções, mas se for hostil a você, '
                'tentará distorcer suas palavras para atingir seus próprios objetivos.',
            inline=False
        )
        # Tempo de conjuração, Alcance, Componentes, Duração
        binding_embed.add_field(
            name='Tempo de Conjuração',
            value='1 hora',
            inline=True
        )
        binding_embed.add_field(
            name='Alcance',
            value='60 pés',
            inline=True
        )
        binding_embed.add_field(
            name='Componentes',
            value='V S M (uma joia valendo, no mínimo, 1000 gp que a magia consome)',
            inline=True
        )
        binding_embed.add_field(
            name='Duração',
            value='24 horas',
            inline=True
        )
        # Footer para níveis superiores
        binding_embed.set_footer(text='Em Níveis Superiores, a duração aumenta para 10 dias com um espaço de magia de 6° nível, '
                'para 30 dias com um espaço de magia de 7° nível, para 180 dias com um espaço de magia de 8° nível '
                'e para um ano com um espaço de magia de 9° nível.')
        
        return binding_embed
    def antilife_shell():
    # Criação do embed
        shell_embed = discord.Embed(
            title='Cúpula Antivida (Antilife Shell)',
            description='Uma barreira cintilante se estende de você até 3 metros de raio [10-foot radius], '
                        'e se move com você, permanecendo centrada em você e restringindo criaturas diferentes de '
                        'mortos-vivos e constructos. A barreira mantém-se pela duração.',
            color=0xff0000  # Cor vermelha para a borda do embed
        )
        # Adicionando campos para detalhes
        shell_embed.add_field(
            name='Restrição de Criaturas',
            value='A barreira previne uma criatura afetada de atravessa-la ou alcançar através dela. '
                'Uma criatura afetada pode conjurar magias ou realizar ataques à distância ou ataques '
                'com armas de haste através da barreira.',
            inline=False
        )
        shell_embed.add_field(
            name='Condição para o término',
            value='Se você se mover forçando uma criatura afetada a atravessar a barreira, a magia termina.',
            inline=False
        )
        # Tempo de conjuração, Alcance, Componentes, Duração
        shell_embed.add_field(
            name='Tempo de Conjuração',
            value='1 ação',
            inline=True
        )
        shell_embed.add_field(
            name='Alcance',
            value='Pessoal',
            inline=True
        )
        shell_embed.add_field(
            name='Componentes',
            value='V S',
            inline=True
        )
        shell_embed.add_field(
            name='Duração',
            value='Concentração, até 1 hora',
            inline=True
        )
        
        return shell_embed
    def dispel_evil_and_good():
    # Criando o embed
        dispel_embed = discord.Embed(
            title='Dissipar o Bem e Mal (Dispel Evil and Good)',
            description='Energia cintilante envolve e protege você de fadas, mortos-vivos e criaturas originárias '
                        'além do Plano Material. Pela duração, celestiais, corruptores, elementais, fadas e mortos-vivos '
                        'tem desvantagem nas jogadas de ataque contra você.',
            color=0xff0000  # Cor vermelha para a borda do embed
        )
        # Adicionando campos para detalhes
        dispel_embed.add_field(
            name='Funções Especiais',
            value='Você pode terminar a magia prematuramente usando uma das funções especiais a seguir:',
            inline=False
        )
        dispel_embed.add_field(
            name='Cancelar Encantamento',
            value='Com sua ação, você toca uma criatura que esteja enfeitiçada, amedrontada ou possuída '
                'por um celestial, corruptor, elemental, fada ou morto-vivo. A criatura tocada não estará '
                'mais enfeitiçada, amedrontada ou possuída por tais criaturas.',
            inline=False
        )
        dispel_embed.add_field(
            name='Demissão',
            value='Com sua ação, faça um ataque corpo-a-corpo com magia contra um celestial, corruptor, '
                'elemental, fada ou morto-vivo que você possa alcançar. Se atingir, você pode tentar '
                'guiar a criatura de volta ao seu plano natal.',
            inline=False
        )
        dispel_embed.add_field(
            name='Teste de Resistência',
            value='A criatura deve ser bem sucedida num teste de resistência de Carisma ou será enviada de volta '
                'ao seu plano natal (se já não for aqui). Se elas não estiverem em seus planos de origem, mortos-vivos '
                'serão enviados para Umbra e fadas serão enviadas para Faéria.',
            inline=False
        )
        # Tempo de conjuração, Alcance, Componentes, Duração
        dispel_embed.add_field(
            name='Tempo de Conjuração',
            value='1 ação',
            inline=True
        )
        dispel_embed.add_field(
            name='Alcance',
            value='Pessoal',
            inline=True
        )
        dispel_embed.add_field(
            name='Componentes',
            value='V S M (água benta ou pó de prata e ferro)',
            inline=True
        )
        dispel_embed.add_field(
            name='Duração',
            value='Concentração, até 1 minuto',
            inline=True
        )
   
        return dispel_embed
    def greater_restoration():
    # Criando o embed
        restoration_embed = discord.Embed(
            title='Restauração Maior (Greater Restoration)',
            description='Você imbui uma criatura que você toca, com energia positiva para desfazer um efeito debilitante. '
                        'Você pode reduzir a exaustão do alvo em um nível ou remover um dos seguintes do alvo:',
            color=0xff0000  # Cor vermelha para a borda do embed
        )
        # Adicionando os efeitos que podem ser removidos
        restoration_embed.add_field(
            name='Efeitos Removíveis',
            value='- Um efeito que enfeitece ou petrifique o alvo\n'
                '- Uma maldição, incluindo a sintonização do alvo com um item mágico amaldiçoado\n'
                '- Qualquer redução a um dos valores de habilidade do alvo\n'
                '- Um efeito que esteja reduzindo o máximo de pontos de vida do alvo.',
            inline=False
        )
        # Tempo de conjuração, Alcance, Componentes, Duração
        restoration_embed.add_field(
            name='Tempo de Conjuração',
            value='1 ação',
            inline=True
        )
        restoration_embed.add_field(
            name='Alcance',
            value='Toque',
            inline=True
        )
        restoration_embed.add_field(
            name='Componentes',
            value='V S M (pó de diamante valendo, no mínimo, 100 gp que a magia consome)',
            inline=True
        )
        restoration_embed.add_field(
            name='Duração',
            value='Instantâneo',
            inline=True
        )
     
        
        return restoration_embed
    def globe_of_invulnerability():
    # Criando o embed
        globe_embed = discord.Embed(
            title='Globo de Invulnerabilidade (Globe of Invulnerability)',
            description='Uma barreira levemente cintilante e imóvel surge em um raio de 3 metros [10-foot] ao redor de você e permanece pela duração.',
            color=0x00ff00  # Cor verde para a borda do embed
        )
        # Descrição dos efeitos
        globe_embed.add_field(
            name='Efeitos',
            value='Qualquer magia de 5° nível ou inferior conjurada de fora da barreira não poderá afetar as criaturas ou objetos dentro dela, mesmo que a magia seja conjurada usando um espaço de magia de nível superior. Tais magias podem ter como alvo criaturas e objetos dentro da barreira, mas a magia não produz nenhum efeito neles. Similarmente, a área dentro da barreira é excluída das áreas afetadas por tais magias.',
            inline=False
        )
        # Tempo de conjuração, Alcance, Componentes, Duração
        globe_embed.add_field(
            name='Tempo de Conjuração',
            value='1 ação',
            inline=True
        )
        globe_embed.add_field(
            name='Alcance',
            value='Pessoal',
            inline=True
        )
        globe_embed.add_field(
            name='Componentes',
            value='V S M (uma pérola de vidro ou cristal que a magia consome)',
            inline=True
        )
        globe_embed.add_field(
            name='Duração',
            value='Concentração, até 1 minuto',
            inline=True
        )
        # Adicionando efeitos em níveis superiores no footer
        globe_embed.set_footer(text='Em Níveis Superiores: Quando conjurada com um espaço de magia de 7° nível ou superior, a barreira bloqueia magias de um nível superior para cada nível do espaço acima do 6°.')
        
        return globe_embed
    def forbiddance():
    # Criando o embed
        forbiddance_embed = discord.Embed(
            title='Proibição (Forbiddance)',
            description='Você cria uma defesa contra viagem mágica que protege até 3.500 metros quadrados [40.000 square feet] de solo até 9 metros [30 feet] de altura do solo.',
            color=0xffa500  # Cor laranja para a borda do embed
        )
        # Descrição dos efeitos
        forbiddance_embed.add_field(
            name='Efeitos',
            value='Pela duração, criaturas não conseguem se teletransportar para dentro da área ou usar portais para entrar na área. A magia protege a área contra viagem planar e também pode causar dano a certos tipos de criatura escolhidos por você quando conjura a magia.',
            inline=False
        )
        # Outros efeitos, componentes e duração
        forbiddance_embed.add_field(
            name='Outros Efeitos',
            value='Quando uma criatura escolhida entra na área pela primeira vez em um turno ou começa seu turno nela, a criatura sofre 5d6 de dano radiante ou necrótico.',
            inline=False
        )
        forbiddance_embed.add_field(
            name='Componentes',
            value='V S M (uma borrifada de água benta, incensos raros e pó de rubi valendo, no mínimo, 1000 gp)',
            inline=True
        )
        forbiddance_embed.add_field(
            name='Tempo de Conjuração',
            value='10 minutos',
            inline=True
        )
        forbiddance_embed.add_field(
            name='Alcance',
            value='Toque',
            inline=True
        )
        forbiddance_embed.add_field(
            name='Duração',
            value='1 dia',
            inline=True
        )
        # Adicionando informações sobre a senha e repetição da magia
        forbiddance_embed.add_field(
            name='Senha e Repetição',
            value='Você pode definir uma senha para permitir a entrada sem sofrer dano. Conjurar diariamente por 30 dias no mesmo local mantém a magia ativa.',
            inline=False
        )
        # Adicionando o footer
        forbiddance_embed.set_footer(text='A área da magia não pode sobrepor a área de outra magia proibição.')
        
        return forbiddance_embed
    def HolyAura():
    # atribui uma variável ao embed criado
        holy_aura = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Aura Sagrada (Holy Aura)',
            # Descrição do efeito da magia
            description='Luz divina emana de você e adere em uma aureola suave num raio de 9 metros [30-foot radius], em volta de você. As criaturas de sua escolha, no raio, quando você conjurar essa magia, emitem penumbra num raio de 1,5 metro [5-foot radius] e têm vantagem em todos os testes de resistência, enquanto as outras criaturas têm desvantagem nas jogadas de ataque contra elas, até a magia acabar. Além disso, quando um corruptor ou morto-vivo atingir uma criatura afetada com um ataque corpo-a-corpo, a aura lampeja com luz plena. O atacante deve ser bem-sucedido num teste de resistência de Constituição ou ficará cego até a magia acabar.',
            color=0xFF0000
        ) 
        # Tempo de conjuração da Magia 
        holy_aura.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        holy_aura.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        holy_aura.add_field(name='Componentes', value='V S M (um minúsculo relicário, contendo uma relíquia sagrada, como um pedaço de tecido do robe de um santo ou um pedaço de pergaminho de um texto religioso valendo, no mínimo, 1000 gp)', inline=False)
        # Duração da magia 
        holy_aura.add_field(name='Duração', value='Concentração, até 1 minuto', inline=False)  
        # o return vai retornar a variável com o embed criado
        return holy_aura
    def MindBlank():
    # atribui uma variável ao embed criado
        mind_blank = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Limpar a Mente (Mind Blank)',
            # Descrição do efeito da magia
            description='Até a magia acabar, uma criatura voluntária que você tocar fica imune a dano psíquico, a qualquer efeito que poderia sentir suas emoções ou ler seus pensamentos, a magias de adivinhação e a condição enfeitiçado. A magia pode até mesmo evitar a magia desejo e magias ou efeitos de poder similar usados para afetar a mente do alvo ou para adquirir informações sobre ele.',
            color=0xFF0000
        ) 
        # Tempo de conjuração da Magia 
        mind_blank.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        mind_blank.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        mind_blank.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia 
        mind_blank.add_field(name='Duração', value='24 horas', inline=False)  
        # o return vai retornar a variável com o embed criado
        return mind_blank


















    







