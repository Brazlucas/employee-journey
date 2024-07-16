#!/usr/bin/env python3

import re
from datetime import datetime, timedelta
import os

def validar_e_formatar_horario(horario_str):
    # Remove todos os caracteres não numéricos
    horario_str = re.sub(r'\D', '', horario_str)
    
    # Garante que o horário tem exatamente 4 dígitos
    if len(horario_str) != 4:
        raise ValueError("Horário deve conter exatamente 4 números (HHMM).")
    
    # Divide em horas e minutos
    horas = int(horario_str[:2])
    minutos = int(horario_str[2:])
    
    # Verifica se o horário é válido
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        raise ValueError("Horário inválido.")
    
    # Converte para o formato HH:MM
    return f"{horas:02}:{minutos:02}"

def obter_horario(mensagem):
    while True:
        horario_str = input(mensagem)
        try:
            return validar_e_formatar_horario(horario_str)
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

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
entrada_str = obter_horario("Hora de entrada (HHMM): ")
almoco_saida_str = obter_horario("Hora de saída para almoço (HHMM): ")
almoco_retorno_str = obter_horario("Hora de retorno do almoço (HHMM): ")

# Calcula o horário de saída
horario_saida = calcular_horario_saida(entrada_str, almoco_saida_str, almoco_retorno_str)
print(f"Você pode sair às {horario_saida}.")

notification = input("Você deseja receber um alerta? [Y/n] ")

if notification.lower() != 'n':
    os.system(f'echo "notify-send \'Hora de sair!\' \'Você pode sair às {horario_saida}.\'" | at "{horario_saida}"')
else:
    print("Bom trabalho!")
