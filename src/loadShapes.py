"""
Universidade Estadual de Campinas - UNICAMP
IT745 - Geração Distribuída de Energia Elétrica
Academics
    Marcus Felipy Glatz Rodrigues <m264538@dac.unicamp.br>
    Jeremias Nhonga David Camarada <j234614@dac.unicamp.br>
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

shape_system = pd.read_csv(r"Resultados load_shape/load_shape-13bus.csv", sep=',')
df_system = pd.DataFrame(shape_system)
# print(df_system)
head_system = []
for i in df_system:
    head_system == head_system.append(i)

time_name = head_system[0]
values_name = head_system[-1]

time = df_system[time_name].to_list()
values = df_system[values_name].to_list()

values_certo = []

obj = {'valores': values}
for val in obj.keys():
    for i in obj[val]:
        if any(txt in i for txt in [","]):
            i = i.replace(",", ".")
            values_certo == values_certo.append(float(i))
             

print(time)
print(values)
print(values_certo)

plt.figure(figsize=(14, 6))
plt.plot(time, values_certo)
plt.title("Load Shape da carga residêncial", fontsize=15)
plt.ylabel('Potência da carga', fontsize=10)
plt.xlabel('Horas do dia', fontsize=10)
# plt.plot(values, 'r', label='loadShape')
# # plt.plot(p3, 'g', label='P3')
# plt.xticks(np.arange(24), ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',\
#     '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'])
plt.yticks([0, .25, .5, .75, 1], ["0%", "25%", "50%", "75%", "100%"])
# plt.legend()
plt.savefig(r"Resultados load_shape/load_shape-13bus.png")

