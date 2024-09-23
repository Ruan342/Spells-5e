import discord

class ilusão:
    def __init__(self):
        pass
    def ilusao_menor():
        minor_illusion_spell = discord.Embed(
            title="Ilusão Menor (Minor Illusion)",
            description=("Você cria um som ou uma imagem de um objeto dentro do alcance, que dura pela duração. "
                        "A ilusão também termina se você a dissipar como uma ação ou conjurar essa magia novamente.\n\n"
                        "Se você criar um som, seu volume pode variar de um sussurro a um grito. Pode ser qualquer som que você escolher, "
                        "como a voz de alguém, o rugido de um leão, batidas de tambores ou qualquer outro ruído. O som continua durante "
                        "a duração ou você pode fazer sons distintos em momentos diferentes antes do término da magia.\n\n"
                        "Se você criar uma imagem de um objeto – como uma cadeira, pegadas de lama ou uma pequena caixa – ela não pode ser maior "
                        "que um cubo de 1,5 metros de lado. A imagem não pode criar som, luz, cheiro ou qualquer outro efeito sensorial. A interação "
                        "física com a imagem revela que ela é uma ilusão, pois as coisas podem passar através dela.\n\n"
                        "**Teste de Inteligência (Investigação):** Uma criatura pode usar sua ação para inspecionar a imagem ou som, fazendo um teste de "
                        "Inteligência (Investigação) contra a CD da sua magia. Se passar, perceberá que se trata de uma ilusão."),
            color=0x808080  # Cor cinza
        )
        minor_illusion_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        minor_illusion_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        minor_illusion_spell.add_field(name="Alcance", value="9 metros", inline=False)
        minor_illusion_spell.add_field(name="Componentes", value="S, M (um pedaço de lã)", inline=False)
        minor_illusion_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return minor_illusion_spell

    def disfarcar_se():
        disguise_self_spell = discord.Embed(
            title="Disfarçar-se (Disguise Self)",
            description=("Você faz parecer que sua forma e aparência mudaram, incluindo suas roupas, armadura, armas e outros pertences. "
                        "Você pode parecer 30 centímetros mais alto ou mais baixo e magro, gordo ou em algum lugar entre os dois. "
                        "Você não pode mudar seu tipo de corpo, então deve adotar uma forma que tenha a mesma disposição básica de membros. "
                        "Caso contrário, as mudanças falham.\n\n"
                        "**Teste de Sabedoria (Percepção):** Qualquer criatura que use sua ação para inspecionar a ilusão pode fazer um teste "
                        "de Sabedoria (Percepção) contra a CD da sua magia para perceber a ilusão. Uma criatura que toque você perceberá a ilusão "
                        "imediatamente."),
            color=0x483D8B  # Cor azul escuro
        )
        disguise_self_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        disguise_self_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        disguise_self_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        disguise_self_spell.add_field(name="Componentes", value="V, S", inline=False)
        disguise_self_spell.add_field(name="Duração", value="1 hora", inline=False)

        return disguise_self_spell

    def imagem_silenciosa():
        silent_image_spell = discord.Embed(
            title="Imagem Silenciosa (Silent Image)",
            description=("Você cria a imagem de um objeto, criatura ou outra forma visual que se situa dentro do alcance e ocupa "
                        "um espaço de até um cubo de 4,5 metros de lado. A imagem não pode criar som, luz, cheiro ou outra sensação sensorial. "
                        "A imagem é puramente visual e desaparece se for atravessada fisicamente.\n\n"
                        "**Ação para Mover a Ilusão:** Durante a duração, você pode usar sua ação para mover a imagem para qualquer ponto dentro "
                        "do alcance da magia. Quando a imagem se move, você pode alterar sua aparência para que seus movimentos pareçam naturais.\n\n"
                        "**Teste de Inteligência (Investigação):** Uma criatura pode usar sua ação para inspecionar a imagem, fazendo um teste de "
                        "Inteligência (Investigação) contra a CD da sua magia. Se passar, perceberá que se trata de uma ilusão."),
            color=0x8A2BE2  # Cor roxa
        )
        silent_image_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        silent_image_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        silent_image_spell.add_field(name="Alcance", value="18 metros", inline=False)
        silent_image_spell.add_field(name="Componentes", value="V, S, M (um pedaço de lã)", inline=False)
        silent_image_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return silent_image_spell

    def borrao():
        blur_spell = discord.Embed(
            title="Borrão (Blur)",
            description=("Sua forma se torna indistinta e embaçada. Por toda a duração, qualquer criatura que tente atacar você tem "
                        "desvantagem nas jogadas de ataque que dependem de visão. Uma criatura que não dependa da visão, como com "
                        "visão cega, ou que possa ver através de ilusões, como com visão verdadeira, não é afetada."),
            color=0x6495ED  # Cor azul claro
        )
        blur_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        blur_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        blur_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        blur_spell.add_field(name="Componentes", value="V", inline=False)
        blur_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return blur_spell

    def espelho_magico():
        mirror_image_spell = discord.Embed(
            title="Reflexo (Mirror Image)",
            description=("Três duplicatas ilusórias de você aparecem no seu espaço. Elas se movem com você e imitam suas ações, "
                        "confundindo os inimigos. Cada vez que uma criatura o atacar, role um d20 para determinar se o ataque acerta uma das "
                        "duplicatas ou você. Se tiver 3 duplicatas, em um resultado de 6 ou mais no d20, o ataque atinge uma duplicata. "
                        "Com 2 duplicatas, o resultado é 8 ou mais. Com 1 duplicata, o resultado é 11 ou mais.\n\n"
                        "**Destruição de Duplicatas:** As duplicatas têm CA igual a 10 + seu modificador de Destreza. Se um ataque acertar uma duplicata, "
                        "ela é destruída. Elas não têm outros atributos e não podem realizar ações."),
            color=0xB0E0E6  # Cor azul pálido
        )
        mirror_image_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        mirror_image_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mirror_image_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        mirror_image_spell.add_field(name="Componentes", value="V, S", inline=False)
        mirror_image_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return mirror_image_spell

    def imagem_persistente():
        phantasmal_force_spell = discord.Embed(
            title="Força fantasmagorica (Phantasmal Force)",
            description=("Você cria uma ilusão tão vívida que engana os sentidos da criatura alvo, que acredita que a ilusão é real e reage a ela de acordo. "
                        "O alvo deve fazer um teste de Inteligência (Investigação) contra a CD da sua magia. Se falhar, ele acredita completamente na ilusão, "
                        "mesmo que ela cause dano. A ilusão pode afetar todos os sentidos do alvo.\n\n"
                        "**Dano Psíquico:** Cada turno, o alvo pode sofrer até 1d6 de dano psíquico se a ilusão criada sugerir um efeito prejudicial, como "
                        "ser atacado por um predador ou preso em um ambiente perigoso.\n\n"
                        "**Interação com o Ambiente:** O alvo pode interagir com a ilusão e tentar se libertar dela. Um teste de Inteligência (Investigação) "
                        "bem-sucedido no início de seu turno ou quando sofre dano pode dissipar a ilusão."),
            color=0x00FA9A  # Cor verde
        )
        phantasmal_force_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        phantasmal_force_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        phantasmal_force_spell.add_field(name="Alcance", value="18 metros", inline=False)
        phantasmal_force_spell.add_field(name="Componentes", value="V, S, M (um pedaço de lã)", inline=False)
        phantasmal_force_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return phantasmal_force_spell
    def circulo_hipnotico():
        hypnotic_pattern_spell = discord.Embed(
            title="Padrãp hipnotico(Hypnotic Pattern)",
            description = (
                "Você cria um padrão de luzes cintilantes e hipnotizantes que se formam em um cubo de 9 metros de lado, centrado em um ponto à sua escolha dentro do alcance. "
                "O padrão aparece por um momento e depois desaparece, cada criatura dentro do cubo que puder ver o padrão deve realizar um teste de resistência de Sabedoria. "
                "Se falhar no teste, a criatura ficará enfeitiçada por você pela duração. Enquanto estiver enfeitiçada por esta magia, a criatura fica incapacitada e com a velocidade reduzida a 0.\n\n"
                "O feitiço termina para um alvo enfeitiçado se ele sofrer qualquer dano ou se alguém usar uma ação para sacudi-lo e tirá-lo de seu transe."
            ),

            color=0xFF69B4  # Cor rosa
        )
        hypnotic_pattern_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        hypnotic_pattern_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        hypnotic_pattern_spell.add_field(name="Alcance", value="36 metros", inline=False)
        hypnotic_pattern_spell.add_field(name="Componentes", value="V, S, M (um incenso que queima)", inline=False)
        hypnotic_pattern_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return hypnotic_pattern_spell
    def invisibilidade_maior():
        greater_invisibility_spell = discord.Embed(
            title="Invisibilidade Maior (Greater Invisibility)",
            description=("Você ou uma criatura que você toca torna-se invisível até o fim da duração da magia. Enquanto estiver invisível, a criatura "
                        "não pode ser vista, exceto por magias ou habilidades que detectem invisibilidade. A invisibilidade persiste mesmo se o alvo "
                        "atacar ou conjurar magias durante a duração da magia.\n\n"
                        "**Interação com o Ambiente:** Qualquer equipamento ou objeto carregado pela criatura também se torna invisível. A criatura ainda "
                        "pode ser detectada por meios indiretos, como som ou rastros, mas os ataques contra ela terão desvantagem."),
            color=0x708090  # Cor cinza ardósia
        )
        greater_invisibility_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        greater_invisibility_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        greater_invisibility_spell.add_field(name="Alcance", value="Toque", inline=False)
        greater_invisibility_spell.add_field(name="Componentes", value="V, S", inline=False)
        greater_invisibility_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return greater_invisibility_spell

    def imagem_maior():
        major_image_spell = discord.Embed(
            title="Imagem Maior (Major Image)",
            description=("Você cria a imagem de um objeto, criatura ou outra forma visual que ocupe até 6 metros cúbicos. A ilusão inclui "
                        "som, cheiro e outras sensações complementares. A ilusão pode ser interativa, mas não causa nenhum dano físico.\n\n"
                        "**Interação com o Ambiente:** Qualquer criatura que interaja fisicamente com a imagem pode perceber que ela é uma ilusão ao "
                        "passar através dela. Além disso, uma criatura pode usar sua ação para inspecionar a imagem e determinar se ela é falsa. "
                        "Se uma criatura fizer isso, ela deve ter sucesso em um teste de Inteligência (Investigação) contra a CD da sua magia.\n\n"
                        "**Aprimoramento:** Se você conjurar essa magia usando um espaço de magia de 6º nível ou superior, a duração se torna permanente."),
            color=0x20B2AA  # Cor azul celeste
        )
        major_image_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        major_image_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        major_image_spell.add_field(name="Alcance", value="36 metros", inline=False)
        major_image_spell.add_field(name="Componentes", value="V, S, M (um pedaço de lã)", inline=False)
        major_image_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return major_image_spell
    def criacao():
        creation_spell = discord.Embed(
            title="Criação (Creation)",
            description=("Você puxa matéria bruta das sombras para criar um objeto inanimado de matéria vegetal, mineral ou metal. A forma do objeto é limitada "
                        "pela sua imaginação, e ele pode ter até 5 pés cúbicos de volume por nível da magia. O material que você pode criar depende do seu nível "
                        "e da duração da magia:\n\n"
                        "- **Nível 5:** Você pode criar objetos de matéria vegetal (como madeira, corda ou tecidos).\n"
                        "- **Nível 6:** Matéria mineral (como pedra).\n"
                        "- **Nível 7:** Metais comuns (como ferro, prata).\n"
                        "- **Nível 8:** Materiais preciosos (como ouro).\n\n"
                        "**Desaparecimento:** O objeto desaparece ao fim da duração da magia. O tempo que o objeto permanece depende do material usado. "
                        "Por exemplo, madeira ou pedra dura por uma hora, mas ferro ou metais comuns duram até 10 minutos. Se o objeto criado for composto por "
                        "múltiplos tipos de materiais, ele durará conforme o material com a duração mais curta."),
            color=0x8B4513  # Cor marrom
        )
        creation_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        creation_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        creation_spell.add_field(name="Alcance", value="9 metros", inline=False)
        creation_spell.add_field(name="Componentes", value="V, S, M (um fragmento do material que você deseja criar)", inline=False)
        creation_spell.add_field(name="Duração", value="Varia conforme o material", inline=False)

        return creation_spell
    def ingrata_beleza():
        mislead_spell = discord.Embed(
            title="Ingrata Beleza (Mislead)",
            description=("Você se torna invisível ao mesmo tempo que cria uma ilusão de si mesmo, que parece se mover e agir conforme os seus comandos. "
                        "A ilusão persiste por toda a duração da magia ou até ser dissipada.\n\n"
                        "**Controle da Ilusão:** Enquanto invisível, você pode usar sua ação para mover a ilusão para qualquer ponto dentro do alcance da magia. "
                        "Você pode fazer com que a ilusão fale e imite ações simples, mas ela não pode interagir fisicamente com nada.\n\n"
                        "**Fim da Invisibilidade:** A invisibilidade termina se você atacar ou conjurar outra magia."),
            color=0xFFD700  # Cor dourada
        )
        mislead_spell.add_field(name="Conjuradores", value="Bardo, Mago", inline=False)
        mislead_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mislead_spell.add_field(name="Alcance", value="18 metros", inline=False)
        mislead_spell.add_field(name="Componentes", value="S", inline=False)
        mislead_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return mislead_spell
    def imagem_programada():
        programmed_illusion_spell = discord.Embed(
            title="Ilusão Programada (Programmed Illusion)",
            description=("Você cria uma ilusão detalhada que se ativa automaticamente conforme uma condição programada. A ilusão pode incluir sons, "
                        "cheiros e outros efeitos sensoriais. Ela pode se estender até um espaço de 9 metros cúbicos.\n\n"
                        "**Ativação:** A ilusão é programada para se ativar sob condições específicas, como quando uma criatura se aproxima de uma área ou quando "
                        "uma palavra-chave é dita. Uma vez ativada, a ilusão dura até 5 minutos, depois desaparece. Se as condições não forem cumpridas, "
                        "a ilusão permanece dormente por até 10 dias.\n\n"
                        "**Interação com a Ilusão:** Uma criatura pode usar sua ação para inspecionar a ilusão. Um teste de Inteligência (Investigação) bem-sucedido "
                        "revela que se trata de uma ilusão."),
            color=0x7B68EE  # Cor roxa média
        )
        programmed_illusion_spell.add_field(name="Conjuradores", value="Bardo, Mago", inline=False)
        programmed_illusion_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        programmed_illusion_spell.add_field(name="Alcance", value="36 metros", inline=False)
        programmed_illusion_spell.add_field(name="Componentes", value="V, S, M (um pedaço de lã e jade no valor de 25 po)", inline=False)
        programmed_illusion_spell.add_field(name="Duração", value="Até ser ativada ou até 10 dias", inline=False)

        return programmed_illusion_spell
    def prisão_mental():
        mental_prison_spell = discord.Embed(
            title="Prisão mental(Mental Prison)",
            description=("Você prende a mente de uma criatura em uma prisão ilusória de horror. O alvo deve fazer um teste de Inteligência. Se falhar, "
                        "ele acredita estar preso em uma situação mortal (como em chamas, rodeado por lâminas afiadas ou outros horrores).\n\n"
                        "**Dano Psíquico:** O alvo sofre 5d10 de dano psíquico imediatamente. Se o alvo tentar sair da área ou tocar qualquer coisa ao seu redor, "
                        "ele sofre mais 10d10 de dano psíquico, encerrando a magia.\n\n"
                        "**Efeito Ilusório:** O alvo não pode ver ou perceber além da prisão, que dura pela duração ou até ele sofrer dano."),
            color=0xDC143C  # Cor vermelha escura
        )
        mental_prison_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        mental_prison_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mental_prison_spell.add_field(name="Alcance", value="18 metros", inline=False)
        mental_prison_spell.add_field(name="Componentes", value="V, S", inline=False)
        mental_prison_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return mental_prison_spell
    def simulacro():
        simulacrum_spell = discord.Embed(
            title="Simulacro (Simulacrum)",
            description=("Você cria uma duplicata ilusória de uma besta ou humanoide que está ao seu alcance por toda a duração da magia. O simulacro "
                        "possui as mesmas estatísticas e habilidades da criatura original, mas seus pontos de vida são reduzidos pela metade.\n\n"
                        "**Comportamento do Simulacro:** Ele obedece aos seus comandos e age conforme suas ordens, mas não pode ganhar pontos de vida ou se "
                        "curar de qualquer forma. Se sofrer dano, ele permanecerá danificado até ser reparado com uma magia adequada.\n\n"
                        "**Duplicata Permanente:** O simulacro dura indefinidamente, até ser destruído. Ele é uma cópia perfeita, mas carece da capacidade de "
                        "crescimento ou evolução, sendo fixo no estado em que foi criado."),
            color=0x4682B4  # Cor azul aço
        )
        simulacrum_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        simulacrum_spell.add_field(name="Tempo de Conjuração", value="12 horas", inline=False)
        simulacrum_spell.add_field(name="Alcance", value="Toque", inline=False)
        simulacrum_spell.add_field(name="Componentes", value="V, S, M (neve ou gelo e pó de rubi no valor de 1.500 po)", inline=False)
        simulacrum_spell.add_field(name="Duração", value="Até ser destruído", inline=False)

        return simulacrum_spell
    def ilusao_permanente():
        illusory_dragon_spell = discord.Embed(
            title="Dragão Ilusorio (Illusory Dragon)",
            description=("Você cria a imagem de um dragão imponente, que parece completamente real e ataca seus inimigos. O dragão é feito de pura ilusão, "
                        "mas age como uma criatura física. O dragão ilusório ocupa um espaço de 18 metros cúbicos, tem presença ameaçadora e é capaz de atacar "
                        "criaturas dentro de sua área de efeito.\n\n"
                        "**Ataque do Dragão:** O dragão pode exalar um sopro de energia ilusória que causa 7d6 de dano psíquico em um cone de 18 metros. "
                        "Cada criatura dentro do cone deve fazer um teste de Sabedoria. Se falhar, sofrerá dano psíquico e será atordoada até o início do próximo turno.\n\n"
                        "**Movimento do Dragão:** O dragão ilusório pode se mover para qualquer lugar dentro do alcance da magia (36 metros) e continuar atacando. "
                        "Ele é imune a todos os tipos de dano físico e não pode ser destruído, exceto pelo fim da concentração do conjurador."),
            color=0x9932CC  # Cor roxa
        )
        illusory_dragon_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        illusory_dragon_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        illusory_dragon_spell.add_field(name="Alcance", value="36 metros", inline=False)
        illusory_dragon_spell.add_field(name="Componentes", value="V, S", inline=False)
        illusory_dragon_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return illusory_dragon_spell
    def metamorfose_verdadeira():
        weird_spell = discord.Embed(
            title="Metamorfose Verdadeira (Weird)",
            description=("Você conjura ilusões tão horríveis que invadem a mente de até 10 criaturas à sua escolha dentro de um raio de 9 metros. "
                        "Cada criatura afetada deve fazer um teste de Sabedoria. Se falhar, ela fica aterrorizada por imagens de seus piores medos, "
                        "incapaz de agir normalmente enquanto a magia durar.\n\n"
                        "**Efeito do Medo:** Uma criatura aterrorizada sofre 4d10 de dano psíquico no início de cada um dos seus turnos. Ela não pode se aproximar "
                        "de você ou das outras criaturas afetadas, e suas ações são limitadas a tentar escapar dos horrores que vê.\n\n"
                        "**Fim do Efeito:** O efeito termina se a criatura passar no teste de Sabedoria em um de seus turnos subsequentes, mas ela continua sofrendo dano "
                        "até que isso aconteça ou a magia termine."),
            color=0x00008B  # Cor azul escuro
        )
        weird_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        weird_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        weird_spell.add_field(name="Alcance", value="9 metros", inline=False)
        weird_spell.add_field(name="Componentes", value="V, S", inline=False)
        weird_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return weird_spell




