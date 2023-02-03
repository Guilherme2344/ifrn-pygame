import pygame
import random
import time
pygame.init()

#largura e altura
tela_largura = 1280
tela_altura = 720

#imprimindo tela
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('Space Junk Escape')

#importando imagens
background = pygame.image.load('imagens/Background.jpg').convert_alpha()
background = pygame.transform.scale(background, (tela_largura, tela_altura))

nave = pygame.image.load('imagens/foguete.png').convert_alpha()
nave = pygame.transform.scale(nave, (50, 50))

lixo_espacial_pequeno_1 = pygame.image.load('imagens/Lixo Espacial pequeno 1.png').convert_alpha()
lixo_espacial_pequeno_1 = pygame.transform.scale(lixo_espacial_pequeno_1, (100, 100))

lixo_espacial_pequeno_2 = pygame.image.load('imagens/Lixo espacial pequeno 2.png').convert_alpha()
lixo_espacial_pequeno_2 = pygame.transform.scale(lixo_espacial_pequeno_2, (100, 100))

lixo_espacial_pequeno_3 = pygame.image.load('imagens/lixo espacial pequeno 3.png').convert_alpha()
lixo_espacial_pequeno_3 = pygame.transform.scale(lixo_espacial_pequeno_3, (100, 100))

lixo_espacial_grande_1 = pygame.image.load('imagens/Lixo espacial Grande 1.png').convert_alpha()
lixo_espacial_grande_1 = pygame.transform.scale(lixo_espacial_grande_1, (200, 200))

lixo_espacial_grande_2 = pygame.image.load('imagens/Lixo Espacial Grande 2.png').convert_alpha()
lixo_espacial_grande_2 = pygame.transform.scale(lixo_espacial_grande_2, (200, 200))

#criando as vidas
vida = 41

#cores
preto = (0,0,0)
branco = (255,255,255)

#sons
som_tela_inicial = pygame.mixer.Sound('sons/Guerra das Estrelas (Star Wars).wav')
som_de_fundo = pygame.mixer.Sound('sons/som do espaço.wav')
som_colisao = pygame.mixer.music.load('sons/colisão nave.wav')
som_tela_final = pygame.mixer.Sound('sons/Jay Sean (feat. Nicki Minaj) - 2012.wav')

#importando a fonte
fonte = pygame.font.Font('fonte/space age.ttf', 50)

#posições
nave_posicao_x = 200
nave_posicao_y = 300

lixo_espacial_pequeno_1_posicao_x = random.randint(200, 640)
lixo_espacial_pequeno_1_posicao_y = random.randint(200, 640)

lixo_espacial_pequeno_2_posicao_x = random.randint(200, 640)
lixo_espacial_pequeno_2_posicao_y = random.randint(200, 640)

lixo_espacial_pequeno_3_posicao_x = random.randint(200, 640)
lixo_espacial_pequeno_3_posicao_y = random.randint(200, 640)

lixo_espacial_grande_1_posicao_x = random.randint(200, 640)
lixo_espacial_grande_1_posicao_y = random.randint(200, 640)

lixo_espacial_grande_2_posicao_x = random.randint(200, 640)
lixo_espacial_grande_2_posicao_y = random.randint(200, 640)

#funções
def respawn():

    x = 1350
    y = random.randint(20, 700)
    return [x, y]

def colisao():
    global vida
    global som_colisao
    if nave_objeto.colliderect(lixo_espacial_pequeno_1_objeto):
        vida -= 1
        pygame.mixer.music.play()
        return True
    elif nave_objeto.colliderect(lixo_espacial_pequeno_2_objeto):
        vida -= 1
        pygame.mixer.music.play()
        return True
    elif nave_objeto.colliderect(lixo_espacial_pequeno_2_objeto):
        vida -= 1
        pygame.mixer.music.play()
        return True
    elif nave_objeto.colliderect(lixo_espacial_pequeno_3_objeto):
        vida -= 1
        pygame.mixer.music.play()
        return True
    elif nave_objeto.colliderect(lixo_espacial_grande_1_objeto):
        vida -= 1
        pygame.mixer.music.play()
        return True
    elif nave_objeto.colliderect(lixo_espacial_grande_2_objeto):
        vida -= 1
        pygame.mixer.music.play()
        return True
    else:
        return False

