from OpenDSS import OpenDSS
from OpenDSS import mon_power
from OpenDSS import mon_voltage

nome = input('Qual é seu nome: ')
# if nome is type(str):
#     nome = nome.upper(nome)
# else:
#     print('Por favor insira apenas letras')
    

print('Vamos começar a roda o OpenDss no caso de 13 barras com ou sem PV, tudo bem %s?' %(nome))

pv_or_not = input('Com ou sem gd? (responda com s ou n) ')

if pv_or_not == 'n':

    print("Perfeito você respondeu '%s' " %(pv_or_not))
    power_or_voltage = input("medidor power ou voltage? (responda com p ou v)")
    if power_or_voltage == 'p':
        ativo_or_reativo = input("Potência ativa ou reativa? (responda com A ou R) ")
        if ativo_or_reativo == 'A':
            solve_power = mon_power()
            ativa = solve_power.pot_ativa()

        if ativo_or_reativo == 'R':
            solve_power = mon_power()
            reativa = solve_power.pot_reativa()

    if power_or_voltage == 'v':

        tensao_or_corrente = input("Tensão ou Corrente? (responda com t ou c) ")
        if tensao_or_corrente == 't':
            solve_voltage = mon_voltage()
            tensao = solve_voltage.tensao()

        if tensao_or_corrente == 'c':
            solve_voltage = mon_voltage()
            corrente = solve_voltage.corrente()
    
    print("%s, você pode encontrar os resultados em 'Resultados mon_power' e 'Resultados mon_voltage'")


