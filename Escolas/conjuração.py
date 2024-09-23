import discord

# conjuração - spells
class Conjuração:
    def __init__(self):
        pass
    import discord

    # Função para criar o Embed da magia "Criar Chamas (Produce Flame)"
    def criar_chamas():
        # Cria um objeto Embed
        produce_flame = discord.Embed(
            title="Criar Chamas (Produce Flame)",
            description="Uma chama tremulante aparece na sua mão. A chama permanece ai pela duração e não machuca nem você nem seu equipamento. A chama emite luz plena num raio de 3 metros [10-foot radius] e penumbra por 3 metros [10 feet] adicionais. A magia acaba se você dissipa-la usando uma ação ou se conjura-la novamente.\n\nVocê pode, também, atacar com a chama, no entanto, fazer isso acaba com a magia. Quando você conjura essa magia ou com uma ação em um turno posterior, você pode arremessar a chama numa criatura a até 9 metros [30 feet] de você. Faça um ataque à distância com magia. Se atingir, o alvo sofre 1d8 de dano de fogo.",
            color=0xFFA500  # Cor laranja
        )
        # Adiciona os detalhes da magia como campos no embed
        produce_flame.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        produce_flame.add_field(name="Alcance", value="pessoal", inline=False)
        produce_flame.add_field(name="Componentes", value="V S", inline=False)
        produce_flame.add_field(name="Duração", value="10 minutos", inline=False)
        produce_flame.set_footer(text="Dano aumentado em níveis superiores: 5° nível (2d8), 11° nível (3d8) e 17° nível (4d8)")

        return produce_flame
    # Função para criar o Embed da magia "Espirro Ácido (Acid Splash)"
    def espirro_acido():
        # Cria um objeto Embed
        acid_splash = discord.Embed(
            title="Espirro Ácido (Acid Splash)",
            description="Você arremessa uma bolha de ácido. Escolha uma criatura dentro do alcance, ou escolha duas criaturas dentro do alcance que estejam a 1,5 metro [5 feet] uma da outra. Um alvo deve ser bem sucedido num teste de resistência de Destreza ou sofrerá 1d6 de dano ácido.",
            color=0x00FF00  # Cor verde
        )
        # Adiciona os detalhes da magia como campos no embed
        acid_splash.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        acid_splash.add_field(name="Alcance", value="60 pés", inline=False)
        acid_splash.add_field(name="Componentes", value="V S", inline=False)
        acid_splash.add_field(name="Duração", value="instantâneo", inline=False)
        acid_splash.set_footer(text="Dano aumentado em níveis superiores: 5° nível (2d6), 11° nível (3d6) e 17° nível (4d6)")

        return acid_splash
    # Função para criar o Embed da magia "Mãos Mágicas (Mage Hand)"
    def maos_magicas():
        # Cria um objeto Embed
        mage_hand = discord.Embed(
            title="Mãos Mágicas (Mage Hand)",
            description="Uma mão espectral flutuante aparece num ponto, à sua escolha, dentro do alcance. A mão permanece pela duração ou até você dissipa-la com uma ação. A mão some se estiver a mais de 9 metros [30 feet] de você ou se você conjurar essa magia novamente.\n\nVocê pode usar sua ação para controlar a mão. Você pode usar a mão para manipular um objeto, abrir uma porta ou recipiente destrancado, guardar ou pegar um item de um recipiente aberto ou derramar o conteúdo de um frasco. Você pode mover a mão até 9 metros [30 feet] a cada vez que a usa.\n\nA mão não pode atacar, ativar itens mágicos ou carregar mais de 5 quilos [10 pounds].",
            color=0xFFD700  # Cor amarela
        )
        # Adiciona os detalhes da magia como campos no embed
        mage_hand.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mage_hand.add_field(name="Alcance", value="30 pés", inline=False)
        mage_hand.add_field(name="Componentes", value="V S", inline=False)
        mage_hand.add_field(name="Duração", value="1 minutos", inline=False)

        return mage_hand
    # Função para criar o Embed da magia "Rajada De Veneno (Poison Spray)"
    def rajada_de_veneno():
        # Cria um objeto Embed
        poison_spray = discord.Embed(
            title="Rajada De Veneno (Poison Spray)",
            description="Você ergue sua mão em direção de uma criatura que você possa ver, dentro do alcance e projeta um sopro de gás tóxico da sua palma. A criatura deve ser bem sucedida num teste de resistência de Constituição ou sofrerá 1d12 de dano de veneno.\n\nO dano dessa magia aumenta em 1d12 quando você alcança o 5° nível (2d12), 11° nível (3d12) e 17° nível (4d12).",
            color=0x228B22  # Cor verde floresta
        )
        # Adiciona os detalhes da magia como campos no embed
        poison_spray.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        poison_spray.add_field(name="Alcance", value="10 pés", inline=False)
        poison_spray.add_field(name="Componentes", value="V S", inline=False)
        poison_spray.add_field(name="Duração", value="1 minutos", inline=False)

        return poison_spray
        # Função para criar o Embed da magia "Alarme (Alarm)"
    def alarme():
        # Cria um objeto Embed
        alarm = discord.Embed(
            title="Alarme (Alarm)",
            description="Você coloca um alarme para intrusos desavisados. Escolha uma porta, uma janela ou uma área dentro do alcance que não seja maior que 6 metros cúbicos [20-foot cube]. Até a magia acabar, um alarme alerta você sempre que uma criatura Miúda ou maior tocarem ou entrarem na área protegida. Quando você conjura a magia, você pode designar as criaturas que não ativarão o alarme. Você também escolhe se o alarme será mental ou audível.\n\nUm alarme mental alerta você com um silvo na sua mente, se você estiver a até de 1,5 quilômetro [1 mile] da área protegida. Esse silvo acordará você se você estiver dormindo. Um alarme audível produz o som de um sino de mão por 10 minutos num raio de 18 metros [60 feet].",
            color=0xFFD700  # Cor dourada
        )
        # Adiciona os detalhes da magia como campos no embed
        alarm.add_field(name="Tempo de Conjuração", value="1 minutos", inline=False)
        alarm.add_field(name="Alcance", value="30 pés", inline=False)
        alarm.add_field(name="Componentes", value="V S M (um minúsculo sino e um pedaço de fino fio de prata)", inline=False)
        alarm.add_field(name="Duração", value="8 horas", inline=False)

        return alarm
    # Função para criar o Embed da magia "Área Escorregadia (Grease)"
    def area_escorregadia():
        # Cria um objeto Embed
        grease = discord.Embed(
            title="Área Escorregadia (Grease)",
            description="Graxa escorregadia cobre o solo em um quadrado de 3 metros [10 feet] centrado em um ponto, dentro do alcance, tornando essa área em terreno difícil pela duração.\n\nQuando a graxa aparece, cada criatura de pé na área deve ser bem sucedida num teste de resistência de Destreza ou cairá no chão. Uma criatura que entre na área ou termine seu turno nela, deve ser bem sucedido num teste de resistência de Destreza ou cairá no chão.",
            color=0x00FF00  # Cor verde
        )
        # Adiciona os detalhes da magia como campos no embed
        grease.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        grease.add_field(name="Alcance", value="60 pés", inline=False)
        grease.add_field(name="Componentes", value="V S M (um pouco de pele de porco ou manteiga)", inline=False)
        grease.add_field(name="Duração", value="1 minutos", inline=False)

        return grease
    import discord

    # Função para criar o Embed da magia "Constrição (Entangle)"
    def constricao():
        # Cria um objeto Embed
        entangle = discord.Embed(
            title="Constrição (Entangle)",
            description="Ervas e vinhas poderosas brotam do solo num quadrado de 6 metros [20-foot square] a partir de um ponto dentro do alcance. Pela duração, essas plantas transformam o solo na área em terreno difícil.\n\nUma criatura na área quando você conjurar a magia deve ser bem sucedida num teste de resistência de Força ou ficará impedida pelo emaranhado de plantas, até a magia acabar. Uma criatura impedida pelas plantas pode usar sua ação para realizar um teste de Força, contra a CD da magia. Se for bem sucedido, irá se libertar.\n\nQuando a magia termina, as plantas conjuradas murcharão.",
            color=0x800080  # Cor roxa
        )
        # Adiciona os detalhes da magia como campos no embed
        entangle.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        entangle.add_field(name="Alcance", value="90 pés", inline=False)
        entangle.add_field(name="Componentes", value="V S", inline=False)
        entangle.add_field(name="Duração", value="concentração, até 1 minutos", inline=False)

        return entangle
        # Função para criar o Embed da magia "Disco Flutuante (Floating Disk)"
    def disco_flutuante():
        # Cria um objeto Embed
        floating_disk = discord.Embed(
            title="Disco Flutuante (Floating Disk)",
            description="Essa magia cria um plano horizontal, circular de energia de 90 cm de diâmetro por 2,5 cm de espessura, que flutua 90 centímetros [3 feet] acima do chão em um espaço desocupado, à sua escolha, que você possa ver dentro do alcance. O disco permanece pela duração e pode suportar até 250 quilos. Se mais peso for colocado nele, a magia termina, e tudo em cima do disco cai no chão.\n\nO disco é imóvel enquanto você estiver a até 6 metros [20 feet] dele. Se você se afastar a mais de 6 metros [20 feet] dele, o disco seguirá você, mantendo-se a 6 metros [20 feet] de você. Ele pode atravessar terreno irregular, subir ou descer escadas, encostas e similares, mas ele não pode atravessar mudanças de elevação de 3 metros [10 feet] ou mais. Por exemplo, o disco não pode atravessar um fosso de 3 metros [10 feet] de profundidade nem poderia sair de tal fosso se tivesse sido criado no fundo dele.\n\nSe você se afastar mais de 30 metros [100 feet] do disco (tipicamente por ele não poder rodear um obstáculo para seguir você), a magia acaba.",
            color=0x00FFFF  # Cor azul ciano
        )
        # Adiciona os detalhes da magia como campos no embed
        floating_disk.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        floating_disk.add_field(name="Alcance", value="30 pés", inline=False)
        floating_disk.add_field(name="Componentes", value="V S M (uma gota de mercúrio)", inline=False)
        floating_disk.add_field(name="Duração", value="1 horas", inline=False)

        return floating_disk
    import discord

    # Função para criar o Embed da magia "Névoa Obscurecente (Fog Cloud)"
    def nevoa_obscurecente():
        # Cria um objeto Embed
        fog_cloud = discord.Embed(
            title="Névoa Obscurecente (Fog Cloud)",
            description="Você cria uma esfera de 6 metros de raio [20-foot radius] de névoa, centrada num ponto, dentro do alcance. A esfera se espalha, dobrando esquinas, e a área dela é de escuridão densa. Ela permanece pela duração ou até um vento moderado ou mais rápido (pelo menos 15 quilômetros [10 miles] por hora) dispersa-la.",
            color=0x708090  # Cor cinza
        )
        # Adiciona os detalhes da magia como campos no embed
        fog_cloud.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        fog_cloud.add_field(name="Alcance", value="120 pés", inline=False)
        fog_cloud.add_field(name="Componentes", value="V S", inline=False)
        fog_cloud.add_field(name="Duração", value="concentração, até 1 horas", inline=False)
        fog_cloud.add_field(name="Níveis Superiores", value="Quando conjurada com espaços de magia de 2° nível ou superior, o raio da névoa aumenta em 6 metros [20 feet] para cada nível acima do 1°.", inline=False)

        return fog_cloud
    # Função para criar o Embed da magia "Servo Invisível (Unseen Servant)"

    def servo_invisivel():
        # Cria um objeto Embed
        unseen_servant = discord.Embed(
            title="Servo Invisível (Unseen Servant)",
            description="Essa magia cria uma força invisível, sem mente e sem forma que realiza tarefas simples, ao seu comando, até a magia acabar. O servo aparece do nada em um espaço desocupado no chão, dentro do alcance. Ele tem CA 10, 1 ponto de vida, Força 2 e não pode atacar. Se ele cair a 0 pontos de vida, a magia acaba.\n\nUma vez em cada um dos seus turnos, com uma ação bônus, você pode comandar, mentalmente, o servo para se mover até 4,5 metros [15 feet] e interagir com um objeto. O servo pode realizar tarefas simples que um serviçal humano faria, como buscar coisas, limpar, consertar, dobrar roupas, acender chamas, servir comida ou derramar vinho. Uma vez que um comando seja dado, o servo realiza a tarefa da melhor forma possível, até completar a tarefa, então esperará o seu próximo comando.\n\nSe você comandar o servo a realizar uma tarefa que poderia afasta-lo a mais de 18 metros [60 feet] de você, a magia termina.",
            color=0xFFD700  # Cor dourada
        )
        # Adiciona os detalhes da magia como campos no embed
        unseen_servant.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        unseen_servant.add_field(name="Alcance", value="60 pés", inline=False)
        unseen_servant.add_field(name="Componentes", value="V S M (um pedaço de barbante e um pouco de madeira)", inline=False)
        unseen_servant.add_field(name="Duração", value="1 horas", inline=False)
        
        return unseen_servant
    # Função para criar o Embed da magia "Convocar Montaria (Find Steed)"
    def convocar_montaria():
        # Cria um objeto Embed
        find_steed = discord.Embed(
            title="Convocar Montaria (Find Steed)",
            description="Você convoca um espírito que assume a forma de uma montaria excepcionalmente inteligente, forte e leal, criando uma ligação duradoura com ela. Aparecendo em um espaço desocupado dentro do alcance, a montaria adquire a forma que você escolher, como um cavalo de guerra, um pônei, um camelo, um alce ou um mastim. (Seu Mestre pode permitir outros animais para serem convocados como montarias.) A montaria tem as estatísticas da forma escolhida, no entanto, ele é um celestial, corruptor ou fada (à sua escolha) ao invés do seu tipo normal. Além disso, se sua montaria tiver Inteligência 5 ou menor, a Inteligência dela se torna 6 e ela ganha a capacidade de compreender um idioma, à sua escolha, que você fala.\n\nSua montaria serve tanto para cavalgar quando para o combate e você tem uma ligação instintiva com ela que permite a vocês lutarem como uma unidade singular. Enquanto estiver montado na sua montaria, você pode fazer com que qualquer magia que você conjure que tenha alcance pessoal, também afete a sua montaria.\n\nQuando a montaria cair a 0 pontos de vida, ela desaparece, não deixando qualquer corpo físico para trás. Você também pode dispensar sua montaria a qualquer momento, com uma ação, fazendo-a desaparecer. Em ambos os casos, conjurar essa magia novamente convocará a mesma montaria, restaurando-a ao seu máximo de pontos de vida.\n\nEnquanto sua montaria estiver a até 1,5 quilômetro [1 mile] de você, você pode se comunicar telepaticamente com ela.\n\nVocê não pode ter mais de uma montaria ligado por essa magia por vez. Com uma ação, você pode liberar a montaria da ligação a qualquer momento, fazendo-a desaparecer.",
            color=0x4169E1  # Cor azul royal
        )
        # Adiciona os detalhes da magia como campos no embed
        find_steed.add_field(name="Tempo de Conjuração", value="10 minutos", inline=False)
        find_steed.add_field(name="Alcance", value="30 pés", inline=False)
        find_steed.add_field(name="Componentes", value="V S", inline=False)
        find_steed.add_field(name="Duração", value="instantâneo", inline=False)
        
        return find_steed
   
    # Função para criar o Embed da magia "Esfera Flamejante (Flaming Sphere)"
    def conjuracao_esfera_flamejante():
        # Cria um objeto Embed
        flaming_sphere = discord.Embed(
            title="Esfera Flamejante (Flaming Sphere)",
            description="Uma esfera de fogo de 1,5 metros de diâmetro [5-foot-diameter sphere] aparece em um espaço desocupado de sua escolha dentro do alcance e dura pela duração do feitiço. Qualquer criatura que termine a sua vez dentro de 1,5 metros [5 feet] da esfera deve fazer um teste de resistência de Destreza. A criatura sofre 2d6 de dano de fogo em um teste com falha, ou metade de dano em um teste bem sucedido.\n\nComo um ação bônus, você pode mover a esfera até 9 metros [30 feet]. Se você chocar a esfera contra uma criatura, essa criatura deve fazer o teste de resistência contra o dano da esfera, e a esfera pára de se mover neste turno.\n\nQuando você move a esfera, você pode dirigi-la sobre barreiras até 1,5 metros [5 feet] de altura e pular por sobre poços de até 3 metros [10 feet] de largura. A esfera inflama objetos inflamáveis que não estejam sendo vestidos ou carregados, e ela emite luz brilhante em um raio de 6 metros [20 feet] e luz fraca por mais 6 metros [20 feet].\n\nEm Níveis Superiores. Quando você conjura esta magia feitiço usando um espaço de magia de 3º nível ou superior, o dano aumenta em 1d6 para cada nível do espaço de magia acima de 2º.",
            color=0xFF4500  # Cor laranja
        )
        # Adiciona os detalhes da magia como campos no embed
        flaming_sphere.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        flaming_sphere.add_field(name="Alcance", value="60 pés", inline=False)
        flaming_sphere.add_field(name="Componentes", value="V S M (um pouco de seco, uma pitada de enxofre e uma camada de pó de ferro)", inline=False)
        flaming_sphere.add_field(name="Duração", value="concentração, até 1 minutos", inline=False)
        
        return flaming_sphere
    # Função para criar o Embed da magia "Passo Nebuloso (Misty Step)"
    def passo_nebuloso():
        # Cria um objeto Embed
        misty_step = discord.Embed(
            title="Passo Nebuloso (Misty Step)",
            description="Brevemente envolto por uma neblina prateada, você se teletransporta a até 9 metros [30 feet] para um espaço desocupado que você possa ver.",
            color=0x87CEEB  # Cor azul claro
        )
        # Adiciona os detalhes da magia como campos no embed
        misty_step.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        misty_step.add_field(name="Alcance", value="pessoal", inline=False)
        misty_step.add_field(name="Componentes", value="V", inline=False)
        misty_step.add_field(name="Duração", value="instantâneo", inline=False)
        
        return misty_step
        # Função para criar o Embed da magia "Teia (Web)"
    def teia():
        # Cria um objeto Embed
        web_spell = discord.Embed(
            title="Teia (Web)",
            description="Você conjura uma massa de teias espessas e pegajosas num ponto, à sua escolha, dentro do alcance. As teias preenchem um cubo de 6 metros [20-foot cube] naquele ponto, pela duração. As teias são terreno difícil e causam escuridão leve na área delas.\n\nSe as teias não estiverem sendo suportadas por duas massas sólidas (como duas paredes ou árvores) ou em camadas sobre um chão, parede ou teto, a teia conjurada desaba sobre si mesma e a magia termina no início do seu próximo turno. As teias em camadas sobre uma superfície plana terão 1,5 metro [5 feet] de profundidade.\n\nCada criatura que começar seu turno nas teias ou entrar nelas durante seu turno, deve realizar um teste de resistência de Destreza. Se falhar na resistência, a criatura estará impedida enquanto permanecer nas teias ou até se libertar.\n\nUma criatura impedida pelas teias pode usar sua ação para realizar um teste de Força contra a CD da magia. Se obtiver sucesso, ela não estará mais impedida.\n\nAs teias são inflamáveis. Qualquer cubo de 1,5 metro [5-foot cube] de teia exposto ao fogo, é consumida por ele em 1 rodada, causando 2d4 de dano de fogo a qualquer criatura que começar seu turno nas chamas.",
            color=0xFFA500  # Cor laranja
        )
        # Adiciona os detalhes da magia como campos no embed
        web_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        web_spell.add_field(name="Alcance", value="60 pés", inline=False)
        web_spell.add_field(name="Componentes", value="V S M (um pedaço de teia de aranha)", inline=False)
        web_spell.add_field(name="Duração", value="concentração, até 1 hora", inline=False)
        
        return web_spell
    # Função para criar o Embed da magia "Conjurar Animais (Conjure Animals)"
    def conjurar_animais():
        # Cria um objeto Embed
        conjurar_animais_spell = discord.Embed(
            title="Conjurar Animais (Conjure Animals)",
            description="Você convoca espíritos feéricos que assumem a forma de bestas e aparecem em espaços desocupados que você pode ver dentro do alcance. Escolha uma das seguintes opções para o que aparece:\n\n- Uma besta de nível de desafio 2 ou inferior.\n- Duas bestas de nível de desafio 1 ou inferior.\n- Quatro bestas de nível de desafio 1/2 ou inferior.\n- Oito bestas de nível de desafio 1/4 ou inferior.\nCada besta é também considerada uma fada e desaparece quando cair a 0 pontos de vida ou quando a magia acabar.\n\nAs criaturas invocadas são amigáveis a você e a seus companheiros. Role a iniciativa para as criaturas invocadas como um grupo, que age no seu próprio turno. Eles obedecem a quaisquer comandos verbais que você emitir (não requer uma ação sua). Se você não emitir nenhum comando a elas, elas se defenderão de criaturas hostis, mas no mais, não realizarão nenhuma ação.\n\nO Mestre possui as estatísticas das criaturas.",
            color=0x008080  # Cor teal
        )
        # Adiciona os detalhes da magia como campos no embed
        conjurar_animais_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        conjurar_animais_spell.add_field(name="Alcance", value="60 pés", inline=False)
        conjurar_animais_spell.add_field(name="Componentes", value="V S", inline=False)
        conjurar_animais_spell.add_field(name="Duração", value="concentração, até 1 hora", inline=False)
        # Adiciona os efeitos de níveis superiores no footer
        conjurar_animais_spell.set_footer(text="Em Níveis Superiores: Se conjurada com espaços superiores, o dobro das criaturas com espaço de 5° nível, o triplo com 7° nível e o quadruplo com 9° nível.")

        return conjurar_animais_spell
    # Função para criar o Embed da magia "Convocar Relâmpagos (Call Lightning)"
    def convocar_relampagos():
        # Cria um objeto Embed
        convocar_relampagos_spell = discord.Embed(
            title="Convocar Relâmpagos (Call Lightning)",
            description="Uma nuvem tempestuosa aparece em formato cilíndrico com 3 metros [10 feet] de altura e 18 metros [60 feet] de raio, centrada num ponto que você possa ver, 30 metros [100 feet] acima de você. A magia falha se você não puder ver um ponto no ar em que a nuvem possa aparecer (por exemplo, se você estiver em uma sala que não possa comportar a nuvem).\n\nQuando você conjurar a magia, escolha um ponto que você possa ver dentro do alcance. Um raio de eletricidade é disparado da nuvem no ponto. Cada criatura a 1,5 metro [5 feet] desse ponto deve realizar um teste de resistência de Destreza. Uma criatura sofre 3d10 de dano elétrico se falhar no teste, ou metade desse dano se passar. Em cada um dos seus turnos, até a magia acabar, você pode usar sua ação para convocar um relâmpago dessa forma novamente, afetando o mesmo ponto ou um diferente.\n\nSe você estiver a céu aberto em condições tempestuosas quando conjurar essa magia, a magia lhe dá controle sobre a tempestade existente ao invés de criar uma nova. Sob tais condições, o dano da magia aumenta em 1d10.",
            color=0xFFD700  # Cor gold
        )
        # Adiciona os detalhes da magia como campos no embed
        convocar_relampagos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        convocar_relampagos_spell.add_field(name="Alcance", value="120 pés", inline=False)
        convocar_relampagos_spell.add_field(name="Componentes", value="V S", inline=False)
        convocar_relampagos_spell.add_field(name="Duração", value="concentração, até 10 minutos", inline=False)
        # Adiciona os efeitos de níveis superiores no footer
        convocar_relampagos_spell.set_footer(text="Em Níveis Superiores: O dano aumenta em 1d10 para cada nível do espaço acima do 3°.")

        return convocar_relampagos_spell
    # Função para criar o Embed da magia "Criar Alimentos e Água (Create Food and Water)"
    def criar_alimentos():
        # Cria um objeto Embed
        criar_alimentos_spell = discord.Embed(
            title="Criar Alimentos e Água (Create Food and Water)",
            description="Você cria 25 quilos [45 pounds] de comida e 100 litros [30 gallons] de água no solo ou em um recipiente dentro do alcance, suficiente para sustentar até quinze humanoides ou cinco montarias por 24 horas. A comida é insossa, porém nutritiva e estraga se não for consumida após 24 horas. A água é limpa e não fica ruim.",
            color=0x00FF00  # Cor green
        )
        # Adiciona os detalhes da magia como campos no embed
        criar_alimentos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        criar_alimentos_spell.add_field(name="Alcance", value="30 pés", inline=False)
        criar_alimentos_spell.add_field(name="Componentes", value="V S", inline=False)
        criar_alimentos_spell.add_field(name="Duração", value="instantâneo", inline=False)

        return criar_alimentos_spell
    # Função para criar o Embed da magia "Espíritos Guardiões (Spirit Guardians)"
    def espiritos_guardioes():
        # Cria um objeto Embed
        espiritos_guardioes_spell = discord.Embed(
            title="Espíritos Guardiões (Spirit Guardians)",
            description="Você evoca espíritos para protegê-lo. Eles flutuam a seu redor, a uma distância de 4,5 metros [15 feet], pela duração. Se você for bom ou neutro, as formas espectrais deles aparentam ser angelicais ou feéricas (à sua escolha). Se você for mau, eles parecerão demoníacos.\n\nQuando você conjura essa magia, você pode designar qualquer quantidade de criaturas que você possa ver para não serem afetadas por ela. O deslocamento de uma criatura afetada é reduzido à metade na área e, quando a criatura entrar na área pela primeira vez num turno ou começar seu turno nela, ela deve realizar um teste de resistência de Sabedoria. Se falhar na resistência, a criatura sofrerá 3d8 de dano radiante (se você for bom ou neutro) ou 3d8 de dano necrótico (se você for mau). Com um sucesso na resistência, a criatura sofre metade desse dano.",
            color=0xFF4500  # Cor orange
        )
        # Adiciona os detalhes da magia como campos no embed
        espiritos_guardioes_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        espiritos_guardioes_spell.add_field(name="Alcance", value="pessoal", inline=False)
        espiritos_guardioes_spell.add_field(name="Componentes", value="V S M (um símbolo sagrado)", inline=False)
        espiritos_guardioes_spell.add_field(name="Duração", value="concentração, até 10 minutos", inline=False)
        espiritos_guardioes_spell.set_footer(text="Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 4° nível ou superior, o dano aumenta em 1d8 para cada nível do espaço acima do 3°.")

        return espiritos_guardioes_spell
   # Função para criar o Embed da magia "Nevasca (Sleet Storm)"
    def nevasca():
        # Cria um objeto Embed
        nevasca_spell = discord.Embed(
            title="Nevasca (Sleet Storm)",
            description="Até a magia acabar, uma chuva congelante e neve caem num cilindro de 6 metros de altura [20-foot-tall] por 12 metros de raio [40-foot radius], centrado num ponto à sua escolha, dentro do alcance. A área é preenchida por escuridão densa, extinguindo chamas expostas na área.\n\nO solo na área é coberto por gelo escorregadio, tornando-o terreno difícil. Quando uma criatura entra na área da magia pela primeira vez em um turno ou começa seu turno nela, ela deve realizar um teste de resistência de Destreza. Se falhar, cairá no chão.\n\nSe uma criatura estiver se concentrando na área da magia, ela deve realizar um teste de resistência de Constituição contra a CD da magia ou perderá a concentração.",
            color=0x00FFFF  # Cor azul claro
        )
        # Adiciona os detalhes da magia como campos no embed
        nevasca_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        nevasca_spell.add_field(name="Alcance", value="150 pés", inline=False)
        nevasca_spell.add_field(name="Componentes", value="V S M (um punhado de poeira e algumas gotas de água)", inline=False)
        nevasca_spell.add_field(name="Duração", value="concentração, até 1 minutos", inline=False)
        nevasca_spell.set_footer(text="")

        return nevasca_spell
    # Função para criar o Embed da magia "Névoa Fétida (Stinking Cloud)"
    def nevoa_fetida():
        # Cria um objeto Embed
        nevoa_fetida_spell = discord.Embed(
            title="Névoa Fétida (Stinking Cloud)",
            description="Você cria uma esfera de gás amarelado nauseante, com um raio de 6 metros [20-foot radius], centrada num ponto dentro do alcance. A névoa se espalha, dobrando esquinas, e sua área é de escuridão densa. A névoa perdura no ar pela duração.\n\nCada criatura completamente dentro da névoa no início do seu turno deve realizar um teste de resistência de Constituição contra veneno. Se falhar, a criatura gastará sua ação nesse turno tentando vomitar e cambaleando.\n\nUm vento moderado (pelo menos 15 quilômetros [10 miles] por hora) dispersará a névoa após 4 rodadas. Um vento forte (pelo menos 30 quilômetros [20 miles] por hora) dispersará a névoa após 1 rodada.",
            color=0x8B4513  # Cor marrom
        )
        # Adiciona os detalhes da magia como campos no embed
        nevoa_fetida_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        nevoa_fetida_spell.add_field(name="Alcance", value="90 pés", inline=False)
        nevoa_fetida_spell.add_field(name="Componentes", value="V S M (um ovo podre ou várias folhas de repolho)", inline=False)
        nevoa_fetida_spell.add_field(name="Duração", value="concentração, até 1 minutos", inline=False)

        return nevoa_fetida_spell
    # Função para criar o Embed da magia "Arca Secreta (Secret Chest)"
    def arca_secreta():
        # Cria um objeto Embed
        arca_secreta_spell = discord.Embed(
            title="Arca Secreta (Secret Chest)",
            description="Você esconde um baú, e todo o seu conteúdo, no Plano Etéreo. Você deve tocar o baú e a réplica em miniatura que serve como componente material para a magia. O baú pode acomodar até 3,6 metros cúbicos [12 cubic feet] de matéria inorgânica (90 cm por 60 cm por 60 cm) [3 feet by 2 feet by 2 feet].\n\nEnquanto o baú permanecer no Plano Etéreo, você pode usar uma ação e tocar a réplica para revocar o baú. Ele aparece em um espaço desocupado no chão a 1,5 metro [5 feet] de você. Você pode enviar o baú de volta ao Plano Etéreo usando uma ação e tocando tanto no baú quanto na réplica.\n\nApós 60 dias, existe 5 por cento de chance, cumulativa, por dia do efeito da magia terminar. Esse efeito termina se você conjurar essa magia novamente, se a pequena réplica do baú for destruída ou se você decidir terminar a magia usando uma ação. Se a magia terminar enquanto o baú maior estiver no Plano Etéreo, ele estará irremediavelmente perdido.",
            color=0x800080  # Cor purple
        )
        # Adiciona os detalhes da magia como campos no embed
        arca_secreta_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        arca_secreta_spell.add_field(name="Alcance", value="toque", inline=False)
        arca_secreta_spell.add_field(name="Componentes", value="V S M (um baú requintado, de 90 cm por 60 cm por 60 cm [3 feet by 2 feet by 2 feet], construído com materiais raros valendo e uma réplica Miúda feita do mesmo material, valendo, no mínimo, 5050 gp)", inline=False)
        arca_secreta_spell.add_field(name="Duração", value="instantâneo", inline=False)
   

        return arca_secreta_spell
    # Função para criar o Embed da magia "Cão Fiel (Faithful Hound)"
    def cao_fiel():
        # Cria um objeto Embed
        cao_fiel_spell = discord.Embed(
            title="Cão Fiel (Faithful Hound)",
            description="Você conjura um cão de guarda fantasma em um espaço desocupado que você possa ver, dentro do alcance, que permanece pela duração, até você dissipa-lo com uma ação ou até você se mover para mais de 30 metros [100 feet] dele.\n\nO cão é invisível para todas as criaturas, exceto para você, e não pode ser ferido. Quando uma criatura Pequena ou maior se aproximar a 9 metros [30 feet] sem, primeiramente, falar a senha que você especifica quando conjura a magia, o cão começa a latir muito alto. O cão vê criaturas invisíveis e pode ver no Plano Etéreo. Ele ignora ilusões.\n\nNo começo de cada um dos seus turnos, o cão tenta morder uma criatura a 1,5 metro [5 feet] dele que seja hostil a você. O bônus de ataque do cão é igual ao seu modificador de habilidade de conjuração + seu bônus de proficiência. Se atingir, ele causa 4d8 de dano perfurante.",
            color=0x0000FF  # Cor blue
        )
        # Adiciona os detalhes da magia como campos no embed
        cao_fiel_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        cao_fiel_spell.add_field(name="Alcance", value="30 pés", inline=False)
        cao_fiel_spell.add_field(name="Componentes", value="V S M (um minúsculo apito de prata, um pedaço de osso e um fio)", inline=False)
        cao_fiel_spell.add_field(name="Duração", value="8 horas", inline=False)

        return cao_fiel_spell
    # Função para criar o Embed da magia "Conjurar Elementais Menores (Conjure Minor Elementals)"
    def conjurar_elementais_menores():
        # Cria um objeto Embed
        elementais_spell = discord.Embed(
            title="Conjurar Elementais Menores (Conjure Minor Elementals)",
            description="Você invoca elementais que aparecem em espaços desocupados, que você possa ver dentro do alcance. Você escolhe uma das opções a seguir para aparecer:\n\n- Um elemental de nível de desafio 2 ou inferior.\n- Dois elementais de nível de desafio 1 ou inferior.\n- Quatro elementais de nível de desafio 1/2 ou inferior.\n- Oito elementais de nível de desafio 1/4 ou inferior.\n\nUm elemental invocado através dessa magia desaparece quando cair a 0 pontos de vida ou quando a magia acabar.\n\nAs criaturas invocadas são amigáveis a você e a seus companheiros. Role a iniciativa para as criaturas invocadas como um grupo, que age no seu próprio turno. Eles obedecem a quaisquer comandos verbais que você emitir (não requer uma ação sua). Se você não emitir nenhum comando a elas, elas se defenderão de criaturas hostis, mas no mais, não realizarão nenhuma ação.\n\nO Mestre possui as estatísticas das criaturas.",
            color=0x00FF00  # Cor green
        )
        # Adiciona os detalhes da magia como campos no embed
        elementais_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        elementais_spell.add_field(name="Alcance", value="90 pés", inline=False)
        elementais_spell.add_field(name="Componentes", value="V S", inline=False)
        elementais_spell.add_field(name="Duração", value="concentração, até 1 hora", inline=False)
        elementais_spell.set_footer(text="Em Níveis Superiores. Se você conjurar essa magia usando certos espaços de magia superiores, você escolhe uma das opções de invocação acima e mais criaturas aparecem: o dobro delas com um espaço de 6° nível e o triplo delas com um espaço de 8° nível.")

        return elementais_spell
    # Função para criar o Embed da magia "Conjurar Seres Da Floresta (Conjure Woodland Beings)"
    def conjuracao_seres_floresta():
    # Cria um objeto Embed
        seres_floresta_spell = discord.Embed(
            title="Conjurar Seres Da Floresta (Conjure Woodland Beings)",
            description="Você invoca criaturas feéricas que aparecem em espaços desocupados, que você possa ver dentro do alcance. Escolha uma das opções a seguir para aparecer:\n\n- Uma criatura feérica de nível de desafio 2 ou inferior\n- Duas criaturas feéricas de nível de desafio 1 ou inferior\n- Quatro criaturas feéricas de nível de desafio 1/2 ou inferior\n- Oito criaturas feéricas de nível de desafio 1/4 ou inferior\n\nUma criatura invocada desaparece quando cair a 0 pontos de vida ou quando a magia acabar.\n\nAs criaturas invocadas são amigáveis a você e a seus companheiros. Role a iniciativa para as criaturas invocadas como um grupo, que age no seu próprio turno. Eles obedecem a quaisquer comandos verbais que você emitir (não requer uma ação sua). Se você não emitir nenhum comando a elas, elas se defenderão de criaturas hostis, mas no mais, não realizarão nenhuma ação.\n\nO Mestre possui as estatísticas das criaturas.",
            color=0x008080  # Cor teal
        )
        # Adiciona os detalhes da magia como campos no embed
        seres_floresta_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        seres_floresta_spell.add_field(name="Alcance", value="60 pés", inline=False)
        seres_floresta_spell.add_field(name="Componentes", value="V S M (um fruto sagrado por criatura invocada)", inline=False)
        seres_floresta_spell.add_field(name="Duração", value="concentração, até 1 hora", inline=False)
        seres_floresta_spell.set_footer(text="Em Níveis Superiores. Se você conjurar essa magia usando certos espaços de magia superiores, você escolhe uma das opções de invocação acima e mais criaturas aparecem: o dobro delas com um espaço de 6° nível e o triplo delas com um espaço de 8° nível.")

        return seres_floresta_spell# Função para criar o Embed da magia "Conjurar Seres Da Floresta (Conjure Woodland Beings)"
    # Função para criar o Embed da magia "Guardião Da Fé (Guardian Of Faith)"
    def conjuracao_guardiao_fe():
        # Cria um objeto Embed
        guardiao_fe_spell = discord.Embed(
            title="Guardião Da Fé (Guardian Of Faith)",
            description="Um guardião espectral Grande aparece e flutua, pela duração, em um espaço desocupado, à sua escolha, que você possa ver dentro do alcance. O guardião ocupa esse espaço e é indistinto, exceto por uma espada reluzente e um escudo brasonado com o símbolo da sua divindade.\n\nQualquer criatura hostil a você que se mover para um espaço a até 3 metros [10 feet] do guardião pela primeira vez em um turno, deve ser bem sucedida num teste de resistência de Destreza. A criatura sofre 20 de dano radiante se falhar na resistência ou metade desse dano se obtiver sucesso. O guardião desaparece após ter causado um total de 60 de dano.",
            color=0xFFFF00  # Cor amarela
        )
        # Adiciona os detalhes da magia como campos no embed
        guardiao_fe_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        guardiao_fe_spell.add_field(name="Alcance", value="30 pés", inline=False)
        guardiao_fe_spell.add_field(name="Componentes", value="V", inline=False)
        guardiao_fe_spell.add_field(name="Duração", value="8 horas", inline=False)

        return guardiao_fe_spell
    # Função para criar o Embed da magia "Porta Dimensional (Dimension Door)"
    def conjuracao_porta_dimensional():
        # Cria um objeto Embed
        porta_dimensional_spell = discord.Embed(
            title="Porta Dimensional (Dimension Door)",
            description="Você se teletransporta da sua posição atual para qualquer local dentro do alcance. Você aparece exatamente no local desejado. Pode ser um lugar que você possa ver, um que você possa visualizar ou um que você possa descrever indicando a distância e direção, como “60 metros [200 feet] diretamente pra baixo” ou “90 metros [300 feet], subindo para noroeste num ângulo de 45 graus”.\n\nVocê pode levar objetos com você, contanto que o peso deles não exceda o que você pode carregar. Você também pode levar uma criatura voluntária do seu tamanho ou menor, que esteja carregando equipamento até o limite da capacidade de carga dela. A criatura deve estar a 1,5 metro [5 feet] de você quando você conjurar a magia.\n\nSe você aparecer em um lugar que já esteja ocupado por um objeto ou uma criatura, você e qualquer criatura viajando com você, sofrem 4d6 de dano de energia cada um e a magia falha em teletransportar vocês.",
            color=0x9370DB  # Cor purple
        )
        # Adiciona os detalhes da magia como campos no embed
        porta_dimensional_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        porta_dimensional_spell.add_field(name="Alcance", value="500 pés", inline=False)
        porta_dimensional_spell.add_field(name="Componentes", value="V", inline=False)
        porta_dimensional_spell.add_field(name="Duração", value="instantâneo", inline=False)

        return porta_dimensional_spell
    # Função para criar o Embed da magia "Tentáculos Negros (Black Tentacles)"
    def conjuracao_tentaculos_negros():
        # Cria um objeto Embed
        tentaculos_negros_spell = discord.Embed(
            title="Tentáculos Negros (Black Tentacles)",
            description="Tentáculos negros retorcidos preenchem um quadrado de 6 metros [20-foot square] no chão, que você possa ver dentro do alcance. Pela duração, esses tentáculos transformam o solo na área em terreno difícil.\n\nQuando uma criatura adentrar a área afetada pela primeira vez em um turno ou começar o turno dela lá, a criatura deve ser bem sucedida num teste de resistência de Destreza ou sofrerá 3d6 de dano de concussão e estará impedida pelos tentáculos até o fim da magia. Uma criatura que começar seu turno na área e já estiver impedida pelos tentáculos sofre 3d6 de dano de concussão.\n\nUma criatura impedida pelos tentáculos pode usar sua ação para realizar um teste de Força ou Destreza (à escolha dela) contra a CD da sua magia. Se ela obtiver sucesso, ela se libertará.",
            color=0x8B4513  # Cor saddlebrown
        )
        # Adiciona os detalhes da magia como campos no embed
        tentaculos_negros_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        tentaculos_negros_spell.add_field(name="Alcance", value="90 pés", inline=False)
        tentaculos_negros_spell.add_field(name="Componentes", value="V S M (um pedaço de tentáculo de um polvo gigante ou lula gigante)", inline=False)
        tentaculos_negros_spell.add_field(name="Duração", value="concentração, até 1 minutos", inline=False)

        return tentaculos_negros_spell
    # Função para criar o Embed da magia "Círculo de Teletransporte (Teleportation Circle)"
    def conjuracao_circulo_teletransporte():
        # Cria um objeto Embed
        circulo_teletransporte_spell = discord.Embed(
            title="Círculo de Teletransporte (Teleportation Circle)",
            description="À medida que você conjura essa magia, você desenha um círculo de 3 metros [10 feet] de diâmetro no chão, inscrevendo selos que conectam sua localização a um círculo de teletransporte permanente, à sua escolha, cuja sequência de selos você conheça e esteja no mesmo plano de existência que você. Um portal cintilante se abre dentro do círculo que você desenhou e permanece aberto até o final do seu próximo turno. Qualquer criatura que entrar no portal, instantaneamente, aparecerá a 1,5 metro [5 feet] do círculo de destino ou no espaço desocupado mais próximo, se o espaço estiver ocupado.\n\nMuitos templos principais, guildas e outros locais importantes possuem círculos de teletransporte permanentes inscritos em algum lugar dos seus confins. Cada círculo desse inclui uma sequência única de selos – uma sequência de runas mágicas dispostas em um padrão específico. Quando você adquire a capacidade de conjurar essa magia pela primeira vez, você aprende a sequência de selos de dois destinos no Plano Material, determinadas pelo Mestre. Você pode aprender sequências de selos adicionais durante suas aventuras. Você pode consignar uma nova sequência de selos a memória após estuda-la por 1 minuto.\n\nVocê pode criar um círculo de teletransporte permanente ao conjurar essa magia no mesmo local a cada dia por um ano. Você não precisa usar o círculo para se teletransportar quando você conjurar a magia desse modo.",
            color=0x0000FF  # Cor azul
        )
        # Adiciona os detalhes da magia como campos no embed
        circulo_teletransporte_spell.add_field(name="Tempo de Conjuração", value="1 minutos", inline=False)
        circulo_teletransporte_spell.add_field(name="Alcance", value="10 pés", inline=False)
        circulo_teletransporte_spell.add_field(name="Componentes", value="V M (giz e tintas raros infundidos com pedras preciosas valendo, no mínimo, 50 gp que a magia consome)", inline=False)
        circulo_teletransporte_spell.add_field(name="Duração", value="1 rodadas", inline=False)

        return circulo_teletransporte_spell
    # Função para criar o Embed da magia "Conjurar Animais (Conjure Animals)"
    def conjurar_animais():
        # Cria um objeto Embed
        conjurar_animais_spell = discord.Embed(
            title="Conjurar Animais (Conjure Animals)",
            description="Você convoca espíritos feéricos que assumem a forma de bestas e aparecem em espaços desocupados que você pode ver dentro do alcance. Escolha uma das seguintes opções para o que aparece:\n\n- Uma besta de nível de desafio 2 ou inferior.\n- Duas bestas de nível de desafio 1 ou inferior.\n- Quatro bestas de nível de desafio 1/2 ou inferior.\n- Oito bestas de nível de desafio 1/4 ou inferior.\n\nCada besta é também considerada uma fada e desaparece quando cair a 0 pontos de vida ou quando a magia acabar.\n\nAs criaturas invocadas são amigáveis a você e a seus companheiros. Role a iniciativa para as criaturas invocadas como um grupo, que age no seu próprio turno. Eles obedecem a quaisquer comandos verbais que você emitir (não requer uma ação sua). Se você não emitir nenhum comando a elas, elas se defenderão de criaturas hostis, mas no mais, não realizarão nenhuma ação.\n\nO Mestre possui as estatísticas das criaturas.",
            color=0x00FF00  # Cor verde
        )
        # Adiciona os detalhes da magia como campos no embed
        conjurar_animais_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        conjurar_animais_spell.add_field(name="Alcance", value="60 pés", inline=False)
        conjurar_animais_spell.add_field(name="Componentes", value="V S", inline=False)
        conjurar_animais_spell.add_field(name="Duração", value="concentração, até 1 horas", inline=False)
        conjurar_animais_spell.set_footer(text="Em Níveis Superiores. Se você conjurar essa magia usando certos espaços de magia superiores, você escolhe uma das opções de invocação acima e mais criaturas aparecem: o dobro delas com um espaço de 5° nível, o triplo delas com um espaço de 7° nível e o quadruplo delas com um espaço de 9° nível.")

        return conjurar_animais_spell
        # Função para criar o Embed da magia "Conjurar Celestial (Conjure Celestial)"
    def conjurar_celestial():
        # Cria um objeto Embed
        conjurar_celestial_spell = discord.Embed(
            title="Conjurar Celestial (Conjure Celestial)",
            description="Você invoca um celestial de nível de desafio 4 ou inferior, que aparece num espaço desocupado, que você possa ver dentro do alcance. O celestial desaparece se cair a 0 pontos de vida ou quando a magia acabar.\n\nO celestial é amigável a você e a seus companheiros pela duração. Role a iniciativa para o celestial, que age no seu próprio turno. Ele obedece a quaisquer comandos verbais que você emitir (não requer uma ação sua), contanto que não violem sua tendência. Se você não emitir nenhum comando a ele, ele se defenderá de criaturas hostis, mas no mais, não realizará nenhuma ação.\n\nO Mestre possui as estatísticas do celestial.",
            color=0xFFD700  # Cor gold
        )
        # Adiciona os detalhes da magia como campos no embed
        conjurar_celestial_spell.add_field(name="Tempo de Conjuração", value="1 minutos", inline=False)
        conjurar_celestial_spell.add_field(name="Alcance", value="90 pés", inline=False)
        conjurar_celestial_spell.add_field(name="Componentes", value="V S", inline=False)
        conjurar_celestial_spell.add_field(name="Duração", value="concentração, até 1 horas", inline=False)
        conjurar_celestial_spell.set_footer(text="Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 9° nível, você invoca um celestial de nível de desafio 5 ou inferior.")

        return conjurar_celestial_spell
    # Função para criar o Embed da magia "Caminhar Em Árvores (Tree Stride)"
    def caminhar_em_arvores():
        # Cria um objeto Embed
        caminhar_em_arvores_spell = discord.Embed(
            title="Caminhar Em Árvores (Tree Stride)",
            description="Você adquire a habilidade de entrar em uma árvore e se mover de dentro dela para dentro de outra árvore do mesmo tipo a até 150 metros [500 pés]. Ambas as árvores precisam estar vivas e ter pelo menos o mesmo tamanho que você. Você precisa usar 1,5 metros [5 pés] de movimento para entrar em uma árvore. Você instantaneamente sabe a localização de todas as outras árvores do mesmo tipo dentro de 150 metros [500 pés] e, como parte do movimento usado para entrar na árvore, pode ou passar para uma destas árvores ou pisar para fora da árvore em que você está. Você aparece em um ponto a sua escolha dentro de 1,5 metros [5 pés] da árvore de destino, usando outros 1,5 metros [5 pés] de movimento. Se você não tiver nenhum movimento sobrando, você aparece dentro de 1,5 metros [5 pés] da árvore em que você entrou.\n\nVocê pode usar esse habilidade de transporte uma vez por rodada pela duração. Você deve terminar cada turno fora da árvore.",
            color=0x228B22  # Cor green
        )
        # Adiciona os detalhes da magia como campos no embed
        caminhar_em_arvores_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        caminhar_em_arvores_spell.add_field(name="Alcance", value="pessoal", inline=False)
        caminhar_em_arvores_spell.add_field(name="Componentes", value="V S", inline=False)
        caminhar_em_arvores_spell.add_field(name="Duração", value="concentração, até 1 minutos", inline=False)

        return caminhar_em_arvores_spell
    # Função para criar o Embed da magia "Conjurar Elemental (Conjure Elemental)"
    def conjurar_elemental():
        # Cria um objeto Embed
        conjurar_elemental_spell = discord.Embed(
            title="Conjurar Elemental (Conjure Elemental)",
            description="Você invoca um servo elemental. Escolha uma área de ar, água, fogo ou terra que preencha 3 metros cúbicos [10-foot cube] dentro do alcance. Um elemental de nível de desafio 5 ou inferior, adequado a área que você escolheu, aparece em um espaço desocupado a até 3 metros [10 feet] dela. Por exemplo, um elemental do fogo emerge de uma fogueira e um elemental da terra erguer-se-ia do solo. O elemental desaparece quando cair a 0 pontos de vida ou quando a magia acabar.\n\nO elemental é amigável a você e a seus companheiros pela duração. Role a iniciativa para o elemental, que age no seu próprio turno. Ele obedece a quaisquer comandos verbais que você emitir (não requer uma ação sua). Se você não emitir nenhum comando a ele, ele se defenderá de criaturas hostis, mas no mais, não realizará nenhuma ação.\n\nSe sua concentração for interrompida, o elemental não desaparece. Ao invés disso, você perde o controle sobre o elemental e ele se torna hostil a você e aos seus companheiros, e os pode atacar. Um elemental fora de controle não pode ser dispensado e desaparece 1 hora depois de você ter o invocado.\n\nO mestre tem as estatísticas do elemental.",
            color=0xFFD700  # Cor gold
        )
        # Adiciona os detalhes da magia como campos no embed
        conjurar_elemental_spell.add_field(name="Tempo de Conjuração", value="1 minutos", inline=False)
        conjurar_elemental_spell.add_field(name="Alcance", value="90 pés", inline=False)
        conjurar_elemental_spell.add_field(name="Componentes", value="V S M (um incenso aceso para ar, argila macia para terra, enxofre e fósforo para fogo, ou água e areia para água)", inline=False)
        conjurar_elemental_spell.add_field(name="Duração", value="concentração, até 1 horas", inline=False)
        conjurar_elemental_spell.set_footer(text="Em Leveis Superiores. Quando você conjura esta magia usando um espaço de magia de 6° nível ou superior, o nível de desafio aumenta em 1 para cada nível do slot acima do 5°.")


        return conjurar_elemental_spell
    # Função para criar o Embed da magia "Névoa Mortal (Cloudkill)"
    def nevoa_mortal():
        # Cria um objeto Embed
        nevoa_mortal_spell = discord.Embed(
            title="Névoa Mortal (Cloudkill)",
            description="Você cria uma esfera de nevoeiro venenoso de cor amarelo-esverdeado, com 6 metros de raio [20-foot radius], centrado em um ponto, à sua escolha, dentro do alcance. O nevoeiro se espalha, dobrando esquinas. Ele permanece pela duração ou até um vento forte dispersar o nevoeiro, terminando a magia. Sua área é de escuridão densa.\n\nQuando uma criatura entra na área da magia pela primeira vez no turno dela ou começa seu turno lá, essa criatura deve realizar um teste de resistência de Constituição. A criatura sofre 5d8 de dano de veneno, ou metade desse dano, se passar no teste. As criaturas serão afetadas mesmo se prenderem a respiração ou não precisarem respirar.\n\nO nevoeiro se afasta 3 metros [10 feet] de você no começo de cada um dos seus turnos, deslizando pela superfície do solo. Os vapores são mais pesados que o ar, mantendo-se nos níveis mais baixos do terreno, até mesmo caindo em aberturas.",
            color=0x00FF00  # Cor green
        )
        # Adiciona os detalhes da magia como campos no embed
        nevoa_mortal_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        nevoa_mortal_spell.add_field(name="Alcance", value="120 pés", inline=False)
        nevoa_mortal_spell.add_field(name="Componentes", value="V S", inline=False)
        nevoa_mortal_spell.add_field(name="Duração", value="concentração, até 10 minutos", inline=False)
        # Adiciona o efeito em níveis superiores no footer
        nevoa_mortal_spell.set_footer(text="Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 6° nível ou superior, o dano aumenta em 1d8 para cada nível do espaço acima do 5°.")

        return nevoa_mortal_spell
    # Função para criar o Embed da magia "Praga de Insetos (Insect Plague)"
    def conjuracao_praga_de_insetos():
        # Cria um objeto Embed
        praga_de_insetos_spell = discord.Embed(
            title="Praga de Insetos (Insect Plague)",
            description="Um enxame voraz de gafanhotos preenche uma esfera de 6 metros de raio, centrada no ponto que você escolher, dentro do alcance. A esfera se espalha dobrando esquinas. A esfera permanece pela duração e sua área é de escuridão leve. A área da esfera é de terreno difícil.\n\nQuando a área aparece, cada criatura dentro dela deve realizar um teste de resistência de Constituição. Uma criatura sofre 4d10 de dano perfurante se falhar na resistência ou metade desse dano se passar. Uma criatura deve, também, realizar um teste de resistência quando entrar na área da magia pela primeira vez num turno ou terminar seu turno nela.",
            color=0x00FF00  # Cor verde
        )
        # Adiciona os detalhes da magia como campos no embed
        praga_de_insetos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        praga_de_insetos_spell.add_field(name="Alcance", value="300 pés", inline=False)
        praga_de_insetos_spell.add_field(name="Componentes", value="V S M (alguns grãos de açúcar, alguns miolos de grão e uma mancha de gordura)", inline=False)
        praga_de_insetos_spell.add_field(name="Duração", value="concentração, até 10 minutos", inline=False)
        praga_de_insetos_spell.set_footer(text="Em Níveis Superiores. Quando conjurada usando um espaço de magia de 6° nível ou superior, o dano aumenta em 1d10 para cada nível do espaço acima do 5°.")

        return praga_de_insetos_spell
    # Função para criar o Embed da magia "Banquete de Heróis (Heroes' Feast)"
    def conjuracao_banquete_herois():
        # Cria um objeto Embed
        banquete_herois_spell = discord.Embed(
            title="Banquete de Heróis (Heroes' Feast)",
            description="Você traz um grande banquete, incluindo comida e bebida magnificas. O banquete leva 1 hora para ser consumido e desaparece ao final desse tempo e os efeitos benéficos não se aplicam até essa hora terminar. Até doze criaturas podem participar do banquete.\n\nUma criatura que participe do banquete ganha diversos benefícios. A criatura é curada de todas as doenças e venenos, torna-se imune a veneno e a ser amedrontada e faz todos os seus testes de resistência de Sabedoria com vantagem. Seu máximo de pontos de vida também aumenta em 2d10 e ela ganha a mesma quantidade de pontos de vida. Esses benefícios duram por 24 horas.",
            color=0xFFD700  # Cor gold
        )
        # Adiciona os detalhes da magia como campos no embed
        banquete_herois_spell.add_field(name="Tempo de Conjuração", value="10 minutos", inline=False)
        banquete_herois_spell.add_field(name="Alcance", value="30 pés", inline=False)
        banquete_herois_spell.add_field(name="Componentes", value="V S M (uma tigela encrustada de gemas valendo, no mínimo, 1000 gp que a magia consome)", inline=False)
        banquete_herois_spell.add_field(name="Duração", value="1 minuto", inline=False)
        banquete_herois_spell.set_footer(text="Até doze criaturas podem participar do banquete.")

        return banquete_herois_spell# Função para criar o Embed da magia "Banquete de Heróis (Heroes' Feast)"
    # Função para criar o Embed da magia "Conjurar Fada (Conjure Fey)"
    def conjuracao_conjurar_fada():
        # Cria um objeto Embed
        conjurar_fada_spell = discord.Embed(
            title="Conjurar Fada (Conjure Fey)",
            description="Você invoca uma criatura feérica de nível de desafio 6 ou inferior ou um espírito feérico que assume a forma de uma besta de nível de desafio 6 ou inferior. Ela aparece num espaço desocupado que você possa ver dentro do alcance. A criatura feérica desaparece se cair a 0 pontos de vida ou quando a magia acabar.\n\nA criatura feérica é amigável a você e a seus companheiros pela duração. Role a iniciativa para a criatura, que age no seu próprio turno. Ela obedece a quaisquer comandos verbais que você emitir (não requer uma ação sua), contanto que não violem sua tendência. Se você não emitir nenhum comando a ela, ela se defenderá de criaturas hostis, mas no mais, não realizará nenhuma ação.\n\nSe sua concentração for interrompida, a criatura feérica não desaparece. Ao invés disso, você perde o controle sobre a criatura feérica e ela se torna hostil a você e aos seus companheiros, e poderá atacar. Uma criatura feérica fora de controle não pode ser dispensada por você, ela desaparece 1 hora depois de você ter a invocada.\n\nO Mestre possui as estatísticas da criatura feérica.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        conjurar_fada_spell.add_field(name="Conjuradores", value="Bruxo/Druida", inline=False)
        conjurar_fada_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        conjurar_fada_spell.add_field(name="Alcance", value="90 pés", inline=False)
        conjurar_fada_spell.add_field(name="Componentes", value="V S", inline=False)
        conjurar_fada_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)
        conjurar_fada_spell.set_footer(text="Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 7° nível ou superior, o nível de desafio aumenta em 1 para cada nível do espaço acima do 6°.")

        return conjurar_fada_spell
    # Função para criar o Embed da magia "Invocação Instantânea (Instant Summons)"

    def conjuracao_invocacao_instantanea():
        # Cria um objeto Embed
        invocacao_instantanea_spell = discord.Embed(
            title="Invocação Instantânea (Instant Summons)",
            description="Você toca um objeto pesando 5 quilos [10 pounds] ou menos com maior dimensão de 1,8 metro [6 feet] ou menos. A magia deixa uma marca invisível na sua superfície e grava invisivelmente o nome do item na safira que você usou como componente material. A cada vez que você conjurar essa magia, você deve usar uma safira diferente.\n\nA qualquer momento, posteriormente, você pode usar sua ação para falar o nome do item e esmagar a safira. O item aparece instantaneamente em suas mãos, independentemente de distâncias físicas ou planares, e a magia termina.\n\nSe outra criatura estiver segurando ou carregando o item, esmagar a safira não irá transportar o item até você, ao invés disso, você descobre quem é a criatura possuindo o objeto e onde, vagamente, a criatura está localizada no momento.\n\n*Dissipar magia ou um efeito similar aplicado com sucesso na safira, termina o efeito da magia.*",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        invocacao_instantanea_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        invocacao_instantanea_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        invocacao_instantanea_spell.add_field(name="Alcance", value="Toque", inline=False)
        invocacao_instantanea_spell.add_field(name="Componentes", value="V S M (uma safira valendo, no mínimo, 1000 gp)", inline=False)
        invocacao_instantanea_spell.add_field(name="Duração", value="Até ser dissipada", inline=False)

        return invocacao_instantanea_spell
    
    # Função para criar o Embed da magia "Muralha De Espinhos (Wall Of Thorns)"
    def conjuracao_muralha_de_espinhos():
        # Cria um objeto Embed
        muralha_de_espinhos_spell = discord.Embed(
            title="Muralha De Espinhos (Wall Of Thorns)",
            description="Você cria uma muralha de arbustos robustos, flexíveis, emaranhados e eriçados com espinhos pontudos. A muralha aparece, dentro do alcance, em uma superfície sólida e permanece pela duração. Você escolher fazer a muralha com até 18 metros [60 feet] de comprimento, 3 metros [10 feet] de altura e 1,5 metro [5 feet] de espessura ou um círculo com 6 metros [20 feet] de diâmetro e até 6 metros de altura [20-foot-tall] com 1,5 metro [5 feet] de espessura. A muralha bloqueia a visão.\n\nQuando a muralha aparece, cada criatura dentro da área deve realizar um teste de resistência de Destreza. Se falhar na resistência, uma criatura sofrerá 7d8 de dano perfurante ou metade desse dano se obtiver sucesso.\n\nUma criatura pode se mover através da muralha, embora lentamente e dolorosamente. Para cada 1,5 metro [5 feet] que a criatura atravesse da muralha, ela deve gastar 6 metros [20 feet] de movimento. Além disso, a primeira vez que a criatura entrar na muralha num turno ou termina o turno nela, ela deve fazer um teste de resistência de Destreza. Ela sofre 7d8 de dano cortante se falhar na resistência ou metade desse dano se obtiver sucesso.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        muralha_de_espinhos_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        muralha_de_espinhos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        muralha_de_espinhos_spell.add_field(name="Alcance", value="120 pés", inline=False)
        muralha_de_espinhos_spell.add_field(name="Componentes", value="V S M (um punhado de espinhos)", inline=False)
        muralha_de_espinhos_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)
        muralha_de_espinhos_spell.set_footer(text="Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 7° nível ou superior, ambos os tipos de dano aumentam em 1d8 para cada nível do espaço acima do 6°.")

        return muralha_de_espinhos_spell
    # Função para criar o Embed da magia "Palavra de Recordação (Word of Recall)"
    def conjuracao_palavra_de_recordacao():
        # Cria um objeto Embed
        palavra_de_recordacao_spell = discord.Embed(
            title="Palavra De Recordação (Word Of Recall)",
            description="Você e até cinco criaturas voluntárias a 1,5 metro [5 feet] de você, instantaneamente são teletransportadas para um santuário previamente designado. Você e qualquer criatura que se teletransportar com você, aparece no espaço desocupado mais próximo do ponto que você designou quando preparou seu santuário (veja abaixo). Se você conjurar essa magia sem ter preparado um santuário primeiro, a magia não funciona.\n\nVocê deve designar um santuário na conjuração dessa magia dentro de um local, como um templo dedicado ou fortemente ligado a sua divindade. Se você tentar conjurar essa magia dessa forma em uma área que não seja dedicada à sua divindade, a magia não funciona.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        palavra_de_recordacao_spell.add_field(name="Conjuradores", value="Clérigo", inline=False)
        palavra_de_recordacao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        palavra_de_recordacao_spell.add_field(name="Alcance", value="5 pés", inline=False)
        palavra_de_recordacao_spell.add_field(name="Componentes", value="V", inline=False)
        palavra_de_recordacao_spell.add_field(name="Duração", value="Instantâneo", inline=False)

        return palavra_de_recordacao_spell
    # Função para criar o Embed da magia "Teletransporte Por Árvores (Transport Via Plants)"
    def conjuracao_teletransporte_por_arvores():
        # Cria um objeto Embed
        teletransporte_por_arvores_spell = discord.Embed(
            title="Teletransporte Por Árvores (Transport Via Plants)",
            description="Essa magia cria uma ligação mágica entre uma planta inanimada Grande ou maior, dentro do alcance, e outra planta a qualquer distância, no mesmo plano de existência. Você deve ter visto ou tocado a planta de destino, pelo menos uma vez antes. Pela duração, qualquer criatura pode entrar na planta alvo e sair da planta destino usando 1,5 metro [5 feet] de movimento.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        teletransporte_por_arvores_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        teletransporte_por_arvores_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        teletransporte_por_arvores_spell.add_field(name="Alcance", value="10 pés", inline=False)
        teletransporte_por_arvores_spell.add_field(name="Componentes", value="V S", inline=False)
        teletransporte_por_arvores_spell.add_field(name="Duração", value="1 rodada", inline=False)

        return teletransporte_por_arvores_spell
    # Função para criar o Embed da magia "Conjurar Celestial (Conjure Celestial)"
    def conjuracao_conjurar_celestial():
        # Cria um objeto Embed
        conjurar_celestial_spell = discord.Embed(
            title="Conjurar Celestial (Conjure Celestial)",
            description="Você invoca um celestial de nível de desafio 4 ou inferior, que aparece num espaço desocupado, que você possa ver dentro do alcance. O celestial desaparece se cair a 0 pontos de vida ou quando a magia acabar.\n\nO celestial é amigável a você e a seus companheiros pela duração. Role a iniciativa para o celestial, que age no seu próprio turno. Ele obedece a quaisquer comandos verbais que você emitir (não requer uma ação sua), contanto que não violem sua tendência. Se você não emitir nenhum comando a ele, ele se defenderá de criaturas hostis, mas no mais, não realizará nenhuma ação.\n\nO Mestre possui as estatísticas do celestial.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        conjurar_celestial_spell.add_field(name="Conjuradores", value="Clérigo", inline=False)
        conjurar_celestial_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        conjurar_celestial_spell.add_field(name="Alcance", value="90 pés", inline=False)
        conjurar_celestial_spell.add_field(name="Componentes", value="V S", inline=False)
        conjurar_celestial_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)
        conjurar_celestial_spell.set_footer(text="Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 9° nível, você invoca um celestial de nível de desafio 5 ou inferior.")

        return conjurar_celestial_spell
    # Função para criar o Embed da magia "Mansão Magnífica (Magnificent Mansion)"
    def conjuracao_magnificent_mansion():
        # Cria um objeto Embed
        magnificent_mansion_spell = discord.Embed(
            title="Mansão Magnífica (Magnificent Mansion)",
            description="Você conjura uma residência extradimensional, dentro do alcance, que permanece pela duração. Você escolhe onde sua única entrada é localizada. A entrada brilha discretamente e tem 1,5 metro [5 feet] de largura por 3 metros [10 feet] de altura. Você e qualquer criatura que você designou, quando conjurou a magia, pode entrar na residência extradimensional enquanto o portal permanecer aberto. Você pode abrir ou fechar o portal se estiver a até 9 metros [30 feet] dele. Enquanto estiver fechado, o portal é invisível.\n\nAlém do portal existe um magnifico salão com inúmeros aposentos. A atmosfera é limpa, fresca e morna.\n\nVocê pode criar qualquer projeto de piso que quiser, mas o espaço não pode exceder 50 cubos, cada cubo tendo 3 metros [10 feet] de cada lado. O local é mobiliado e decorado como você desejar. Ele contém comida suficiente para servir nove banquetes para até 100 pessoas. Uma equipe de 100 servos quase-transparentes atende todos que entrarem. Você decide a aparência visual dos servos e o vestuário deles. Eles são completamente obedientes as suas ordens. Cada servo pode realizar qualquer tarefa que um servo humano comum poderia fazer, mas eles não podem atacar ou realizar qualquer ação que poderia causar malefício direto a outra criatura. Portanto, os servos podem buscar coisas, limpar, remendar, dobrar roupas, acender lareiras, servir comida, despejar vinho e assim por diante. Os servos podem ir a qualquer lugar na mansão, mas não podem deixá-la. Mobília e outros objetos criados por essa magia viram fumaça se forem removidos da mansão. Quando a magia acabar, qualquer criatura dentro do espaço extradimensional é expelida para o espaço vago mais próximo da entrada.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        magnificent_mansion_spell.add_field(name="Conjuradores", value="Bardo/Mago", inline=False)
        magnificent_mansion_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        magnificent_mansion_spell.add_field(name="Alcance", value="300 pés", inline=False)
        magnificent_mansion_spell.add_field(name="Componentes", value="V S M (um portal em miniatura esculpido em marfim, um pedaço de mármore polido e uma pequena colher de prata valendo, no mínimo, 15 gp)", inline=False)
        magnificent_mansion_spell.add_field(name="Duração", value="24 horas", inline=False)

        return magnificent_mansion_spell
    # Função para criar o Embed da magia "Viagem Planar (Plane Shift)"
    def conjuracao_plane_shift():
        # Cria um objeto Embed
        plane_shift_spell = discord.Embed(
            title="Viagem Planar (Plane Shift)",
            description="Você e até oito criaturas voluntárias, que estejam de mãos dadas em um círculo, são transportadas para um plano de existência diferente. Você pode especificar o destino alvo em termos gerais, como a Cidade de Bronze do Plano Elemental do Fogo ou o palácio de Dispater na segunda camada dos Nove Infernos e você aparece no ou perto do destino. Se você estiver tentando chegar a Cidade de Bronze, por exemplo, você poderia chegar na Estrada de Aço dela, em frente aos Portões de Cinzas ou contemplando a cidade do outro lado do Mar de Fogo, à critério do Mestre.\n\nAlternativamente, se você conhecer a sequência de selos do círculo de teletransporte em outro plano de existência, essa magia pode leva-lo para esse círculo. Se o círculo de teletransporte for muito pequeno para comportar as criaturas que você está transportando, elas aparecerão no espaço desocupado mais próximo do círculo.\n\nVocê pode usar essa magia para banir uma criatura involuntária para outro plano. Escolha uma criatura ao seu alcance e realize um ataque corpo-a-corpo com magia contra ela. Se atingir, a criatura deve realizar um teste de resistência de Carisma. Se a criatura falhar na resistência, ela é transportada para um local aleatório no plano de existência que você especificou. Uma criatura, uma vez transportada, deve encontrar seu próprio meio de retornar para seu plano de existência atual.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        plane_shift_spell.add_field(name="Conjuradores", value="Bruxo/Clérigo/Druida/Feiticeiro/Mago", inline=False)
        plane_shift_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        plane_shift_spell.add_field(name="Alcance", value="Toque", inline=False)
        plane_shift_spell.add_field(name="Componentes", value="V S M (uma haste metálica bifurcada valendo, sintonizada com um plano de existência em particular, valendo, no mínimo, 250 gp)", inline=False)
        plane_shift_spell.add_field(name="Duração", value="Instantâneo", inline=False)

        return plane_shift_spell
    # Função para criar o Embed da magia "Labirinto (Maze)"
    def conjuracao_labirinto():
        # Cria um objeto Embed
        maze_spell = discord.Embed(
            title="Labirinto (Maze)",
            description="Você bane uma criatura que você possa ver, dentro do alcance, para um semiplano labiríntico. O alvo permanece lá pela duração ou até escapar do labirinto.\n\nO alvo pode usar sua ação para tentar escapar. Quando o fizer, ele realiza um teste de Inteligência com CD 20. Se for bem sucedido, ele escapa e a magia termina (um minotauro ou um demônio goristro, obtém sucesso automaticamente).\n\nQuando a magia termina, o alvo reaparece no espaço que ela estava ou, se o espaço estiver ocupado, no espaço desocupado mais próximo.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        maze_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        maze_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        maze_spell.add_field(name="Alcance", value="60 pés", inline=False)
        maze_spell.add_field(name="Componentes", value="V S", inline=False)
        maze_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return maze_spell
        # Função para criar o Embed da magia "Nuvem Incendiária (Incendiary Cloud)"
    def conjuracao_nuvem_incendiaria():
        # Cria um objeto Embed
        incendiary_cloud_spell = discord.Embed(
            title="Nuvem Incendiária (Incendiary Cloud)",
            description="Uma nuvem de fumaça rodopiante que dispara brasas incandescentes aparece numa esfera de 6 metros [20 feet] centrada num ponto, dentro do alcance. A nuvem se espalha, dobrando esquinas, e gera escuridão densa. Ela permanece pela duração ou até que um vento de velocidade moderada ou mais forte (pelo menos 15 quilômetros [10 miles] por hora) a disperse.\n\nQuando a nuvem aparece, cada criatura deve realizar um teste de resistência de Destreza. Uma criatura sofre 10d8 de dano de fogo se falhar na resistência ou metade desse dano se passar. Uma criatura deve, também, realizar um teste de resistência quando entrar na área da magia pela primeira vez num turno ou terminar seu turno nela.\n\nA nuvem se afasta 3 metros [10 feet] de você numa direção, que você escolheu, no começo de cada um dos seus turnos.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        incendiary_cloud_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        incendiary_cloud_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        incendiary_cloud_spell.add_field(name="Alcance", value="150 pés", inline=False)
        incendiary_cloud_spell.add_field(name="Componentes", value="V S", inline=False)
        incendiary_cloud_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return incendiary_cloud_spell
    # Função para criar o Embed da magia "Semiplano (Demiplane)"
    def conjuracao_semiplano():
        # Cria um objeto Embed
        demiplane_spell = discord.Embed(
            title="Semiplano (Demiplane)",
            description="Você cria uma porta umbral em uma superfície sólida e lisa que você possa ver, dentro do alcance. A porta é grande o suficiente para permitir a passagem de criaturas Médias sem dificuldade. Quando aberta, a porta levará a um semiplano que parece uma sala vazia de 9 metros quadrados [30 feet square] de dimensão, feita de madeira ou pedra. Quando a magia termina, a porta desaparece e qualquer criatura ou objeto dentro do semiplano permanecerá preso lá, à medida que a porta desaparece do outro lado.\n\nCada vez que você conjura essa magia, você pode criar um novo semiplano ou fazer a porta umbral se conectar a um semiplano que você tenha criado em uma conjuração anterior dessa magia. Além disso, se você conhecer a natureza e conteúdo do semiplano criado através da conjuração dessa magia por outra criatura, você pode fazer com que a porta umbral se conecte a esse semiplano.",
            color=0x4B0082  # Cor indigo
        )
        # Adiciona os detalhes da magia como campos no embed
        demiplane_spell.add_field(name="Conjuradores", value="Bruxo/Mago", inline=False)
        demiplane_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        demiplane_spell.add_field(name="Alcance", value="60 pés", inline=False)
        demiplane_spell.add_field(name="Componentes", value="S", inline=False)
        demiplane_spell.add_field(name="Duração", value="1 hora", inline=False)

        return demiplane_spell
    def conjuracao_arma_espiritual():
        spiritual_weapon_spell = discord.Embed(
            title="Arma Espiritual (Spiritual Weapon)",
            description="Você cria uma arma espectral flutuante na forma de sua escolha que dura pela duração ou até você conjurar essa magia novamente. Quando você conjura a magia, você pode fazer um ataque corpo-a-corpo com a arma contra uma criatura dentro de 1,5 metro dela. Em um acerto, o alvo sofre dano radiante igual a 1d8 + seu modificador de conjuração. Como uma ação bônus em cada um dos seus turnos subsequentes, você pode mover a arma até 6 metros e repetir o ataque contra uma criatura dentro de 1,5 metro dela.",
            color=0xFFD700  # Cor dourada
        )
        spiritual_weapon_spell.add_field(name="Conjuradores", value="Clérigo", inline=False)
        spiritual_weapon_spell.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        spiritual_weapon_spell.add_field(name="Alcance", value="18 metros", inline=False)
        spiritual_weapon_spell.add_field(name="Componentes", value="V, S", inline=False)
        spiritual_weapon_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return spiritual_weapon_spell
    def conjuracao_invocar_aberracao():
        summon_aberration_spell = discord.Embed(
            title="Invocar Aberração (Summon Aberration)",
            description="Você convoca uma aberração do plano de sua escolha para ajudar você em combate. A criatura invocada obedece aos seus comandos e age no turno imediatamente após o seu. A criatura desaparece quando seus pontos de vida chegam a zero ou quando a magia termina.",
            color=0x800080  # Cor roxa
        )
        summon_aberration_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        summon_aberration_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        summon_aberration_spell.add_field(name="Alcance", value="27 metros", inline=False)
        summon_aberration_spell.add_field(name="Componentes", value="V, S, M (um item relacionado à aberração)", inline=False)
        summon_aberration_spell.add_field(name="Duração", value="1 hora", inline=False)

        return summon_aberration_spell
    def conjuracao_invocar_constructo():
        summon_construct_spell = discord.Embed(
            title="Invocar Constructo (Summon Construct)",
            description="Você conjura um constructo que luta por você. O constructo aparece em um espaço desocupado dentro do alcance. Ele age no turno imediatamente após o seu e segue suas ordens.",
            color=0x696969  # Cor cinza
        )
        summon_construct_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        summon_construct_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        summon_construct_spell.add_field(name="Alcance", value="27 metros", inline=False)
        summon_construct_spell.add_field(name="Componentes", value="V, S, M (uma gema no valor de 100 PO)", inline=False)
        summon_construct_spell.add_field(name="Duração", value="1 hora", inline=False)

        return summon_construct_spell
    def conjuracao_invocar_demonio():
        summon_demon_spell = discord.Embed(
            title="Invocar Demônio (Summon Demon)",
            description="Você invoca um demônio das profundezas do inferno para lutar por você. O demônio obedece aos seus comandos, mas há sempre o risco de ele se voltar contra você se você perder o controle.",
            color=0x8B0000  # Cor vermelha escura
        )
        summon_demon_spell.add_field(name="Conjuradores", value="Feiticeiro/Bruxo", inline=False)
        summon_demon_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        summon_demon_spell.add_field(name="Alcance", value="18 metros", inline=False)
        summon_demon_spell.add_field(name="Componentes", value="V, S, M (um item relacionado ao demônio)", inline=False)
        summon_demon_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return summon_demon_spell
    def conjuracao_invocar_familiar():
        summon_familiar_spell = discord.Embed(
            title="Invocar Familiar (Find Familiar)",
            description="Você ganha os serviços de um familiar, um espírito que assume uma forma animal à sua escolha. O familiar obedece aos seus comandos e pode servir como seus olhos e ouvidos, podendo até se comunicar telepaticamente com você.",
            color=0x008080  # Cor teal
        )
        summon_familiar_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        summon_familiar_spell.add_field(name="Tempo de Conjuração", value="1 hora", inline=False)
        summon_familiar_spell.add_field(name="Alcance", value="3 metros", inline=False)
        summon_familiar_spell.add_field(name="Componentes", value="V, S, M (carvão, incenso e ervas no valor de 10 PO)", inline=False)
        summon_familiar_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return summon_familiar_spell
    def conjuracao_invocar_guardiao_da_natureza():
        nature_guardian_spell = discord.Embed(
            title="Invocar Guardião da Natureza (Summon Nature's Guardian)",
            description="Você invoca um poderoso espírito da natureza que assume a forma de um guardião bestial ou vegetal para proteger você e seus aliados. O guardião luta ao seu lado e obedece aos seus comandos.",
            color=0x228B22  # Cor verde floresta
        )
        nature_guardian_spell.add_field(name="Conjuradores", value="Druida/Ranger", inline=False)
        nature_guardian_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        nature_guardian_spell.add_field(name="Alcance", value="27 metros", inline=False)
        nature_guardian_spell.add_field(name="Componentes", value="V, S, M (um item relacionado à natureza)", inline=False)
        nature_guardian_spell.add_field(name="Duração", value="1 hora", inline=False)

        return nature_guardian_spell
    def conjuracao_invocar_servo_da_natureza():
        nature_servant_spell = discord.Embed(
            title="Invocar Servo da Natureza (Summon Nature's Servant)",
            description="Você invoca um servo da natureza, uma criatura que age de acordo com os princípios naturais e obedece aos seus comandos. O servo pode ser uma fera, uma planta animada ou outro ser relacionado à natureza.",
            color=0x6B8E23  # Cor verde oliva
        )
        nature_servant_spell.add_field(name="Conjuradores", value="Druida/Ranger", inline=False)
        nature_servant_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        nature_servant_spell.add_field(name="Alcance", value="27 metros", inline=False)
        nature_servant_spell.add_field(name="Componentes", value="V, S, M (um item relacionado à natureza)", inline=False)
        nature_servant_spell.add_field(name="Duração", value="1 hora", inline=False)

        return nature_servant_spell
    def muralha_de_pedra():
        muralha_de_pedra_spell = discord.Embed(
            title="Muralha de Pedra (Wall of Stone)",
            description=(
                "Uma muralha de pedra sólida emerge em um ponto que você possa ver dentro do alcance. A muralha pode ter até 9 metros de comprimento, 3 metros de altura e 15 centímetros de espessura. Você pode modelar a muralha da maneira que desejar, incluindo criar rampas, plataformas ou outras formas simples.\n\n"
                "Se a muralha corta o espaço ocupado por uma criatura, a criatura pode realizar um teste de Destreza para se mover para o lado mais próximo da muralha. Se não for feito o teste, a criatura será empurrada para o lado. A muralha de pedra é permanente a menos que seja destruída ou desfeita magicamente."
            ),
            color=0x696969  # Cor cinza pedra
        )
        muralha_de_pedra_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        muralha_de_pedra_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        muralha_de_pedra_spell.add_field(name="Alcance", value="36 metros", inline=False)
        muralha_de_pedra_spell.add_field(name="Componentes", value="V, S, M (um pequeno bloco de granito)", inline=False)
        muralha_de_pedra_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return muralha_de_pedra_spell



