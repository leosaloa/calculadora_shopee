# Importar biblioteca
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

############ FUNÇÕES PARA CACALCULOS ############

# Função principal com os cálculos de comissão e taxas.
def home(vl_produto, qtd_prod, tipo_frete):
    gvl_produto = float(vl_produto)
    gqtd_prod = int(qtd_prod)
    pct_comissao_p = 0.14  # Comissão padrão 14%
    pct_comissao_a = 0.06  # Comissão adicional 6%
    item_v = 3  # Valor por item vendido
    comissao = 0.5 # Porcentagem de lucro em cima do produto
    tx_maior_100_comissao = 100 # Regra: Teto de comissão de R$ 100, exemplo: Comissão deu R$ 200 ele fica travado em R$ 100
    tx_item_6 = gvl_produto / 2 # Regra: Quando o valor é menor que R$ 6,00 o valor da taxa é dividido por 2
    tx_item = qtd_prod * item_v   

    vl_sem_taxa = (gvl_produto * comissao) + gvl_produto  # Valor do produto com a % de lucro em cima do produto (protudo*comissao) e sem a taxa da Shopee
    tx_com_comissao = (pct_comissao_p + pct_comissao_a) * vl_produto
    tx_sem_comissao = pct_comissao_p * vl_produto
    tx_com_total = tx_com_comissao + tx_item
    taxa_com_frete = (vl_sem_taxa * (pct_comissao_p + pct_comissao_a)) + (qtd_prod * item_v)  # Taxa Shopee com o programa frete grátis
    taxa_sem_frete = (vl_sem_taxa * pct_comissao_p) + (qtd_prod * item_v)  # Taxa Shopee sem o programa frete grátis
    tx_sem_6 = (vl_sem_taxa * pct_comissao_p) + (gvl_produto / 2)
    tx_com_total_6 = tx_com_comissao + tx_item_6
    tx_sem_total_6 = tx_sem_comissao + tx_item_6
    tx_total_100 = tx_maior_100_comissao + tx_item
    tx_com_menor_total_100 = tx_com_comissao + tx_item
    tx_sem_menor_total_100 = tx_sem_comissao + tx_item
    lucro_com_frete = (vl_sem_taxa + taxa_com_frete) - taxa_com_frete - gvl_produto  # Lucro sem taxas
    lucro_sem_frete = (vl_sem_taxa + taxa_sem_frete) - taxa_sem_frete - gvl_produto  # Lucro sem taxas
    vl_venda_com_6 = vl_sem_taxa + tx_com_total_6
    vl_venda_sem_6 = vl_sem_taxa + tx_sem_total_6
    vl_venda_maior_100 = vl_sem_taxa + tx_total_100
    vl_venda_com_menor_100 = vl_sem_taxa + tx_com_menor_total_100
    vl_venda_sem_menor_100 = vl_sem_taxa + tx_sem_menor_total_100
    com_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, lucro_com_frete, 
               item_v, comissao, pct_comissao_p, pct_comissao_a, tx_item_6, tx_com_comissao,
               tx_com_total_6, vl_venda_com_6, vl_venda_maior_100, tx_maior_100_comissao, tx_item,
               tx_total_100, tx_com_total, tx_com_menor_total_100, vl_venda_com_menor_100
            )
    sem_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_sem_frete, lucro_sem_frete, 
                tx_sem_6, item_v, comissao, pct_comissao_p, vl_venda_sem_6, tx_sem_comissao, tx_item_6,
                tx_sem_total_6, vl_venda_maior_100, tx_item, vl_venda_sem_menor_100, tx_sem_menor_total_100,
                tx_total_100, tx_maior_100_comissao
            )

