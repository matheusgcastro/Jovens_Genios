""" Jogo Show do Milhão """

def premio():
    """Função que aplica as chamadas adequadas para cada pergunta"""
    for c1 in chamada_perguntas.items():
        yield (chamada_perguntas['1'])
        yield(chamada_perguntas['2'])
        yield(chamada_perguntas['3'])
        yield(chamada_perguntas['4'])
        yield(chamada_perguntas['5'])
        yield(chamada_perguntas['6'])  #


"""
A função "premio" foi criada para que fosse feita uma chamada para cada pergunta que aparecesse, simulando o programa
de forma mais realista. Vai avançando de acordo com as respostas certas selecionadas pelo player. 

O yield foi utilizado para que não a função não fosse encerada, como seria com o return. E foi sendo chamado com a utilização
do next(), que explicarei mais abaixo.
"""

perguntas = {
    'Pergunta 1': {'questao':'Qual é o nome dado ao estado da água em forma de gelo?',
                'resposta': {'1)': 'Líquido', '2)': 'Sólido', '3)': 'Gasoso', '4)': 'Vaporoso'},
                'resposta_correta': '2'},

    'Pergunta 2': {'questao': 'Quem é a namorada do Mickey?',
                'resposta': {'1)': 'Margarida', '2)': 'Minnie', '3)': 'A Pequena Sereia', '4)': 'Olívia Palito'},
                'resposta_correta': '2'},

    'Pergunta 3': {'questao': 'A água ferve a quantos graus Celsius?',
                'resposta': {'1)': '200', '2)': '100', '3)': '170', '4)': '220'},
                'resposta_correta': '2'},

    'Pergunta 4': {'questao': 'Quando é comemorado o dia da Independência do Brasil?',
                'resposta': {'1)': '21 de Abril', '2)': '12 de Outubro', '3)': '7 de Setembro', '4)': '25 de Dezembro'},
                'resposta_correta': '3'},

    'Pergunta 5': {'questao': 'Quem foi o grande amor de Julieta?',
                'resposta': {'1)': 'Romeu', '2)': 'Orfeu', '3)': 'Hamlet', '4)': 'Iago'},
                'resposta_correta': '1'},

}


chamada_perguntas = {
    '1': 'Vamos para a primeira pergunta valendo 1 Mil reais:',
    '2': 'Vamos para a segunda pergunta valendo 10 Mil reais:',
    '3': 'Vamos para a terceira pergunta valendo 100 Mil reais:',
    '4': 'Vamos para a penúltima pergunta valendo 500 Mil reais:',
    '5': 'Vamos para a última pergunta valendo 1 Milhão reais. Boa sorte!:',
    '6': 'VOCÊ GANHOU 1 MILHÃO DE REAIS!!!'
}

"""
Acima, foi criado dois dicionários: um para agrupar todas as perguntas do jogo e outro as chamadas para cada uma delas.
Achei o dicionário a melhor forma, pois consigo acessar os valores para cada um dos itens que desejo: Perguntas, opções
de resposta e resposta corrreta.
"""


# Regras do jogo, para uma melhor experiência do usuário.
print(
    'Família Aguiar, sejam bem-vindos ao SHOW DO MILHÃO!!!\n'
    '------------------------------------------------------------------------------\n'
    'Como o jogo funciona?\n'
    'Digite APENAS o número que corresponde com a alternativa desejada. \n'
    'Espero que tenham uma divertida jornada no caminho do Milhão! Boa sorte a todos!\n'
    '------------------------------------------------------------------------------'
)

# input do usuário para início do jogo com as opções S ou N. O upper() foi utilizado para padronizar a entrada do usuário e facilitar a verificação.
inicio = (str(input('Estão preparados para o início do jogo?  Digite S para sim ou N para não: \n'))).upper()

#loop while para evitar que o usuário quebre o jogo por engano. Sendo a resposta diferente de S ou N, será requisitado uma entrada válida.
while inicio != 'S' and inicio != 'N':
    print('Desculpe, mas não entendi. Poderia informar uma opção válida?\n')
    inicio = (str(input('Digite S ou N: '))).upper()

# Início do jogo caso a resposta seja Sim.
if inicio == 'S':
    # Foi atribuído ao valor contador2 a função prêmio, para que fosse associado a função next() quando necessário.
    contador2 = premio()
    print(next(contador2)) # 1º next() utilizado para chamada da primeira pergunta.


    for pergk, pergv in perguntas.items(): # Acesso de {chave : valor} ao dicionário perguntas.
        print(f'{pergk}: {pergv["questao"]}') # Print da pergunta para o usuário.

        for respk, respv in pergv['resposta'].items(): # Acesso de {chave : valor} ao dicionário dentro de cada pergunta: 'questao', 'resposta' e 'resposta_correta'.
            print(f'{respk} {respv}') # Print das alternativas de resposta para o usuário.
        resposta_usuario = input('Qual a alternativa correta? \n')

        if resposta_usuario == pergv['resposta_correta']: # Verificação da resposta do usuário com o valor da chave "resposta_correta". Caso positivo, recebe os parabéns e segue no jogo.
            print('Parabéns! Você acertou.')
            print(next(contador2))
        else:
            print('Que pena! Você errou.') # Caso o usuário erre a resposta, o jogo termina utilizando o break.
            break

elif inicio == 'N': # Finalização do jogo caso a resposta seja negativa para seu início.
    print('Tudo bem! Espero que voltem em breve.')

