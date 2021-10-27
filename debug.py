"""
Universidade Estadual de Campinas - UNICAMP
IT745 - Geração Distribuída de Energia Elétrica
Academics
    Marcus Felipy Glatz Rodrigues <m264538@dac.unicamp.br>
    Jeremias Nhonga David Camarada <j234614@dac.unicamp.br>
"""

from src.OpenDSS import OpenDSS
from src.OpenDSS import mon_power
from src.OpenDSS import mon_voltage

# Debug é para saídas do medidor 'mon power' e 'mon voltage'

output = input("Saída do medidor 'mon power' ou do medidor 'mon voltage'? \
    (resposta com *power* para 'mon power' e *voltage* para 'mon voltage'):\n ")
output = output.upper()

if output in 'POWER':
    solve_power = mon_power()
    ativa_or_reativa = input("Plot de potência ativa ou reativa? \
        (resposta com *kw* para ativa e *kvar* para reativa):\n ")
    ativa_or_reativa = ativa_or_reativa.upper()

    if ativa_or_reativa in 'KW':
        solve_power.pot_ativa()

    elif ativa_or_reativa in 'KVAR':
        solve_power.pot_reativa()
    
    elif ativa_or_reativa is None:
        print('Entrada não é uma string')

    else:
        print("Except Error: Resposta com kw ou kvar")

elif output in 'VOLTAGE':
    solve_voltage = mon_voltage()
    tensao_ou_corrente = input("Plot de tensão ou corrente? \
        (resposta com *v* para tensão e *i* para corrente):\n ")

    tensao_ou_corrente = tensao_ou_corrente.upper()

    if tensao_ou_corrente in 'V':
        solve_voltage.tensao()

    elif tensao_ou_corrente in 'I':
        solve_voltage.corrente()
    
    elif tensao_ou_corrente is None:
        print('Entrada não é uma string')

    else:
        print("Except Error: Resposta com v ou i")

elif output is None:
    print('Entrada não é uma string')

else:
    print("Except Error: Resposta com power ou voltage")
