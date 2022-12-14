Entrada = open('Entrada.txt', 'r')
Saida = open('Saida.txt', 'w')


def main():
    tick = 0
    counter = 0
    serverNum = 1
    custo = 0
    servidoresInativos = 0
    concluido = False
    serverList = {}
    totalUsersServ = 0
    order = []

    for cnt, line in enumerate(Entrada):
        if cnt == 0:
            ttask = int(line)
            if ttask >= 1 and ttask <= 10:
                continue
            else:
                print('Erro: ttask fora dos limites!')
                exit()
        elif cnt == 1:
            umax = int(line)
            if umax >= 1 and ttask <= 10:
                continue
            else:
                print('Erro: umax fora dos limites!')
                exit()
        else:
            order.append(int(line))

    while concluido == False:
        try:
            line = order[counter]
        except:
            line = 0
        tick += 1

        if tick > ttask:
            try:
                pos = order[tick-ttask-1]
            except:
                pos = 0
            for n in range(pos):
                for servidor in serverList:
                    if serverList[servidor]['NumUser'] > 0:
                        serverList[servidor]['NumUser'] = int(serverList[servidor]['NumUser']) - 1
                        if serverList[servidor]['NumUser'] == 0:
                            serverList[servidor]['Status'] = 'Inativo'
                        break
                    else:
                        serverList[servidor]['Status'] = 'Inativo'
            #counter += 1

        for i in range(line):
            totalUsersServ += 1
            if totalUsersServ <= umax:
                try:
                    serverList['Servidor'+str(serverNum)]['NumUser'] = totalUsersServ
                except:
                    serverList['Servidor'+str(serverNum)] = {'NumUser': totalUsersServ, 'Status': 'Ativo'}
            else:
                totalUsersServ = 1
                serverNum += 1
                serverList['Servidor'+str(serverNum)] = {'NumUser': totalUsersServ, 'Status': 'Ativo'}

        output = ''
        for j, servidor in enumerate(serverList):
            if serverList[servidor]['Status'] == 'Inativo':
                servidoresInativos += 1
            else:
                try:
                    serverList[servidor]['Tick'] += 1
                except:
                    serverList[servidor]['Tick'] = 1
                output = output + str(serverList[servidor]['NumUser']) + ','
                servidoresInativos = 0
        if output == '':
            print('0')
            Saida.write('0\n')
        else:
            print(output[:-1])
            Saida.write(output[:-1]+'\n')

        if order[0] != 0:
            if servidoresInativos == len(serverList):
                concluido = True

        counter += 1
        print(serverList)

    for servidor in serverList:
        custo = custo + (serverList[servidor]['Tick'] * 1)

    print(custo)
    Saida.write(str(custo)+'\n')
    Entrada.close()
    Saida.close()
    print('Processamento Concluido com Sucesso!')

main()