# Função com os cálculos do programa frete grátis
def com_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, lucro_com_frete, item_v, comissao, pct_comissao_p, 
                pct_comissao_a, tx_item_6, tx_com_comissao, tx_com_total_6, 
                vl_venda_com_6, vl_venda_maior_100, tx_maior_100_comissao, tx_item, tx_total_100,
                tx_com_total, tx_com_menor_total_100, vl_venda_com_menor_100
              ):
    if tipo_frete == '1 - Programa Frete grátis':
        if vl_produto <= 6:
            com_menor6 = ctk.CTkLabel(janela, text = f'''1 - Programa Frete grátis:\n
Valor da Venda: R$ {vl_venda_com_6:.2f}
Valor do produto: R$ {vl_produto:.2f}
Valor do produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas da Shopee:\n
Comissão: R$ {tx_com_comissao:.2f} 
Item: R$ {tx_item_6:.2f}
Total: R$ {tx_com_total_6:.2f}
            \nLucro líquido: R$ {lucro_com_frete:.2f}''', width = 300, height = 250, bg_color = '#ADADAD',
            text_color = '#000000', font = ('comfortaa', 14))
            com_menor6.pack(padx = 10, pady = 10)
            com_menor6.place(x = 400, y = 65)

        elif (tx_com_comissao) <= 100:
            com_menor_100 = ctk.CTkLabel(janela, text = f'''1 - Programa Frete grátis:\n
Valor da Venda: R$ {vl_venda_com_menor_100:.2f}
Valor do produto: R$ {vl_produto:.2f}
Valor do produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas da Shopee\n
Comissão: R$ {tx_com_comissao:.2f}
Item: R$ {tx_item:.2f}
Total: R$ {tx_com_menor_total_100:.2f}
            \nLucro líquido R$ {lucro_com_frete:.2f}''', width = 300, height = 250, bg_color = '#ADADAD',
            text_color = '#000000', font = ('comfortaa', 14))
            com_menor_100.pack(padx = 10, pady = 10)
            com_menor_100.place(x = 400, y = 65)
        elif (tx_com_comissao) > 100:     ###### AJUSTANDO AQUI ######
            com_maior_100 = ctk.CTkLabel(janela, text = f'''1 - Programa Frete grátis:\n
Valor da Venda: R$ {vl_venda_maior_100:.2f}
Valor do produto: R$ {vl_produto:.2f}
Valor do produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas da Shopee\n
Comissão: R$ {tx_maior_100_comissao:.2f}
Item: R$ {tx_item:.2f}
Total: R$ {tx_total_100:.2f}
            \nLucro líquido R$ {lucro_com_frete:.2f}''', width = 300, height = 250, bg_color = '#ADADAD',
            text_color = '#000000', font = ('comfortaa', 14))
            com_maior_100.pack(padx = 10, pady = 10)
            com_maior_100.place(x = 400, y = 65)
        else:
            print('Algo deu errado na opção 1, refaça o processo.')
            
# Função para quando escolher a opção Sem Frete grátis
def sem_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_sem_frete, lucro_sem_frete,
              tx_sem_6, item_v, comissao, pct_comissao_p, vl_venda_sem_6, tx_sem_comissao,
              tx_item_6, tx_sem_total_6, vl_venda_maior_100, tx_item, vl_venda_sem_menor_100, 
              tx_sem_menor_total_100, tx_total_100, tx_maior_100_comissao
            ):
    if tipo_frete == '2 - Sem Frete grátis':
        if vl_produto <= 6:
            sem_menor6 = ctk.CTkLabel(janela, text = f'''2 - Sem Frete grátis:\n
Valor da Venda: R$ {vl_venda_sem_6:.2f}
Valor do produto: R$ {vl_produto:.2f}
Valor do produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas da Shopee\n
Comissão: R$ {tx_sem_comissao:.2f}
Item: R$ {tx_item_6:.2f}
Total: R$ {tx_sem_total_6:.2f}
            \nLucro líquido R$ {lucro_sem_frete:.2f}''', width = 300, height = 250, bg_color = '#ADADAD',
            text_color = '#000000', font = ('comfortaa', 14))
            sem_menor6.pack(padx = 10, pady = 10)
            sem_menor6.place(x = 400, y = 65)
        elif (tx_sem_comissao) <= 100:
            sem_menor_100 = ctk.CTkLabel(janela, text = f'''2 - Sem Frete grátis:\n
 Valor da Venda: R$ {vl_venda_sem_menor_100:.2f}
 Valor do produto: R$ {vl_produto:.2f}
 Valor do produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas da Shopee\n
Comissão: R$ {tx_sem_comissao:.2f}
Item: R$ {tx_item:.2f}
Total: R$ {tx_sem_menor_total_100:.2f}
            \nLucro líquido R$ {lucro_sem_frete:.2f}''', width = 300, height = 250, bg_color = '#ADADAD',
            text_color = '#000000', font = ('comfortaa', 14))
            sem_menor_100.pack(padx = 10, pady = 10)
            sem_menor_100.place(x = 400, y = 65)
        elif (tx_sem_comissao) > 100:
            sem_maior_100 = ctk.CTkLabel(janela, text = f'''2 - Sem Frete grátis:\n
Valor da Venda: R$ {vl_venda_maior_100:.2f}
Valor do produto: R$ {vl_produto:.2f}
Valor do produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas da Shopee\n
Comissão: R$ {tx_maior_100_comissao:.2f}
Item: R$ {tx_item:.2f}
Total: R$ {tx_total_100:.2f}
            \nLucro líquido R$ {lucro_sem_frete:.2f}''', width = 300, height = 250, bg_color = '#ADADAD',
            text_color = '#000000', font = ('comfortaa', 14))
            sem_maior_100.pack(padx = 10, pady = 10)
            sem_maior_100.place(x = 400, y = 65)
        else:
            sem_erro = ctk.CTkLabel(janela, text = 'Algo deu errado na opção 2, refaça o processo.', bg_color = 'red')
            sem_erro.pack(padx = 10, pady = 10)

# Função para chamar o tipo de escolha do menu
def combobox_callback(choice):
    tipo_frete_val = str(tipo_frete.get()) # Obter o tipo de frete selecionado

