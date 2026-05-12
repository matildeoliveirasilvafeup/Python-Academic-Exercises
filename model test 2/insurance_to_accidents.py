def insurance_totals(cars):
    totals = {}
    for plate, info in cars.items():
        accidents = info[2]   # list of (insurance_company, damage_value)

        for company, value in accidents:
            if company not in totals.keys():
                totals[company] = (1, value)
            else:
                count, total = totals[company] #pega os valores atuais !!!
                totals[company] = (count + 1, total + value) #como ja nao é a primeira vez adiciona 1 ao count de acidentes por seguradora,
                #adiciona value ao total

    return totals