def tela_inicial(tela, largura, altura):
    global executar
    #configurando imagem
    tamanho = (largura,altura)
    imagem = pygame.image.load('imagens/Capa do Jogo.png').convert_alpha()
    imagem = pygame.transform.scale(imagem, tamanho)

    #som
    som_tela_inicial.set_volume(0.3)
    som_tela_inicial.play()

    #configurando texto
    fonte_tela_inicial_1 = pygame.font.Font('fonte/space age.ttf', 30)
    fonte_tela_inicial_2 = pygame.font.Font('fonte/space age.ttf', 20)
    titulo = fonte.render('Space Junk Escape', True, branco)
    mensagem_iniciar = fonte_tela_inicial_1.render('Pressione a tecla SPACE para iniciar', True, branco)
    mensagem_creditos_desenvolvedores = fonte_tela_inicial_2.render('Desenvolvido por:', True, branco)
    mensagem_desenvolvedor_1 = fonte_tela_inicial_2.render('Cauã Henrique', True, branco)
    mensagem_desenvolvedor_2 = fonte_tela_inicial_2.render('Guilherme Cristiano', True, branco)
    titulo_retangulo = titulo.get_rect()
    titulo_retangulo.center = (largura // 2, 320)
    mensagem_iniciar_retangulo = mensagem_iniciar.get_rect()
    mensagem_iniciar_retangulo.center = (largura // 2, 400)
    mensagem_creditos_desenvolvedores_retangulo = mensagem_creditos_desenvolvedores.get_rect()
    mensagem_creditos_desenvolvedores_retangulo.center = (1140, 670)
    mensagem_desenvolvedor_1_retangulo = mensagem_desenvolvedor_1.get_rect()
    mensagem_desenvolvedor_1_retangulo.center = (1165, 690)
    mensagem_desenvolvedor_2_retangulo = mensagem_desenvolvedor_2.get_rect()
    mensagem_desenvolvedor_2_retangulo.center = (1123, 710)

    #mostrando na tela
    tela.blit(imagem, (0,0))
    tela.blit(titulo, titulo_retangulo)
    tela.blit(mensagem_iniciar, mensagem_iniciar_retangulo)
    tela.blit(mensagem_creditos_desenvolvedores, mensagem_creditos_desenvolvedores_retangulo)
    tela.blit(mensagem_desenvolvedor_1, mensagem_desenvolvedor_1_retangulo)
    tela.blit(mensagem_desenvolvedor_2, mensagem_desenvolvedor_2_retangulo)
    
    #atualizando tela
    pygame.display.flip()
    sair_tela_entrada = False
    while not sair_tela_entrada:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            sair_tela_entrada = event.key == pygame.K_SPACE
	# retorna a imagem com o tamanho correto
    return imagem

#transformando imagens em objetos
nave_objeto = nave.get_rect()
lixo_espacial_pequeno_1_objeto = lixo_espacial_pequeno_1.get_rect()
lixo_espacial_pequeno_2_objeto = lixo_espacial_pequeno_2.get_rect()
lixo_espacial_pequeno_3_objeto = lixo_espacial_pequeno_3.get_rect()
lixo_espacial_grande_1_objeto = lixo_espacial_grande_1.get_rect()
lixo_espacial_grande_2_objeto = lixo_espacial_grande_2.get_rect()

#abrir tela inicial
abrir_tela_inicial = tela_inicial(tela, tela_largura, tela_altura)

#loop
executar = True
while executar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executar = False

    #colocando imagem da tela de fundo        
    tela.blit(background, (0,0))

    #movimento da tela de fundo
    movimento_x = tela_largura % background.get_rect().width
    tela.blit(background, (movimento_x - background.get_rect().width, 0))
    if movimento_x < 1280:
        tela.blit(background, (movimento_x, 0))
    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] and nave_posicao_y > 1:
        nave_posicao_y -= 2
    elif tecla[pygame.K_s] and nave_posicao_y < 640:
        nave_posicao_y += 2

    #som
    som_tela_inicial.stop()
    som_de_fundo.play()

    #posição dos retângulos dos objetos
    nave_objeto.x = nave_posicao_x
    nave_objeto.y = nave_posicao_y

    lixo_espacial_pequeno_1_objeto.x = lixo_espacial_pequeno_1_posicao_x
    lixo_espacial_pequeno_1_objeto.y = lixo_espacial_pequeno_1_posicao_y

    lixo_espacial_pequeno_2_objeto.x = lixo_espacial_pequeno_2_posicao_x
    lixo_espacial_pequeno_2_objeto.y = lixo_espacial_pequeno_2_posicao_y

    lixo_espacial_pequeno_3_objeto.x = lixo_espacial_pequeno_3_posicao_x
    lixo_espacial_pequeno_3_objeto.y = lixo_espacial_pequeno_3_posicao_y

    lixo_espacial_grande_1_objeto.x = lixo_espacial_grande_1_posicao_x
    lixo_espacial_grande_1_objeto.y = lixo_espacial_grande_1_posicao_y

    lixo_espacial_grande_2_objeto.x = lixo_espacial_grande_2_posicao_x
    lixo_espacial_grande_2_objeto.y = lixo_espacial_grande_2_posicao_y
    
    #colocando o tempo
    segundos = pygame.time.get_ticks() // 1000
    minutos = 0
    if segundos < 10:
        fonte_tempo = fonte.render(f'{minutos}:0{segundos}', True, branco)
        tela.blit(fonte_tempo, (1130, 680))
    elif segundos >= 60 and segundos < 120:
        segundos -= 60
        minutos += 1
        if segundos < 10:
            fonte_tempo = fonte.render(f'{minutos}:0{segundos}', True, branco)
            tela.blit(fonte_tempo, (1160, 680))
        else:
            fonte_tempo = fonte.render(f'{minutos}:{segundos}', True, branco)
            tela.blit(fonte_tempo, (1160, 680))
    elif segundos >= 120 and segundos < 180:
        segundos -= 120
        minutos += 2
        if segundos < 10:
            fonte_tempo = fonte.render(f'{minutos}:0{segundos}', True, branco)
            tela.blit(fonte_tempo, (1160, 680))
        else:
            fonte_tempo = fonte.render(f'{minutos}:{segundos}', True, branco)
            tela.blit(fonte_tempo, (1160, 680))
    else:
        fonte_tempo = fonte.render(f'{minutos}:{segundos}', True, branco)
        tela.blit(fonte_tempo, (1130, 680))

    #movimento
    tela_largura -= 2
    lixo_espacial_pequeno_1_posicao_x -= 4
    lixo_espacial_pequeno_2_posicao_x -= 4
    lixo_espacial_pequeno_3_posicao_x -= 4
    lixo_espacial_grande_1_posicao_x -= 4
    lixo_espacial_grande_2_posicao_x -= 4

    #se o jogador não tiver mais vida
    if vida == 0:
        executar = False

    #respawn
    if lixo_espacial_pequeno_1_posicao_x == 2:
        lixo_espacial_pequeno_1_posicao_x = respawn()[0]
        lixo_espacial_pequeno_1_posicao_y = respawn()[1]
        lixo_espacial_pequeno_2_posicao_x = respawn()[0]
        lixo_espacial_pequeno_2_posicao_y = respawn()[1]
        lixo_espacial_pequeno_3_posicao_x = respawn()[0]
        lixo_espacial_pequeno_3_posicao_y = respawn()[1]
        lixo_espacial_grande_1_posicao_x = respawn()[0]
        lixo_espacial_grande_1_posicao_y = respawn()[1]
        lixo_espacial_grande_2_posicao_x = respawn()[0]
        lixo_espacial_grande_2_posicao_y = respawn()[1]
    if colisao():
        lixo_espacial_pequeno_1_posicao_x = respawn()[0]
        lixo_espacial_pequeno_1_posicao_y = respawn()[1]
        lixo_espacial_pequeno_2_posicao_x = respawn()[0]
        lixo_espacial_pequeno_2_posicao_y = respawn()[1]
        lixo_espacial_pequeno_3_posicao_x = respawn()[0]
        lixo_espacial_pequeno_3_posicao_y = respawn()[1]
        lixo_espacial_grande_1_posicao_x = respawn()[0]
        lixo_espacial_grande_1_posicao_y = respawn()[1]
        lixo_espacial_grande_2_posicao_x = respawn()[0]
        lixo_espacial_grande_2_posicao_y = respawn()[1]

    #colocando a fonte
    fonte_titulo = fonte.render('Space Junk Escape', True, branco)
    tela.blit(fonte_titulo, (315, 20))
    fonte_vida = fonte.render(f'Vidas: {vida}', True, branco)
    tela.blit(fonte_vida, (10, 680))

    #colocando imagens
    tela.blit(nave, (nave_posicao_x, nave_posicao_y))
    tela.blit(lixo_espacial_pequeno_1, (lixo_espacial_pequeno_1_posicao_x, lixo_espacial_pequeno_1_posicao_y))
    tela.blit(lixo_espacial_pequeno_2, (lixo_espacial_pequeno_2_posicao_x, lixo_espacial_pequeno_2_posicao_y))
    tela.blit(lixo_espacial_pequeno_3, (lixo_espacial_pequeno_3_posicao_x, lixo_espacial_pequeno_3_posicao_y))
    tela.blit(lixo_espacial_grande_1, (lixo_espacial_grande_1_posicao_x, lixo_espacial_grande_1_posicao_y))
    tela.blit(lixo_espacial_grande_2, (lixo_espacial_grande_2_posicao_x, lixo_espacial_grande_2_posicao_y))

    #tela final
    if minutos >= 2:
        fonte_final_1 = pygame.font.Font('fonte/space age.ttf', 100)
        fonte_final_2 = pygame.font.Font('fonte/space age.ttf', 35)
        fonte_final_3 = pygame.font.Font('fonte/space age.ttf', 20)
        tela.fill(preto)
        pygame.mixer.music.stop()
        som_de_fundo.stop()
        som_tela_final.play()
        mensagem_fim_de_jogo = fonte_final_1.render('Game Over', True, branco)
        mensagem_final = fonte_final_2.render('Você Salvou a Terra. Vamos Festejar!!!', True, branco)
        mensagem_creditos_musicas = fonte_final_3.render('Músicas:', True, branco)
        mensagem_musica_tela_inicial = fonte_final_3.render('guerra das estrelas (star wars)', True, branco)
        mensagem_musica_tela_final = fonte_final_3.render('jay sean - 2012', True, branco)
        tela.blit(mensagem_fim_de_jogo, (270, 250))
        tela.blit(mensagem_final, (150, 450))
        tela.blit(mensagem_creditos_musicas, (5, 660))
        tela.blit(mensagem_musica_tela_inicial, (5, 680))
        tela.blit(mensagem_musica_tela_final, (5, 700))

    pygame.display.update()