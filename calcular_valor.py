from colorama import init, Fore, deinit

# Função principal com os calculos de comissão e taxas.
def home(vl_produto, qtd_prod, tipo_frete):
    cont = 0 # Contador
    comissao_p = 0.14 # Comissão padrão 14%
    comissao_a = 0.06 # Comissão adicional 6%
    item_v = 3 # Valor por item vendido
    comissao = 0.5
    vl_sem_taxa = (vl_produto * comissao) + vl_produto # Valor do produto com 60% de lucro e sem a taxa da shopee
    taxa_com_frete = (vl_sem_taxa * (comissao_p + comissao_a)) + (qtd_prod * item_v) # Taxa Shopee com o programa frete gratis
    taxa_sem_frete = (vl_sem_taxa * comissao_p) + (qtd_prod * item_v) # Taxa Shopee sem o programa frete gratis
    lucro_com_frete = (vl_sem_taxa + taxa_com_frete) - taxa_com_frete - vl_produto # Lucro sem taxas
    lucro_sem_frete = (vl_sem_taxa + taxa_sem_frete) - taxa_sem_frete - vl_produto # Lucro sem taxas
    taxa_com_frete_100 = (qtd_prod * item_v) + 100
    taxa_sem_frete_100 = (qtd_prod * item_v) + 100
    taxa_com_frete_6 = (vl_sem_taxa * (comissao_p + comissao_a)) + (vl_produto//2)
    taxa_sem_frete_6 = (vl_sem_taxa * comissao_p) + (vl_produto//2)
    com_frete(vl_produto, qtd_prod, tipo_frete, cont, comissao_p, comissao_a, item_v, comissao, vl_sem_taxa, taxa_com_frete, taxa_sem_frete, lucro_com_frete, lucro_sem_frete,
            taxa_com_frete_100, taxa_sem_frete_100, taxa_com_frete_6, taxa_sem_frete_6)
    sem_frete(vl_produto, qtd_prod, tipo_frete, cont, comissao_p, comissao_a, item_v, comissao, vl_sem_taxa, taxa_com_frete, taxa_sem_frete, lucro_com_frete, lucro_sem_frete,
            taxa_com_frete_100, taxa_sem_frete_100, taxa_com_frete_6, taxa_sem_frete_6)

# Função com os calculos do programa frete gratis
def com_frete(vl_produto, qtd_prod, tipo_frete, cont, comissao_p, comissao_a, item_v, comissao, vl_sem_taxa, taxa_com_frete, taxa_sem_frete, lucro_com_frete, lucro_sem_frete,
            taxa_com_frete_100, taxa_sem_frete_100, taxa_com_frete_6, taxa_sem_frete_6):
    if tipo_frete == 1: # Verificar se o usuario escolheu a opção Programa frete gratis
        if vl_produto <= 6:
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {vl_sem_taxa:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_com_frete_6:.2f}')
            print(f'\nLucro R$ {lucro_com_frete:.2f}')
        elif ((vl_sem_taxa * (comissao_p + comissao_a))) > 100:
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {(qtd_prod * item_v) + 100:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_com_frete_100:.2f}')
            print(f'\nLucro R$ {lucro_com_frete:.2f}')
        elif ((vl_sem_taxa * (comissao_p + comissao_a))) <= 100: # Verificar se o valor da comissão é maior que 100
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {taxa_com_frete:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_com_frete:.2f}')
            print(f'\nLucro R$ {lucro_com_frete:.2f}')
        else:
            print('Algo deu errado na opção 1, refaça o processo.')
            
# Função sem os calculos do programa frete gratis
def sem_frete(vl_produto, qtd_prod, tipo_frete, cont, comissao_p, comissao_a, item_v, comissao, vl_sem_taxa, taxa_com_frete, taxa_sem_frete, lucro_com_frete, lucro_sem_frete,
            taxa_com_frete_100, taxa_sem_frete_100, taxa_com_frete_6, taxa_sem_frete_6):
    if tipo_frete == 2:
        if vl_produto <= 6:
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {taxa_sem_frete_6:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_sem_frete_6:.2f}')
            print(f'\nLucro R$ {lucro_sem_frete:.2f}')
        elif ((vl_sem_taxa * (comissao_p))) <= 100:
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {taxa_sem_frete:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_sem_frete:.2f}')
            print(f'\nLucro R$ {lucro_sem_frete:.2f}')
        elif ((vl_sem_taxa * (comissao_p))) > 100:
            print(f'\nValor produto R$ {vl_produto:.2f}.')
            print(f'\nValor produto + {comissao * 100:.0f}% de lucro R$ {vl_sem_taxa:.2f}.')
            print(f'\nTaxas Shopee R$ {(qtd_prod * item_v) + 100:.2f}.')
            print(f'\nValor sugerido R$ {vl_sem_taxa + taxa_sem_frete_100:.2f}')
            print(f'\nLucro R$ {lucro_sem_frete:.2f}')
        else:
            print('Algo deu errado na opção 2, refaça o processo.')


print('\n', Fore.YELLOW, '-=-'*10, 'Calculadora de precificação Shopee!', '-=-'*10, Fore.RESET)

vl_produto = float(input('\nDigite o valor do produto: R$ ')) # Valor pago no produto
qtd_prod = int(input('\nDigite a quantidade de produtos: ')) # Quantidade de produtos para calculo de taxa shopee

print('\nOpções de venda:')
print(Fore.BLUE, '\n1- Programa Frete grátis.', Fore.RESET, '\nCustos:\nComissão padrão de 14%.\nComissão adicional 6%.\nR$ 3,00 por item vendido.')
print(Fore.BLUE, '\n2- Sem Frete grátis.', Fore.RESET, '\nCustos:\nComissão padrão de 14%.\nR$ 3,00 por item vendido.')
tipo_frete = int(input('\nEscolha uma opção: '))

home(vl_produto, qtd_prod, tipo_frete)