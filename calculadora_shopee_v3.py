# Importar biblioteca
import customtkinter as ctk

############ FUNÇÕES PARA CACALCULOS ############

# Função principal com os cálculos de comissão e taxas.
def home(vl_produto, qtd_prod, tipo_frete):
    gvl_produto = float(vl_produto)
    gqtd_prod = int(qtd_prod)
    comissao_p = 0.14  # Comissão padrão 14%
    comissao_a = 0.06  # Comissão adicional 6%
    item_v = 3  # Valor por item vendido
    comissao = 0.5
    vl_sem_taxa = (gvl_produto * comissao) + gvl_produto  # Valor do produto com 60% de lucro e sem a taxa da Shopee
    taxa_com_frete = (vl_sem_taxa * (comissao_p + comissao_a)) + (qtd_prod * item_v)  # Taxa Shopee com o programa frete grátis
    taxa_sem_frete = (vl_sem_taxa * comissao_p) + (qtd_prod * item_v)  # Taxa Shopee sem o programa frete grátis
    lucro_com_frete = (vl_sem_taxa + taxa_com_frete) - taxa_com_frete - gvl_produto  # Lucro sem taxas
    lucro_sem_frete = (vl_sem_taxa + taxa_sem_frete) - taxa_sem_frete - gvl_produto  # Lucro sem taxas
    taxa_com_frete_100 = (qtd_prod * item_v) + 100
    taxa_sem_frete_100 = (qtd_prod * item_v) + 100
    taxa_com_frete_6 = (vl_sem_taxa * (comissao_p + comissao_a)) + (gvl_produto//2)
    taxa_sem_frete_6 = (vl_sem_taxa * comissao_p) + (gvl_produto//2)
    com_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_com_frete, lucro_com_frete, taxa_com_frete_100,
              taxa_com_frete_6, item_v, comissao, comissao_p, comissao_a)
    sem_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_sem_frete, lucro_sem_frete, taxa_sem_frete_100,
              taxa_sem_frete_6, item_v, comissao, comissao_p, comissao_a)

# Função com os cálculos do programa frete grátis
def com_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_com_frete, lucro_com_frete,
              taxa_com_frete_100, taxa_com_frete_6, item_v, comissao, comissao_p, comissao_a):
    if tipo_frete == '1 - Programa Frete grátis':
        if vl_produto <= 6:
            com_menor6 = ctk.CTkLabel(janela, text = f'''1 - Programa Frete grátis:\n
            \nValor produto: R$ {vl_produto:.2f}
            \nValor produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas Shopee: R$ {vl_sem_taxa:.2f}
            \nValor sugerido: R$ {vl_sem_taxa + taxa_com_frete_6:.2f}
            \nLucro: R$ {lucro_com_frete:.2f}''', width = 300, height = 250, bg_color = '#4F4F4F')
            com_menor6.pack(padx = 10, pady = 10)
            com_menor6.place(x = 400, y = 95)
        elif ((vl_sem_taxa * (comissao_p + comissao_a))) > 100:
            com_maior_100 = ctk.CTkLabel(janela, text = f'''1 - Programa Frete grátis:\n
            \nValor produto: R$ {vl_produto:.2f}
            \nValor produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas Shopee: R$ {(qtd_prod * item_v) + 100:.2f}
            \nValor sugerido: R$ {vl_sem_taxa + taxa_com_frete_100:.2f}
            \nLucro: R$ {lucro_com_frete:.2f}''', width = 300, height = 250, bg_color = '#4F4F4F')
            com_maior_100.pack(padx = 10, pady = 10)
            com_maior_100.place(x = 400, y = 95)
        elif ((vl_sem_taxa * (comissao_p + comissao_a))) <= 100:
            com_menor_100 = ctk.CTkLabel(janela, text = f'''1 - Programa Frete grátis:\n
            \nValor produto: R$ {vl_produto:.2f}
            \nValor produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas Shopee: R$ {taxa_com_frete:.2f}
            \nValor sugerido: R$ {vl_sem_taxa + taxa_com_frete:.2f}
            \nLucro: R$ {lucro_com_frete:.2f}''', width = 300, height = 250, bg_color = '#4F4F4F')
            com_menor_100.pack(padx = 10, pady = 10)
            com_menor_100.place(x = 400, y = 95)
        else:
            print('Algo deu errado na opção 1, refaça o processo.')
            
