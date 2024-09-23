import discord

class transmutação:
    def __init__(self):
        pass
    def forma_gasosa():
        forma_gasosa_spell = discord.Embed(
            title="Forma Gasosa (Gaseous Form)",
            description=(
                "Você transforma uma criatura voluntária que você possa ver dentro do alcance, junto com tudo o que ela estiver vestindo e carregando, em uma névoa gasosa pelo período de duração. "
                "Enquanto estiver na forma de névoa, o alvo não pode atacar ou lançar magias, e tem resistência a dano não mágico. Ele pode passar por pequenas fendas e fendas finas, e fica imune a efeitos de estado como cair ou ser envenenado.\n\n"
                "A criatura permanece consciente e pode mover-se com uma velocidade de voo de 3 metros. A forma de névoa é difícil de ser atacada, pois o alvo ganha a habilidade de passar por lugares apertados."
            ),
            color=0xADD8E6  # Cor azul clara
        )
        forma_gasosa_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        forma_gasosa_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        forma_gasosa_spell.add_field(name="Alcance", value="Toque", inline=False)
        forma_gasosa_spell.add_field(name="Componentes", value="V, S, M (um pouco de fumaça)", inline=False)
        forma_gasosa_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return forma_gasosa_spell
    def polimorfia():
        polimorfia_spell = discord.Embed(
            title="Metamorfose (Polymorph)",
            description=(
                "Esta magia transforma uma criatura que você possa ver dentro do alcance em uma nova forma. Um alvo não voluntário deve fazer um teste de resistência de Sabedoria para evitar o efeito. "
                "A transformação dura pela duração, ou até que os pontos de vida da nova forma sejam reduzidos a 0. O novo corpo pode ser qualquer besta cujo nível de desafio seja igual ou inferior ao do alvo original.\n\n"
                "O alvo assume as estatísticas da nova forma, incluindo pontos de vida, mas mantém a própria personalidade. O alvo não pode lançar magias ou realizar ações que dependam de habilidades não adquiridas pela nova forma."
            ),
            color=0xFFD700  # Cor dourada
        )
        polimorfia_spell.add_field(name="Conjuradores", value="Bardo, Druida, Feiticeiro, Mago", inline=False)
        polimorfia_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        polimorfia_spell.add_field(name="Alcance", value="18 metros", inline=False)
        polimorfia_spell.add_field(name="Componentes", value="V, S, M (um cocô de lagarta)", inline=False)
        polimorfia_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return polimorfia_spell
    def aprimorar_habilidade():
        aprimorar_habilidade_spell = discord.Embed(
        title="Aprimorar Habilidade (Enhance Ability)",
        description=(
            "Você toca uma criatura e concede a ela uma benção mágica, conferindo uma habilidade aprimorada. Escolha um dos seguintes efeitos; o alvo recebe o benefício até o fim da duração:\n\n"
            "- **Força de Touro**: O alvo tem vantagem em testes de Força, e sua capacidade de carga é dobrada.\n"
            "- **Resistência do Urso**: O alvo tem vantagem em testes de Constituição, e também ganha 2d6 pontos de vida temporários.\n"
            "- **Graça do Gato**: O alvo tem vantagem em testes de Destreza. Não sofre dano de queda a partir de uma altura de 6 metros ou menos.\n"
            "- **Esperteza da Raposa**: O alvo tem vantagem em testes de Inteligência.\n"
            "- **Astúcia da Coruja**: O alvo tem vantagem em testes de Sabedoria.\n"
            "- **Carisma da Águia**: O alvo tem vantagem em testes de Carisma."
        ),
        color=0x800080  # Cor roxa
        )
        aprimorar_habilidade_spell.add_field(name="Conjuradores", value="Bardo, Clérigo, Druida, Feiticeiro, Mago", inline=False)
        aprimorar_habilidade_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        aprimorar_habilidade_spell.add_field(name="Alcance", value="Toque", inline=False)
        aprimorar_habilidade_spell.add_field(name="Componentes", value="V, S, M (pelo ou pena de uma besta)", inline=False)
        aprimorar_habilidade_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return aprimorar_habilidade_spell
    def alterar_se():
        alterar_se_spell = discord.Embed(
            title="Alterar-se (Alter Self)",
            description=(
                "Você assume uma nova forma. Ao conjurar esta magia, escolha uma das seguintes opções, o efeito dura pela duração da magia:\n\n"
                "- **Mudar de Aparência**: Você pode mudar sua aparência física, incluindo altura, peso, traços faciais, e cor da pele ou do cabelo. Você pode até adquirir membros extras, como asas ou nadadeiras, mas isso não concede a você habilidades funcionais adicionais (como voo).\n"
                "- **Adaptação Aquática**: Você pode se adaptar a ambientes aquáticos. Ganha uma velocidade de natação igual à sua velocidade de caminhada, e pode respirar embaixo d'água.\n"
                "- **Armas Naturais**: Você pode fazer com que garras, presas ou outras armas naturais surjam de seu corpo. Você pode realizar ataques corpo a corpo com essas armas naturais, causando 1d6 de dano cortante, perfurante ou contundente (à sua escolha)."
            ),
            color=0x4682B4  # Cor azul aço
        )
        alterar_se_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        alterar_se_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        alterar_se_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        alterar_se_spell.add_field(name="Componentes", value="V, S", inline=False)
        alterar_se_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return alterar_se_spell
    def acelerar():
        acelerar_spell = discord.Embed(
        title="Acelerar (Haste)",
        description=(
            "Escolha uma criatura que você possa ver dentro do alcance. Até a magia acabar, o alvo recebe uma velocidade de movimento dobrada, ganha um bônus de +2 na CA, tem vantagem em testes de resistência de Destreza e recebe uma ação adicional em cada um dos seus turnos.\n\n"
            "Essa ação pode ser usada apenas para realizar a ação de ataque (com uma arma ou um ataque desarmado), realizar uma Corrida, Esquiva, Usar um Objeto ou se Desengajar.\n\n"
            "Quando a magia termina, o alvo não pode se mover ou realizar ações até o fim do seu próximo turno, pois fica exausto pela energia liberada."
        ),
        color=0xFFFF00  # Cor amarela
        )
        acelerar_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        acelerar_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        acelerar_spell.add_field(name="Alcance", value="9 metros", inline=False)
        acelerar_spell.add_field(name="Componentes", value="V, S, M (um lasco de alcaçuz)", inline=False)
        acelerar_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return acelerar_spell
    def reduzir_ampliar():
        reduzir_ampliar_spell = discord.Embed(
            title="Reduzir/Ampliar (Enlarge/Reduce)",
            description=(
                "Você faz com que uma criatura ou objeto que você possa ver dentro do alcance se torne maior ou menor pelo período de duração. Escolha uma das seguintes opções:\n\n"
                "- **Ampliar**: O tamanho do alvo aumenta em uma categoria — de Médio para Grande, por exemplo. O alvo também tem vantagem em testes de Força e testes de resistência de Força. As armas do alvo também crescem, causando 1d4 adicional de dano.\n"
                "- **Reduzir**: O tamanho do alvo diminui em uma categoria. O alvo tem desvantagem em testes de Força e testes de resistência de Força. As armas do alvo também diminuem, causando 1d4 a menos de dano."
            ),
            color=0xB22222  # Cor vermelha escura
        )
        reduzir_ampliar_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        reduzir_ampliar_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        reduzir_ampliar_spell.add_field(name="Alcance", value="9 metros", inline=False)
        reduzir_ampliar_spell.add_field(name="Componentes", value="V, S, M (um pouco de pó de ferro)", inline=False)
        reduzir_ampliar_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return reduzir_ampliar_spell
    def respirar_na_agua():
        respirar_na_agua_spell = discord.Embed(
            title="Respirar na Água (Water Breathing)",
            description=(
                "Você concede a até dez criaturas que possa ver dentro do alcance a habilidade de respirar debaixo d'água pela duração da magia. Afetadas pela magia, as criaturas continuam a respirar normalmente sob a água, sem perder a capacidade de respirar ar.\n\n"
                "Este efeito dura 24 horas, e é especialmente útil em ambientes subaquáticos ou para viagens prolongadas por rios e oceanos."
            ),
            color=0x1E90FF  # Cor azul
        )
        respirar_na_agua_spell.add_field(name="Conjuradores", value="Bardo, Druida, Feiticeiro, Mago", inline=False)
        respirar_na_agua_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        respirar_na_agua_spell.add_field(name="Alcance", value="9 metros", inline=False)
        respirar_na_agua_spell.add_field(name="Componentes", value="V, S, M (um grão de areia)", inline=False)
        respirar_na_agua_spell.add_field(name="Duração", value="24 horas", inline=False)

        return respirar_na_agua_spell
    def mover_terra():
        mover_terra_spell = discord.Embed(
            title="Mover Terra (Move Earth)",
            description=(
                "Você escolhe uma área de terreno composta por terra, areia ou argila que esteja dentro do alcance e tenha até 12 metros de lado. Você pode remodelar a área à vontade, escavando ou erguendo montes de terra.\n\n"
                "A mudança acontece gradualmente e leva o tempo de duração da magia. Este feitiço não afeta pedra, rocha ou terra sólida, apenas materiais mais maleáveis como solo e argila. Você pode criar trincheiras, aterros ou até mesmo remodelar terrenos para fins táticos ou construtivos."
            ),
            color=0x8B4513  # Cor marrom terra
        )
        mover_terra_spell.add_field(name="Conjuradores", value="Druida, Mago", inline=False)
        mover_terra_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mover_terra_spell.add_field(name="Alcance", value="36 metros", inline=False)
        mover_terra_spell.add_field(name="Componentes", value="V, S, M (um pequeno pedaço de casca de árvore)", inline=False)
        mover_terra_spell.add_field(name="Duração", value="Concentração, até 2 horas", inline=False)

        return mover_terra_spell
    def passos_longos():
        passos_longos_spell = discord.Embed(
            title="Passos Longos (Longstrider)",
            description=(
                "Você toca uma criatura e aumenta sua velocidade de movimento em 3 metros até o fim da duração. O alvo pode ser você mesmo ou outra criatura que você toque.\n\n"
                "A velocidade extra não requer concentração e permite ao alvo se mover mais rapidamente sem quaisquer penalidades. Além disso, você pode conjurar essa magia em níveis superiores para afetar criaturas adicionais."
            ),
            color=0x228B22  # Cor verde floresta
        )
        passos_longos_spell.add_field(name="Conjuradores", value="Bardo, Druida, Feiticeiro, Mago, Patrulheiro", inline=False)
        passos_longos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        passos_longos_spell.add_field(name="Alcance", value="Toque", inline=False)
        passos_longos_spell.add_field(name="Componentes", value="V, S, M (um pouco de terra)", inline=False)
        passos_longos_spell.add_field(name="Duração", value="1 hora", inline=False)

        return passos_longos_spell
    def metamorfose_verdadeira():
        metamorfose_verdadeira_spell = discord.Embed(
            title="Metamorfose Verdadeira (True Polymorph)",
            description=(
                "Você transforma uma criatura ou objeto que possa ver dentro do alcance em uma nova forma. Se você concentrar-se na magia por toda a sua duração, a transformação se torna permanente.\n\n"
                "- **Criatura em Criatura**: A nova forma pode ser de qualquer criatura, cujos Pontos de Vida sejam iguais ou inferiores ao alvo. A criatura assume as estatísticas e habilidades da nova forma.\n"
                "- **Objeto em Criatura**: Você pode transformar um objeto em uma criatura, desde que o objeto não seja mágico e a criatura tenha um CR (nível de desafio) igual ou inferior a 9.\n"
                "- **Criatura em Objeto**: A criatura transforma-se em um objeto de sua escolha e perde todas as suas estatísticas, tornando-se um objeto inerte."
            ),
            color=0x9400D3  # Cor roxa escura
        )
        metamorfose_verdadeira_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        metamorfose_verdadeira_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        metamorfose_verdadeira_spell.add_field(name="Alcance", value="9 metros", inline=False)
        metamorfose_verdadeira_spell.add_field(name="Componentes", value="V, S, M (um pouco de mercúrio, goma arábica e fumaça de incenso)", inline=False)
        metamorfose_verdadeira_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return metamorfose_verdadeira_spell
    def forma_eterea():
        forma_eterea_spell = discord.Embed(
            title="Forma Etérea (Etherealness)",
            description=(
                "Você entra no Plano Etéreo, no plano da fronteira, onde pode se mover através de objetos e criaturas no Plano Material. Enquanto estiver no Plano Etéreo, você é capaz de ver e ouvir o Plano Material, mas tudo parece esmaecido e distante.\n\n"
                "Você é incapaz de afetar ou ser afetado por qualquer coisa no Plano Material, exceto em locais que se sobreponham ao Plano Etéreo, como o espaço de uma criatura etérea."
            ),
            color=0x708090  # Cor cinza
        )
        forma_eterea_spell.add_field(name="Conjuradores", value="Bardo, Clérigo, Feiticeiro, Mago", inline=False)
        forma_eterea_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        forma_eterea_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        forma_eterea_spell.add_field(name="Componentes", value="V, S", inline=False)
        forma_eterea_spell.add_field(name="Duração", value="Até 8 horas", inline=False)

        return forma_eterea_spell
    def controlar_agua():
        controlar_agua_spell = discord.Embed(
            title="Controlar Água (Control Water)",
            description=(
                "Você pode controlar qualquer corpo de água dentro do alcance, criando um dos seguintes efeitos:\n\n"
                "- **Inundação**: Aumenta o nível da água em até 6 metros em uma área de 30 metros de lado.\n"
                "- **Redemoinho**: Cria um redemoinho em uma área de 9 metros de raio, sugando criaturas e objetos para o centro.\n"
                "- **Correnteza**: Muda o fluxo da água, redirecionando correntes em qualquer direção desejada.\n"
                "- **Parte as Águas**: Você cria uma fenda de até 30 metros de comprimento na água, abrindo espaço por onde criaturas podem passar."
            ),
            color=0x1E90FF  # Cor azul
        )
        controlar_agua_spell.add_field(name="Conjuradores", value="Clérigo, Druida, Feiticeiro, Mago", inline=False)
        controlar_agua_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        controlar_agua_spell.add_field(name="Alcance", value="90 metros", inline=False)
        controlar_agua_spell.add_field(name="Componentes", value="V, S, M (uma gota de água e um pouco de pó)", inline=False)
        controlar_agua_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return controlar_agua_spell
    def bordao_mistico():
        bordao_mistico_spell = discord.Embed(
            title="Bordão Místico (Shillelagh)",
            description=(
                "A madeira de um bastão ou clava que você está segurando é imbuída com poder da natureza. Pela duração da magia, você pode usar seu modificador de Sabedoria em vez de Força para ataques e danos com a arma, "
                "e o dano se torna 1d8. A arma também se torna mágica, se já não for."
            ),
            color=0x8B4513  # Cor marrom
        )
        bordao_mistico_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        bordao_mistico_spell.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        bordao_mistico_spell.add_field(name="Alcance", value="Toque", inline=False)
        bordao_mistico_spell.add_field(name="Componentes", value="V, S, M (um bastão ou clava)", inline=False)
        bordao_mistico_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return bordao_mistico_spell
    def consertar():
        consertar_spell = discord.Embed(
            title="Consertar (Mending)",
            description=(
                "Esta magia repara uma pequena quebra ou fenda em um objeto que você toque, como um elo de corrente partido, duas metades de uma chave quebrada ou uma capa rasgada. "
                "Desde que o rompimento ou fenda não exceda 30 centímetros em qualquer dimensão, você pode consertar o objeto, deixando a área de reparo com as marcas originais."
            ),
            color=0x4682B4  # Cor azul aço
        )
        consertar_spell.add_field(name="Conjuradores", value="Bardo, Druida, Feiticeiro, Mago, Clérigo", inline=False)
        consertar_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        consertar_spell.add_field(name="Alcance", value="Toque", inline=False)
        consertar_spell.add_field(name="Componentes", value="V, S, M (dois ímãs)", inline=False)
        consertar_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return consertar_spell
    def chicote_de_espinhos():
        chicote_de_espinhos_spell = discord.Embed(
            title="Chicote de Espinhos (Thorn Whip)",
            description=(
                "Você cria um longo chicote de espinhos, que causa 1d6 de dano perfurante quando atinge uma criatura dentro do alcance. Se o alvo for Grande ou menor, você pode puxá-lo até 3 metros em sua direção. "
                "O dano aumenta em níveis superiores: 2d6 no 5º nível, 3d6 no 11º e 4d6 no 17º."
            ),
            color=0x006400  # Cor verde escura
        )
        chicote_de_espinhos_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        chicote_de_espinhos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        chicote_de_espinhos_spell.add_field(name="Alcance", value="9 metros", inline=False)
        chicote_de_espinhos_spell.add_field(name="Componentes", value="V, S, M (um espinho)", inline=False)
        chicote_de_espinhos_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return chicote_de_espinhos_spell
    def druidismo():
        druidismo_spell = discord.Embed(
            title="Druidismo (Druidcraft)",
            description=(
                "Druidismo é uma magia simples, usada para realizar pequenos feitos naturais. Você cria um dos seguintes efeitos mágicos dentro do alcance:\n\n"
                "- Você cria um efeito que prediz o clima nas próximas 24 horas. O efeito se manifesta como um orbe sensorial: uma esfera clara para céu limpo, nuvens para nublado, chuva para tempestades e assim por diante.\n"
                "- Você faz uma flor desabrochar, uma folha brotar, ou um botão de flor abrir.\n"
                "- Você cria um efeito instantâneo e sensorial, como um leve som de animais, o perfume de uma flor, ou uma pequena rajada de vento.\n"
                "- Você instantaneamente acende ou apaga uma pequena chama, como uma vela, uma tocha ou uma fogueira."
            ),
            color=0x32CD32  # Cor verde claro
        )
        druidismo_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        druidismo_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        druidismo_spell.add_field(name="Alcance", value="9 metros", inline=False)
        druidismo_spell.add_field(name="Componentes", value="V, S", inline=False)
        druidismo_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return druidismo_spell
    def mensagem():
        mensagem_spell = discord.Embed(
            title="Mensagem (Message)",
            description=(
                "Você aponta para uma criatura dentro do alcance e sussurra uma mensagem. O alvo (e somente ele) pode ouvir a mensagem e pode responder em sussurros que apenas você pode ouvir.\n\n"
                "Você pode lançar essa magia através de objetos sólidos, se você souber o alvo está atrás deles. A magia não atravessa 1 metro de pedra, 2,5 centímetros de metal comum, uma folha de chumbo, ou 90 centímetros de madeira ou terra.\n"
                "A magia não precisa de linha de visão para funcionar, mas você deve estar familiarizado com a localização do alvo."
            ),
            color=0xFFD700  # Cor dourada
        )
        mensagem_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        mensagem_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mensagem_spell.add_field(name="Alcance", value="36 metros", inline=False)
        mensagem_spell.add_field(name="Componentes", value="V, S, M (um fio de cobre)", inline=False)
        mensagem_spell.add_field(name="Duração", value="1 rodada", inline=False)

        return mensagem_spell
    def prestidigitacao():
        prestidigitacao_spell = discord.Embed(
            title="Prestidigitação (Prestidigitation)",
            description=(
                "Esta magia é um pequeno truque mágico que aprendizes usam para praticar. Você cria um dos seguintes efeitos mágicos dentro do alcance:\n\n"
                "- Você cria um efeito sensorial inofensivo, como uma chuva de faíscas, uma baforada de vento, leves sons, ou um odor inofensivo.\n"
                "- Você instantaneamente acende ou apaga uma vela, uma tocha ou uma pequena fogueira.\n"
                "- Você instantaneamente limpa ou suja um objeto não maior que 30 centímetros cúbicos.\n"
                "- Você esfria, aquece ou tempera até 1 metro cúbico de material inanimado.\n"
                "- Você cria uma marca ou um símbolo colorido que aparece em um objeto ou superfície por 1 hora.\n"
                "- Você cria um pequeno item não mágico, como uma chave, um trinket, ou uma moeda falsa, que dura até o final de seu próximo turno."
            ),
            color=0xFF69B4  # Cor rosa
        )
        prestidigitacao_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        prestidigitacao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        prestidigitacao_spell.add_field(name="Alcance", value="3 metros", inline=False)
        prestidigitacao_spell.add_field(name="Componentes", value="V, S", inline=False)
        prestidigitacao_spell.add_field(name="Duração", value="Até 1 hora", inline=False)

        return prestidigitacao_spell
    def taumaturgia():
        taumaturgia_spell = discord.Embed(
            title="Taumaturgia (Thaumaturgy)",
            description=(
                "Você manifesta um pequeno milagre, criando um dos seguintes efeitos dentro do alcance:\n\n"
                "- Sua voz aumenta de volume, ficando até três vezes mais alta por até 1 minuto.\n"
                "- Você faz tremer o chão em um raio de 9 metros ao seu redor, por 1 minuto.\n"
                "- Você faz todas as chamas não-mágicas em um raio de 9 metros piscarem, aumentarem ou diminuírem de intensidade por 1 minuto.\n"
                "- Você abre ou fecha uma porta ou janela destrancada.\n"
                "- Você altera a cor de uma chama por 1 minuto.\n"
                "- Você cria um som instantâneo, como um trovão, um sussurro ou um rugido."
            ),
            color=0xFF4500  # Cor laranja
        )
        taumaturgia_spell.add_field(name="Conjuradores", value="Clérigo", inline=False)
        taumaturgia_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        taumaturgia_spell.add_field(name="Alcance", value="9 metros", inline=False)
        taumaturgia_spell.add_field(name="Componentes", value="V", inline=False)
        taumaturgia_spell.add_field(name="Duração", value="Até 1 minuto", inline=False)

        return taumaturgia_spell
    def bomfruto():
        bomfruto_spell = discord.Embed(
            title="Bomfruto (Goodberry)",
            description=(
                "Você imbui até 10 frutos com poder mágico. Uma criatura pode usar sua ação para comer um fruto e restaurar 1 ponto de vida. Consumir o fruto também oferece nutrição suficiente para um dia completo.\n\n"
                "Os frutos imbuídos por essa magia perdem sua potência após 24 horas."
            ),
            color=0x228B22  # Cor verde floresta
        )
        bomfruto_spell.add_field(name="Conjuradores", value="Druida, Patrulheiro", inline=False)
        bomfruto_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        bomfruto_spell.add_field(name="Alcance", value="Toque", inline=False)
        bomfruto_spell.add_field(name="Componentes", value="V, S, M (um ramo de visco)", inline=False)
        bomfruto_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return bomfruto_spell
    def bomfruto():
        bomfruto_spell = discord.Embed(
            title="Bomfruto (Goodberry)",
            description=(
                "Você imbui até 10 frutos com poder mágico. Uma criatura pode usar sua ação para comer um fruto e restaurar 1 ponto de vida. Consumir o fruto também oferece nutrição suficiente para um dia completo.\n\n"
                "Os frutos imbuídos por essa magia perdem sua potência após 24 horas."
            ),
            color=0x228B22  # Cor verde floresta
        )
        bomfruto_spell.add_field(name="Conjuradores", value="Druida, Patrulheiro", inline=False)
        bomfruto_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        bomfruto_spell.add_field(name="Alcance", value="Toque", inline=False)
        bomfruto_spell.add_field(name="Componentes", value="V, S, M (um ramo de visco)", inline=False)
        bomfruto_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return bomfruto_spell
    def criar_destruir_agua():
        criar_destruir_agua_spell = discord.Embed(
            title="Criar e Destruir Água (Create or Destroy Water)",
            description=(
                "Você pode criar ou destruir água.\n\n"
                "**Criar Água:** Você cria até 40 litros de água limpa em um recipiente dentro do alcance, ou faz a água cair em uma área aberta como chuva, enchendo um espaço de 9 metros cúbicos.\n\n"
                "**Destruir Água:** Você destrói até 40 litros de água em um recipiente dentro do alcance, ou faz desaparecer uma neblina em uma área de até 9 metros cúbicos."
            ),
            color=0x1E90FF  # Cor azul
        )
        criar_destruir_agua_spell.add_field(name="Conjuradores", value="Clérigo, Druida", inline=False)
        criar_destruir_agua_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        criar_destruir_agua_spell.add_field(name="Alcance", value="9 metros", inline=False)
        criar_destruir_agua_spell.add_field(name="Componentes", value="V, S, M (uma gota de água, ou um grão de areia)", inline=False)
        criar_destruir_agua_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return criar_destruir_agua_spell
    def purificar_alimentos():
        purificar_alimentos_spell = discord.Embed(
            title="Purificar Alimentos e Bebidas (Purify Food and Drink)",
            description=(
                "Todos os alimentos e bebidas não-mágicos em um raio de 1,5 metros ao seu redor são purificados e tornam-se seguros para consumo. Isso remove quaisquer venenos, toxinas ou outros elementos nocivos presentes."
            ),
            color=0xFFD700  # Cor dourada
        )
        purificar_alimentos_spell.add_field(name="Conjuradores", value="Clérigo, Druida", inline=False)
        purificar_alimentos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        purificar_alimentos_spell.add_field(name="Alcance", value="1,5 metros", inline=False)
        purificar_alimentos_spell.add_field(name="Componentes", value="V, S", inline=False)
        purificar_alimentos_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return purificar_alimentos_spell
    def queda_suave():
        queda_suave_spell = discord.Embed(
            title="Queda Suave (Feather Fall)",
            description=(
                "Escolha até cinco criaturas caindo dentro do alcance. A taxa de queda delas se reduz para 18 metros por rodada até o final da magia. Se uma criatura atingir o solo antes do feitiço terminar, "
                "ela não sofre dano de queda, pois aterrissa suavemente."
            ),
            color=0x87CEEB  # Cor azul claro
        )
        queda_suave_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        queda_suave_spell.add_field(name="Tempo de Conjuração", value="1 reação", inline=False)
        queda_suave_spell.add_field(name="Alcance", value="18 metros", inline=False)
        queda_suave_spell.add_field(name="Componentes", value="V, M (uma pena de pássaro)", inline=False)
        queda_suave_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return queda_suave_spell
    def recuo_acelerado():
        recuo_acelerado_spell = discord.Embed(
            title="Recuo Acelerado (Expeditious Retreat)",
            description=(
                "Esta magia permite que você se mova em grande velocidade. Ao lançar esta magia, você pode usar a ação de Correr (Dash) e, a cada um dos seus turnos subsequentes, pode usar a ação de Correr novamente como uma ação bônus."
            ),
            color=0xDC143C  # Cor vermelho escuro
        )
        recuo_acelerado_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        recuo_acelerado_spell.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        recuo_acelerado_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        recuo_acelerado_spell.add_field(name="Componentes", value="V, S", inline=False)
        recuo_acelerado_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return recuo_acelerado_spell
    def salto():
        salto_spell = discord.Embed(
            title="Salto (Jump)",
            description=(
                "Você toca uma criatura. A distância de salto dessa criatura é triplicada até o fim da duração da magia."
            ),
            color=0x32CD32  # Cor verde claro
        )
        salto_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago, Patrulheiro", inline=False)
        salto_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        salto_spell.add_field(name="Alcance", value="Toque", inline=False)
        salto_spell.add_field(name="Componentes", value="V, S, M (a perna traseira de um gafanhoto)", inline=False)
        salto_spell.add_field(name="Duração", value="1 minuto", inline=False)

        return salto_spell
    def arma_magica():
        arma_magica_spell = discord.Embed(
            title="Arma Mágica (Magic Weapon)",
            description=(
                "Você toca uma arma não mágica. Até o final da duração, essa arma se torna mágica e concede um bônus de +1 nas jogadas de ataque e dano.\n\n"
                "Quando conjurada usando um espaço de magia de 4º nível ou superior, o bônus aumenta para +2. Se conjurada com um espaço de magia de 6º nível ou superior, o bônus aumenta para +3."
            ),
            color=0x8A2BE2  # Cor roxa
        )
        arma_magica_spell.add_field(name="Conjuradores", value="Paladino", inline=False)
        arma_magica_spell.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        arma_magica_spell.add_field(name="Alcance", value="Toque", inline=False)
        arma_magica_spell.add_field(name="Componentes", value="V, S", inline=False)
        arma_magica_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return arma_magica_spell
    def arrombar():
        arrombar_spell = discord.Embed(
            title="Arrombar (Knock)",
            description=(
                "Escolha um objeto que você possa ver dentro do alcance. O objeto pode ser uma porta, baú ou qualquer outro objeto fechado mecanicamente. "
                "Um alvo que esteja trancado, fechado ou travado é destravado. Se o objeto tiver múltiplos mecanismos de bloqueio, apenas um deles é destravado.\n\n"
                "Se o objeto for trancado magicamente, a magia Arrombar suprime a magia por 10 minutos, durante os quais o objeto pode ser aberto e fechado normalmente."
            ),
            color=0xFF8C00  # Cor laranja escuro
        )
        arrombar_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        arrombar_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        arrombar_spell.add_field(name="Alcance", value="18 metros", inline=False)
        arrombar_spell.add_field(name="Componentes", value="V", inline=False)
        arrombar_spell.add_field(name="Duração", value="Instantânea", inline=False)
        return arrombar_spell
    def cordao_de_flechas():
        cordao_de_flechas_spell = discord.Embed(
            title="Cordão de Flechas (Cordón of Arrows)",
            description=(
                "Você planta até quatro flechas ou virotes no chão, imbuindo-os com magia. Quando uma criatura que não seja você ou seus aliados se mover dentro de 9 metros de uma das flechas pela primeira vez em um turno ou terminar seu turno lá, uma flecha voa em direção à criatura e faz um ataque à distância mágico contra ela.\n\n"
                "Você pode usar um espaço de magia de nível superior para criar duas flechas adicionais para cada nível acima do 2º."
            ),
            color=0x8B4513  # Cor marrom
        )
        cordao_de_flechas_spell.add_field(name="Conjuradores", value="Patrulheiro", inline=False)
        cordao_de_flechas_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        cordao_de_flechas_spell.add_field(name="Alcance", value="5 metros", inline=False)
        cordao_de_flechas_spell.add_field(name="Componentes", value="V, S, M (quatro flechas ou virotes)", inline=False)
        cordao_de_flechas_spell.add_field(name="Duração", value="8 horas", inline=False)

        return cordao_de_flechas_spell
    def crescer_espinhos():
        crescer_espinhos_spell = discord.Embed(
            title="Crescer Espinhos (Spike Growth)",
            description=(
                "O solo em uma área de raio de 6 metros centrado em um ponto que você escolher, dentro do alcance, fica coberto de espinhos e espigões por toda a duração. "
                "A área se torna terreno difícil, e qualquer criatura que se mova dentro dela sofre 2d4 de dano perfurante para cada 1,5 metros que percorrer.\n\n"
                "O disfarce natural dos espinhos faz com que qualquer criatura que não veja a área inicialmente tenha de fazer um teste de Sabedoria (Percepção) para notar o perigo antes de entrar na área."
            ),
            color=0x228B22  # Cor verde floresta
        )
        crescer_espinhos_spell.add_field(name="Conjuradores", value="Druida, Patrulheiro", inline=False)
        crescer_espinhos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        crescer_espinhos_spell.add_field(name="Alcance", value="45 metros", inline=False)
        crescer_espinhos_spell.add_field(name="Componentes", value="V, S, M (sete espinhos de uma planta)", inline=False)
        crescer_espinhos_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return crescer_espinhos_spell
    def esquentar_metal():
        esquentar_metal_spell = discord.Embed(
            title="Esquentar Metal (Heat Metal)",
            description=(
                "Escolha um objeto de metal, como uma arma ou uma peça de armadura, que você possa ver dentro do alcance. Você faz o metal brilhar com um calor intenso. "
                "Qualquer criatura em contato físico com o objeto sofre 2d8 de dano de fogo quando você conjura a magia. Até o feitiço acabar, você pode usar uma ação bônus a cada um dos seus turnos para fazer o dano de fogo se repetir.\n\n"
                "Se a criatura estiver segurando ou usando o objeto, ela deve ter sucesso em um teste de resistência de Constituição ou soltá-lo. Se não soltar, ela tem desvantagem nas jogadas de ataque e testes de habilidade até o início do seu próximo turno."
            ),
            color=0xB22222  # Cor vermelho fogo
        )
        esquentar_metal_spell.add_field(name="Conjuradores", value="Bardo, Druida", inline=False)
        esquentar_metal_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        esquentar_metal_spell.add_field(name="Alcance", value="18 metros", inline=False)
        esquentar_metal_spell.add_field(name="Componentes", value="V, S, M (um pedaço de ferro e uma chama)", inline=False)
        esquentar_metal_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return esquentar_metal_spell
    def levitacao():
        levitacao_spell = discord.Embed(
            title="Levitação (Levitate)",
            description=(
                "Um alvo à sua escolha que você possa ver dentro do alcance sobe verticalmente até 6 metros e permanece suspenso por toda a duração. "
                "O alvo pode ser uma criatura ou um objeto não preso que pese até 225 quilos.\n\n"
                "A criatura pode realizar um teste de resistência de Constituição para resistir ao efeito. Se a criatura for bem-sucedida, a magia não tem efeito. Enquanto levitando, o alvo pode se mover apenas empurrando ou puxando-se contra um objeto fixo próximo, como uma parede ou teto."
            ),
            color=0x8A2BE2  # Cor roxa
        )
        levitacao_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        levitacao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        levitacao_spell.add_field(name="Alcance", value="18 metros", inline=False)
        levitacao_spell.add_field(name="Componentes", value="V, S, M (um pequeno laço de couro)", inline=False)
        levitacao_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return levitacao_spell
    def patas_de_aranha():
        patas_de_aranha_spell = discord.Embed(
            title="Patas de Aranha (Spider Climb)",
            description=(
                "Até o fim da duração, uma criatura voluntária que você tocar ganha a habilidade de mover-se por superfícies verticais e de cabeça para baixo no teto, sem precisar fazer um teste de habilidade.\n\n"
                "Além disso, a criatura ganha uma velocidade de escalada igual à sua velocidade de caminhada."
            ),
            color=0x808080  # Cor cinza
        )
        patas_de_aranha_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        patas_de_aranha_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        patas_de_aranha_spell.add_field(name="Alcance", value="Toque", inline=False)
        patas_de_aranha_spell.add_field(name="Componentes", value="V, S, M (uma gota de betume e um aranha)", inline=False)
        patas_de_aranha_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return patas_de_aranha_spell
    def pele_de_arvore():
        pele_de_arvore_spell = discord.Embed(
            title="Pele de Árvore (Barkskin)",
            description=(
                "Você toca uma criatura voluntária e sua pele assume uma aparência áspera e cascuda. Pela duração da magia, a Classe de Armadura da criatura não pode ser menor que 16, independentemente da armadura que ela esteja usando."
            ),
            color=0x8B4513  # Cor marrom
        )
        pele_de_arvore_spell.add_field(name="Conjuradores", value="Druida, Patrulheiro", inline=False)
        pele_de_arvore_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        pele_de_arvore_spell.add_field(name="Alcance", value="Toque", inline=False)
        pele_de_arvore_spell.add_field(name="Componentes", value="V, S, M (um pedaço de casca de árvore)", inline=False)
        pele_de_arvore_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return pele_de_arvore_spell
    def truque_da_corda():
        truque_da_corda_spell = discord.Embed(
            title="Truque da Corda (Rope Trick)",
            description=(
                "Você toca uma corda que tem até 18 metros de comprimento. A corda se ergue no ar e permanece suspensa, permitindo que você e até oito criaturas que a toquem escalem por ela e entrem em um espaço extradimensional, onde as criaturas ficam escondidas."
                " O espaço extradimensional dura até o final da magia, e a corda permanece visível e acessível. No final da magia, qualquer criatura que ainda estiver no espaço extradimensional é ejetada dele."
            ),
            color=0xC0C0C0  # Cor prata
        )
        truque_da_corda_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        truque_da_corda_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        truque_da_corda_spell.add_field(name="Alcance", value="Toque", inline=False)
        truque_da_corda_spell.add_field(name="Componentes", value="V, S, M (uma corda de até 18 metros)", inline=False)
        truque_da_corda_spell.add_field(name="Duração", value="1 hora", inline=False)

        return truque_da_corda_spell
    def visao_no_escuro():
        visao_no_escuro_spell = discord.Embed(
            title="Visão no Escuro (Darkvision)",
            description=(
                "Você toca uma criatura voluntária e lhe concede a capacidade de ver no escuro. Pela duração da magia, a criatura ganha visão no escuro em um raio de 18 metros."
            ),
            color=0x696969  # Cor cinza escuro
        )
        visao_no_escuro_spell.add_field(name="Conjuradores", value="Druida, Feiticeiro, Mago, Patrulheiro", inline=False)
        visao_no_escuro_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        visao_no_escuro_spell.add_field(name="Alcance", value="Toque", inline=False)
        visao_no_escuro_spell.add_field(name="Componentes", value="V, S, M (um pedaço de carvão)", inline=False)
        visao_no_escuro_spell.add_field(name="Duração", value="8 horas", inline=False)

        return visao_no_escuro_spell
    def ampliar_plantas():
        ampliar_plantas_spell = discord.Embed(
            title="Ampliar Plantas (Plant Growth)",
            description=(
                "Esta magia canaliza vitalidade em plantas dentro de uma área específica. Você pode escolher um dos seguintes efeitos ao conjurar esta magia:\n\n"
                "- **Efeito Instantâneo:** Todas as plantas normais em um raio de 30 metros centrado em um ponto de sua escolha tornam-se supercrescidas. O terreno torna-se difícil, impedindo movimento fácil.\n\n"
                "- **Efeito Prolongado:** Você pode enriquecer o solo em um raio de 1,5 km. Durante o próximo ano, as colheitas na área são dobradas."
            ),
            color=0x228B22  # Cor verde floresta
        )
        ampliar_plantas_spell.add_field(name="Conjuradores", value="Bardo, Druida, Feiticeiro, Mago, Paladino", inline=False)
        ampliar_plantas_spell.add_field(name="Tempo de Conjuração", value="1 ação ou 8 horas", inline=False)
        ampliar_plantas_spell.add_field(name="Alcance", value="45 metros", inline=False)
        ampliar_plantas_spell.add_field(name="Componentes", value="V, S", inline=False)
        ampliar_plantas_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return ampliar_plantas_spell
    def andar_na_agua():
        andar_na_agua_spell = discord.Embed(
            title="Andar na Água (Water Walk)",
            description=(
                "Esta magia concede a até dez criaturas à sua escolha a capacidade de andar na superfície de líquidos como se fossem terreno sólido. Se um alvo afundar em um líquido por conta própria, ele flutua até a superfície no início de seu próximo turno. Se você afetar uma criatura submersa em um líquido, a magia ergue o alvo para a superfície do líquido a uma taxa de 18 metros por rodada."
            ),
            color=0x1E90FF  # Cor azul
        )
        andar_na_agua_spell.add_field(name="Conjuradores", value="Clérigo, Druida, Feiticeiro, Mago", inline=False)
        andar_na_agua_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        andar_na_agua_spell.add_field(name="Alcance", value="9 metros", inline=False)
        andar_na_agua_spell.add_field(name="Componentes", value="V, S, M (um pedaço de cortiça)", inline=False)
        andar_na_agua_spell.add_field(name="Duração", value="1 hora", inline=False)

        return andar_na_agua_spell
    def arma_elemental():
        arma_elemental_spell = discord.Embed(
            title="Arma Elemental (Elemental Weapon)",
            description=(
                "Você toca uma arma e imbuí-la com energia mágica. Escolha um dos seguintes tipos de dano: ácido, frio, fogo, eletricidade ou trovão. Pela duração da magia, a arma mágica ganha um bônus de +1 nas jogadas de ataque e causa 1d4 de dano adicional do tipo escolhido.\n\n"
                "Se você conjurar esta magia usando um espaço de magia de 5º nível ou superior, o bônus aumenta para +2."
            ),
            color=0xFFD700  # Cor dourada
        )
        arma_elemental_spell.add_field(name="Conjuradores", value="Paladino", inline=False)
        arma_elemental_spell.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        arma_elemental_spell.add_field(name="Alcance", value="Toque", inline=False)
        arma_elemental_spell.add_field(name="Componentes", value="V, S", inline=False)
        arma_elemental_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return arma_elemental_spell
    def flecha_relampejante():
        flecha_relampejante_spell = discord.Embed(
            title="Flecha Relampejante (Lightning Arrow)",
            description=(
                "Na próxima vez que você fizer um ataque à distância com uma arma durante a duração desta magia, a munição ou arma usada transforma-se em eletricidade. Faça o ataque como de costume. "
                "O alvo sofre 4d8 de dano elétrico em vez do dano normal, e cada criatura a até 3 metros do alvo deve realizar um teste de resistência de Destreza, sofrendo 2d8 de dano elétrico em uma falha, ou metade do dano em um sucesso."
            ),
            color=0x1E90FF  # Cor azul
        )
        flecha_relampejante_spell.add_field(name="Conjuradores", value="Patrulheiro", inline=False)
        flecha_relampejante_spell.add_field(name="Tempo de Conjuração", value="1 bônus", inline=False)
        flecha_relampejante_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        flecha_relampejante_spell.add_field(name="Componentes", value="V, S", inline=False)
        flecha_relampejante_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return flecha_relampejante_spell
    def lentidao():
        lentidao_spell = discord.Embed(
            title="Lentidão (Slow)",
            description=(
                "Você altera o tempo para até seis criaturas à sua escolha dentro de um raio de 12 metros. Cada alvo deve fazer um teste de resistência de Sabedoria; se falhar, seu movimento é reduzido pela metade, "
                "recebe uma penalidade de -2 na CA e testes de Destreza, e não pode usar reações. Além disso, em cada turno, a criatura pode realizar apenas uma ação ou uma ação bônus, mas não ambos."
            ),
            color=0x808080  # Cor cinza
        )
        lentidao_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        lentidao_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        lentidao_spell.add_field(name="Alcance", value="36 metros", inline=False)
        lentidao_spell.add_field(name="Componentes", value="V, S, M (um pouco de melaço)", inline=False)
        lentidao_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return lentidao_spell
    def mesclar_se_as_rochas():
        mesclar_se_as_rochas_spell = discord.Embed(
            title="Mesclar-se às Rochas (Meld into Stone)",
            description=(
                "Você se funde com uma rocha sólida grande o suficiente para conter seu corpo inteiro, junto com o equipamento que estiver carregando. Pela duração da magia, você permanece dentro da rocha, consciente de tudo ao seu redor, "
                "mas incapaz de ver ou agir. Você pode sair da rocha a qualquer momento como uma ação bônus."
            ),
            color=0xA9A9A9  # Cor cinza escuro
        )
        mesclar_se_as_rochas_spell.add_field(name="Conjuradores", value="Clérigo, Druida", inline=False)
        mesclar_se_as_rochas_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        mesclar_se_as_rochas_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        mesclar_se_as_rochas_spell.add_field(name="Componentes", value="V, S", inline=False)
        mesclar_se_as_rochas_spell.add_field(name="Duração", value="Concentração, até 8 horas", inline=False)

        return mesclar_se_as_rochas_spell
    def piscar():
        piscar_spell = discord.Embed(
            title="Piscar (Blink)",
            description=(
                "A magia faz com que você intermitentemente desapareça do plano material e reapareça no plano etéreo. No final de cada um dos seus turnos, role um d20. Com um resultado de 11 ou mais, você desaparece para o Plano Etéreo "
                "e retorna no início do seu próximo turno em um ponto à sua escolha a até 3 metros de onde desapareceu. Se não houver espaço, você reaparece no local mais próximo possível."
            ),
            color=0x4682B4  # Cor azul aço
        )
        piscar_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        piscar_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        piscar_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        piscar_spell.add_field(name="Componentes", value="V, S", inline=False)
        piscar_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return piscar_spell
    def voo():
        voo_spell = discord.Embed(
            title="Voo (Fly)",
            description=(
                "Você toca uma criatura e concede a ela a habilidade de voar com uma velocidade de 18 metros. Quando a magia termina, a criatura perde a habilidade de voar, a menos que esteja pairando sobre uma superfície segura, "
                "caindo se estiver no ar."
            ),
            color=0xADD8E6  # Cor azul clara
        )
        voo_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        voo_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        voo_spell.add_field(name="Alcance", value="Toque", inline=False)
        voo_spell.add_field(name="Componentes", value="V, S, M (uma pena de asa de pássaro)", inline=False)
        voo_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return voo_spell
    def fabricar():
        fabricar_spell = discord.Embed(
            title="Fabricar (Fabricate)",
            description=(
                "Você converte matérias-primas em produtos acabados. Escolha matéria-prima que você possa ver dentro do alcance, e você pode fabricar um objeto dela. O volume do material não pode exceder 3 metros cúbicos.\n\n"
                "Se estiver trabalhando com materiais minerais, como pedra ou metal, o volume máximo é reduzido para 1,5 metros cúbicos. Você deve ter o conhecimento necessário para fabricar o item desejado."
            ),
            color=0xB8860B  # Cor dourada escura
        )
        fabricar_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        fabricar_spell.add_field(name="Tempo de Conjuração", value="10 minutos", inline=False)
        fabricar_spell.add_field(name="Alcance", value="36 metros", inline=False)
        fabricar_spell.add_field(name="Componentes", value="V, S", inline=False)
        fabricar_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return fabricar_spell
    def inseto_gigante():
        inseto_gigante_spell = discord.Embed(
            title="Inseto Gigante (Giant Insect)",
            description=(
                "Você transforma até dez centopeias, três aranhas, cinco vespas ou uma escorpião dentro do alcance em suas formas gigantes por toda a duração. "
                "Cada criatura obedece a seus comandos verbais, e você pode se comunicar com elas telepaticamente. A magia termina para uma criatura se seus Pontos de Vida chegarem a 0.\n\n"
                "A critério do Mestre, outras criaturas semelhantes podem ser transformadas. Quando a magia termina, as criaturas retornam ao tamanho normal e não lembram de nada ocorrido enquanto estavam gigantes."
            ),
            color=0x006400  # Cor verde escuro
        )
        inseto_gigante_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        inseto_gigante_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        inseto_gigante_spell.add_field(name="Alcance", value="9 metros", inline=False)
        inseto_gigante_spell.add_field(name="Componentes", value="V, S", inline=False)
        inseto_gigante_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return inseto_gigante_spell
    def aljava_veloz():
        aljava_veloz_spell = discord.Embed(
            title="Aljava Veloz (Swift Quiver)",
            description=(
                "Você transforma sua aljava em um estoque mágico de munições. Pela duração da magia, sempre que você fizer um ataque com uma arma à distância, a arma cria automaticamente uma nova munição. "
                "Além disso, você pode usar uma ação bônus a cada turno para fazer dois ataques adicionais com uma arma à distância."
            ),
            color=0xFFD700  # Cor dourada
        )
        aljava_veloz_spell.add_field(name="Conjuradores", value="Bardo, Patrulheiro", inline=False)
        aljava_veloz_spell.add_field(name="Tempo de Conjuração", value="1 ação bônus", inline=False)
        aljava_veloz_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        aljava_veloz_spell.add_field(name="Componentes", value="V, S, M (uma aljava)", inline=False)
        aljava_veloz_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return aljava_veloz_spell
    def animar_objetos():
        animar_objetos_spell = discord.Embed(
            title="Animar Objetos (Animate Objects)",
            description=(
                "Você imbuí objetos inanimados com movimento e vida temporária. Escolha até dez objetos inanimados de tamanho Pequeno ou menor dentro do alcance. Eles se tornam criaturas animadas e obedecem aos seus comandos. "
                "Se você animar um objeto Grande, ele conta como dois objetos; um objeto Enorme conta como quatro objetos. Você pode controlar os objetos com uma ação bônus.\n\n"
                "Cada objeto animado tem uma quantidade específica de pontos de vida, Classe de Armadura e força de ataque, dependendo do tamanho."
            ),
            color=0xB22222  # Cor vermelha
        )
        animar_objetos_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        animar_objetos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        animar_objetos_spell.add_field(name="Alcance", value="36 metros", inline=False)
        animar_objetos_spell.add_field(name="Componentes", value="V, S", inline=False)
        animar_objetos_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return animar_objetos_spell
    def animar_objetos():
        animar_objetos_spell = discord.Embed(
            title="Animar Objetos (Animate Objects)",
            description=(
                "Você imbuí objetos inanimados com movimento e vida temporária. Escolha até dez objetos inanimados de tamanho Pequeno ou menor dentro do alcance. Eles se tornam criaturas animadas e obedecem aos seus comandos. "
                "Se você animar um objeto Grande, ele conta como dois objetos; um objeto Enorme conta como quatro objetos. Você pode controlar os objetos com uma ação bônus.\n\n"
                "Cada objeto animado tem uma quantidade específica de pontos de vida, Classe de Armadura e força de ataque, dependendo do tamanho."
            ),
            color=0xB22222  # Cor vermelha
        )
        animar_objetos_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro, Mago", inline=False)
        animar_objetos_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        animar_objetos_spell.add_field(name="Alcance", value="36 metros", inline=False)
        animar_objetos_spell.add_field(name="Componentes", value="V, S", inline=False)
        animar_objetos_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return animar_objetos_spell
    def criar_passagem():
        criar_passagem_spell = discord.Embed(
            title="Criar Passagem (Passwall)",
            description=(
                "Você cria uma passagem temporária através de uma parede ou superfície sólida que você possa ver dentro do alcance. A abertura pode ter até 6 metros de profundidade, 1,8 metros de largura e 3 metros de altura. "
                "Quando a magia termina, a passagem desaparece e quaisquer criaturas ou objetos ainda dentro são expulsos para o lado mais próximo da parede."
            ),
            color=0x696969  # Cor cinza escuro
        )
        criar_passagem_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        criar_passagem_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        criar_passagem_spell.add_field(name="Alcance", value="9 metros", inline=False)
        criar_passagem_spell.add_field(name="Componentes", value="V, S, M (um pequeno pedaço de madeira)", inline=False)
        criar_passagem_spell.add_field(name="Duração", value="1 hora", inline=False)

        return criar_passagem_spell
    def despertar():
        despertar_spell = discord.Embed(
            title="Despertar (Awaken)",
            description=(
                "Depois de gastar o tempo de lançamento da magia, você toca uma besta ou planta, conferindo-lhe inteligência. A criatura ou planta ganha um valor de Inteligência de 10 e a habilidade de falar uma língua conhecida por você. "
                "Se o alvo for uma planta, ele ganha a habilidade de se mover. O alvo fica amigável a você e obedece a seus comandos por 30 dias. Depois disso, ele age conforme sua própria vontade, dependendo de como foi tratado."
            ),
            color=0x32CD32  # Cor verde claro
        )
        despertar_spell.add_field(name="Conjuradores", value="Bardo, Druida", inline=False)
        despertar_spell.add_field(name="Tempo de Conjuração", value="8 horas", inline=False)
        despertar_spell.add_field(name="Alcance", value="Toque", inline=False)
        despertar_spell.add_field(name="Componentes", value="V, S, M (um pouco de alimento, um graveto e 1000 PO de diamantes)", inline=False)
        despertar_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return despertar_spell
    def reencarnacao():
        reencarnacao_spell = discord.Embed(
            title="Reencarnação (Reincarnate)",
            description=(
                "Você toca um cadáver ou parte de um cadáver morto dentro de 10 dias e faz com que o espírito do falecido retorne a um novo corpo vivo. O novo corpo é criado aleatoriamente e pode pertencer a qualquer uma das raças humanoides. "
                "Se o espírito estiver disposto e não tiver sido impedido de retornar, ele habita o novo corpo e recomeça sua vida. O novo corpo é jovem e saudável, mas o espírito mantém todas as memórias e habilidades que tinha anteriormente."
            ),
            color=0x8B0000  # Cor vermelho escuro
        )
        reencarnacao_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        reencarnacao_spell.add_field(name="Tempo de Conjuração", value="1 hora", inline=False)
        reencarnacao_spell.add_field(name="Alcance", value="Toque", inline=False)
        reencarnacao_spell.add_field(name="Componentes", value="V, S, M (1000 PO de pó de jade e rubis)", inline=False)
        reencarnacao_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return reencarnacao_spell
    def telecinesia():
        telecinesia_spell = discord.Embed(
            title="Telecinesia (Telekinesis)",
            description=(
                "Você ganha a habilidade de mover ou manipular criaturas e objetos à distância, usando sua mente. Quando você conjura a magia, e como sua ação a cada turno, você pode usar sua vontade para tentar mover uma criatura ou objeto à sua escolha que você possa ver dentro do alcance.\n\n"
                "**Criaturas:** Faça um teste de habilidade com seu modificador de conjuração, contestado por um teste de resistência de Força da criatura. Se você vencer o teste, pode mover a criatura até 9 metros em qualquer direção, incluindo para o ar.\n\n"
                "**Objetos:** Você pode mover um objeto que pese até 500 quilos. Se o objeto não estiver sendo usado ou carregado por outra criatura, ele se move automaticamente até 9 metros."
            ),
            color=0x4682B4  # Cor azul aço
        )
        telecinesia_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        telecinesia_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        telecinesia_spell.add_field(name="Alcance", value="18 metros", inline=False)
        telecinesia_spell.add_field(name="Componentes", value="V, S", inline=False)
        telecinesia_spell.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)

        return telecinesia_spell
    def caminhar_no_vento():
        caminhar_no_vento_spell = discord.Embed(
            title="Caminhar no Vento (Wind Walk)",
            description=(
                "Você e até dez criaturas voluntárias que você possa ver dentro do alcance assumem uma forma gasosa e podem voar a uma velocidade de 90 metros. Enquanto estiver nesta forma, as criaturas só podem realizar ações limitadas. "
                "Elas podem passar por fendas e fendas estreitas e são resistentes a danos não mágicos, mas não podem atacar, conjurar magias ou interagir fisicamente com objetos.\n\n"
                "A transformação leva 1 minuto para acontecer e pode ser revertida a qualquer momento, gastando 1 minuto novamente."
            ),
            color=0x87CEEB  # Cor azul claro
        )
        caminhar_no_vento_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        caminhar_no_vento_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        caminhar_no_vento_spell.add_field(name="Alcance", value="9 metros", inline=False)
        caminhar_no_vento_spell.add_field(name="Componentes", value="V, S, M (fogo e água)", inline=False)
        caminhar_no_vento_spell.add_field(name="Duração", value="8 horas", inline=False)

        return caminhar_no_vento_spell
    def carne_para_pedra():
        carne_para_pedra_spell = discord.Embed(
            title="Carne para Pedra (Flesh to Stone)",
            description=(
                "Você tenta transformar uma criatura que possa ver dentro do alcance em pedra. A criatura deve fazer um teste de resistência de Constituição. Se falhar, ela começa a transformar-se em pedra e fica **restrita**. "
                "Ela deve repetir o teste de resistência no final de cada turno. Se falhar três vezes, a criatura transforma-se completamente em pedra e fica **petrificada** permanentemente. Se for bem-sucedida no teste três vezes, a magia termina."
            ),
            color=0x808080  # Cor cinza
        )
        carne_para_pedra_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        carne_para_pedra_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        carne_para_pedra_spell.add_field(name="Alcance", value="18 metros", inline=False)
        carne_para_pedra_spell.add_field(name="Componentes", value="V, S, M (um pouco de cal e água)", inline=False)
        carne_para_pedra_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return carne_para_pedra_spell
    def desintegrar():
        desintegrar_spell = discord.Embed(
            title="Desintegrar (Disintegrate)",
            description=(
                "Um alvo que você possa ver dentro do alcance deve fazer um teste de resistência de Destreza. Se falhar, o alvo sofre 10d6 + 40 de dano de força. Se esse dano reduzir o alvo a 0 pontos de vida, ele é completamente desintegrado, deixando para trás apenas suas roupas, equipamentos e armas.\n\n"
                "Objetos não mágicos grandes também podem ser desintegrados instantaneamente. Se a magia for usada contra uma criação mágica, ela deve fazer um teste de resistência de Constituição ou ser desintegrada."
            ),
            color=0xFF4500  # Cor laranja fogo
        )
        desintegrar_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        desintegrar_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        desintegrar_spell.add_field(name="Alcance", value="18 metros", inline=False)
        desintegrar_spell.add_field(name="Componentes", value="V, S, M (um pouco de pó de jade)", inline=False)
        desintegrar_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return desintegrar_spell
    def inverter_a_gravidade():
        inverter_a_gravidade_spell = discord.Embed(
            title="Inverter a Gravidade (Reverse Gravity)",
            description=(
                "Esta magia inverte a gravidade em uma área cilíndrica de até 30 metros de raio e 30 metros de altura, centrada em um ponto que você possa ver. Todas as criaturas e objetos na área sobem até o topo do cilindro, a menos que estejam ancorados a algo.\n\n"
                "No final da magia, as criaturas e objetos caem novamente. Qualquer criatura que atingir o chão ao cair deve fazer um teste de resistência de Destreza para reduzir o dano de queda pela metade."
            ),
            color=0xFFD700  # Cor dourada
        )
        inverter_a_gravidade_spell.add_field(name="Conjuradores", value="Druida, Feiticeiro, Mago", inline=False)
        inverter_a_gravidade_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        inverter_a_gravidade_spell.add_field(name="Alcance", value="30 metros", inline=False)
        inverter_a_gravidade_spell.add_field(name="Componentes", value="V, S, M (um pouco de magnetita)", inline=False)
        inverter_a_gravidade_spell.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)

        return inverter_a_gravidade_spell
    def isolamento():
        isolamento_spell = discord.Embed(
            title="Isolamento (Sequester)",
            description=(
                "Você torna uma criatura ou objeto completamente indetectável enquanto estiver sob os efeitos desta magia. A criatura ou objeto é invisível, indetectável por magias de adivinhação e não pode ser localizado por meios mágicos. "
                "A criatura pode também ser colocada em um estado de animação suspensa, o que interrompe a passagem do tempo para ela enquanto estiver sob efeito da magia."
            ),
            color=0x2F4F4F  # Cor verde musgo escuro
        )
        isolamento_spell.add_field(name="Conjuradores", value="Mago", inline=False)
        isolamento_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        isolamento_spell.add_field(name="Alcance", value="Toque", inline=False)
        isolamento_spell.add_field(name="Componentes", value="V, S, M (um pequeno rubi no valor de pelo menos 1000 PO)", inline=False)
        isolamento_spell.add_field(name="Duração", value="Até ser dissolvido", inline=False)

        return isolamento_spell
    def regeneracao():
        regeneracao_spell = discord.Embed(
            title="Regeneração (Regenerate)",
            description=(
                "Você toca uma criatura e estimula seus poderes naturais de cura. Pela duração da magia, a criatura regenera 4d8 + 15 pontos de vida imediatamente e, em seguida, recupera 1 ponto de vida a cada minuto enquanto a magia durar.\n\n"
                "A magia também regenera membros perdidos. Se o alvo perdeu um membro, um novo membro se regenera após 2 minutos."
            ),
            color=0x228B22  # Cor verde floresta
        )
        regeneracao_spell.add_field(name="Conjuradores", value="Clérigo, Druida", inline=False)
        regeneracao_spell.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        regeneracao_spell.add_field(name="Alcance", value="Toque", inline=False)
        regeneracao_spell.add_field(name="Componentes", value="V, S, M (uma gota de sangue e um graveto)", inline=False)
        regeneracao_spell.add_field(name="Duração", value="1 hora", inline=False)

        return regeneracao_spell
    def controlar_o_clima():
        controlar_o_clima_spell = discord.Embed(
            title="Controlar o Clima (Control Weather)",
            description=(
                "Você altera o clima em uma área ao ar livre de até 8 quilômetros de diâmetro, centrada em um ponto que você possa ver. Você pode alterar as condições climáticas atuais, como temperatura, precipitação e direção do vento, ajustando-as gradualmente ao longo de 10 minutos.\n\n"
                "O clima muda lentamente durante o período da magia, e as novas condições persistem até o fim da magia ou até você decidir mudá-las novamente."
            ),
            color=0x4682B4  # Cor azul aço
        )
        controlar_o_clima_spell.add_field(name="Conjuradores", value="Clérigo, Druida, Mago", inline=False)
        controlar_o_clima_spell.add_field(name="Tempo de Conjuração", value="10 minutos", inline=False)
        controlar_o_clima_spell.add_field(name="Alcance", value="8 quilômetros", inline=False)
        controlar_o_clima_spell.add_field(name="Componentes", value="V, S, M (sementes ou pólen)", inline=False)
        controlar_o_clima_spell.add_field(name="Duração", value="Concentração, até 8 horas", inline=False)

        return controlar_o_clima_spell
    def forma_animais():
        forma_animais_spell = discord.Embed(
            title="Forma de Animais (Animal Shapes)",
            description=(
                "Você transforma criaturas voluntárias que possa ver dentro do alcance em formas de animais. Cada criatura assume a forma de uma besta de tamanho Médio ou menor. "
                "Cada criatura retém sua mente, mas ganha as estatísticas físicas da nova forma, incluindo seus Pontos de Vida, Classe de Armadura e habilidades.\n\n"
                "As criaturas podem continuar se transformando em diferentes formas de bestas enquanto a magia durar, cada transformação requer sua ação."
            ),
            color=0x8B4513  # Cor marrom
        )
        forma_animais_spell.add_field(name="Conjuradores", value="Druida", inline=False)
        forma_animais_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        forma_animais_spell.add_field(name="Alcance", value="9 metros", inline=False)
        forma_animais_spell.add_field(name="Componentes", value="V, S", inline=False)
        forma_animais_spell.add_field(name="Duração", value="Concentração, até 24 horas", inline=False)

        return forma_animais_spell
    def loquacidade():
        loquacidade_spell = discord.Embed(
            title="Loquacidade (Glibness)",
            description=(
                "Até o fim da magia, toda vez que você fizer um teste de Carisma (Enganação) ou Carisma (Persuasão), você pode substituir qualquer rolagem menor que 15 por um 15. "
                "Além disso, você é incapaz de ser detectado por magias de verdade ou efeitos semelhantes enquanto estiver mentindo."
            ),
            color=0xFF69B4  # Cor rosa
        )
        loquacidade_spell.add_field(name="Conjuradores", value="Bardo, Feiticeiro", inline=False)
        loquacidade_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        loquacidade_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        loquacidade_spell.add_field(name="Componentes", value="V", inline=False)
        loquacidade_spell.add_field(name="Duração", value="1 hora", inline=False)

        return loquacidade_spell
    def alterar_forma():
        alterar_forma_spell = discord.Embed(
            title="Alterar Forma (Shapechange, 9º nível)",
            description=(
                "Você assume a forma de uma criatura diferente. A nova forma pode ser de qualquer criatura cuja categoria de tamanho seja igual à sua ou uma categoria maior, e que tenha um nível de desafio igual ou inferior ao seu.\n\n"
                "Você ganha as estatísticas da criatura que assume, exceto por seu valor de Inteligência, Sabedoria e Carisma, que permanecem os mesmos. Você também mantém todas as suas habilidades de classe, raça e nível."
            ),
            color=0x9400D3  # Cor roxa
        )
        alterar_forma_spell.add_field(name="Conjuradores", value="Druida, Feiticeiro, Mago", inline=False)
        alterar_forma_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        alterar_forma_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        alterar_forma_spell.add_field(name="Componentes", value="V, S, M (um pedaço de uma criatura que você quer se transformar)", inline=False)
        alterar_forma_spell.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)

        return alterar_forma_spell
    def parar_o_tempo():
        parar_o_tempo_spell = discord.Embed(
            title="Parar o Tempo (Time Stop)",
            description=(
                "Você brevemente detém o fluxo do tempo para todos, exceto para você. Você pode realizar até 1d4 + 1 turnos consecutivos enquanto o tempo está parado. Durante esses turnos, você é indetectável aos outros e pode se mover e agir livremente, "
                "contanto que não faça nenhum ataque ou ação direta que afete outra criatura ou objeto.\n\n"
                "Se você afetar diretamente outra criatura ou objeto, a magia termina imediatamente."
            ),
            color=0x1E90FF  # Cor azul
        )
        parar_o_tempo_spell.add_field(name="Conjuradores", value="Feiticeiro, Mago", inline=False)
        parar_o_tempo_spell.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        parar_o_tempo_spell.add_field(name="Alcance", value="Pessoal", inline=False)
        parar_o_tempo_spell.add_field(name="Componentes", value="V", inline=False)
        parar_o_tempo_spell.add_field(name="Duração", value="Instantânea", inline=False)

        return parar_o_tempo_spell











