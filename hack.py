import pygame
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o Pygame
pygame.init()

# Dimensões da janela
largura, altura = 900, 650
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("prototipo base")

# Cores
cor_fundo = (0, 0, 0)
cor_texto = (0, 255, 0)
cor_desenho = (255, 0, 0)

# Fonte
fonte = pygame.font.SysFont('monospace', 15)
fonte_login = pygame.font.SysFont('monospace', 30)

# Caracteres possíveis
caracteres = '0123456789'

# Coordenadas
colunas = int(largura / 10)
queda = [0] * colunas

# Função para desenhar um rosto simples
def desenhar_rosto():
    pygame.draw.circle(tela, cor_desenho, (largura // 2, altura // 2), 100)  # Cabeça
    pygame.draw.circle(tela, cor_fundo, (largura // 2 - 40, altura // 2 - 30), 20)  # Olho esquerdo
    pygame.draw.circle(tela, cor_fundo, (largura // 2 + 40, altura // 2 - 30), 20)  # Olho direito
    pygame.draw.arc(tela, cor_fundo, (largura // 2 - 50, altura // 2, 100, 50), 3.14, 0, 2)  # Boca

# Função para exibir a tela de login
def tela_login():
    login_ativo = True
    usuario = ""
    senha = ""
    while login_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if usuario == "user" and senha == "1234":
                        login_ativo = False
                    else:
                        usuario = ""
                        senha = ""
                elif evento.key == pygame.K_BACKSPACE:
                    if senha:
                        senha = senha[:-1]
                    elif usuario:
                        usuario = usuario[:-1]
                else:
                    if len(usuario) < 4:
                        usuario += evento.unicode
                    elif len(senha) < 4:
                        senha += evento.unicode

        tela.fill(cor_fundo)
        texto_usuario = fonte_login.render(f"User: {usuario}", True, cor_texto)
        texto_senha = fonte_login.render(f"Senha: {'*' * len(senha)}", True, cor_texto)
        tela.blit(texto_usuario, (largura // 4, altura // 3))
        tela.blit(texto_senha, (largura // 4, altura // 2))
        pygame.display.flip()

# Função principal para a chuva de números
def chuva_de_numeros():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill(cor_fundo)

        for i in range(len(queda)):
            caractere = random.choice(caracteres)
            texto = fonte.render(caractere, True, cor_texto)
            posicao = (i * 10, queda[i] * 10)
            tela.blit(texto, posicao)
            if queda[i] * 10 > altura and random.random() > 0.975:
                queda[i] = 0
            queda[i] += 1

        desenhar_rosto()

        pygame.display.flip()
        pygame.time.delay(30)


def pesquisar_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys("ChatBot")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    links = driver.find_elements_by_css_selector("div.r > a")
    for link in links:
        if "dialogFlow" in link.get_attribute("href"):
            link.click()
            break
    time.sleep(5)
    driver.quit()

# Exibir a tela de login antes de iniciar a chuva de números
tela_login()
# Iniciar a chuva de números
chuva_de_numeros()
# Pesquisar no Google e abrir o site da Black Trunk Fishing
pesquisar_google()