# Função para quando escolher a opção Sem Frete grátis
def sem_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_sem_frete, lucro_sem_frete,
              taxa_sem_frete_100, taxa_sem_frete_6, item_v, comissao, comissao_p, comissao_a):
    if tipo_frete == '2 - Sem Frete grátis':
        if vl_produto <= 6:
            sem_menor6 = ctk.CTkLabel(janela, text = f'''2 - Sem Frete grátis:\n
            \nValor produto: R$ {vl_produto:.2f}
            \nValor produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas Shopee: R$ {taxa_sem_frete_6:.2f}
            \nValor sugerido: R$ {vl_sem_taxa + taxa_sem_frete_6:.2f}
            \nLucro: R$ {lucro_sem_frete:.2f}''', width = 300, height = 250, bg_color = '#4F4F4F')
            sem_menor6.pack(padx = 10, pady = 10)
            sem_menor6.place(x = 400, y = 95)
        elif ((vl_sem_taxa * (comissao_p))) <= 100:
            sem_menor_100 = ctk.CTkLabel(janela, text = f'''2 - Sem Frete grátis:\n
            \nValor produto: R$ {vl_produto:.2f}
            \nValor produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas Shopee: R$ {taxa_sem_frete:.2f}
            \nValor sugerido: R$ {vl_sem_taxa + taxa_sem_frete:.2f}
            \nLucro: R$ {lucro_sem_frete:.2f}''', width = 300, height = 250, bg_color = '#4F4F4F')
            sem_menor_100.pack(padx = 10, pady = 10)
            sem_menor_100.place(x = 400, y = 95)
        elif ((vl_sem_taxa * (comissao_p))) > 100:
            sem_maior_100 = ctk.CTkLabel(janela, text = f'''2 - Sem Frete grátis:\n
            \nValor produto: R$ {vl_produto:.2f}
            \nValor produto + {comissao * 100:.0f}% de lucro: R$ {vl_sem_taxa:.2f}
            \nTaxas Shopee: R$ {(qtd_prod * item_v) + 100:.2f}
            \nValor sugerido: R$ {vl_sem_taxa + taxa_sem_frete_100:.2f}
            \nLucro: R$ {lucro_sem_frete:.2f}''', width = 300, height = 250, bg_color = '#4F4F4F')
            sem_maior_100.pack(padx = 10, pady = 10)
            sem_maior_100.place(x = 400, y = 95)
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
janela.geometry('800x600')
janela.title('Calculadora Shopee')

# Titulo dentro da pagina
titulo = ctk.CTkLabel(janela, text = 'Calculadora Shopee') # Consigo editar a fonte
titulo.pack(padx = 5, pady = 5)

# Valor do produto:
ds_produto = ctk.CTkLabel(janela, text = 'Digite o valor')
ds_produto.place(x = 95, y = 45)

# Obter o valor do produto
vl_produto = ctk.CTkEntry(janela, placeholder_text = 'Valor do produto')
vl_produto.pack(padx = 10, pady = 10)
vl_produto.place(x = 180, y = 45)

# Quantidade de produtos:
qtd_produtos = ctk.CTkLabel(janela, text = 'Digite a quantidade')
qtd_produtos.place(x = 60, y = 85)

# Obter a quantidade de produtos
qtd_prod = ctk.CTkEntry(janela, placeholder_text = 'Quantidade de produtos')
qtd_prod.pack(padx = 10, pady = 10)
qtd_prod.place(x = 180, y = 85)

# Menu para escolher o tipo de Frete
combobox_var = ctk.StringVar(value = 'Selecione')
tipo_frete = ctk.CTkComboBox(janela, values = ['1 - Programa Frete grátis', '2 - Sem Frete grátis'],
                                     command = combobox_callback, variable = combobox_var)
combobox_var.set('Escolha o frete')
tipo_frete.pack(padx = 10, pady = 10)
tipo_frete.place(x = 180, y = 125)

# Botão laranja
botao = ctk.CTkButton(janela
                      ,text = 'Calcular'
                      ,fg_color = '#D2691E'
                      ,command = clique
                      ,width = 120
                      ,height = 32
                      ,border_width = 0
                      ,corner_radius = 8)
botao.pack(padx = 10, pady = 10, anchor = ctk.CENTER)
botao.place(x = 190, y = 165)


box_resul = ctk.CTkLabel(janela, text = '', width = 300, height = 250, fg_color= '#4F4F4F')
box_resul.pack(padx = 10, pady = 10)
box_resul.place(x = 400, y = 95)

# Texto informativo para escolher o tipo de frete
pfrete_gratis = ctk.CTkLabel(janela, text = '1 - Programa Frete grátis.\n\nCustos:\nComissão padrão de 14%.\nComissão adicional 6%.\nR$ 3,00 por item vendido.'
                             , width = 170, height = 140, fg_color = '#363636')
pfrete_gratis.pack(padx = 10, pady = 10)
pfrete_gratis.place(x = 170, y = 220)

# Texto informativo para escolher o tipo de frete
pfrete = ctk.CTkLabel(janela, text = '2 - Sem Frete grátis.\n\nCustos:\nComissão padrão de 14%.\nR$ 3,00 por item vendido.',
                      width = 170, height = 140, fg_color = '#363636')
pfrete.pack(padx = 10, pady = 10)
pfrete.place(x = 170, y = 365)

janela.mainloop()