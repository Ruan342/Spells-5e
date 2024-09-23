import discord

# Adivinhação
class Adivinhação:
    def __init__(self):
        pass
    def TrueStrike():
        # atribui uma variável ao embed criado
        true_strike = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Ataque Certeiro (True Strike)',
            # Descrição do efeito da magia
            description='Você estende sua mão e aponta o dedo para um alvo no alcance. Sua magia garante a você uma breve intuição sobre as defesas do alvo. No seu próximo turno, você terá vantagem na primeira jogada de ataque contra o alvo, considerando que essa magia não tenha acabado.',
            color=0xA020F0

        ) 
        # Tempo de conjuração da Magia 
        true_strike.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        true_strike.add_field(name='Alcance', value='30 pés', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        true_strike.add_field(name='Componentes', value='S', inline=False)
        # Duração da magia 
        true_strike.add_field(name='Duração', value='Concentração, até 1 rodada', inline=False)  
        # o return vai retornar a variável com o embed criado
        return true_strike
    def Guidance():
    # Atribui uma variável ao embed criado
        guidance = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Orientação (Guidance)',
            # Descrição do efeito da magia
            description='Você toca uma criatura voluntária. Uma vez, antes da magia acabar, o alvo pode rolar um d4 e adicionar o número rolado a um teste de habilidade a escolha dele. Ele pode rolar o dado antes ou depois de realizar o teste de habilidade. Após isso, a magia termina.',
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        guidance.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        guidance.add_field(name='Alcance', value='Toque', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        guidance.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia 
        guidance.add_field(name='Duração', value='Concentração, até 1 minuto', inline=False)  
        # O return vai retornar a variável com o embed criado
        return guidance
    def ComprehendLanguages():
    # Atribui uma variável ao embed criado
        comprehend_languages = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Compreender Idiomas (Comprehend Languages)',
            # Descrição do efeito da magia
            description='Pela duração, você compreende o significado literal de qualquer idioma falado que você ouvir. Você também compreende qualquer idioma escrito que vir, mas você deve tocar a superfície onde as palavras estão escritas. Leva, aproximadamente, 1 minuto para ler uma página de texto.\n\nEssa magia não decifra mensagens secretas em textos ou glifos, como um selo arcano, que não seja parte de um idioma escrito.',
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        comprehend_languages.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        comprehend_languages.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        comprehend_languages.add_field(name='Componentes', value='V S M (um pitada de fuligem e sal)', inline=False)
        # Duração da magia 
        comprehend_languages.add_field(name='Duração', value='1 hora', inline=False)  
        # O return vai retornar a variável com o embed criado
        return comprehend_languages
    def DetectMagic():
    # Atribui uma variável ao embed criado
        detect_magic = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Detectar Magia (Detect Magic)',
            # Descrição do efeito da magia
            description='Pela duração, você sente a presença de magia a até 9 metros [30 feet] de você. Se você sentir magia dessa forma, você pode usar sua ação para ver uma aura suave em volta de qualquer criatura ou objeto visível, na área que carrega magia, e você descobre a escola de magia, se houver uma.\n\nA magia pode penetrar a maioria das barreiras, mas é bloqueada por 30 centímetros [1 foot] de rocha, 2,5 centímetros [1 inch] de metal comum, uma fina camada de chumbo, ou 90 centímetros [3 feet] de madeira ou terra.',
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        detect_magic.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        detect_magic.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        detect_magic.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia 
        detect_magic.add_field(name='Duração', value='Concentração, até 10 minutos', inline=False)  
        # O return vai retornar a variável com o embed criado
        return detect_magic
    def DetectEvilAndGood():
    # Atribui uma variável ao embed criado
        detect_evil_good = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Detectar o Bem e Mal (Detect Evil and Good)',
            # Descrição do efeito da magia
            description='Pela duração, você sabe se existe uma aberração, celestial, corruptor, elemental, fada ou morto-vivo, a até 9 metros [30 feet] de você, assim como onde a criatura está localizada. Similarmente, você sabe se existe um local ou objeto, a até 9 metros [30 feet] de você, que tenha sido consagrado ou profanado magicamente.\n\nA magia pode penetrar a maioria das barreiras, mas é bloqueada por 30 centímetros [1 foot] de rocha, 2,5 centímetros [1 inch] de metal comum, uma fina camada de chumbo, ou 90 centímetros [3 feet] de madeira ou terra.',
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        detect_evil_good.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        detect_evil_good.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        detect_evil_good.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia 
        detect_evil_good.add_field(name='Duração', value='Concentração, até 10 minutos', inline=False)  
        # O return vai retornar a variável com o embed criado
        return detect_evil_good
    def DetectPoisonAndDisease():
    # Atribui uma variável ao embed criado
        detect_poison_disease = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Detectar Veneno e Doença (Detect Poison and Disease)',
            # Descrição do efeito da magia
            description='Pela duração, você sente a presença e localização de venenos, criaturas venenosas e doenças a até 9 metros [30 feet] de você. Você também identifica o tipo de veneno, criatura venenosa ou doença em cada caso.\n\nA magia pode penetrar a maioria das barreiras, mas é bloqueada por 30 centímetros [1 foot] de rocha, 2,5 centímetros [1 inch] de metal comum, uma fina camada de chumbo, ou 90 centímetros [3 feet] de madeira ou terra.',
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        detect_poison_disease.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        detect_poison_disease.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        detect_poison_disease.add_field(name='Componentes', value='V S M (uma folha de teixo)', inline=False)
        # Duração da magia 
        detect_poison_disease.add_field(name='Duração', value='Concentração, até 10 minutos', inline=False)  
        # O return vai retornar a variável com o embed criado
        return detect_poison_disease
    def SpeakWithAnimals():
    # Atribui uma variável ao embed criado
        speak_with_animals = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title='Falar Com Animais (Speak With Animals)',
            # Descrição do efeito da magia
            description='Você adquire a habilidade de compreender e se comunicar verbalmente com bestas, pela duração. O conhecimento e consciência de muitas bestas é limitado pela inteligência delas, mas, no mínimo, as bestas poderão dar informações a você sobre os locais e monstros próximos, incluindo tudo que eles possam perceber ou tenham percebido no dia anterior. Você pode tentar persuadir uma besta a lhe prestar um favor, à critério do Mestre.',
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        speak_with_animals.add_field(name='Tempo de Conjuração', value='1 ação', inline=False)
        # Alcance da Magia 
        speak_with_animals.add_field(name='Alcance', value='Pessoal', inline=False)
        # Componentes da Magia (Se tiver Materiais)
        speak_with_animals.add_field(name='Componentes', value='V S', inline=False)
        # Duração da magia 
        speak_with_animals.add_field(name='Duração', value='10 minutos', inline=False)  
        # O return vai retornar a variável com o embed criado
        return speak_with_animals
    def HuntersMark():
    # Atribui uma variável ao embed criado
        hunters_mark = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Marca do Caçador (Hunter's Mark)",
            # Descrição do efeito da magia
            description="Você escolhe uma criatura que possa ver, dentro do alcance e a marca misticamente como sua presa. Até a magia acabar, você causa 1d6 de dano extra ao alvo sempre que você o atingir com um ataque com arma e você tem vantagem em quaisquer testes de Sabedoria (Percepção) ou Sabedoria (Sobrevivência) feitos para encontrá-la. Se o alvo cair a 0 pontos de vida antes da magia acabar, você pode usar uma ação bônus, no seu turno subsequente para marcar uma nova criatura.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        hunters_mark.add_field(name="Tempo de Conjuração", value="1 ação bonus", inline=False)
        # Alcance da Magia 
        hunters_mark.add_field(name="Alcance", value="90 pés", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        hunters_mark.add_field(name="Componentes", value="V", inline=False)
        # Duração da magia 
        hunters_mark.add_field(name="Duração", value="Concentração, até 1 hora", inline=False)
        # Efeitos em Níveis Superiores, se aplicável
        hunters_mark.add_field(name="Em Níveis Superiores", value="Quando você conjurar essa magia usando um espaço de magia de 3° ou 4° nível, você poderá manter sua concentração na magia por até 8 horas. Quando você usar um espaço de magia de 5° nível ou superior, você poderá manter sua concentração na magia por até 24 horas.", inline=False)
        # O return vai retornar a variável com o embed criado
        return hunters_mark
    def Augury():
    # Atribui uma variável ao embed criado
        augury = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Augúrio (Augury)",
            # Descrição do efeito da magia
            description="Ao lançar varetas cravejados com gemas, rolar ossos de dragão, puxar cartas ornamentadas ou usar outro tipo de ferramenta de adivinhação, você recebe um presságio de uma entidade de outro mundo, sobre os resultados de cursos de ação específicos que você planeja tomar nos próximos 30 minutos. O Mestre escolhe dentre os possíveis presságios a seguir:\n• Êxito, para resultados bons\n• Fracasso, para resultados maus\n• Êxito e fracasso, para resultados bons e maus\n• Nada, para resultados que não são especialmente bons ou ruins.\nA magia não leva em conta qualquer possível circunstancia que possa mudar o resultado, como a conjuração de magias adicionais ou a perda ou ganho de um companheiro.\nSe você conjurar a magia duas ou mais vezes antes de completar seu próximo descanso longo, existe uma chance cumulativa de 25 por cento de cada conjuração, depois da primeira que você fez, ter um resultado aleatório. O Mestre faz essa jogada secretamente.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        augury.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        # Alcance da Magia 
        augury.add_field(name="Alcance", value="Pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        augury.add_field(name="Componentes", value="V S M (varetas, ossos ou objetos similares especialmente marcados valendo, no mínimo, 25 gp)", inline=False)
        # Duração da magia 
        augury.add_field(name="Duração", value="Instantâneo", inline=False)
        # O return vai retornar a variável com o embed criado
        return augury
    def Detectar_Pensamentos():
    # Atribui uma variável ao embed criado
        detectar_pensamentos = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Detectar Pensamentos (Detect Thoughts)",
            # Descrição do efeito da magia
            description="Pela duração, você pode ler os pensamentos de certas criaturas. Quando você conjura essa magia e, com sua ação a cada turno até o fim da magia, você pode focar sua mente em qualquer criatura que você puder ver a até 9 metros [30 feet] de você. Se a criatura escolhida possuir Inteligência 3 ou inferior ou não falar nenhum tipo de idioma, a criatura não poderá ser afetada.\n\nVocê, inicialmente, descobre os pensamentos superficiais da criatura – o que está mais presente na sua mente no momento. Com uma ação, você pode tanto mudar sua atenção para os pensamentos de outra criatura, como tentar sondar mais profundamente na mente da mesma criatura. Se você resolver sondar profundamente, a criatura deve realizar um teste de resistência de Sabedoria. Se falhar, você ganha ciência do seu raciocínio (se possuir), seu estado emocional e algo que tome grande parte da sua mente (como algo que ele se preocupe, amores ou ódios). Se ele for bem sucedido, a magia termina. Em ambas situações, o alvo saberá que você está sondando a mente dele e, a não ser que você mude sua atenção para os pensamentos de outra criatura, a criatura pode usar a ação dela, no turno dela, para realizar um teste de Inteligência resistido por seu teste de Inteligência; se ela for bem sucedida, a magia termina.\n\nPerguntas feitas diretamente para a criatura alvo, normalmente moldarão o curso dos seus pensamentos, portanto, essa magia é particularmente eficiente como parte de um interrogatório.\n\nVocê pode, também, usar essa magia para detectar a presença que criaturas pensantes que você não possa ver. Quando você conjura essa magia ou, com sua ação enquanto ela durar, você pode procurar por pensamentos a até 9 metros [30 feet] de você. A magia pode penetrar a maioria das barreiras, mas é bloqueada por 30 centímetros [1 foot] de rocha, 2,5 centímetros [1 inch] de metal comum, uma fina camada de chumbo, ou 90 centímetros [3 feet] de madeira ou terra. Você não pode detectar uma criatura com Inteligência 3 ou inferior ou uma que não fale qualquer idioma.\n\nUma vez que você tenha detectado a presença de uma criatura dessa forma, você pode ler os pensamentos dela pelo resto da duração, como descrito acima, mesmo que você não possa vê-la, mas ela ainda precisa estar dentro do alcance.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        detectar_pensamentos.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        detectar_pensamentos.add_field(name="Alcance", value="Pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        detectar_pensamentos.add_field(name="Componentes", value="V S M (um pedaço de cobre)", inline=False)
        # Duração da magia 
        detectar_pensamentos.add_field(name="Duração", value="Concentração, até 1 minuto", inline=False)
        # O return vai retornar a variável com o embed criado
        return detectar_pensamentos
    def Encontrar_Armadilhas():
    # Atribui uma variável ao embed criado
        encontrar_armadilhas = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Encontrar Armadilhas (Find Traps)",
            # Descrição do efeito da magia
            description="Você sente a presença de qualquer armadilha dentro do alcance a qual você tenha linha de visão. Uma armadilha, para os propósitos dessa magia, inclui qualquer coisa que possa causar um efeito repentino ou inesperado em você, considerado nocivo ou indesejável, que foi especificamente planejado para ser por seu criador. Portanto, a magia sentirá a área afetada pela magia alarme, um glifo de vigilância ou uma armadilha mecânica de fosso, mas ela não revelará uma fragilidade natural no piso, um teto instável ou um sumidouro escondido.\n\nEssa magia apenas revela que existe uma magia presente. Você não descobre a localização de cada armadilha, mas você também descobre a natureza genérica do perigo representando pela armadilha que você sentiu.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        encontrar_armadilhas.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        encontrar_armadilhas.add_field(name="Alcance", value="120 pés", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        encontrar_armadilhas.add_field(name="Componentes", value="V S", inline=False)
        # Duração da magia 
        encontrar_armadilhas.add_field(name="Duração", value="Instantâneo", inline=False)
        # O return vai retornar a variável com o embed criado
        return encontrar_armadilhas
    def Localizar_Animais_Ou_Plantas():
    # Atribui uma variável ao embed criado
        localizar_animais_ou_plantas = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Localizar Animais Ou Plantas (Locate Animals Or Plants)",
            # Descrição do efeito da magia
            description="Descreva ou nomeie um tipo específico de besta ou planta. Concentre-se na voz da natureza ao seu redor, você descobre a direção e distância da criatura ou planta mais próxima desse tipo dentro de 7,5 quilômetros [5 miles], se houver alguma presente.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        localizar_animais_ou_plantas.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        localizar_animais_ou_plantas.add_field(name="Alcance", value="Pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        localizar_animais_ou_plantas.add_field(name="Componentes", value="V S M (um pouco de pelo de um cão de caça)", inline=False)
        # Duração da magia 
        localizar_animais_ou_plantas.add_field(name="Duração", value="Instantâneo", inline=False)
        # O return vai retornar a variável com o embed criado
        return localizar_animais_ou_plantas
    def Localizar_Objeto():
    # Atribui uma variável ao embed criado
        localizar_objeto = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Localizar Objeto (Locate Object)",
            # Descrição do efeito da magia
            description="Descreva ou nomeie um objeto que seja familiar a você. Você sente a direção da localização do objeto, contanto que o objeto esteja a até 300 metros de você. Se o objeto estiver em movimento, você saberá a direção do movimento dele.\n\nA magia pode localizar um objeto especifico que você, desde que você já tenha o visto de perto – a até 9 metros [30 feet] – pelo menos uma vez. Alternativamente, a magia pode localizar o objeto de um tipo em particular mais próximo, como certo tipo de vestuário, joia, móvel, ferramenta ou arma.\n\nEssa magia não pode localizar um objeto se qualquer espessura de chumbo, até mesmo uma folha fina, bloquear o caminho direto entre você e o objeto.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        localizar_objeto.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        localizar_objeto.add_field(name="Alcance", value="Pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        localizar_objeto.add_field(name="Componentes", value="V S M (um galho bifurcado)", inline=False)
        # Duração da magia 
        localizar_objeto.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)
        # O return vai retornar a variável com o embed criado
        return localizar_objeto
    def Ver_O_Invisivel():
    # Atribui uma variável ao embed criado
        ver_o_invisivel = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Ver o Invisível (See Invisibility)",
            # Descrição do efeito da magia
            description="Pela duração, você vê criaturas e objetos invisíveis como se eles fossem visíveis e você pode ver no Plano Etéreo. Criaturas e objetos etéreos parecem espectrais e translúcidos.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        ver_o_invisivel.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        ver_o_invisivel.add_field(name="Alcance", value="Pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        ver_o_invisivel.add_field(name="Componentes", value="V S M (um pouco de talco e um pó de prata polvilhado)", inline=False)
        # Duração da magia 
        ver_o_invisivel.add_field(name="Duração", value="1 hora", inline=False)
        # O return vai retornar a variável com o embed criado
        return ver_o_invisivel
    def Clarividencia():
    # Atribui uma variável ao embed criado
        clarividencia = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Clarividência (Clairvoyance)",
            # Descrição do efeito da magia
            description="Você cria um sensor invisível, dentro do alcance, em um local familiar a você ou em um local obvio que não seja familiar a você. O sensor se mantém no local pela duração e não pode ser atacado ou manipulado de outra forma.\n\n Quando você conjurar essa magia, escolhe visão ou audição. Você pode escolher sentir através do sensor como se você estivesse no espaço dele. Com sua ação, você pode trocar entre visão e audição.\n\n Uma criatura que puder ver o sensor (como uma criatura beneficiada por ver o invisível ou visão verdadeira) vê um globo luminoso e intangível do tamanho do seu olho.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        clarividencia.add_field(name="Tempo de Conjuração", value="10 minutos", inline=False)
        # Alcance da Magia 
        clarividencia.add_field(name="Alcance", value="1 milha", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        clarividencia.add_field(name="Componentes", value="V S M (um chifre cravejado de joias para ouvir ou um olho de vidro para ver valendo, no mínimo, 100 gp)", inline=False)
        # Duração da magia 
        clarividencia.add_field(name="Duração", value="Concentração, até 10 minutos", inline=False)
        # O return vai retornar a variável com o embed criado
        return clarividencia
    def Idiomas():
    # Atribui uma variável ao embed criado
        idiomas = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Idiomas (Tongues)",
            # Descrição do efeito da magia
            description="Essa magia garante a criatura que você tocar a habilidade de compreender e falar o idioma que ela ouvir. Além disso, quando o alvo fala, qualquer criatura que saiba, pelo menos, um idioma pode ouvir o alvo e compreender o que ele diz.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        idiomas.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        idiomas.add_field(name="Alcance", value="Toque", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        idiomas.add_field(name="Componentes", value="V M (uma pequena estátua de argila de um zigurate)", inline=False)
        # Duração da magia 
        idiomas.add_field(name="Duração", value="1 hora", inline=False)
        # O return vai retornar a variável com o embed criado
        return idiomas
    def Adivinhacao():
    # Atribui uma variável ao embed criado
        adivinhacao = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Adivinhação (Divination)",
            # Descrição do efeito da magia
            description="Sua magia e uma oferenda colocam você em contato com um deus ou servo divino. Você faz uma única pergunta a respeito de um objetivo, evento ou atividade específico que irá ocorrer dentro de 7 dias. O Mestre oferece uma resposta confiável. A resposta deve ser uma frase curta, uma rima enigmática ou um presságio.\n\n A magia não leva em consideração qualquer possível circunstância que possa mudar o que está por vir, como a conjuração de magias adicionais ou a perda ou ganho de um companheiro.\n\nSe você conjurar a magia duas ou mais vezes antes de completar seu próximo descanso longo, existe uma chance cumulativa de 25 por cento de cada conjuração, depois da primeira que você fez, ter um resultado aleatório. O Mestre faz essa jogada secretamente.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        adivinhacao.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        adivinhacao.add_field(name="Alcance", value="30 pés", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        adivinhacao.add_field(name="Componentes", value="V S M (um incenso e uma oferenda apropriada para sacrifício à sua religião valendo, no mínimo, 25 gp que a magia consome)", inline=False)
        # Duração da magia 
        adivinhacao.add_field(name="Duração", value="1 minuto", inline=False)
        # O return vai retornar a variável com o embed criado
        return adivinhacao
    def LocalizarCriatura():
    # Atribui uma variável ao embed criado
        localizar_criatura = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Localizar Criatura (Locate Creature)",
            # Descrição do efeito da magia
            description="Descreva ou nomeie uma criatura que seja familiar a você. Você sente a direção da localização da criatura, contanto que a criatura esteja a até 300 metros de você. Se a criatura se mover, você saberá a direção do movimento dela.\n\n A magia pode localizar uma criatura especifica que você conheça ou a criatura mais próxima de um tipo especifico (como um humano ou um unicórnio), desde que você já tenha visto tal criatura de perto – a até 9 metros [30 feet] – pelo menos uma vez. Se a criatura que você descreveu ou nomeou estiver em uma forma diferente, como se estiver sob efeito da magia metamorfose, essa magia não localizará a criatura.A magia pode localizar uma criatura especifica que você conheça ou a criatura mais próxima de um tipo especifico (como um humano ou um unicórnio), desde que você já tenha visto tal criatura de perto – a até 9 metros [30 feet] – pelo menos uma vez. Se a criatura que você descreveu ou nomeou estiver em uma forma diferente, como se estiver sob efeito da magia metamorfose, essa magia não localizará a criatura.\n\n Essa magia não pode localizar uma criatura se água corrente de, pelo menos 3 metros [10 feet] de largura, bloquear o caminho direito entre você e a criatura.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        localizar_criatura.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        localizar_criatura.add_field(name="Alcance", value="pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        localizar_criatura.add_field(name="Componentes", value="V S M (um pouco de pelo de um cão de caça)", inline=False)
        # Duração da magia 
        localizar_criatura.add_field(name="Duração", value="concentração, até 1 hora", inline=False)
        # O return vai retornar a variável com o embed criado
        return localizar_criatura
    def OlhoArcano():
    # Atribui uma variável ao embed criado
        olho_arcano = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Olho Arcano (Arcane Eye)",
            # Descrição do efeito da magia
            description="Você cria um olho mágico invisível, dentro do alcance, que flutua no ar pela duração. Você mentalmente recebe informações visuais do olho, que possui visão normal e visão no escuro com alcance de 9 metros [30 feet]. O olho pode ver em todas as direções.\n\n Com uma ação, você pode mover o olho até 9 metros [30 feet] em qualquer direção. Não existe limite de quão longe de você o olho pode se mover, mas ele não pode entrar em outro plano de existência. Uma barreira solida bloqueia o movimento do olho, mas o olho pode passar através de aberturas de até 3 centímetros de diâmetro.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        olho_arcano.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        # Alcance da Magia 
        olho_arcano.add_field(name="Alcance", value="30 pés", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        olho_arcano.add_field(name="Componentes", value="V S M (um punhado de pelo de morcego)", inline=False)
        # Duração da magia 
        olho_arcano.add_field(name="Duração", value="concentração, até 1 hora", inline=False)
        # O return vai retornar a variável com o embed criado
        return olho_arcano
    def Comunhao():
    # Atribui uma variável ao embed criado
        comunhao = discord.Embed(
            # Nome da Magia começando com letra em maiúsculo
            title="Comunhão (Commune)",
            # Descrição do efeito da magia
            description="Você contata sua divindade ou um representante divino e faz até três perguntas que podem ser respondidas com um sim ou não. Você deve fazer suas perguntas antes da magia terminar. Você recebe uma resposta correta para cada pergunta.\n\n Seres divinos não são necessariamente oniscientes, portanto, você pode receber “incerto” como uma resposta se uma pergunta que diga respeito a uma informação além do conhecimento da divindade. Em caso de uma resposta de única palavra puder levar ao engano ou contrariar os interesses da divindade, o Mestre pode oferecer uma frase curta como resposta, no lugar.\n\nSe você conjurar essa magia duas ou mais vezes antes de terminar um descanso longo, existe uma chance cumulativa de 25 por cento de cada conjuração, depois da primeira que você fez, ter um resultado aleatório. O Mestre faz essa jogada secretamente.",
            color=0xA020F0
        ) 
        # Tempo de conjuração da Magia 
        comunhao.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        # Alcance da Magia 
        comunhao.add_field(name="Alcance", value="pessoal", inline=False)
        # Componentes da Magia (Se tiver Materiais)
        comunhao.add_field(name="Componentes", value="V S M (incenso e um frasco de água benta ou profana)", inline=False)
        # Duração da magia 
        comunhao.add_field(name="Duração", value="1 minuto", inline=False)
        # O return vai retornar a variável com o embed criado
        return comunhao
    def ComunhaoComNatureza():
    # Cria um embed com as informações da magia
        comunhao_natureza = discord.Embed(
            title="Comunhão com a Natureza (Commune With Nature)",
            description="Você, momentaneamente, se torna uno com a natureza e ganha conhecimento do território ao seu redor. Ao ar livre, a magia lhe oferece conhecimento do terreno a até 4,5 quilômetros [3 miles] de você. Em cavernas e outros formações subterrâneas naturais, o raio é limitado a 150 metros [300 feet]. A magia não funciona onde a natureza foi substituída por construções, como em masmorras ou cidades.\n\nVocê, instantaneamente, adquire conhecimento de até três fatos, à sua escolha, sobre qualquer dos assuntos a seguir, relacionados a área:\n- Terrenos e corpos de água\n- Plantas, minérios, animais e povo predominante\n- Celestiais, fadas, corruptores, elementais ou mortos-vivos mais poderosos\n- Influência de outros planos de existência\n- Construções\nPor exemplo, você poderia determinar a localização de um morto-vivo poderoso na área, a localização da maior fonte de água potável e a localização de quaisquer cidades próximas.",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        comunhao_natureza.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        comunhao_natureza.add_field(name="Alcance", value="pessoal", inline=False)
        comunhao_natureza.add_field(name="Componentes", value="V S", inline=False)
        comunhao_natureza.add_field(name="Duração", value="instantâneo", inline=False)
        
        return comunhao_natureza
    def ConhecimentoLendario():
    # Cria um embed com as informações da magia
        conhecimento_lendario = discord.Embed(
            title="Conhecimento Lendário (Legend Lore)",
            description="Nomeie ou descreva uma pessoa, lugar ou objeto. A magia traz à sua mente um breve resumo do conhecimento significativo sobre a coisa que você nomeou. O conhecimento pode consistir de contos atuais, histórias esquecidas, ou até conhecimentos secretos que nunca foram amplamente conhecidos. Se a coisa que você nomeou não é de importância lendária, você não recebe nenhuma informação. Quanto mais informação você já tem sobre a coisa, mais precisa e detalhada é a informação recebida.\n\nAs informações que você aprende são precisas, mas podem ser apresentadas em linguagem figurada. Por exemplo, se você tem um machado mágico misterioso em mãos, a magia pode oferecer a informação: 'Ai do malfeitor cuja mão toca o machado, pois até o punho corta a mão dos malignos. Somente um verdadeiro Filho de Pedra, amante e amado de Moradin, pode despertar os verdadeiros poderes do machado, e somente com a palavra sagrada Rudnogg nos lábios.'",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        conhecimento_lendario.add_field(name="Tempo de Conjuração", value="10 minutos", inline=False)
        conhecimento_lendario.add_field(name="Alcance", value="pessoal", inline=False)
        conhecimento_lendario.add_field(name="Componentes", value="V S M (incenso, quatro tiras de marfim valendo, no mínimo, 450 gp que a magia consome)", inline=False)
        conhecimento_lendario.add_field(name="Duração", value="instantâneo", inline=False)
        
        return conhecimento_lendario
    def ContatoExtraplanar():
    # Cria um embed com as informações da magia
        contato_extraplanar = discord.Embed(
            title="Contato Extraplanar (Contact Other Plane)",
            description="Você contata mentalmente um semideus, o espírito de um sábio morto há muito tempo ou alguma outra entidade misteriosa de outro plano. Contatar esse extraplanar inteligente pode distorcer ou até mesmo arruinar com sua mente. Quando você conjurar essa magia, faça um teste de resistência de Inteligência CD 15. Se falhar, você sofre 6d6 de dano psíquico e fica insano até terminar um descanso longo. Enquanto estiver insano, você não pode realizar ações, não entende o que as outras criaturas dizem, não pode ler e fala apenas coisas sem sentido. Conjurar a magia restauração maior em você acaba com esse efeito.\n\nSe obtiver sucesso no teste de resistência, você pode fazer até cinco perguntas à entidade. Você deve fazer suas perguntas antes da magia acabar. O Mestre responde cada pergunta com uma única palavra, como “sim”, “não”, “talvez”, “nunca”, “irrelevante” ou “incerto” (se a entidade não souber a resposta para a pergunta). Em caso de uma resposta de única palavra puder levar ao engano, o Mestre pode, ao invés disso, oferecer uma frase curta como resposta.",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        contato_extraplanar.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        contato_extraplanar.add_field(name="Alcance", value="pessoal", inline=False)
        contato_extraplanar.add_field(name="Componentes", value="V", inline=False)
        contato_extraplanar.add_field(name="Duração", value="1 minuto", inline=False)
        
        return contato_extraplanar
    def LigacaoTelepatica():
    # Cria um embed com as informações da magia
        ligacao_telepatica = discord.Embed(
            title="Ligação Telepática (Telepathic Bond)",
            description="Você forja uma ligação telepática entre até oito criaturas voluntárias, à sua escolha, dentro do alcance, ligando psiquicamente cada criatura a todas as outras, pela duração. Criaturas com valores de Inteligência 2 ou menos não são afetadas por essa magia.\n\nAté a magia acabar, os alvos podem se comunicar telepaticamente através do elo, independentemente de terem ou não um idioma em comum. A comunicação é possível a qualquer distância, apesar de não se estender a outros planos de existência.",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        ligacao_telepatica.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        ligacao_telepatica.add_field(name="Alcance", value="30 pés", inline=False)
        ligacao_telepatica.add_field(name="Componentes", value="V S M (pedaços de cascas de ovos de dois tipos diferentes de criatura)", inline=False)
        ligacao_telepatica.add_field(name="Duração", value="1 hora", inline=False)
        
        return ligacao_telepatica
    def encontrar_caminho():
    # Cria um objeto Embed
        find_the_path = discord.Embed(
            title="Encontrar o Caminho (Find The Path)",
            description="Essa magia permite que você encontre a rota física mais curta e direta para um local especifico estático, que você seja familiar, no mesmo plano de existência. Se você denominar um destino em outro plano de existência, um local que se mova (como uma fortaleza andante) ou um destino que não seja especifico (como “o covil do dragão verde”), a magia falha.\n\nPela duração, contanto que você esteja no mesmo plano de existência do destino, você saberá o quão longe ele está e em que direção ele se encontra. Enquanto estiver viajando, sempre que você se deparar com uma escolha de trajetória no caminho, você automaticamente determina qual trajetória tem a rota mais curta e direta (mas não necessariamente a rota mais segura) para o destino.",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        find_the_path.add_field(name="Tempo de Conjuração", value="1 minuto", inline=False)
        find_the_path.add_field(name="Alcance", value="pessoal", inline=False)
        find_the_path.add_field(name="Componentes", value="V S M (um objeto do lugar que você deseja encontrar e um conjunto de ferramentas de adivinhação – como ossos, bastões de marfim, dentes ou runas esculpidas – valendo, no mínimo, 100 gp)", inline=False)
        find_the_path.add_field(name="Duração", value="concentração, até 1 dias", inline=False)
        
        return find_the_path
    def visao_da_verdade():
    # Cria um objeto Embed
        true_seeing = discord.Embed(
            title="Visão da Verdade (True Seeing)",
            description="Essa magia concede a uma criatura voluntária tocada a habilidade de ver as coisas como elas realmente são. Pela duração, a criatura terá visão verdadeira, percebendo portas secretas escondidas por magia e podendo ver no Plano Etéreo, tudo num alcance de até 36 metros [120 feet].",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        true_seeing.add_field(name="Tempo de Conjuração", value="1 ação", inline=False)
        true_seeing.add_field(name="Alcance", value="toque", inline=False)
        true_seeing.add_field(name="Componentes", value="V S M (unguento para os olhos, feito de pó de cogumelo, açafrão e gordura, valendo, no mínimo, 25 gp que a magia consome)", inline=False)
        true_seeing.add_field(name="Duração", value="1 horas", inline=False)
        
        return true_seeing
    def sexto_sentido():
    # Cria um objeto Embed
        foresight = discord.Embed(
            title="Sexto Sentido (Foresight)",
            description="Você toca uma criatura voluntária e a abençoa com uma habilidade limitada de ver o futuro iminente. Pela duração, o alvo não pode ser surpreendido e tem vantagem nas jogadas de ataque, testes de habilidade e testes de resistência. Além disso, outras criaturas tem desvantagem nas jogadas de ataque contra o alvo, pela duração.\n\nEssa magia termina imediatamente, se você conjura-la novamente antes da duração acabar.",
            color=0xA020F0
        )
        # Adiciona os detalhes da magia como campos no embed
        foresight.add_field(name="Tempo de Conjuração", value="1 minutos", inline=False)
        foresight.add_field(name="Alcance", value="toque", inline=False)
        foresight.add_field(name="Componentes", value="V S M (uma pena de colibri)", inline=False)
        foresight.add_field(name="Duração", value="8 horas", inline=False)
        
        return foresight
    













