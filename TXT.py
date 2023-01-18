''' Desafio onde vamos aprender:
Na Hashtag, sempre analisamos o nosso "Funil de Vendas". Para isso, rastreamos de onde veio os alunos por meio de um código, do tipo:
hashtag_site_org -> Pessoas que vieram pelo site da Hashtag
hashtag_yt_org -> Pessoas que vieram pelo Youtube da Hashtag
hashtag_ig_org -> Pessoas que vieram pelo Instagram da Hashtag
hashtag_igfb_org -> Pessoas que vieram pelo Instagram ou Facebook da Hashtag
Os códigos diferentes disso, são códigos de anúncio da Hashtag.

Queremos analisar quantos alunos vieram de anúncio e quantos vieram "orgânico".
Qual a melhor fonte "orgânica" de alunos
Obs: orgânico é tudo aquilo que não veio de anúncios.

No nosso sistema, conseguimos exportar um txt com as informações dos alunos, conforme o arquivo Alunos.txt
(Os dados foram gerados aleatoriamente para simular uma situação real, já que não podemos fornecer os dados reais dos alunos por questões de segurança)

No final, para treinar, vamos escrever todas essas respostas em um novo arquivo txt'''

arquivo = open('Alunos.txt', 'r')
linhas = arquivo.readlines()
del linhas[:4]

# criar indicadores
qtde_anuncio = 0
qtde_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_site_org = 0

# percorrer o arquivo
for linha in linhas:
    email, origem = linha.split(',')
    if '_org' in origem:
        qtde_org += 1
        if 'hashtag_yt_org' in origem:
            qtde_yt_org += 1
        if 'hashtag_site_org' in origem:
            qtde_site_org += 1
        if 'hashtag_ig_org' in origem or 'hashtag_igfb_org' in origem:
            qtde_igfb_org += 1
    else:
        qtde_anuncio += 1

arquivo.close()

with open('Indicadores.txt', 'w') as arquivo_indicadores:
    arquivo_indicadores.write('Quantidade Anuncio: {}\n'.format(qtde_anuncio))
    arquivo_indicadores.write('Quantidade Orgânico: {}\n'.format(qtde_org))
    arquivo_indicadores.write('Quantidade Youtube: {}\n'.format(qtde_yt_org))
    arquivo_indicadores.write('Quantidade Instagram: {}\n'.format(qtde_igfb_org))
    arquivo_indicadores.write('Quantidade Site: {}\n'.format(qtde_site_org))