# Função para quando digitar o valor do produto e a quantidade
def clique():
    # Obter os valores inseridos pelo usuário e mostrar o resultado
    vl_produto_val = float(vl_produto.get()) # Convertendo para float
    qtd_prod_val = int(qtd_prod.get()) # Convertendo para inteiro
    tipo_frete_val = tipo_frete.get() # Obtendo o tipo de frete selecionado
    home(vl_produto_val, qtd_prod_val, tipo_frete_val)  # Chamando a função home com os valores obtidos

############ FIM FUNÇÕES ############

# Criar Janela com titulo
janela = ctk.CTk()
janela.config(bg = '#ADADAD')
janela.geometry('800x600')
janela.title('Calculadora Shopee')

# Titulo dentro da pagina
titulo = ctk.CTkLabel(janela, text = 'Calculadora Shopee', bg_color = '#ADADAD', font = ('comfortaa', 24, 'bold' ),
                      text_color = '#000000')
titulo.pack(padx = 5, pady = 5)

# Valor do produto:
ds_produto = ctk.CTkLabel(janela, text = 'Digite o valor', bg_color = '#ADADAD', text_color = '#000000', font = ('comfortaa', 14))
ds_produto.place(x = 45, y = 65)

# Obter o valor do produto
vl_produto = ctk.CTkEntry(janela, placeholder_text = 'Valor do produto', bg_color = '#ADADAD',
                          text_color = '#ffffff', font = ('comfortaa', 12))
vl_produto.pack(padx = 10, pady = 10)
vl_produto.place(x = 180, y = 65)

# Quantidade de produtos:
qtd_produtos = ctk.CTkLabel(janela, text = 'Digite a quantidade', bg_color = '#ADADAD', text_color = '#000000', font = ('comfortaa', 14))
qtd_produtos.place(x = 45, y = 105)

# Obter a quantidade de produtos
qtd_prod = ctk.CTkEntry(janela, placeholder_text = 'Quantidade de produtos', bg_color = '#ADADAD', 
                        text_color = '#ffffff', font = ('comfortaa', 12))
qtd_prod.pack(padx = 10, pady = 10)
qtd_prod.place(x = 180, y = 105)

# Menu para escolher o tipo de Frete
combobox_var = ctk.StringVar(value = 'Selecione')
tipo_frete = ctk.CTkComboBox(janela, values = ['1 - Programa Frete grátis', '2 - Sem Frete grátis'],
                                     command = combobox_callback, variable = combobox_var, bg_color = '#ADADAD',
                                     text_color = '#ffffff', font = ('comfortaa', 12)
                            )
combobox_var.set('Escolha o frete')
tipo_frete.pack(padx = 10, pady = 10)
tipo_frete.place(x = 180, y = 145)

# Botão de Calcular
botao = ctk.CTkButton(janela
                      ,text = 'Calcular'
                      ,fg_color = '#EE4D2D'
                      ,bg_color = '#ADADAD'
                      ,hover_color = '#FF5230'
                      ,font = ('comfortaa', 14)
                      ,command = clique
                      ,width = 120
                      ,height = 32
                      ,border_width = 0
                      ,corner_radius = 8)
botao.pack(padx = 10, pady = 10, anchor = ctk.CENTER)
botao.place(x = 190, y = 185)

# Resultado dos calculos
box_resul = ctk.CTkLabel(janela, text = '', width = 300, height = 250, fg_color= '#ADADAD', bg_color = '#ADADAD')
box_resul.pack(padx = 10, pady = 10)
box_resul.place(x = 400, y = 65)

# Texto informativo para escolher o tipo de frete
pfrete_gratis = ctk.CTkLabel(janela, text = '1 - Programa Frete grátis.\n\nCustos:\nComissão padrão de 14%.\nComissão adicional 6%.\nR$ 3,00 por item vendido.',
                                width = 170, height = 140, fg_color = '#ADADAD', bg_color = '#000000',
                                text_color = '#000000', font = ('comfortaa', 14)
                             )
pfrete_gratis.pack(padx = 10, pady = 10)
pfrete_gratis.place(x = 165, y = 240)

# Texto informativo para escolher o tipo de frete
pfrete = ctk.CTkLabel(janela, text = '2 - Sem Frete grátis.\n\nCustos:\nComissão padrão de 14%.\nR$ 3,00 por item vendido.',
                        width = 170, height = 140, fg_color = '#ADADAD', bg_color = '#000000',
                        text_color = '#000000', font = ('comfortaa', 14)
                    )
pfrete.pack(padx = 10, pady = 10)
pfrete.place(x = 165, y = 385)

# Criar um Frame para a imagem
frame_imagem = ctk.CTkFrame(janela)
frame_imagem.pack(padx = 10, pady = 10)
frame_imagem.place(x = 380, y = 340)

# Carregar a imagem
logo = tk.PhotoImage(file = r'c:\Users\leona\Documents\_Estudo\projetos\calculadora_shopee\imagens\icone_shopee.png')
logo = logo.subsample(5, 5)

# Criar um Label dentro do Frame para exibir a imagem
figura1 = tk.Label(frame_imagem, image = logo, background = '#ADADAD')
figura1.pack(padx = 0, pady = 0)

janela.mainloop()