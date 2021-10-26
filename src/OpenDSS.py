"""
Universidade Estadual de Campinas - UNICAMP
IT745 - Geração Distribuída de Energia Elétrica
Written by Marcus Felipy Glatz Rodrigues <m264538@dac.unicamp.br>
"""

# Imports para o script
import dss
import pandas as pd
import matplotlib.pyplot as plt

# OpenDSS objeto
solver_dss = dss.DSS
# Método para solve
circuit = solver_dss.ActiveCircuit
# Método comando por texto
text = solver_dss.Text

# Adicionando caso de estudo 13Bus_IEEE
text.Command = "Redirect 13Bus/IEEE13Nodeckt.dss"
text.Command = "compile 13Bus/IEEE13Nodeckt.dss"

# Solve OpenDSS
circuit.Solution.Solve()

# Exportando os monitores para formato .csv
text.Command = f'Export monitors linha1_voltage'
text.Command = f'Export monitors linha1_power'
# Comando para mostrar informações relevantes
text.Command = f'Show voltage ln nodes'
text.Command = f'Show Powers kva elem'

# Pegando informações do medidor_power e adicionando em um Data Frame
mon_power = pd.read_csv('IEEE13Nodeckt_Mon_linha1_power.csv', sep=',')
df_power = pd.DataFrame(mon_power)

# Pegando informações do medidor_voltage e adicionando em um Data Frame
mon_voltage = pd.read_csv('IEEE13Nodeckt_Mon_linha1_voltage.csv', sep=',')
df_voltage = pd.DataFrame(mon_voltage)

# Descobrindo a posição de cada elemento do data frame para o mon_power
head_power = []
for i in df_power:
    head_power == head_power.append(i)

# Descobrindo a posição de cada elemento do data frame para o mon_voltage
head_voltage = []
for i in df_voltage:
    head_voltage == head_voltage.append(i)


# Função para potência ativa
def pot_ativa(head=head_power, df=df_power):
    head_power = head
    df_power = df
    # Adicionando os nomes para cada elemento para potência
    p1_name = head_power[2]
    p2_name = head_power[4]
    p3_name = head_power[6]
    # Transformando potências em listas
    p1 = df_power[p1_name].tolist()
    p2 = df_power[p2_name].tolist()
    p3 = df_power[p3_name].tolist()
    # Plotagem para potência ativa
    plt.title("Representação das Curvas de potência ativa em cada fase")
    plt.ylabel('KW')
    plt.xlabel('Horas do dia')
    plt.plot(p1, 'r', label='P1')
    plt.plot(p2, 'b', label='P2')
    plt.plot(p3, 'g', label='P3')
    plt.legend()
    plt.savefig("../Potência_ativa.png")


# Função para potência reativa
def pot_reativa(head=head_power, df=df_power):
    head_power = head
    df_power = df
    # Adicionando os nomes para cada elemento para potência
    q1_name = head_power[3]
    q2_name = head_power[5]
    q3_name = head_power[7]
    # Transformando potências em listas
    q1 = df_power[q1_name].tolist()
    q2 = df_power[q2_name].tolist()
    q3 = df_power[q3_name].tolist()
    # Plotagem para potência reativa
    plt.title("Representação das Curvas de potência reativa em cada fase")
    plt.ylabel('KVAR')
    plt.xlabel('Horas do dia')
    plt.plot(q1, 'r', label='Q1')
    plt.plot(q2, 'b', label='Q2')
    plt.plot(q3, 'g', label='Q3')
    plt.legend()
    plt.savefig("../Potência_reativa.png")


def tensao(head=head_voltage, df=df_voltage):
    head_voltage = head
    df_voltage = df
    # Adicionando os nomes para cada elemento para tensão
    v1_name = head_voltage[2]
    v2_name = head_voltage[4]
    v3_name = head_voltage[6]
    # Transformando tensão em listas
    v1 = df_voltage[v1_name].tolist()
    v2 = df_voltage[v2_name].tolist()
    v3 = df_voltage[v3_name].tolist()
    # Plotagem para tensão
    plt.title("Gráfico da Variação de Tensão em cada fase do sistema")
    plt.ylabel('Volts')
    plt.xlabel('Horas do dia')
    plt.plot(v1, 'r', label='V1')
    plt.plot(v2, 'b', label='V2')
    plt.plot(v3, 'g', label='V3')
    plt.legend()
    plt.savefig("../Tensão.png")


def corrente(head=head_voltage, df=df_voltage):
    head_voltage = head
    df_voltage = df
    # Adicionando os nomes para cada elemento para corrente
    i1_name = head_voltage[8]
    i2_name = head_voltage[10]
    i3_name = head_voltage[12]
    # Transformando corrente em listas
    i1 = df_voltage[i1_name].tolist()
    i2 = df_voltage[i2_name].tolist()
    i3 = df_voltage[i3_name].tolist()
    # Plotagem para corrente
    plt.title("Gráfico da Variação de Corrente em cada fase do sistema")
    plt.ylabel('Ampéres')
    plt.xlabel('Horas do dia')
    plt.plot(i1, 'r', label='I1')
    plt.plot(i2, 'b', label='I2')
    plt.plot(i3, 'g', label='I3')
    plt.legend()
    plt.savefig("../Corrente.png")


plot = pot_ativa()
