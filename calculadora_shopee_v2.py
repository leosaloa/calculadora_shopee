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
            print('\n1 - Programa Frete grátis:\n')
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {vl_sem_taxa:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_com_frete_6:.2f}')
            print(f'\nLucro R$ {lucro_com_frete:.2f}')
        elif ((vl_sem_taxa * (comissao_p + comissao_a))) > 100:
            print('\n1 - Programa Frete grátis:\n')
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {(qtd_prod * item_v) + 100:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_com_frete_100:.2f}')
            print(f'\nLucro R$ {lucro_com_frete:.2f}')
        elif ((vl_sem_taxa * (comissao_p + comissao_a))) <= 100:
            print('\n1 - Programa Frete grátis:\n')
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {taxa_com_frete:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_com_frete:.2f}')
            print(f'\nLucro R$ {lucro_com_frete:.2f}')
        else:
            print('Algo deu errado na opção 1, refaça o processo.')
            
# Função para quando escolher a opção Sem Frete grátis
def sem_frete(vl_produto, qtd_prod, tipo_frete, vl_sem_taxa, taxa_sem_frete, lucro_sem_frete,
              taxa_sem_frete_100, taxa_sem_frete_6, item_v, comissao, comissao_p, comissao_a):
    if tipo_frete == '2 - Sem Frete grátis':
        if vl_produto <= 6:
            sem_menor6 = f'''print('\n2 - Sem Frete grátis:\n
            \nValor produto R$ {vl_produto:.2f}.
            \nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.
            \nTaxas Shopee R$ {taxa_sem_frete_6:.2f}.
            \nValor sugerido R$ {vl_sem_taxa + taxa_sem_frete_6:.2f}.
            \nLucro R$ {lucro_sem_frete:.2f}.'''
            print(sem_menor6)
        elif ((vl_sem_taxa * (comissao_p))) <= 100:
            sem_menor_100 = f'''\n2 - Sem Frete grátis:\n
            \nValor produto R$ {vl_produto:.2f}.
            \nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.
            \nTaxas Shopee R$ {taxa_sem_frete:.2f}.
            \nValor sugerido R$ {vl_sem_taxa + taxa_sem_frete:.2f}
            \nLucro R$ {lucro_sem_frete:.2f}'''
            print(sem_menor_100)
        elif ((vl_sem_taxa * (comissao_p))) > 100:
            sem_maior_100 = f'''\n2 - Sem Frete grátis:\n
            \nValor produto R$ {vl_produto:.2f}.
            \nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.
            \nTaxas Shopee R$ {(qtd_prod * item_v) + 100:.2f}.
            \nValor sugerido R$ {vl_sem_taxa + taxa_sem_frete_100:.2f}.
            \nLucro R$ {lucro_sem_frete:.2f}.'''
            print(sem_maior_100)
        else:
            sem_erro = 'Algo deu errado na opção 2, refaça o processo.'

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
janela.geometry('900x700')
janela.title('Calculadora Shopee')

# # Criar abas
# tabview = ctk.CTkTabview(janela, width = 900, height = 700, corner_radius = 10, fg_color = '#008B8B')
# tabview.pack()
# tabview.add('Home')
# tabview.add('Calculadora')

# Titulo dentro da pagina
titulo = ctk.CTkLabel(janela, text = 'Calculadora Shopee') # Consigo editar a fonte
titulo.pack(padx = 5, pady = 5)

# Valor do produto:
ds_produto = ctk.CTkLabel(janela, text = 'Valor do produto')
ds_produto.place(x = 270, y = 45)

# Quantidade de produtos:
qtd_produtos = ctk.CTkLabel(janela, text = 'Quantidade de produtos')
qtd_produtos.place(x = 230, y = 95)


# Obter o valor do produto
vl_produto = ctk.CTkEntry(janela, placeholder_text = 'Valor do produto')
vl_produto.pack(padx = 10, pady = 10)

# Obter a quantidade de produtos
qtd_prod = ctk.CTkEntry(janela, placeholder_text = 'Quantidade de produtos')
qtd_prod.pack(padx = 10, pady = 10)

# Menu para escolher o tipo de Frete
combobox_var = ctk.StringVar(value = 'Selecione')
tipo_frete = ctk.CTkComboBox(janela, values = ['1 - Programa Frete grátis', '2 - Sem Frete grátis'],
                                     command = combobox_callback, variable = combobox_var)
combobox_var.set('Escolha')
tipo_frete.pack(padx = 10, pady = 10)

# Botão laranja
botao = ctk.CTkButton(janela
                      ,text = 'Calcular'
                      ,fg_color = 'orange'
                      ,command = clique
                      ,width = 120
                      ,height = 32
                      ,border_width = 0
                      ,corner_radius = 8)
botao.pack(padx = 10, pady = 10, anchor = ctk.CENTER)

# Aparecer o resultado na janela
lab = ctk.CTkLabel(janela, text = '', width = 200, height = 25, text_color = 'yellow')
lab.pack(padx = 10, pady = 10)

# Texto informativo para escolher o tipo de frete
pfrete_gratis = ctk.CTkLabel(janela, text = '\n1 - Programa Frete grátis.\nCustos:\nComissão padrão de 14%.\nComissão adicional 6%.\nR$ 3,00 por item vendido.')
pfrete_gratis.pack(padx = 10, pady = 10)
# Texto informativo para escolher o tipo de frete
pfrete = ctk.CTkLabel(janela, text = '\n2 - Sem Frete grátis.\nCustos:\nComissão padrão de 14%.\nR$ 3,00 por item vendido.')
pfrete.pack(padx = 10, pady = 10)

janela.mainloop()