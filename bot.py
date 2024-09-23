import discord
from Escolas.abjuração import Abjuracao
from Escolas.adivinhação import Adivinhação
from Escolas.conjuração import Conjuração
from Escolas.encantamento import Encantamento
from Escolas.transmutação import transmutação
import os
intents = discord.Intents.default()
intents.message_content = True
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv('TOKEN')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        #Magias de Abjuração 
        if message.content =='?resistencia':
            await message.channel.send(embed=Abjuracao.Resistencia())
        elif message.content =='?armadura arcana':
            await message.channel.send(embed=Abjuracao.ArmaduraArcana())
        elif message.content =='?escudo arcano':
            await message.channel.send(embed=Abjuracao.EscudoArcano())
        elif message.content =='?escudo da fé':
            await message.channel.send(embed=Abjuracao.EscudoDaFe())
        elif message.content =='?proteção contra o bem e o mal':
            await message.channel.send(embed=Abjuracao.ProtecaoContraOBemEMal())
        elif message.content =='?santuario':
            await message.channel.send(embed=Abjuracao.Santuario())
        elif message.content =='?ajuda':
            await message.channel.send(embed=Abjuracao.Ajuda())
        elif message.content =='?passos sem pegadas':
            await message.channel.send(embed=Abjuracao.PassosSemPegadas())
        elif message.content =='?proteção contra veneno':
            await message.channel.send(embed=Abjuracao.ProtecaoContraVeneno())
        elif message.content =='?restauração menor':
            await message.channel.send(embed=Abjuracao.RestauracaoMenor())
        elif message.content =='?tranca arcana':
            await message.channel.send(embed=Abjuracao.TrancaArcana())
        elif message.content =='?vinculo protetor':
            await message.channel.send(embed=Abjuracao.VinculoProtetor())
        elif message.content =='?circulo magico':
            await message.channel.send(embed=Abjuracao.CirculoMagico())
        elif message.content =='?contramagica':
            await message.channel.send(embed=Abjuracao.Contramagica())
        elif message.content =='?dificultar detecção':
            await message.channel.send(embed=Abjuracao.DificultarDetecao())
        elif message.content =='?dissipar magia':
            await message.channel.send(embed=Abjuracao.DissiparMagia())
        elif message.content =='?muralha de vento':
            await message.channel.send(embed=Abjuracao. MuralhaDeVento())
        elif message.content =='?proteção contra energia':
            await message.channel.send(embed=Abjuracao.ProtecaoContraEnergia())
        elif message.content =='?remover maldição':
            await message.channel.send(embed=Abjuracao.RemoverMaldicao())
        elif message.content =='?sinal de esperança':
            await message.channel.send(embed=Abjuracao.SinalDeEsperanca())
        elif message.content =='?banimento':
            await message.channel.send(embed=Abjuracao.Banimento())
        elif message.content =='?movimentação livre':
            await message.channel.send(embed=Abjuracao.MovimentacaoLivre())
        elif message.content =='?pele de pedra':
            await message.channel.send(embed=Abjuracao.PeleDePedra())
        elif message.content =='?proteção contra a morte':
            await message.channel.send(embed=Abjuracao.ProtecaoContraMorte())
        elif message.content =='?santuario':
            await message.channel.send(embed=Abjuracao.Sanctum())
        elif message.content =='?ancora planar':
            await message.channel.send(embed=Abjuracao.planar_binding())
        elif message.content =='?cupula antivida':
            await message.channel.send(embed=Abjuracao.antilife_shell())
        elif message.content =='?dissipar bem e mal':
            await message.channel.send(embed=Abjuracao.dispel_evil_and_good())
        elif message.content =='?restauração maior':
            await message.channel.send(embed=Abjuracao.greater_restoration())
        elif message.content =='?globo de invulnerabilidade':
            await message.channel.send(embed=Abjuracao.globe_of_invulnerability())
        elif message.content =='?proibição':
            await message.channel.send(embed=Abjuracao.forbiddance())
        elif message.content =='?aura sagrada ':
            await message.channel.send(embed=Abjuracao.HolyAura())
        elif message.content =='?limpar a mente':
            await message.channel.send(embed=Abjuracao.MindBlank())
        #Magias adivinhação
        elif message.content =='?ataque certeiro':
            await message.channel.send(embed=Adivinhação.TrueStrike())
        elif message.content =='?orientação':
            await message.channel.send(embed=Adivinhação.Guidance())
        elif message.content =='?compreender idiomas':
            await message.channel.send(embed=Adivinhação.ComprehendLanguages())
        elif message.content =='?detectar magia':
            await message.channel.send(embed=Adivinhação.DetectMagic())
        elif message.content =='?detectar bem e o mal':
            await message.channel.send(embed=Adivinhação.DetectEvilAndGood())   
        elif message.content =='?detectar veneno e doença':
            await message.channel.send(embed=Adivinhação.DetectPoisonAndDisease()) 
        elif message.content =='?falar com os animais':
            await message.channel.send(embed=Adivinhação.SpeakWithAnimals())
        elif message.content =='?marca do caçador':
            await message.channel.send(embed=Adivinhação.HuntersMark())
        elif message.content =='?augurio':
            await message.channel.send(embed=Adivinhação.Augury())
        elif message.content =='?detectar pensamentos':
            await message.channel.send(embed=Adivinhação.Detectar_Pensamentos())
        elif message.content =='?encontrar armadilhas':
            await message.channel.send(embed=Adivinhação.Encontrar_Armadilhas())
        elif message.content =='?localizar animais ou plantas':
            await message.channel.send(embed=Adivinhação.Localizar_Animais_Ou_Plantas())
        elif message.content =='?localizar objeto':
            await message.channel.send(embed=Adivinhação.Localizar_Objeto())   
        elif message.content =='?ver o inisivel':
            await message.channel.send(embed=Adivinhação.Ver_O_Invisivel()) 
        elif message.content =='?clarividencia':
            await message.channel.send(embed=Adivinhação.Clarividencia())
        elif message.content =='?idiomas':
            await message.channel.send(embed=Adivinhação.Idiomas())
        elif message.content =='?adivinhação':
            await message.channel.send(embed=Adivinhação.Adivinhacao())
        elif message.content =='?localizar criatura':
            await message.channel.send(embed=Adivinhação.LocalizarCriatura()) 
        elif message.content =='?olho arcano':
            await message.channel.send(embed=Adivinhação.OlhoArcano())  
        elif message.content =='?comunhão':
            await message.channel.send(embed=Adivinhação.Comunhao()) 
        elif message.content =='?comunhão com a natureza':
            await message.channel.send(embed=Adivinhação.ComunhaoComNatureza()) 
        elif message.content =='?conhecimento lendario':
            await message.channel.send(embed=Adivinhação.ConhecimentoLendario()) 
        elif message.content =='?contato extraplanar':
            await message.channel.send(embed=Adivinhação.ContatoExtraplanar()) 
        elif message.content =='?ligação telepatica':
            await message.channel.send(embed=Adivinhação.LigacaoTelepatica())
        elif message.content =='?visão da verdade':
            await message.channel.send(embed=Adivinhação.visao_da_verdade()) 
        elif message.content =='?encontrar caminho':
            await message.channel.send(embed=Adivinhação.encontrar_caminho()) 
        elif message.content =='?sexto sentido':
            await message.channel.send(embed=Adivinhação.sexto_sentido()) 
        #Magias Conjuração
        elif message.content =='?criar chamas':
            await message.channel.send(embed=Conjuração.criar_chamas())
        elif message.content =='?espirro acido':
            await message.channel.send(embed=Conjuração.espirro_acido())
        elif message.content =='?mãos magicas':
            await message.channel.send(embed=Conjuração.maos_magicas())
        elif message.content =='?rajada de veneno':
            await message.channel.send(embed=Conjuração.rajada_de_veneno())
        elif message.content =='?alarme':
            await message.channel.send(embed=Conjuração.alarme())
        elif message.content =='?area escorregadia':
            await message.channel.send(embed=Conjuração.area_escorregadia())
        elif message.content =='?constrição':
            await message.channel.send(embed=Conjuração.constricao())
        elif message.content =='?disco flutuante':
            await message.channel.send(embed=Conjuração.disco_flutuante())
        elif message.content =='?nevoa obscurecente':
            await message.channel.send(embed=Conjuração.nevoa_obscurecente())
        elif message.content =='?servo inisivel':
            await message.channel.send(embed=Conjuração.servo_invisivel())
        elif message.content =='?convocar montaria':
            await message.channel.send(embed=Conjuração.convocar_montaria())
        elif message.content =='?esfera flamejante':
            await message.channel.send(embed=Conjuração.conjuracao_esfera_flamejante())
        elif message.content =='?passo nebuloso':
            await message.channel.send(embed=Conjuração.passo_nebuloso())
        elif message.content =='?teia':
            await message.channel.send(embed=Conjuração.teia())
        elif message.content =='?conjurar animais':
            await message.channel.send(embed=Conjuração.conjurar_animais())
        elif message.content =='?convocar relampagos':
            await message.channel.send(embed=Conjuração.convocar_relampagos())
        elif message.content =='?criar alimentos':
            await message.channel.send(embed=Conjuração.criar_alimentos())
        elif message.content =='?espiritos guariões':
            await message.channel.send(embed=Conjuração.espiritos_guardioes())
        elif message.content =='?neasca':
            await message.channel.send(embed=Conjuração.nevasca())
        elif message.content =='?nevoa fetida':
            await message.channel.send(embed=Conjuração.nevoa_fetida())
        elif message.content =='?arca secreta':
            await message.channel.send(embed=Conjuração.arca_secreta())
        elif message.content =='?cao fiel':
            await message.channel.send(embed=Conjuração.cao_fiel())
        elif message.content =='?conjurar elementais menores ':
            await message.channel.send(embed=Conjuração.conjurar_elementais_menores())
        elif message.content =='?conjurar seres da floresta':
            await message.channel.send(embed=Conjuração.conjuracao_seres_floresta())
        elif message.content =='?guardião da fé':
            await message.channel.send(embed=Conjuração.conjuracao_guardiao_fe())
        elif message.content =='?porta dimensional':
            await message.channel.send(embed=Conjuração.conjuracao_porta_dimensional())
        elif message.content =='?tentaculos negros':
            await message.channel.send(embed=Conjuração.conjuracao_tentaculos_negros())
        elif message.content =='?caminhar em arvores':
            await message.channel.send(embed=Conjuração.caminhar_em_arvores())
        elif message.content =='?conjurar elemental':
            await message.channel.send(embed=Conjuração.conjurar_elemental())
        elif message.content =='?nevoa mortal':
            await message.channel.send(embed=Conjuração.nevoa_mortal())
        elif message.content =='?praga de insetos':
            await message.channel.send(embed=Conjuração.conjuracao_praga_de_insetos())
        elif message.content =='?banquete de herois':
            await message.channel.send(embed=Conjuração.conjuracao_banquete_herois())
        elif message.content =='?conjurar fada':
            await message.channel.send(embed=Conjuração.conjuracao_conjurar_fada())
        elif message.content =='?invocação instantanea':
            await message.channel.send(embed=Conjuração.conjuracao_invocacao_instantanea())
        elif message.content =='?muralha de espinhos':
            await message.channel.send(embed=Conjuração.conjuracao_muralha_de_espinhos())
        elif message.content =='?palavra de recordação':
            await message.channel.send(embed=Conjuração.conjuracao_palavra_de_recordacao())
        elif message.content =='?teletransporte por arvores':
            await message.channel.send(embed=Conjuração.conjuracao_teletransporte_por_arvores())
        elif message.content =='?conjurar celestial':
            await message.channel.send(embed=Conjuração.conjuracao_conjurar_celestial())
        elif message.content =='?Mansão magnifica':
            await message.channel.send(embed=Conjuração.conjuracao_magnificent_mansion())
        elif message.content =='?Viagem planar':
            await message.channel.send(embed=Conjuração.conjuracao_plane_shift())
        elif message.content =='?labirinto':
            await message.channel.send(embed=Conjuração.conjuracao_labirinto())
        elif message.content =='?nuvem incendiaria':
            await message.channel.send(embed=Conjuração.conjuracao_nuvem_incendiaria())
        elif message.content =='?semiplano':
            await message.channel.send(embed=Conjuração.conjuracao_semiplano())
        elif message.content =='?arma espiritual':
            await message.channel.send(embed=Conjuração.conjuracao_arma_espiritual())
        elif message.content =='?invocar aberração':
            await message.channel.send(embed=Conjuração.conjuracao_invocar_aberracao())
        elif message.content =='?invocar constructo':
            await message.channel.send(embed=Conjuração.conjuracao_invocar_constructo())
        elif message.content =='?invocar demonio':
            await message.channel.send(embed=Conjuração.conjuracao_invocar_demonio())
        elif message.content =='?invocar Familiar':
            await message.channel.send(embed=Conjuração.conjuracao_invocar_familiar())
        elif message.content =='?Guardião da natureza':
            await message.channel.send(embed=Conjuração.conjuracao_invocar_guardiao_da_natureza())
        elif message.content =='?Servo da natureza':
            await message.channel.send(embed=Conjuração.conjuracao_invocar_servo_da_natureza())
        elif message.content =='?Muralha de pedra ':
            await message.channel.send(embed=Conjuração.muralha_de_pedra())
        #Encantamento
        elif message.content == '?amizade':
            await message.channel.send(embed=Encantamento.amizade())
        elif message.content == '?zombaria viciosa':
            await message.channel.send(embed=Encantamento.zombaria_viciosa())
        elif message.content == '?amizade animal':
            await message.channel.send(embed=Encantamento.amizade_animal())
        elif message.content == '?bruxaria':
            await message.channel.send(embed=Encantamento.bruxaria())
        elif message.content == '?bencao':
            await message.channel.send(embed=Encantamento.bencao())
        elif message.content == '?comando':
            await message.channel.send(embed=Encantamento.comando())
        elif message.content == '?duelo compelido':
            await message.channel.send(embed=Encantamento.duelo_compelido())
        elif message.content == '?enfeiticar pessoa':
            await message.channel.send(embed=Encantamento.enfeiticar_pessoa())
        elif message.content == '?heroismo':
            await message.channel.send(embed=Encantamento.heroismo())
        elif message.content == '?perdicao':
            await message.channel.send(embed=Encantamento.perdicao())
        elif message.content == '?riso histerico de tasha':
            await message.channel.send(embed=Encantamento.riso_histerico_de_tasha())
        elif message.content == '?sono':
            await message.channel.send(embed=Encantamento.sono())
        elif message.content == '?sussurros dissonantes':
            await message.channel.send(embed=Encantamento.sussurros_dissonantes())
        elif message.content == '?acalmar emocoes':
            await message.channel.send(embed=Encantamento.acalmar_emocoes())
        elif message.content == '?cativar':
            await message.channel.send(embed=Encantamento.cativar())
        elif message.content == '?coroa da loucura':
            await message.channel.send(embed=Encantamento.coroa_da_loucura())
        elif message.content == '?imobilizar pessoa':
            await message.channel.send(embed=Encantamento.imobilizar_pessoa())
        elif message.content == '?mensageiro animal':
            await message.channel.send(embed=Encantamento.mensageiro_animal())
        elif message.content == '?sugestao':
            await message.channel.send(embed=Encantamento.sugestao())
        elif message.content == '?zona da verdade':
            await message.channel.send(embed=Encantamento.zona_da_verdade())
        elif message.content == '?infestar de inimigos':
            await message.channel.send(embed=Encantamento.infestar_de_inimigos())
        elif message.content == '?soneca':
            await message.channel.send(embed=Encantamento.soneca())
        elif message.content == '?compulsao':
            await message.channel.send(embed=Encantamento.compulsao())
        elif message.content == '?confusao':
            await message.channel.send(embed=Encantamento.confusao())
        elif message.content == '?dominar a besta':
            await message.channel.send(embed=Encantamento.dominar_a_besta())
        elif message.content == '?dominar pessoa':
            await message.channel.send(embed=Encantamento.dominar_pessoa())
        elif message.content == '?estetica sinaptica':
            await message.channel.send(embed=Encantamento.estetica_sinaptica())
        elif message.content == '?imobilizar o monstro':
            await message.channel.send(embed=Encantamento.imobilisar_o_monstro())
        elif message.content == '?missao':
            await message.channel.send(embed=Encantamento.missao())
        elif message.content == '?modificar memoria':
            await message.channel.send(embed=Encantamento.modificar_memoria())
        elif message.content == '?danca irresistivel de Otto':
            await message.channel.send(embed=Encantamento.dança_irresistivel_de_otto())
        elif message.content == '?sugestao em massa':
            await message.channel.send(embed=Encantamento.sugestao_em_massa())
        elif message.content == '?palavra de poder dor':
            await message.channel.send(embed=Encantamento.palavra_de_poder_dor())
        elif message.content == '?antipatia simpatia':
            await message.channel.send(embed=Encantamento.antipatia_simpatia())
        elif message.content == '?dominar o monstro':
            await message.channel.send(embed=Encantamento.dominar_o_monstro())
        elif message.content == '?enfraquecer intelecto':
            await message.channel.send(embed=Encantamento.enfraquecer_o_intelecto())
        elif message.content == '?palavra de poder atordoar':
            await message.channel.send(embed=Encantamento.palavra_de_poder_atordoar())
        elif message.content == '?grito psiquico':
            await message.channel.send(embed=Encantamento.grito_psiquico())
        elif message.content == '?palavra de poder matar':
            await message.channel.send(embed=Encantamento.palavra_de_poder_matar())
        elif message.content == '?Assassino fantasmagorico':
            await message.channel.send(embed=Encantamento.phantasmal_killer())
        elif message.content == '?comandar em massa':
            await message.channel.send(embed=Encantamento.comandar_em_massa())
        #transmutação
        elif message.content == '?forma gasosa':
            await message.channel.send(embed=transmutação.forma_gasosa())
        elif message.content == '?Metamorfose':
            await message.channel.send(embed=transmutação.polimorfia())
        elif message.content == '?aprimorar habilidade':
            await message.channel.send(embed=transmutação.aprimorar_habilidade())  
        elif message.content == '?alterar-se':
            await message.channel.send(embed=transmutação.alterar_se())  
        elif message.content == '?velocidade':
            await message.channel.send(embed=transmutação.acelerar())  
        elif message.content == '?aumentar e reduzir':
            await message.channel.send(embed=transmutação.reduzir_ampliar())  
        elif message.content == '?respirar na agua':
            await message.channel.send(embed=transmutação.respirar_na_agua())
        elif message.content == '?mover terra':
            await message.channel.send(embed=transmutação.mover_terra())
        elif message.content == '?passos longos':
            await message.channel.send(embed=transmutação.passos_longos())
        elif message.content == '?metamorfose verdadeira':
            await message.channel.send(embed=transmutação.metamorfose_verdadeira())
        elif message.content == '?forma eterea':
            await message.channel.send(embed=transmutação.forma_eterea())
        elif message.content == '?controlar agua':
            await message.channel.send(embed=transmutação.controlar_agua())
        elif message.content == '?bordão mistico':
            await message.channel.send(embed=transmutação.bordao_mistico())
        elif message.content == '?consertar':
            await message.channel.send(embed=transmutação.consertar())
        elif message.content == '?chicote de espinhos':
            await message.channel.send(embed=transmutação.chicote_de_espinhos())
        elif message.content == '?druidismo':
            await message.channel.send(embed=transmutação.druidismo())    
        elif message.content == '?mensagem':
            await message.channel.send(embed=transmutação.mensagem())
        elif message.content == '?prestidigitação':
            await message.channel.send(embed=transmutação.prestidigitacao()) 
        elif message.content == '?taumaturgia':
            await message.channel.send(embed=transmutação.taumaturgia()) 
        elif message.content == '?bom fruto':
            await message.channel.send(embed=transmutação.bomfruto())
        elif message.content == '?criar e destruir agua':
            await message.channel.send(embed=transmutação.criar_destruir_agua())
        elif message.content == '?purificar alimentos':
            await message.channel.send(embed=transmutação.purificar_alimentos())
        elif message.content == '?queda suave':
            await message.channel.send(embed=transmutação.queda_suave())
        elif message.content == '?recuo acelerado':
            await message.channel.send(embed=transmutação.recuo_acelerado())
        elif message.content == '?salto':
            await message.channel.send(embed=transmutação.salto())
        elif message.content == '?arma magica':
            await message.channel.send(embed=transmutação.arma_magica())
        elif message.content == '?arrombar':
            await message.channel.send(embed=transmutação.arrombar())
        elif message.content == '?cordão de flechas':
            await message.channel.send(embed=transmutação.cordao_de_flechas())
        elif message.content == '?crescer espinhos':
            await message.channel.send(embed=transmutação.crescer_espinhos())
        elif message.content == '?esquentar metal':
            await message.channel.send(embed=transmutação.esquentar_metal())
        elif message.content == '?levitação':
            await message.channel.send(embed=transmutação.levitacao())
        elif message.content == '?patas de aranha':
            await message.channel.send(embed=transmutação.patas_de_aranha())
        elif message.content == '?pele de arvore':
            await message.channel.send(embed=transmutação.pele_de_arvore())
        elif message.content == '?truque da corda':
            await message.channel.send(embed=transmutação.truque_da_corda())
        elif message.content == '?visão no escuro':
            await message.channel.send(embed=transmutação.visao_no_escuro())
        elif message.content == '?ampliar plantas':
            await message.channel.send(embed=transmutação.ampliar_plantas())
        elif message.content == '?andar na agua':
            await message.channel.send(embed=transmutação.andar_na_agua())
        elif message.content == '?arma elemental':
            await message.channel.send(embed=transmutação.arma_elemental())
        elif message.content == '?flecha flamejante':
            await message.channel.send(embed=transmutação.flecha_relampejante())
        elif message.content == '?lentidao':
            await message.channel.send(embed=transmutação.lentidao())
        elif message.content == '?mesclar-se as rochas':
            await message.channel.send(embed=transmutação.mesclar_se_as_rochas())
        elif message.content == '?piscar':
            await message.channel.send(embed=transmutação.piscar())
        elif message.content == '?voo':
            await message.channel.send(embed=transmutação.voo())
        elif message.content == '?fabricar':
            await message.channel.send(embed=transmutação.fabricar())
        elif message.content == '?inseto gigante':
            await message.channel.send(embed=transmutação.inseto_gigante())
        elif message.content == '?aljava veloz':
            await message.channel.send(embed=transmutação.aljava_veloz())
        elif message.content == '?animar objetos':
            await message.channel.send(embed=transmutação.animar_objetos())
        elif message.content == '?criar passagem':
            await message.channel.send(embed=transmutação.criar_passagem())
        elif message.content == '?despertar':
            await message.channel.send(embed=transmutação.despertar())
        elif message.content == '?reencarnação':
            await message.channel.send(embed=transmutação.reencarnacao())
        elif message.content == '?telecinesia':
            await message.channel.send(embed=transmutação.telecinesia())
        elif message.content == '?caminhar no vento':
            await message.channel.send(embed=transmutação.caminhar_no_vento())
        elif message.content == '?carne para pedra':
            await message.channel.send(embed=transmutação.carne_para_pedra())
        elif message.content == '?desintegrar':
            await message.channel.send(embed=transmutação.desintegrar())
        elif message.content == '?inverter a gravidade':
            await message.channel.send(embed=transmutação.inverter_a_gravidade())
        elif message.content == '?isolamento':
            await message.channel.send(embed=transmutação.isolamento())
        elif message.content == '?regeneração':
            await message.channel.send(embed=transmutação.regeneracao())
        elif message.content == '?controlar o clima':
            await message.channel.send(embed=transmutação.controlar_o_clima())
        elif message.content == '?forma animal':
            await message.channel.send(embed=transmutação.forma_animais())
        elif message.content == '?loquacidade':
            await message.channel.send(embed=transmutação.loquacidade())
        elif message.content == '?alterar forma':
            await message.channel.send(embed=transmutação.alterar_forma())
        elif message.content == '?parar o tempo':
            await message.channel.send(embed=transmutação.parar_o_tempo())
client = MyClient(intents=intents)
client.run(discord_token)
