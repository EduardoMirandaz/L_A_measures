altura_cm = 110
largura_cm = 257.42
expessura_haste_vertical_cm = 3/8 * 2.54 # diametro da barra redonda.
expessura_haste_horizontal_cm = 3/16 * 2.54 # expessura da barra chata

# na hora de mostrar para o usuário, o legal será sempre calcular o resultado usando o espacamento ideal
# e deixar na esquerda um card alternativo com um vao menor (calculado com base no (espacamento_ideal - floor(0.1*espacamento_ideal)) )
# e na direita um card alternativo com um vao maior (ceil(espacamento_ideal + 0.1*espacamento_ideal)) )


espacamento_ideal_horizontal = 12
# A margem de erro deve ser indicada por conta das divisões nao exatas
margem_de_erro_horizontal = 0.1


espacamento_ideal_vertical = 50
margem_de_erro_vertical = 0.2



expessura_lado_esquerdo_quadro = 3/16 * 2.54
expessura_lado_direito_quadro = 3/16 * 2.54


quantidade_inicial_de_vaos_horizontais = ((largura_cm-expessura_lado_esquerdo_quadro-expessura_lado_direito_quadro)) / espacamento_ideal_horizontal
tamanho_total_das_hastes_cm = (int(quantidade_inicial_de_vaos_horizontais)-1)*expessura_haste_vertical_cm
tamanho_dos_vaos_cm = (largura_cm-expessura_lado_esquerdo_quadro-expessura_lado_direito_quadro-tamanho_total_das_hastes_cm) / int(quantidade_inicial_de_vaos_horizontais)
diferenca_entre_tamanho_vao_ideal_e_atual = abs(tamanho_dos_vaos_cm-espacamento_ideal_horizontal)
novo_espacamento_ideal_horizontal = espacamento_ideal_horizontal
    # Se a diferença entre o tamanho do vão ideal e o tamanho calculado for maior que X%, vamos recalcular
contagem_de_recalculo = 0
while(diferenca_entre_tamanho_vao_ideal_e_atual > (margem_de_erro_horizontal*espacamento_ideal_horizontal)):
    novo_espacamento_ideal_horizontal = novo_espacamento_ideal_horizontal - (margem_de_erro_horizontal*espacamento_ideal_horizontal)

    quantidade_inicial_de_vaos_horizontais = ((largura_cm-expessura_lado_esquerdo_quadro-expessura_lado_direito_quadro)) / novo_espacamento_ideal_horizontal
    tamanho_total_das_hastes_cm = (int(quantidade_inicial_de_vaos_horizontais)-1)*expessura_haste_vertical_cm
    tamanho_dos_vaos_cm = (largura_cm-expessura_lado_esquerdo_quadro-expessura_lado_direito_quadro-tamanho_total_das_hastes_cm) / int(quantidade_inicial_de_vaos_horizontais)
    diferenca_entre_tamanho_vao_ideal_e_atual = abs(tamanho_dos_vaos_cm-espacamento_ideal_horizontal)
    contagem_de_recalculo +=1
    if(contagem_de_recalculo >= 4):
        margem_de_erro_horizontal += 0.1
    if(margem_de_erro_horizontal >= 0.6):
        print('Já estamos em uma margem de erro para o tamanho do vão muito grande (60%) e ainda não encontramos uma solução, melhore seus parâmetros.')
        break
else:
    with open('medidas.txt', 'w') as arquivo:
        arquivo.write(f'Largura ->{largura_cm}cm\n')
        arquivo.write(f'quantidade de vãos({int(quantidade_inicial_de_vaos_horizontais)})  *  tamanho dos vãos ({tamanho_dos_vaos_cm:.2f}) = {(int(quantidade_inicial_de_vaos_horizontais) * tamanho_dos_vaos_cm):.2f}\n')
        arquivo.write(f'quantidade de hastes({int(quantidade_inicial_de_vaos_horizontais)-1})  *  expessura das hastes verticais ({expessura_haste_vertical_cm:.2f}) = {((int(quantidade_inicial_de_vaos_horizontais)-1) * expessura_haste_vertical_cm):.2f}\n')
        arquivo.write(f'expessura_lado_esquerdo_quadro ({expessura_lado_esquerdo_quadro:.2f}) + expessura_lado_direito_quadro ({expessura_lado_esquerdo_quadro:.2f}) = {expessura_lado_esquerdo_quadro + expessura_lado_direito_quadro}\n')
        arquivo.write(f'total:{expessura_lado_esquerdo_quadro+expessura_lado_direito_quadro+(int(quantidade_inicial_de_vaos_horizontais)*tamanho_dos_vaos_cm)+((int(quantidade_inicial_de_vaos_horizontais)-1)*expessura_haste_vertical_cm)}\n') 
        print(f'Largura ->{largura_cm}cm\n')
        print(f'quantidade de vãos({int(quantidade_inicial_de_vaos_horizontais)})  *  tamanho dos vãos ({tamanho_dos_vaos_cm:.2f}) = {(int(quantidade_inicial_de_vaos_horizontais) * tamanho_dos_vaos_cm):.2f}\n')
        print(f'quantidade de hastes({int(quantidade_inicial_de_vaos_horizontais)-1})  *  expessura das hastes verticais ({expessura_haste_vertical_cm:.2f}) = {((int(quantidade_inicial_de_vaos_horizontais)-1) * expessura_haste_vertical_cm):.2f}\n')
        print(f'expessura_lado_esquerdo_quadro ({expessura_lado_esquerdo_quadro:.2f}) + expessura_lado_direito_quadro ({expessura_lado_esquerdo_quadro:.2f}) = {expessura_lado_esquerdo_quadro + expessura_lado_direito_quadro}\n')
        print(f'margem de erro {margem_de_erro_horizontal:.2f}')
        print(f'total:{expessura_lado_esquerdo_quadro+expessura_lado_direito_quadro+(int(quantidade_inicial_de_vaos_horizontais)*tamanho_dos_vaos_cm)+((int(quantidade_inicial_de_vaos_horizontais)-1)*expessura_haste_vertical_cm)}\n') 


# print('inicialmente, podemos dividir uma grade de',largura_cm,'centimetros')
# print('em',quantidade_inicial_de_vaos_horizontais,'vãos de',tamanho_dos_vaos_cm ,'centimetros cada')
# print('então, somando tudo, em comprimento, temos:')
# print('expessura lado esquerdo', expessura_lado_esquerdo_quadro)
# print('expessura lado direito', expessura_lado_direito_quadro)







