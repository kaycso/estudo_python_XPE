cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

# def disp_dois_especialistas(medico01, medico02):
#     mensagem_indisponibilidade = 'não há dias em comum para estas especialidades'
    
#     dias_disponíveis_medico_01 = list(medico01)
#     dias_disponíveis_medico_02 = list(medico02)

#     dias_em_comum = [dia for dia in dias_disponíveis_medico_01 if dia in dias_disponíveis_medico_02]
            
#     if(len(dias_em_comum) == 0):
#         print(mensagem_indisponibilidade)
#         return
#     else:
#         print(dias_em_comum)
#         return
    

mensagem_indisponibilidade = 'não há dias em comum para estas especialidades'

def verfica_conjunto_vazio(conjunto):
    conjunto = conjunto if conjunto else mensagem_indisponibilidade
    return conjunto

def disp_dois_especialistas(medico01, medico02):
    dias_em_comum = medico01 & medico02
    dias_em_comum = verfica_conjunto_vazio(dias_em_comum)
    print(dias_em_comum)
    return


def disp_tres_especialistas(medico01, medico02, medico03):
    dias_em_comum = medico01 & medico02 & medico03
    print(dias_em_comum)
    return

disp_dois_especialistas(dermatologista, ortopedista)

disp_tres_especialistas(neurologista, ortopedista, cardiologista)
