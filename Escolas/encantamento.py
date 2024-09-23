import discord

# encantamento - spells
class Encantamento:
    def __init__(self):
        pass
    def amizade():
        amizade_spell = discord.Embed(
            title="Amizade (Friends)",
            description = (
                "Por toda a duração, você tem vantagem em todas as jogadas de Carisma direcionadas a uma criatura de sua escolha que não seja hostil a você. "
                "Quando o feitiço termina, a criatura percebe que você usou magia para influenciar seu humor e pode se tornar hostil a você.\n\n"
                "A criatura pode não tomar ações violentas imediatamente, dependendo da natureza da sua interação com ela, mas a magia certamente irá alterar sua percepção de você."
            ),

            color=0xFF69B4  # Cor rosa
        )
        amizade_spell.add_field(name="Conjuradores", value="Bardo/Bruxo/Feiticeiro/Mago", inline=False)
        amizade_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        amizade_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        amizade_spell.add_field(name="Componentes", value="S, M (um pouco de maquiagem aplicada ao rosto enquanto você conjura a magia)", inline=False)
        amizade_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return amizade_spell

    def zombaria_viciosa():
        zombaria_viciosa_spell = discord.Embed(
            title="Zombaria Viciosa (Vicious Mockery)",
            description="Você libera uma série de insultos pungentes cobertos de encantamentos sutis na direção de uma criatura que você possa ver dentro do alcance. Se o alvo puder ouvir você (embora ele não precise entender), ele deve fazer um teste de resistência de Sabedoria. Se falhar, ele sofre 1d4 de dano psíquico e tem desvantagem no próximo ataque que fizer antes do final do próximo turno dele.",
            color=0x8B0000  # Cor vermelha escura
        )
        zombaria_viciosa_spell.add_field(name="Conjuradores", value="Bardo", inline=False)
        zombaria_viciosa_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        zombaria_viciosa_spell.add_field(name="Alcance", value="18 metros", inline=False)
        zombaria_viciosa_spell.add_field(name="Componentes", value="V", inline=False)
        zombaria_viciosa_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return zombaria_viciosa_spell

    def amizade_animal():
        amizade_animal_spell = discord.Embed(
            title="Amizade Animal (Animal Friendship)",
            description="Esta magia permite que você convença uma besta que você possa ver dentro do alcance de que você não quer machucá-la. A besta deve ver e ouvir você. Se a inteligência da besta for 4 ou maior, a magia falha. Caso contrário, a besta deve ser bem-sucedida em um teste de resistência de Sabedoria ou ficará encantada por você pela duração da magia.",
            color=0x228B22  # Cor verde floresta
        )
        amizade_animal_spell.add_field(name="Conjuradores", value="Bardo/Druida/Ranger", inline=False)
        amizade_animal_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        amizade_animal_spell.add_field(name="Alcance", value="9 metros", inline=False)
        amizade_animal_spell.add_field(name="Componentes", value="V, S, M (um pedaço de comida)", inline=False)
        amizade_animal_spell.add_field(name="Duração", value="24 horas", inline=False)

        return amizade_animal_spell

    def bruxaria():
        bruxaria_spell = discord.Embed(
            title="Bruxaria (Hex)",
            description="Você coloca uma maldição em uma criatura que você possa ver dentro do alcance. Até a magia acabar, você causa 1d6 de dano necrótico adicional ao alvo sempre que você acertar com um ataque. Além disso, escolha uma habilidade; o alvo tem desvantagem nos testes de habilidade feitos com a habilidade escolhida.",
            color=0x800080  # Cor roxa
        )
        bruxaria_spell.add_field(name="Conjuradores", value="Bruxo", inline=False)
        bruxaria_spell.add_field(name="Tempo de Conjuração", value="1 bônus", inline=False)
        bruxaria_spell.add_field(name="Alcance", value="27 metros", inline=False)
        bruxaria_spell.add_field(name="Componentes", value="V, S, M (um objeto que possua valor sentimental para você)", inline=False)
        bruxaria_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return bruxaria_spell

    def bencao():
        bencao_spell = discord.Embed(
            title="Benção (Bless)",
            description="Você abençoa até três criaturas à sua escolha dentro do alcance. Sempre que um alvo abençoado fizer um teste de ataque ou de resistência antes da magia acabar, o alvo pode adicionar 1d4 ao resultado.",
            color=0xFFFF00  # Cor amarela
        )
        bencao_spell.add_field(name="Conjuradores", value="Clérigo/Paladino", inline=False)
        bencao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        bencao_spell.add_field(name="Alcance", value="9 metros", inline=False)
        bencao_spell.add_field(name="Componentes", value="V, S, M (um pouco de água benta)", inline=False)
        bencao_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return bencao_spell

    def comando():
        comando_spell = discord.Embed(
            title="Comando (Command)",
            description = (
            "Você fala uma única palavra de comando a uma criatura que você possa ver dentro do alcance. O alvo deve ser bem-sucedido em um teste de resistência de Sabedoria ou deve seguir o comando no seu próximo turno.\n\n"
            "O feitiço não tem efeito se o alvo for um morto-vivo, se ele não entender sua língua ou se o comando dado for diretamente prejudicial a ele. Aqui estão alguns exemplos de comandos e seus possíveis efeitos:\n\n"
            "'Aproxime-se' – O alvo se move na direção de você pelo caminho mais curto e direto possível, terminando seu movimento o mais próximo de você que for possível.\n"
            "'Caia' – O alvo cai no chão e fica deitado.\n"
            "'Fuja' – O alvo gasta seu movimento para se afastar de você pela rota mais rápida possível.\n"
            "'Pare' – O alvo não faz nada no seu turno.\n"
            "'Renda-se' – O alvo entrega a você um item que esteja carregando.\n\n"
            "Em Níveis Superiores: Quando você conjura esta magia usando um espaço de 2° nível ou superior, você pode afetar uma criatura adicional para cada nível acima do 1°."
        ),

            color=0xFFA500  # Cor laranja
        )
        comando_spell.add_field(name="Conjuradores", value="Clérigo/Paladino", inline=False)
        comando_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        comando_spell.add_field(name="Alcance", value="18 metros", inline=False)
        comando_spell.add_field(name="Componentes", value="V", inline=False)
        comando_spell.add_field(name="Duração", value="1 rodada", inline=False)

        return comando_spell

    def duelo_compelido():
        duelo_compelido_spell = discord.Embed(
            title="Duelo Compelido (Compelled Duel)",
            description="Você tenta compelir uma criatura em direção ao duelo. Uma criatura à sua escolha que você possa ver dentro do alcance deve ser bem-sucedida em um teste de resistência de Sabedoria ou será compelida a lutar somente com você. Durante esse tempo, ela tem desvantagem em ataques contra criaturas que não sejam você e deve fazer um teste de Sabedoria toda vez que tentar se mover para um espaço que esteja a mais de 9 metros de você.",
            color=0xFFD700  # Cor ouro
        )
        duelo_compelido_spell.add_field(name="Conjuradores", value="Paladino", inline=False)
        duelo_compelido_spell.add_field(name="Tempo de Conjuração", value="1 bônus", inline=False)
        duelo_compelido_spell.add_field(name="Alcance", value="9 metros", inline=False)
        duelo_compelido_spell.add_field(name="Componentes", value="V", inline=False)
        duelo_compelido_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return duelo_compelido_spell

    def enfeiticar_pessoa():
        enfeiticar_pessoa_spell = discord.Embed(
            title="Enfeitiçar Pessoa (Charm Person)",
            description = (
                "Você tenta enfeitiçar uma criatura humanoide que você possa ver dentro do alcance. Ela deve ser bem-sucedida num teste de resistência de Sabedoria ou ficará enfeitiçada por você até o final da magia ou até que receba dano de você ou seus aliados.\n\n"
                "Se você ou seus companheiros estiverem lutando com a criatura, ela terá vantagem no teste de resistência. "
                "Enquanto a criatura estiver enfeitiçada, ela o considera um amigo próximo e confiável, mas o efeito não muda a disposição geral da criatura em relação a você. "
                "Quando a magia acabar, a criatura saberá que foi enfeitiçada por você.\n\n"
                "Em Níveis Superiores: Quando você conjurar esta magia usando um espaço de magia de 2° nível ou superior, você pode afetar uma criatura adicional para cada nível acima do 1°."
            ),

            color=0xDA70D6  # Cor violeta orquídea
        )
        enfeiticar_pessoa_spell.add_field(name="Conjuradores", value="Bardo/Bruxo/Druida/Feiticeiro/Mago", inline=False)
        enfeiticar_pessoa_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        enfeiticar_pessoa_spell.add_field(name="Alcance", value="9 metros", inline=False)
        enfeiticar_pessoa_spell.add_field(name="Componentes", value="V, S", inline=False)
        enfeiticar_pessoa_spell.add_field(name="Duração", value="1 hora", inline=False)

        return enfeiticar_pessoa_spell
    def coroa_da_loucura():
        coroa_da_loucura_spell = discord.Embed(
            title="Coroa da Loucura (Crown of Madness)",
            description = (
                "Uma criatura humanoide à sua escolha que você possa ver dentro do alcance deve ser bem-sucedida num teste de resistência de Sabedoria ou ficará enfeitiçada por você pela duração. "
                "Enquanto estiver enfeitiçada desta forma, uma coroa de ferro retorcido aparece em sua cabeça e uma loucura brilha em seus olhos.\n\n"
                "A criatura enfeitiçada deve usar sua ação antes de se mover em cada um de seus turnos para realizar um ataque corpo a corpo contra uma criatura, diferente dela mesma, que você escolher mentalmente. "
                "A criatura pode agir normalmente nos turnos seguintes, se você não escolher nenhum alvo. "
                "Nos turnos seguintes, você deve usar sua ação para manter o controle da criatura, caso contrário, o feitiço termina. "
                "A criatura também pode realizar um novo teste de resistência de Sabedoria no final de cada um dos seus turnos. Se for bem-sucedida, a magia termina."
            ),

            color=0x8B4513
        )
        coroa_da_loucura_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Mago", inline=False)
        coroa_da_loucura_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        coroa_da_loucura_spell.add_field(name="Alcance", value="36 metros", inline=False)
        coroa_da_loucura_spell.add_field(name="Componentes", value="V, S", inline=False)
        coroa_da_loucura_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return coroa_da_loucura_spell

    def imobilizar_pessoa():
        imobilizar_pessoa_spell = discord.Embed(
            title="Imobilizar Pessoa (Hold Person)",
            description="Escolha um humanoide que você possa ver dentro do alcance. O alvo deve ser bem-sucedido em um teste de resistência de Sabedoria ou ficará paralisado pela duração da magia. No final de cada um dos turnos do alvo, ele pode fazer outro teste de resistência de Sabedoria. Em um sucesso, o feitiço acaba para o alvo.",
            color=0xFF4500
        )
        imobilizar_pessoa_spell.add_field(name="Conjuradores", value="Bardo/Clérigo/Druida/Feiticeiro/Feiticeiro/Mago", inline=False)
        imobilizar_pessoa_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        imobilizar_pessoa_spell.add_field(name="Alcance", value="18 metros", inline=False)
        imobilizar_pessoa_spell.add_field(name="Componentes", value="V, S, M (um pequeno pedaço de ferro)", inline=False)
        imobilizar_pessoa_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return imobilizar_pessoa_spell

    def mensageiro_animal():
        mensageiro_animal_spell = discord.Embed(
            title="Mensageiro Animal (Animal Messenger)",
            description="Você usa um animal para entregar uma mensagem. Escolha uma besta à sua escolha que você possa ver dentro do alcance, como um pássaro, um roedor ou outro pequeno animal. Você especifica um local que visitou e um destinatário que se encontra nesse local. O animal viaja para lá e entrega a mensagem verbal que você pronunciou, até 25 palavras de comprimento.",
            color=0x32CD32
        )
        mensageiro_animal_spell.add_field(name="Conjuradores", value="Bardo/Druida/Ranger", inline=False)
        mensageiro_animal_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mensageiro_animal_spell.add_field(name="Alcance", value="9 metros", inline=False)
        mensageiro_animal_spell.add_field(name="Componentes", value="V, S, M (um pedaço de comida)", inline=False)
        mensageiro_animal_spell.add_field(name="Duração", value="24 horas", inline=False)

        return mensageiro_animal_spell

    def sugestao():
        sugestao_spell = discord.Embed(
            title="Sugestão (Suggestion)",
            description = (
                "Você sugere um curso de ação (limitado a uma frase ou duas) e influencia magicamente uma criatura que você possa ver dentro do alcance e que possa ouvi-lo. "
                "Criaturas que não possam ser enfeitiçadas são imunes a este efeito. A sugestão deve ser apresentada de forma que pareça razoável. "
                "Pedir à criatura para se esfaquear, jogar-se em uma lança, se imolar, ou fazer outro ato obviamente prejudicial encerra o feitiço.\n\n"
                "O alvo deve realizar um teste de resistência de Sabedoria. Em uma falha, ele segue o curso de ação que você descreveu da melhor forma possível. "
                "O curso de ação sugerido pode continuar por toda a duração do feitiço. Se a criatura completar o curso de ação antes do feitiço terminar, o feitiço acaba.\n\n"
                "Você também pode especificar condições que disparem uma ação especial durante a duração. Por exemplo, você pode sugerir a um cavaleiro que entregue seu cavalo ao primeiro mendigo que encontrar. "
                "Se a condição não for cumprida antes do feitiço terminar, a criatura não executará a ação.\n\n"
                "Em Níveis Superiores: Quando você conjurar esta magia usando um espaço de 3° nível ou superior, a duração será estendida para 8 horas."
            ),

            color=0x8A2BE2
        )
        sugestao_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Feiticeiro/Mago", inline=False)
        sugestao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        sugestao_spell.add_field(name="Alcance", value="9 metros", inline=False)
        sugestao_spell.add_field(name="Componentes", value="V, M (uma língua de cobra e mel ou uma gota de óleo doce)", inline=False)
        sugestao_spell.add_field(name="Duração", value="Concentração, até 8 horas", inline=False)

        return sugestao_spell

    def zona_da_verdade():
        zona_da_verdade_spell = discord.Embed(
            title="Zona da Verdade (Zone of Truth)",
            description="Você cria uma zona mágica que protege contra mentiras. Esta zona tem um raio de 4,5 metros e permanece por 10 minutos. Toda criatura que entrar na área ou começar seu turno nela deve fazer um teste de resistência de Carisma. Se falhar, a criatura não pode deliberadamente mentir. Você sabe se a criatura passou ou falhou no teste de resistência, mas a criatura pode evitar responder perguntas para as quais normalmente mentiria.",
            color=0xFFD700
        )
        zona_da_verdade_spell.add_field(name="Conjuradores", value="Bardo/Clérigo/Paladino", inline=False)
        zona_da_verdade_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        zona_da_verdade_spell.add_field(name="Alcance", value="18 metros", inline=False)
        zona_da_verdade_spell.add_field(name="Componentes", value="V, S", inline=False)
        zona_da_verdade_spell.add_field(name="Duração", value="10 minutos", inline=False)

        return zona_da_verdade_spell

    def infestar_de_inimigos():
        infestar_de_inimigos_spell = discord.Embed(
            title="Infestar de Inimigos (Enemies Abound)",
            description="Você causa uma onda de paranoia em uma criatura que você possa ver dentro do alcance. A criatura deve fazer um teste de resistência de Inteligência. Se falhar, ela considera todas as outras criaturas como inimigas e se torna incapaz de distinguir amigos de inimigos.",
            color=0x800080
        )
        infestar_de_inimigos_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Feiticeiro/Mago", inline=False)
        infestar_de_inimigos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        infestar_de_inimigos_spell.add_field(name="Alcance", value="36 metros", inline=False)
        infestar_de_inimigos_spell.add_field(name="Componentes", value="V, S, M (um pouco de carne podre)", inline=False)
        infestar_de_inimigos_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return infestar_de_inimigos_spell

    def soneca():
        soneca_spell = discord.Embed(
            title="Soneca (Catnap)",
            description="Você escolhe até três criaturas dispostas que você possa ver dentro do alcance e as coloca em um sono mágico por 10 minutos. As criaturas recuperam os pontos de vida e outros benefícios de um descanso curto.",
            color=0x4682B4
        )
        soneca_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Feiticeiro/Mago", inline=False)
        soneca_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        soneca_spell.add_field(name="Alcance", value="9 metros", inline=False)
        soneca_spell.add_field(name="Componentes", value="V, S, M (um pouco de areia ou uma folha seca)", inline=False)
        soneca_spell.add_field(name="Duração", value="10 minutos", inline=False)

        return soneca_spell

    def compulsao():
        compulsao_spell = discord.Embed(
            title="Compulsão (Compulsion)",
            description = (
                "Você escolhe um número de criaturas de sua escolha que você possa ver dentro do alcance e as enfeitiça, forçando-as a se moverem em uma direção de sua escolha. "
                "Cada alvo afetado deve realizar um teste de resistência de Sabedoria no início de cada um dos seus turnos. Se falharem, eles devem usar seu movimento para se mover em uma direção especificada por você.\n\n"
                "Eles podem se mover sobre terreno perigoso, mas não diretamente para um perigo óbvio, como uma fogueira. Se o alvo for capaz de completar o movimento, ele pode agir normalmente no turno.\n\n"
                "A magia dura até que a concentração seja interrompida, com uma duração máxima de 1 minuto."
            ),

            color=0x4B0082
        )
        compulsao_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Feiticeiro/Mago", inline=False)
        compulsao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
    def heroismo():
        heroismo_spell = discord.Embed(
            title="Heroísmo (Heroism)",
            description = (
            "Uma criatura voluntária que você toca é imbuída de bravura. Até que o feitiço termine, a criatura é imune a ser amedrontada e ganha pontos de vida temporários iguais ao seu modificador de conjuração no início de cada um dos seus turnos.\n\n"
            "Quando o feitiço termina, a criatura perde todos os pontos de vida temporários remanescentes dessa magia.\n\n"
            "Em Níveis Superiores: Quando você conjura esta magia usando um espaço de 2° nível ou superior, você pode afetar uma criatura adicional para cada nível acima do 1°."
        ),

            color=0x1E90FF  # Cor azul dodger
        )
        heroismo_spell.add_field(name="Conjuradores", value="Bardo/Paladino", inline=False)
        heroismo_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        heroismo_spell.add_field(name="Alcance", value="Toque", inline=False)
        heroismo_spell.add_field(name="Componentes", value="V, S", inline=False)
        heroismo_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return heroismo_spell

    def perdicao():
        perdicao_spell = discord.Embed(
            title="Perdição (Bane)",
            description="Até três criaturas à sua escolha que você possa ver dentro do alcance devem fazer um teste de resistência de Carisma. Sempre que um alvo que falhar neste teste fizer um teste de ataque ou de resistência antes da magia acabar, o alvo deve rolar 1d4 e subtrair o número rolado do resultado do teste de ataque ou resistência.",
            color=0x8B0000  # Cor vermelha escura
        )
        perdicao_spell.add_field(name="Conjuradores", value="Bardo/Clérigo", inline=False)
        perdicao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        perdicao_spell.add_field(name="Alcance", value="9 metros", inline=False)
        perdicao_spell.add_field(name="Componentes", value="V, S, M (um pouco de sangue de uma criatura)", inline=False)
        perdicao_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return perdicao_spell

    def riso_histerico_de_tasha():
        riso_histerico_de_tasha_spell = discord.Embed(
            title="Riso Histérico de Tasha (Tasha's Hideous Laughter)",
            description = (
                "Uma criatura de sua escolha que você possa ver dentro do alcance percebe tudo como hilariantemente engraçado e cai em uma crise de riso incontrolável. "
                "O alvo deve realizar um teste de resistência de Sabedoria ou cairá no chão, ficando incapacitado e incapaz de se levantar durante a duração da magia.\n\n"
                "Uma criatura com um valor de Inteligência de 4 ou menos não é afetada. No final de cada um dos turnos da criatura, e cada vez que sofrer dano, o alvo pode realizar um novo teste de resistência de Sabedoria. "
                "Em um sucesso, o feitiço termina."
            ),

            color=0xFF4500  # Cor laranja avermelhada
        )
        riso_histerico_de_tasha_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Mago", inline=False)
        riso_histerico_de_tasha_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        riso_histerico_de_tasha_spell.add_field(name="Alcance", value="9 metros", inline=False)
        riso_histerico_de_tasha_spell.add_field(name="Componentes", value="V, S, M (pequenas tortas e uma pena que é agitada no ar)", inline=False)
        riso_histerico_de_tasha_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return riso_histerico_de_tasha_spell

    def sono():
        sono_spell = discord.Embed(
            title="Sono (Sleep)",
            description = (
            "Esta magia faz com que criaturas entrem em um sono mágico. Lance 5d8; o total é quanto de pontos de vida de criaturas essa magia pode afetar. "
            "As criaturas dentro de 6 metros de um ponto à sua escolha dentro do alcance são afetadas em ordem ascendente de seus pontos de vida atuais (ignorando criaturas inconscientes).\n\n"
            "Começando com a criatura que tem os menores pontos de vida atuais, cada criatura afetada por esta magia cai inconsciente até a magia acabar, o alvo sofrer dano, ou alguém usar uma ação para sacudir ou esbofetear o alvo e acordá-lo.\n\n"
            "Em Níveis Superiores: Quando você conjura esta magia usando um espaço de 2° nível ou superior, role 2d8 adicionais para cada nível acima do 1°."
        ),

            color=0xF0E68C  # Cor cáqui
        )
        sono_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Feiticeiro/Paladino/Mago", inline=False)
        sono_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        sono_spell.add_field(name="Alcance", value="27 metros", inline=False)
        sono_spell.add_field(name="Componentes", value="V, S, M (uma pitada de areia, pétalas de rosa ou um grilo)", inline=False)
        sono_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return sono_spell

    def sussurros_dissonantes():
        sussurros_dissonantes_spell = discord.Embed(
            title="Sussurros Dissonantes (Dissonant Whispers)",
            description="Você sussurra uma melodia discordante que só uma criatura de sua escolha dentro do alcance pode ouvir, e ela deve fazer um teste de resistência de Sabedoria. Se falhar, ela sofre 3d6 de dano psíquico e deve imediatamente usar sua reação, se disponível, para se mover o máximo de distância possível de você.",
            color=0x8A2BE2  # Cor azul violeta
        )
        sussurros_dissonantes_spell.add_field(name="Conjuradores", value="Bardo", inline=False)
        sussurros_dissonantes_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        sussurros_dissonantes_spell.add_field(name="Alcance", value="18 metros", inline=False)
        sussurros_dissonantes_spell.add_field(name="Componentes", value="V", inline=False)
        sussurros_dissonantes_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return sussurros_dissonantes_spell

    def acalmar_emocoes():
        acalmar_emocoes_spell = discord.Embed(
            title="Acalmar Emoções (Calm Emotions)",
            description = (
            "Você tenta suprimir fortes emoções em um grupo de pessoas. Cada humanoide em uma esfera de 6 metros de raio centrada em um ponto de sua escolha dentro do alcance deve realizar um teste de resistência de Carisma. "
            "Se falhar, o alvo será afetado da seguinte forma: \n\n"
            "1. Você pode suprimir qualquer efeito que cause a condição amedrontado ou enfeitiçado. Quando o feitiço acabar, qualquer efeito suprimido volta a afetar a criatura, desde que sua duração não tenha acabado.\n"
            "2. Alternativamente, você pode fazer com que uma criatura que esteja hostil a você ou a seus aliados não possa atacar você ou seus aliados enquanto o feitiço durar. Isso termina se ela for atacada ou sofrer dano."
        ),

            color=0x4682B4  # Cor azul aço
        )
        acalmar_emocoes_spell.add_field(name="Conjuradores", value="Bardo/Clérigo", inline=False)
        acalmar_emocoes_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        acalmar_emocoes_spell.add_field(name="Alcance", value="18 metros", inline=False)
        acalmar_emocoes_spell.add_field(name="Componentes", value="V, S", inline=False)
        acalmar_emocoes_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return acalmar_emocoes_spell

    def cativar():
        cativar_spell = discord.Embed(
            title="Cativar (Enthrall)",
            description = (
            "Você fala de forma encantadora para criaturas de sua escolha dentro do alcance que possam ouvi-lo e entender o que você está dizendo. Cada alvo deve realizar um teste de resistência de Sabedoria. "
            "Qualquer alvo que não puder ser enfeitiçado automaticamente passa no teste.\n\n"
            "Se falharem, eles ficam fascinados por você pela duração. Enquanto estiver fascinado, o alvo tem desvantagem em testes de Sabedoria (Percepção) feitos para perceber qualquer criatura além de você. "
            "O feitiço termina se você causar dano a uma criatura afetada ou se ela sofrer algum efeito prejudicial."
        ),

            color=0xFF6347  # Cor tomate
        )
        cativar_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Feiticeiro", inline=False)
        cativar_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        cativar_spell.add_field(name="Alcance", value="18 metros", inline=False)
        cativar_spell.add_field(name="Componentes", value="V, S", inline=False)
        cativar_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return cativar_spell
    def confusao():
        confusao_spell = discord.Embed(
            title="Confusão (Confusion)",
            description="Essa magia ataca e embaralha as mentes das criaturas, gerando delírios e provocando ações descontroladas. Cada criatura em uma esfera com 3 metros de raio, centrada num ponto, à sua escolha, dentro do alcance, deve ser bem sucedida num teste de resistência de Sabedoria, quando você conjurar essa magia ou for afetada por ela.Um alvo afetado não pode realizar reações e deve rolar um d10 no início de cada um dos seus turnos para determinar seu comportamento nesse turno.",
            color=0xFF6347  # Cor tomate
        )
        confusao_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Mago", inline=False)
        confusao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        confusao_spell.add_field(name="Alcance", value="9 metros", inline=False)
        confusao_spell.add_field(name="Componentes", value="V, S, M (pequeno pedaço de carvão)", inline=False)
        confusao_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return confusao_spell

    def dominar_a_besta():
        dominar_a_besta_spell = discord.Embed(
            title="Dominar a Besta (Dominate Beast)",
            description=("Você tenta seduzir uma besta que você possa ver dentro do alcance. Ela deve ser bem sucedida num teste de resistência de Sabedoria ou ficará enfeitiçada por você pela duração. \n\n"
	     		        "Se você ou criaturas amigáveis a você estiverem lutando com ela, ela terá vantagem no teste de resistência."
                        "Enquanto a besta estiver enfeitiçada, você terá uma ligação telepática com ela, contanto que ambos estejam no mesmo plano de existência. Você pode usar essa ligação telepática para emitir comandos para a criatura" 			
                        "enquanto você estiver consciente não requer uma ação, aos quais ela obedece da melhor forma possível. Você pode especificar um curso de ação simples e genérico, como 'Ataque aquela criatura', 'Corra até ali'	"			
                        "'ou Traga aquele objeto'. Se a criatura completar a ordem e não receber direções posteriores de você, ela se defenderá e se auto preservará da melhor forma que puder"
                        "Você pode usar sua ação para tomar controle total e preciso do alvo. Até o final do seu próximo turno, a criatura realiza apenas as ações que você escolher e não faz nada que você não permita que ela faça."					
                        "Durante esse período, você também pode fazer com que a criatura use uma reação, mas isso requer que você usa sua própria reação também.\n\n"
                        "Cada vez que o alvo sofrer dano, ele realiza um novo teste de resistência de Sabedoria contra a magia. Se obtiver sucesso no teste de resistência, a magia termina.\n\n "
                        "Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 5° nível, a duração será concentração, até 10 minutos. Quando você usar um espaço de magia de 6° nível, a duração será"					
                        "concentração, até 1 hora. Quando você usar um espaço de magia de 7° nível, a duração será concentração, até 8 horas."
                        ),
            color=0x32CD32  # Cor verde limão
                                           )
        dominar_a_besta_spell.add_field(name="Conjuradores", value="Druida/Feiticeiro/Mago", inline=False)
        dominar_a_besta_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        dominar_a_besta_spell.add_field(name="Alcance", value="36 metros", inline=False)
        dominar_a_besta_spell.add_field(name="Componentes", value="V, S, M (um pequeno pedaço de carne)", inline=False)
        dominar_a_besta_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return dominar_a_besta_spell

    def enfeitiçar_o_monstro():
        enfeitiçar_o_monstro_spell = discord.Embed(
            title="Enfeitiçar o Monstro (Charm Monster)",
            description="Você encanta uma criatura que pode ver dentro do alcance. O alvo deve fazer um teste de resistência de Sabedoria. Se falhar, fica encantado por você. Enquanto encantado, a criatura considera você como um amigo e não atacará você.",
            color=0x8A2BE2  # Cor azul violeta
        )
        enfeitiçar_o_monstro_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        enfeitiçar_o_monstro_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        enfeitiçar_o_monstro_spell.add_field(name="Alcance", value="9 metros", inline=False)
        enfeitiçar_o_monstro_spell.add_field(name="Componentes", value="V, S", inline=False)
        enfeitiçar_o_monstro_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return enfeitiçar_o_monstro_spell

    def dominar_pessoa():
        dominar_pessoa_spell = discord.Embed(
            title="Dominar Pessoa (Dominate Person)",
           description = (
            "Você tenta seduzir uma humanoide que você possa ver dentro do alcance. Ela deve ser bem-sucedida num teste de resistência de Sabedoria ou ficará enfeitiçada por você pela duração.\n\n"
            "Se você ou criaturas amigáveis a você estiverem lutando com ela, ela terá vantagem no teste de resistência.\n\n"
            "Enquanto a humanoide estiver enfeitiçada, você terá uma ligação telepática com ela, contanto que ambos estejam no mesmo plano de existência. "
            "Você pode usar essa ligação telepática para emitir comandos para a criatura enquanto estiver consciente, aos quais ela obedece da melhor forma possível. "
            "Você pode especificar um curso de ação simples, como 'Ataque aquela criatura', 'Corra até ali' ou 'Traga aquele objeto'. "
            "Se a criatura completar a ordem e não receber direções posteriores de você, ela se defenderá e se auto preservará da melhor forma que puder.\n\n"
            "Você pode usar sua ação para tomar controle total e preciso do alvo. Até o final do seu próximo turno, a criatura realiza apenas as ações que você escolher e não faz nada que você não permita que ela faça. "
            "Durante esse período, você também pode fazer com que a criatura use uma reação, mas isso requer que você use sua própria reação também.\n\n"
            "Cada vez que o alvo sofrer dano, ele realiza um novo teste de resistência de Sabedoria. Se obtiver sucesso, a magia termina.\n\n"
            "Em Níveis Superiores: Quando você conjurar essa magia usando um espaço de 6° nível ou superior, a duração será concentração, até 1 hora."
                        ),

            color=0x6A5ACD  # Cor azul ardósia
        )
        dominar_pessoa_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        dominar_pessoa_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        dominar_pessoa_spell.add_field(name="Alcance", value="36 metros", inline=False)
        dominar_pessoa_spell.add_field(name="Componentes", value="V, S, M (um fio de cabelo ou uma gota de sangue da criatura)", inline=False)
        dominar_pessoa_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return dominar_pessoa_spell

    def estetica_sinaptica():
        estetica_sinaptica_spell = discord.Embed(
            title="Estética Sináptica (Synaptic Static)",
            description="Você cria uma explosão de energia psíquica em um ponto à sua escolha dentro do alcance. Cada criatura em uma área de 9 metros de raio deve fazer um teste de resistência de Inteligência. Uma criatura que falhe no teste sofre dano psíquico e tem desvantagem em testes de habilidade e ataques enquanto estiver na área de efeito.",
            color=0xDAA520  # Cor dourado
        )
        estetica_sinaptica_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        estetica_sinaptica_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        estetica_sinaptica_spell.add_field(name="Alcance", value="18 metros", inline=False)
        estetica_sinaptica_spell.add_field(name="Componentes", value="V, S", inline=False)
        estetica_sinaptica_spell.add_field(name="Duração", value="Instantâneo", inline=False)

        return estetica_sinaptica_spell

    def imobilisar_o_monstro():
        imobilisar_o_monstro_spell = discord.Embed(
            title="Imobilizar o Monstro (Hold Monster)",
            description="Você paralisa uma criatura que pode ver dentro do alcance. A criatura deve fazer um teste de resistência de Sabedoria. Se falhar, fica paralisada enquanto a magia durar. A criatura pode fazer novos testes de resistência no final de cada um dos seus turnos para tentar se libertar.",
            color=0x4682B4  # Cor azul aço
        )
        imobilisar_o_monstro_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        imobilisar_o_monstro_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        imobilisar_o_monstro_spell.add_field(name="Alcance", value="18 metros", inline=False)
        imobilisar_o_monstro_spell.add_field(name="Componentes", value="V, S, M (um pouco de ferro)", inline=False)
        imobilisar_o_monstro_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return imobilisar_o_monstro_spell

    def missao():
        missao_spell = discord.Embed(
            title="Missão (Mission)",
            description = (
            "Você impõe uma ordem mágica em uma criatura que você possa ver dentro do alcance, forçando-a a realizar ou se abster de alguma ação conforme sua escolha por toda a duração do feitiço. "
            "Se a criatura puder entendê-lo, ela deve ser bem-sucedida em um teste de resistência de Sabedoria ou ficará enfeitiçada por você pela duração.\n\n"
            "Enquanto estiver enfeitiçada desta forma, a criatura sofre 5d10 de dano psíquico toda vez que agir de forma direta contra suas instruções, mas não sofre dano por fazer algo que contrarie o feitiço indiretamente. "
            "Você pode emitir uma nova ordem sempre que quiser, substituindo a anterior.\n\n"
            "O feitiço pode durar 30 dias e pode ser finalizado antecipadamente por Dissipar Magia, Cura Completa ou Remoção de Maldição."
        ),

            color=0x00BFFF  # Cor azul profundo
        )
        missao_spell.add_field(name="Conjuradores", value="Bardo/Feiticeiro/Mago", inline=False)
        missao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        missao_spell.add_field(name="Alcance", value="9 metros", inline=False)
        missao_spell.add_field(name="Componentes", value="V", inline=False)
        missao_spell.add_field(name="Duração", value="Instantâneo", inline=False)

        return missao_spell
    def modificar_memoria():
        modificar_memoria_spell = discord.Embed(
            title="Modificar Memória (Modify Memory)",
           description = (
            "Você tenta remodelar as memórias de outra criatura. Uma criatura que você possa ver deve fazer um teste de resistência de Sabedoria. "
            "Em uma falha, a criatura está enfeitiçada por você pela duração e você pode modificar uma memória que ela tenha da última 24 horas.\n\n"
            "Você pode eliminar todos os eventos da memória da criatura nos últimos 24 horas e criar novos eventos que nunca aconteceram, ou alterar a percepção de eventos reais. "
            "A modificação dura até que o feitiço termine e a criatura não tenha forma de perceber que suas memórias foram alteradas, a menos que você crie inconsistências óbvias.\n\n"
            "Em Níveis Superiores: Usando um espaço de 6° nível ou superior, você pode afetar memórias de até 7 dias atrás. Com um espaço de 8° nível, até 30 dias atrás, e com um espaço de 9° nível, até 1 ano."
        ),

            color=0xFF69B4  # Cor rosa quente
        )
        modificar_memoria_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        modificar_memoria_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        modificar_memoria_spell.add_field(name="Alcance", value="9 metros", inline=False)
        modificar_memoria_spell.add_field(name="Componentes", value="V, S, M (uma lembrança especial)", inline=False)
        modificar_memoria_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return modificar_memoria_spell

    def dança_irresistivel_de_otto():
        dança_irresistivel_de_otto_spell = discord.Embed(
            title="Dança Irresistível de Otto (Otto's Irresistible Dance)",
            description="Você faz uma criatura que pode ver dentro do alcance começar a dançar incontrolavelmente. A criatura deve fazer um teste de resistência de Sabedoria. Se falhar, fica encantada e se vê forçada a dançar durante a duração da magia, tornando-se vulnerável a ataques enquanto dança.",
            color=0xFFD700  # Cor dourada
        )
        dança_irresistivel_de_otto_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        dança_irresistivel_de_otto_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        dança_irresistivel_de_otto_spell.add_field(name="Alcance", value="18 metros", inline=False)
        dança_irresistivel_de_otto_spell.add_field(name="Componentes", value="V, S, M (uma flauta mágica)", inline=False)
        dança_irresistivel_de_otto_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return dança_irresistivel_de_otto_spell

    def sugestao_em_massa():
        sugestao_em_massa_spell = discord.Embed(
            title="Sugestão em Massa (Mass Suggestion)",
           description = (
            "Você sugere um curso de ação (limitado a uma frase ou duas) e influencia magicamente até doze criaturas de sua escolha dentro do alcance e que possam ouvi-lo. "
            "As criaturas que não puderem ser enfeitiçadas são imunes a este efeito. A sugestão deve ser apresentada de forma que pareça razoável. "
            "Pedir às criaturas para se esfaquearem, jogarem-se em uma lança, se imolarem, ou fazer outro ato obviamente prejudicial encerrará o feitiço.\n\n"
            "Cada alvo deve realizar um teste de resistência de Sabedoria. Em uma falha, ele segue o curso de ação que você descreveu da melhor forma possível. "
            "O curso de ação sugerido pode continuar por toda a duração do feitiço, que é de até 24 horas. Se a criatura completar a ordem antes de o feitiço acabar, o feitiço termina para aquela criatura.\n\n"
            "Em Níveis Superiores: Quando você conjurar esta magia usando um espaço de 7° nível ou superior, a duração será de até 10 dias."
        ),

            color=0x00FA9A  # Cor verde marinho
        )
        sugestao_em_massa_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        sugestao_em_massa_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        sugestao_em_massa_spell.add_field(name="Alcance", value="18 metros", inline=False)
        sugestao_em_massa_spell.add_field(name="Componentes", value="V, S, M (uma pequena caneta de prata)", inline=False)
        sugestao_em_massa_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return sugestao_em_massa_spell

    def palavra_de_poder_dor():
        palavra_de_poder_dor_spell = discord.Embed(
            title="Palavra de Poder: Dor (Power Word Pain)",
            description="Você invoca uma palavra de poder que causa uma dor intensa em uma criatura à sua escolha que você possa ver dentro do alcance. A criatura deve fazer um teste de resistência de Constituição. Se falhar, sofre uma grande quantidade de dano psíquico e fica incapacitada durante a duração da magia.",
            color=0x8B0000  # Cor vermelho escuro
        )
        palavra_de_poder_dor_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        palavra_de_poder_dor_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        palavra_de_poder_dor_spell.add_field(name="Alcance", value="18 metros", inline=False)
        palavra_de_poder_dor_spell.add_field(name="Componentes", value="V", inline=False)
        palavra_de_poder_dor_spell.add_field(name="Duração", value="Instantâneo", inline=False)

        return palavra_de_poder_dor_spell

    def antipatia_simpatia():
        antipatia_simpatia_spell = discord.Embed(
            title="Antipatia/Simpatia (Antipathy/Sympathy)",
           description = (
            "Esta magia permite influenciar criaturas de duas formas opostas: Antipatia ou Simpatia. Você pode escolher uma das opções ao conjurar a magia.\n\n"
            "**Antipatia:** Escolha uma criatura, tipo de criatura ou objeto dentro do alcance. As criaturas designadas por você sentirão uma repulsa intensa pelo alvo. Elas devem realizar um teste de resistência de Sabedoria. "
            "Se falharem, elas evitarão o alvo de todas as formas possíveis. Em caso de sucesso, a criatura não é afetada.\n\n"
            "**Simpatia:** Você escolhe uma criatura, tipo de criatura ou objeto. As criaturas designadas por você sentirão uma atração irresistível pelo alvo, movendo-se em sua direção de todas as maneiras possíveis, a menos que obtenham sucesso em um teste de resistência de Sabedoria.\n\n"
            "Essa magia dura 10 dias e pode ser finalizada antecipadamente por Dissipar Magia ou por magias de Remoção de Encantamento."
        ),

            color=0x4B0082  # Cor índigo
        )
        antipatia_simpatia_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        antipatia_simpatia_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        antipatia_simpatia_spell.add_field(name="Alcance", value="18 metros", inline=False)
        antipatia_simpatia_spell.add_field(name="Componentes", value="V, S, M (um pedaço de cristal ou gema)", inline=False)
        antipatia_simpatia_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return antipatia_simpatia_spell

    def dominar_o_monstro():
        dominar_o_monstro_spell = discord.Embed(
            title="Dominar Monstro (Dominate Monster)",
            description = (
            "Você tenta seduzir um monstro que você possa ver dentro do alcance. Ele deve ser bem-sucedido em um teste de resistência de Sabedoria ou ficará enfeitiçado por você pela duração. "
            "Enquanto o monstro estiver enfeitiçado, você terá uma ligação telepática com ele e poderá emitir comandos telepáticos sem usar uma ação, aos quais ele obedecerá. "
            "Você pode usar sua ação para tomar controle total do alvo, e até o final do seu próximo turno, ele executará as ações que você escolher. Cada vez que o alvo sofrer dano, ele realiza um novo teste de resistência para encerrar o efeito."
        ),

            color=0x5F9F9F  # Cor cinza verde
        )
        dominar_o_monstro_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        dominar_o_monstro_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        dominar_o_monstro_spell.add_field(name="Alcance", value="36 metros", inline=False)
        dominar_o_monstro_spell.add_field(name="Componentes", value="V, S, M (um pouco de cada tipo de sangue)", inline=False)
        dominar_o_monstro_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return dominar_o_monstro_spell

    def enfraquecer_o_intelecto():
        enfraquecer_o_intelecto_spell = discord.Embed(
            title="Enfraquecer o Intelecto (Etherealness)",
            description = (
                "Você foca sua mente para lançar uma maldição psíquica em uma criatura. Escolha um alvo dentro do alcance. Ele deve fazer um teste de resistência de Inteligência. Em caso de falha, o alvo sofre 3d6 de dano psíquico e sua pontuação de Inteligência é reduzida para 1. A criatura não consegue lançar magias, ativar itens mágicos ou usar habilidades que dependam de Inteligência enquanto estiver sob este efeito.\n\n"
                "O efeito dura até que seja removido por uma magia como restauração maior ou desejo."
            ),

            color=0xFF4500  # Cor laranja avermelhada
        )
        enfraquecer_o_intelecto_spell.add_field(name="Conjuradores", value="Feiticeiro/Mago", inline=False)
        enfraquecer_o_intelecto_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        enfraquecer_o_intelecto_spell.add_field(name="Alcance", value="9 metros", inline=False)
        enfraquecer_o_intelecto_spell.add_field(name="Componentes", value="V, S", inline=False)
        enfraquecer_o_intelecto_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return enfraquecer_o_intelecto_spell
    def palavra_de_poder_atordoar():
        stun_spell = discord.Embed(
            title="Palavra de Poder: Atordoar (Power Word Stun)",
            description = (
            "Você pronuncia uma palavra de poder que pode atordoar uma criatura. Escolha uma criatura que você possa ver dentro do alcance. Se o alvo tiver 150 pontos de vida ou menos, ele fica atordoado. Caso contrário, a magia não tem efeito.\n\n"
            "A criatura atordoada permanece assim até o fim do próximo turno do conjurador. Não há testes de resistência para evitar o efeito, mas criaturas com mais de 150 pontos de vida são imunes a essa magia."
                ),

            color=0xFFD700  # Cor dourada
        )
        stun_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        stun_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        stun_spell.add_field(name="Alcance", value="18 metros", inline=False)
        stun_spell.add_field(name="Componentes", value="V", inline=False)
        stun_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return stun_spell
    def grito_psiquico():
        psychic_scream_spell = discord.Embed(
            title="Grito Psíquico (Psychic Scream)",
            description = (
            "Você emite um grito devastador que afeta as mentes de até 10 criaturas de sua escolha dentro do alcance. Cada alvo deve fazer um teste de resistência de Inteligência. Se falhar, ele sofre 14d6 de dano psíquico e fica atordoado. Em um sucesso, ele sofre metade do dano e não fica atordoado.\n\n"
            "Uma criatura atordoada pode repetir o teste de resistência de Inteligência no final de cada um de seus turnos, terminando o efeito sobre si em um sucesso."
             ),

            color=0x8A2BE2  # Cor roxa
        )
        psychic_scream_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        psychic_scream_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        psychic_scream_spell.add_field(name="Alcance", value="36 metros", inline=False)
        psychic_scream_spell.add_field(name="Componentes", value="V", inline=False)
        psychic_scream_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return psychic_scream_spell
    def palavra_de_poder_matar():
        kill_spell = discord.Embed(
            title="Palavra de Poder: Matar (Power Word Kill)",
            description = (
                "Você pronuncia uma palavra de poder que mata instantaneamente uma criatura de sua escolha que possa ouvi-lo dentro do alcance. "
                "Se o alvo tiver 100 pontos de vida ou menos, ele morre imediatamente, sem necessidade de um teste de resistência. Criaturas com mais de 100 pontos de vida não são afetadas pela magia."
            ),

            color=0xFF0000  # Cor vermelha
        )
        kill_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        kill_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        kill_spell.add_field(name="Alcance", value="18 metros", inline=False)
        kill_spell.add_field(name="Componentes", value="V", inline=False)
        kill_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return kill_spell
    def comandar_em_massa():
        mass_comand_spell = discord.Embed(
            title="Comandar em Massa (Mass command)",
            description = (
                "Você fala uma única palavra de comando a várias criaturas de sua escolha dentro do alcance. Cada alvo deve ser bem-sucedido em um teste de resistência de Sabedoria ou deve seguir o comando no seu próximo turno.\n\n"
                "O feitiço não tem efeito se o alvo for um morto-vivo, se ele não entender sua língua ou se o comando dado for diretamente prejudicial a ele. Aqui estão alguns exemplos de comandos e seus possíveis efeitos:\n\n"
                "'Aproxime-se' – Os alvos se movem na direção de você pelo caminho mais curto e direto possível.\n"
                "'Caia' – Os alvos caem no chão e ficam deitados.\n"
                "'Fuja' – Os alvos gastam seus movimentos para se afastarem de você pela rota mais rápida possível.\n"
                "'Pare' – Os alvos não fazem nada no seu turno.\n"
                "'Renda-se' – Os alvos entregam a você itens que estejam carregando."
            ),

            color=0xFF0000  # Cor vermelha
        )
        mass_comand_spell.add_field(name="Conjuradores", value="Clérigo", inline=False)
        mass_comand_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mass_comand_spell.add_field(name="Alcance", value="18 metros", inline=False)
        mass_comand_spell.add_field(name="Componentes", value="V", inline=False)
        mass_comand_spell.add_field(name="Duração", value="1 rodada", inline=False)

        return mass_comand_spell
    def phantasmal_killer():
        phantasmal_killer_spell = discord.Embed(
            title="Comandar em Massa (Mass command)",
            description = (
    "Você aproveita os medos mais profundos de uma criatura para criar uma ilusão na mente dela, algo terrível que somente ela pode ver. O alvo deve realizar um teste de resistência de Sabedoria. "
    "Em uma falha, o alvo fica amedrontado pela duração.\n\n"
    "No final de cada um dos turnos do alvo, antes do feitiço acabar, o alvo deve realizar outro teste de resistência de Sabedoria. "
    "Em uma falha, o alvo sofre 4d10 de dano psíquico. Em um sucesso, o feitiço termina."
                    ),

            color=0xFF0000  # Cor vermelha
        )
        phantasmal_killer_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        phantasmal_killer_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        phantasmal_killer_spell.add_field(name="Alcance", value="36 metros", inline=False)
        phantasmal_killer_spell.add_field(name="Componentes", value="V, S", inline=False)
        phantasmal_killer_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return phantasmal_killer_spell