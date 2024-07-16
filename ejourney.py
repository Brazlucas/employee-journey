#!/usr/bin/env python3

from datetime import datetime, timedelta
import os

def calcular_horario_saida(entrada_str, almoco_saida_str, almoco_retorno_str):
    # Converte strings de entrada em objetos datetime
    entrada = datetime.strptime(entrada_str, '%H:%M')
    almoco_saida = datetime.strptime(almoco_saida_str, '%H:%M')
    almoco_retorno = datetime.strptime(almoco_retorno_str, '%H:%M')
    
    # Jornada de trabalho de 8 horas e 48 minutos
    jornada_diaria = timedelta(hours=8, minutes=48)
    
    # Calcula o tempo trabalhado antes do almoço
    tempo_trabalhado_manha = almoco_saida - entrada
    
    # Calcula o tempo restante para completar a jornada diária
    tempo_restante = jornada_diaria - tempo_trabalhado_manha
    
    # Calcula o horário de saída
    horario_saida = almoco_retorno + tempo_restante
    
    return horario_saida.strftime('%H:%M')

# Inputs
entrada_str = input("Hora de entrada (HH:MM): ")
almoco_saida_str = input("Hora de saída para almoço (HH:MM): ")
almoco_retorno_str = input("Hora de retorno do almoço (HH:MM): ")

# Calcula o horário de saída
horario_saida = calcular_horario_saida(entrada_str, almoco_saida_str, almoco_retorno_str)
print(f"Você pode sair às {horario_saida}.")

notification = input("Você deseja receber um alerta? [Y/n] ")

if (notification != "n"):
    os.system(f'echo "notify-send \'Hora de sair!\' \'Você pode sair às {horario_saida}.\'" | at "{horario_saida}"')
else
    print("Bom trabalho!")
```
