import ast
import os
while True:
    print("1 - REGISTRAR PACIENTE")
    print("2 - BUSCAR PACIENTE")
    print('3 - INTERNAR PACIENTE')
    print('4 - PRESCREVER PACIENTE')
    print("5 - SAIR")
    op = int(input(""))
    os.system("cls")
    if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('Opção incorreta!\nAPERTE ENTER PARA VOLTAR');input('')
        os.system("cls")
    elif op == 1:
        M = 's'
        while M == 's':
            dicregisto = {}
            print("REGISTRO DE PACIENTE")
            name = input("Nome completo do paciente: ")
            dicregisto['Name'] = name
            raca = input('Etnia do paciente: ')
            dicregisto['Raça'] = raca
            genitores = input("Nome do(a) genitor(a): ")
            dicregisto['Genitor(a)'] = genitores
            rg = input("RG: ")
            dicregisto['RG'] = rg
            cpf = input("CPF: ")
            dicregisto['CPF'] = cpf
            print("ENDEREÇO COMPLETO DO PACIENTE")
            city = input("Cidade: ").lower()
            city = city[0].upper()+city[1:]
            dicregisto['City'] = city
            stats = input("Estado: ").upper()
            dicregisto['City'] += ('-'+stats[0:2])
            street = input("Nome da rua: ")
            dicregisto['Address'] = street
            opp = input("Apartamento ou casa? ").lower().startswith('a')
            if opp:
                numero = input("Numero do apartamento: ")
                dicregisto['Address'] += (' Apt N°:'+numero)
            else:
                numero = input("Numero da casa: ")
                dicregisto['Address'] += (' Casa N°:' + numero)
            phone = input("Telefone do responsável com DDD: ")
            dicregisto['Phone'] = phone
            os.system("cls")
            N = [name]
            N = name.split(" ")
            print("Deseja guardar os dados do paciente "+N[0]+"?")
            print('Nome : '+dicregisto['Name'])
            print('Etnia do paciente: '+dicregisto['Raça'])
            print('Genitor(a): '+dicregisto['Genitor(a)'])
            print('Cidade: '+dicregisto['City'])
            print('Endereço: '+dicregisto['Address'])
            print('RG: '+dicregisto['RG'])
            print('CPF: '+dicregisto['CPF'])
            print('Telefone: '+dicregisto['Phone'])
            while True:
                oppp = input("(S/N)\n").lower()
                os.system("cls")
                if oppp == 's':
                    with open ('cadastroPaciente.txt','a+') as file:
                        file.write(str(dicregisto)+'\n')
                    file.close()
                    M = 'n'
                    break
                elif oppp == 'n':
                    M = 'n'
                    break
    elif op == 2:
        R = True
        while R:
            print('BUSCA DE PACIENTE\n1 - PACIENTE INTERNADO\n2 - PACIENTE CADASTRADO\n3 - PACIENTE COM PRESCRIÇÃO MEDICA\n4 - VOLTAR PARA MENU PRINCIPAL');busca = int(input(''))
            os.system("cls")
            if busca == 1:
                print('BUSCA DE PACIENTE INTERNADO')
                name = input('Digite o nome completo: ')
                with open('internaPaciente.txt', 'r+') as arq:
                    for i in arq:
                        dicBusca = ast.literal_eval(i)
                        if dicBusca['Name'] == name:
                            print('SEGUE OS DADOS DO PACIENTE\n')
                            print('Nome : ' + dicBusca['Name'])
                            print('CPF: ' + dicBusca['CPF'])
                            print('Enfermaria: ' + dicBusca['Enfermaria'])
                            print('Leito: ' + dicBusca['Leito'])
                            R = input("Quer tentar outro nome?(S/N)\n").lower().startswith('s')
                            os.system("cls")
                            break
                    if dicBusca['Name'] != name:
                        R = input('Paciente não encontrado!\nDeseja continuar buscando?(S/N)\n').lower().startswith('s')
                        os.system("cls")
            elif busca == 2:
                print('BUSCA DE PACIENTE CADASTRADO')
                name = input('Digite o nome completo: ')
                with open('cadastroPaciente.txt', 'r+') as arq:
                    for i in arq:
                        dicBusca = ast.literal_eval(i)
                        if dicBusca['Name'] == name:
                            print('SEGUE OS DADOS DO PACIENTE\n')
                            print('Nome : ' + dicBusca['Name'])
                            print('Etnia do paciente: ' + dicBusca['Raça'])
                            print('Genitor(a): ' + dicBusca['Genitor(a)'])
                            print('Cidade: ' + dicBusca['City'])
                            print('Endereço: ' + dicBusca['Address'])
                            print('RG: ' + dicBusca['RG'])
                            print('CPF: ' + dicBusca['CPF'])
                            print('Telefone: ' + dicBusca['Phone'])
                            R = input("Quer tentar outro nome?(S/N)\n").lower().startswith('s')
                            os.system("cls")
                            break
                    if dicBusca['Name'] != name:
                        R = input('Paciente não encontrado!\nDeseja continuar buscando?(S/N)\n').lower().startswith('s')
                        os.system("cls")
            elif busca == 3:
                print('BUSCA DE PACIENTE COM PRESCRIÇÃO')
                name = input('Digite o nome completo: ')
                with open('prescriPaciente.txt', 'r+') as arq:
                    for i in arq:
                        dicBusca = ast.literal_eval(i)
                        if dicBusca['Name'] == name:
                            print('SEGUE OS DADOS DO PACIENTE\n')
                            print('Nome : ' + dicBusca['Name'])
                            print('CPF: ' + dicBusca['CPF'])
                            print('Enfermaria: ' + dicBusca['Enfermaria'])
                            print('Leito: ' + dicBusca['Leito'])
                            print('Medicamento: ' + dicBusca['Medicamento'])
                            print('Concentração: ' + dicBusca['Concentração'])
                            print('Horário(s): ' + dicBusca['Horario'])
                            print('Via de administração: ' + dicBusca['Viadm'])
                            print('Descrição da diluição: ' + dicBusca['Dilui'])
                            R = input("Quer tentar outro nome?(S/N)\n").lower().startswith('s')
                            os.system("cls")
                            break
                    if dicBusca['Name'] != name:
                        R = input('Paciente não encontrado!\nDeseja continuar buscando?(S/N)\n').lower().startswith('s')
                        os.system("cls")
            elif busca == 4:
                os.system("cls")
                break
            elif busca != 1 and busca != 2 and busca != 3 and busca != 4:
                print('Opção incorreta!\nAPERTE ENTER PARA VOLTAR');input('')
                os.system("cls")
    elif op == 3:
        R = True
        while R:
            print('INTERNAÇÃO DE PACIENTE\nPara internar, o paciente antes precisa ter cadastro.')
            name = input('Digite o nome completo: ')
            with open('cadastroPaciente.txt', 'r+') as arq:
                for i in arq:
                    dicInterna = ast.literal_eval(i)
                    if dicInterna['Name'] == name:
                        print('SEGUE OS DADOS DO PACIENTE\n')
                        print('Nome : ' + dicInterna['Name'])
                        print('CPF: ' + dicInterna['CPF'])
                        R = input('O(A) paciente '+dicInterna['Name']+' será internado(a)?(S/N)\n').lower().startswith('s')
                        os.system("cls")
                        if R:
                            enfermaria = input('Enfermaria do paciente(A,B, ou C): ').upper()
                            dicInterna['Enfermaria'] = enfermaria
                            leito = input('Leito(1,2 ou 3): ')
                            dicInterna['Leito'] = leito+enfermaria[0]
                            with open('internaPaciente.txt','a+') as file:
                                file.write(str(dicInterna)+'\n')
                            R = input('Paciente internado com sucessso!\nDeseja fazer nova internação?(S/N)\n').lower().startswith('s')
                            os.system("cls")
                        break
                if dicInterna['Name'] != name:
                    R = input('Paciente não encontrado!\nDeseja continuar buscando?(S/N)\n').lower().startswith('s')
                    os.system("cls")
    elif op == 4:
        R = True
        while R:
            print('BUSCA DE PACIENTE INTERNADO\nA função deve ser usada por médicos para prescrição de pacientes.')
            name = input('Digite o nome completo: ')
            with open('internaPaciente.txt', 'r+') as arq:
                for i in arq:
                    dicInterna = ast.literal_eval(i)
                    if dicInterna['Name'] == name:
                        print('SEGUE OS DADOS DO PACIENTE\n')
                        print('Nome : ' + dicInterna['Name'])
                        print('CPF: ' + dicInterna['CPF'])
                        print('Enfermaria: ' + dicInterna['Enfermaria'])
                        print('Leito: ' + dicInterna['Leito'])
                        R = input('O(A) paciente '+dicInterna['Name']+' será atendido(a)?(S/N)\n').lower().startswith('s')
                        os.system("cls")
                        if R:
                            medicamento = input('Medicamento do(a) paciente: ')
                            dicInterna['Medicamento'] = medicamento
                            concentra = input('Concentração do medicamento: ')
                            dicInterna['Concentração'] = concentra
                            horario = input('Horário(s) da medicação (HH/MM): ').lower()
                            dicInterna['Horario'] = horario
                            viadm = input('Via de administração: ').lower()
                            dicInterna['Viadm'] = viadm
                            dilui = input('Descrição da diluição do medicamento\n')
                            dicInterna['Dilui'] = dilui
                            with open('prescriPaciente.txt','a+') as file:
                                file.write(str(dicInterna)+'\n')
                            R = input('Prescrição realizada com sucessso!\nDeseja fazer nova prescrição?(S/N)\n').lower().startswith('s')
                            os.system("cls")
                            if R == False:
                                break
                            else:
                                break
                        else:
                            break
                if dicInterna['Name'] != name:
                    R = input('Paciente não encontrado!\nDeseja continuar buscando?(S/N)\n').lower().startswith('s')
                    os.system("cls")
    elif op == 5:
        os.system("cls")
        break