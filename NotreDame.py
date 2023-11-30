medicos = [['Victor', 'Cardiologista', [12, 13, 14, 15]], ['Lucas', 'Pediatra',[12, 13, 14, 15]], ['Felipe', 'Otorrino',[12, 13, 14, 15]], ['João', 'Psicologo', [12, 13, 14, 15]], ['Pedro', 'Anestesista', [12, 13, 14, 15]]]

consultasAgendadas = []
mensagens = []

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


def participarDeConsultas():
    '''
    :return: Função para permitir que o usuário participe de uma consulta agendada.
    '''

    listarConsultas()
    if consultasAgendadas:
        numeroConsulta = int(input('Escolha o número da consulta para participar: ')) - 1
        if 0 <= numeroConsulta < len(consultasAgendadas):
            consultaEscolhida = consultasAgendadas[numeroConsulta]
            print(f'Você escolheu participar da consulta agendada para o Dr.{consultaEscolhida[1]} no dia {consultaEscolhida[3]} às {consultaEscolhida[4]}.')
            print('A consulta está marcada para amanhã!')
        else:
            print('Número de consulta inválido.')
    else:
        print('Não há consultas agendadas.')


def chatPrivadoComDoutor():
    '''
    :return: Função para permitir que o usuário tenha um chat privado com o médico.
    '''

    listarConsultas()
    if consultasAgendadas:
        numeroConsulta = int(input('Escolha o número da consulta para iniciar o chat privado: ')) - 1
        if 0 <= numeroConsulta < len(consultasAgendadas):
            consultaEscolhida = consultasAgendadas[numeroConsulta]
            medico = consultaEscolhida[1]
            horarioDisponivel = '8:00'
            print(f'O doutor {medico} estará disponível para um chat privado a partir das {horarioDisponivel} no dia seguinte.')
            mensagem = input('Deixe sua mensagem para o Doutor que ele responderá assim que possível: ')
            mensagem = f'Dr. {medico}: Mensagem enviada: {mensagem}'
            mensagens.append(mensagem)
            print('Mensagem enviada com sucesso!')
        else:
            print('Número de consulta inválido.')
    else:
        print('Não há consultas agendadas.')

def verMensagens():
    print('''
    Mensagens enviadas
    ------------------
    ''')
    print(mensagens)

def duvidasFrequentes():
    '''

    :return: Função com algumas possíveis duvidas do usario
    '''
    while True:
        duvida = input('''
Selecione alguma dúvida:
        
    1. Como faço para agendar consultas?
    2. Quanto tempo geralmente dura uma consulta?
    3. Qual o valor das consultas?
    4. Por onde eu acesso a consulta?
    0. Sair
    ''')



        if duvida == '0':
            break

        elif duvida == '1':
            print('Para agendar uma consulta você deverá selecionar a opção numero "1" do nosso sistemas\nonde você podera escolher o Doutor e sua especialidade de acordo com suas necessidades.')
            maisDuvida = input('Tem mais alguma duvida? S/N')
            maisDuvida = maisDuvida.upper()
            if maisDuvida == 'S':
                pass
            elif maisDuvida == 'N':
                break
            else:
                print('opção inválida!')
                break

        elif duvida == '2':
            print('O tempo médio das consultas é de 1 hora, porem o tempo pode variar dependendo do caso.')
            maisDuvida = input('Tem mais alguma duvida? S/N')
            maisDuvida = maisDuvida.upper()
            if maisDuvida == 'S':
                pass
            elif maisDuvida == 'N':
                break
            else:
                print('opção inválida!')

        elif duvida == '3':
            print('O valor das cosultas variam de acordo com o profissional e da consulta solicitada.')
            maisDuvida = input('Tem mais alguma duvida? S/N')
            maisDuvida = maisDuvida.upper()
            if maisDuvida == 'S':
                pass
            elif maisDuvida == 'N':
                break
            else:
                print('opção inválida!')

        elif duvida == '4':
            print('Você pode acessar a sua consulta pela opção numero "4" do nosso sistema onde lá você irá \n'
                  'selicionar a consulta de acordo com seus agendamentos.')
            maisDuvida = input('Tem mais alguma duvida? S/N')
            maisDuvida = maisDuvida.upper()
            if maisDuvida == 'S':
                pass
            elif maisDuvida == 'N':
                break
            else:
                print('opção inválida!')

while True:
    print('''
      Seja Bem-vindo ao sistema do Hospital Notre Dame
      ------------------------------------------------
  1. Agendar Consulta
  2. Lista de Consultas Agendadas
  3. Cancelar Consulta
  4. Participar de consultas
  5. Chat Privado com o Doutor
  6. Ver Mensagens
  7. Duvidas Frequentes
  0. Sair''')

    escolha = input("Escolha a opção desejada: ")


    if escolha == "1":
        agendarConsulta()

    elif escolha == "2":
        listarConsultas()

    elif escolha == "3":
        cancelarConsulta()

    elif escolha == "4":
        participarDeConsultas()

    elif escolha == "5":
        chatPrivadoComDoutor()

    elif escolha == '6':
        verMensagens()

    elif escolha == '7':
        duvidasFrequentes()

    elif escolha == "0":
        print('Obrigado por acessar nosso Sistema... Até logo')
        break

    else:
        print("Opção inválida. Tentenovamente.")

