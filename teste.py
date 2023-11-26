medicos = []
consultasAgendadas = []

def listarMedicos():
    '''

    :return: Função para listar os medicos e sua respectiva especialidade da lista
    '''


    print('Médicos Cadastrados:')
    a = 0
    for i in medicos:
        print(f"{a + 1}. {medicos[a][0]} - {medicos[a][1]}")
        a += 1


def agendarConsulta():
    '''

    :return: função para agendar consulta a partir da escolha do medico e do horario disponivel
    '''
    print('Agendamento de Consultas')
    listarMedicos()

    if medicos:
        escolhaMedico = int(input('Escolha o número do médico: ')) - 1
        if 0 <= escolhaMedico < len(medicos):
            medicoEscolhido = medicos[escolhaMedico]

            print(f'Horários disponíveis do Dr.{medicoEscolhido[0]}: {medicoEscolhido[2]}')

            horarioConsulta = input('Escolha o horário da consulta: ')
            pacienteConsulta = input('Qual o nome do paciente: ')
            dataConsulta = input('Qual seria a data da consulta? ')

            consulta = [pacienteConsulta, medicoEscolhido[0], medicoEscolhido[1], dataConsulta, horarioConsulta]
            consultasAgendadas.append(consulta)

            print('Consulta agendada com sucesso.')
        else:
            print('Número de médico inválido.')
    else:
        print('Não há médicos cadastrados.')


def listarConsultas():
    '''
    :return: Função para mostrar as consultas
    '''
    if not consultasAgendadas:
        print('Não há consultas agendadas.')
        return

    print('Lista de Consultas Agendadas:')
    for i, consulta in enumerate(consultasAgendadas, start=1):
        print(f"{i}. Paciente: {consulta[0]}, Médico: {consulta[1]}, "
              f"Especialidade: {consulta[2]}, Data: {consulta[3]}, "
              f"Horário: {consulta[4]}")
    print('Fim da lista de consultas agendadas.')


def cancelarConsulta():
    '''

    :return: Função para cancelar uma consulta
    '''


    listarConsultas()
    if consultasAgendadas:
        numeroConsulta = int(input('Escolha o número da consulta a ser cancelada:')) - 1
        if 0 <= numeroConsulta < len(consultasAgendadas):
            consultaCancelada = consultasAgendadas.pop(numeroConsulta)
            print(f'Consulta do paciente {consultaCancelada[0]} com o Dr{consultaCancelada[1]} no dia {consultaCancelada[3]} às{consultaCancelada[4]} foi cancelada.')
        else:
            print('Número de consulta inválido.')
    else:
        print('Não há consultas agendadas.')


def gerarRelatorio():
    '''

    :return: Função para gerar um relatorio de todas as consultas
    '''
    opcao = input('''Deseja visualizar o relatório por 
    1. dia 
    2. médico 
    3. paciente
     ''')
    if opcao == '1':
        dia = input('Digite o dia: ')
        consultasDia = [consulta for consulta in consultasAgendadas if consulta[3] == dia]
        if consultasDia:
            print(f'Relatório de Consultas no dia {dia}:')
            for consulta in consultasDia:
                print(f"Paciente: {consulta[0]}, Médico: {consulta[1]}, Data: {consulta[3]}, Horário: {consulta[4]}")
        else:
            print('Não há consultas neste dia.')
    elif opcao == '2':
        medico = input('Digite o nome do médico: ')
        consultasMedico = [consulta for consulta in consultasAgendadas if consulta[1] == medico]
        if consultasMedico:
            print(f'Relatório de Consultas do Dr.{medico}:')
            for consulta in consultasMedico:
                print(f"Paciente: {consulta[0]}, Data: {consulta[3]}, Horário: {consulta[4]}")
        else:
            print('Este médico não tem consultas agendadas.')
    elif opcao == '3':
        paciente = input('Digite o nome do paciente: ')
        consultasPaciente = [consulta for consulta in consultasAgendadas if consulta[0] == paciente]
        if consultasPaciente:
            print(f'Relatório de Consultas do paciente {paciente}:')
            for consulta in consultasPaciente:
                print(f"Médico: {consulta[1]}, Data: {consulta[3]}, Horário: {consulta[4]}")
        else:
            print('Este paciente não tem consultas agendadas.')
    else:
        print('Opção inválida.')


def adicionarHorarios():
    '''

    :return: função para adicionar novos horarios para medicos ja cadastrados
    '''
    print('Gestão de Médicos - Adicionar Novos Horários')
    listarMedicos()

    if medicos:
        escolhaMedico = int(input('Escolha o número do médico: ')) - 1
        if 0 <= escolhaMedico < len(medicos):
            medicoEscolhido = medicos[escolhaMedico]
            novosHorarios = input('Digite os novos horários (separados por vírgula): ').split(',')
            medicoEscolhido[2].extend(novosHorarios)
            print('Novos horários adicionados com sucesso.')
        else:
            print('Número de médico inválido.')
    else:
        print('Não há médicos cadastrados.')


while True:
  print('''
  Sistema de Gerenciamento de Consultas Hospitalares")
  1. Cadastrar Médico
  2. Agendar Consulta
  3. Lista de Consultas Agendadas
  4. Cancelar Consulta
  5. Relatório de Consultas
  6. Adicionar Horários
  0. Sair''')

  escolha = input("Escolha a opção desejada: ")

  if escolha == "1":
    cadastrarMedico()

  elif escolha == "2":
    agendarConsulta()

  elif escolha == "3":
    listarConsultas()

  elif escolha == "4":
    cancelarConsulta()

  elif escolha == "5":
    gerarRelatorio()

  elif escolha == "6":
    adicionarHorarios()

  elif escolha == "0":
    print('Obrigado por acessar nosso Sistema... Até logo')
    break

  else:
    print("Opção inválida. Tentenovamente.")

