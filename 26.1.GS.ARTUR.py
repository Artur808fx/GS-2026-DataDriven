# =============================================================
# Global Solutions - 1º Semestre 2026
# Disciplina: Data Driven Application & Data Science
# Professora: Patrícia Angelini
# Integrantes: ARTUR NOLETO DA SILVA RM: 572875
# Representante: ARTUR NOLETO DA SILVA 
# =============================================================



# LISTAS DE ARMAZENAMENTO


tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []


# 1. ENTRADA DE DADOS


# Solicita a quantidade de eventos com validação
while True:
    try:
        quantidade = int(input("Insira a quantidade de eventos: "))
        if quantidade > 0:
            break
        else:
            print("A quantidade deve ser maior que zero.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

# Coleta os dados de cada evento
for i in range(quantidade):
    print(f"\n--- Evento {i + 1} ---")

    tipo = input("Tipo (ex: desmatamento, queimadas): ").strip()
    tipos_eventos.append(tipo)

    pais = input("País: ").strip()
    paises.append(pais)

    regiao = input("Região: ").strip()
    regioes.append(regiao)

    cidade = input("Cidade: ").strip()
    cidades.append(cidade)

    # Validação da área afetada (deve ser maior que zero)
    while True:
        try:
            area = float(input("Área afetada (km²): "))
            if area > 0:
                areas_afetadas.append(area)
                break
            else:
                print("A área deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número.")

    # Validação da intensidade (deve estar entre 1 e 10)
    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if 1 <= intensidade <= 10:
                intensidades.append(intensidade)
                break
            else:
                print("A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    # Validação das ocorrências (deve ser maior que zero)
    while True:
        try:
            num_ocorrencias = int(input("Número de ocorrências: "))
            if num_ocorrencias > 0:
                ocorrencias.append(num_ocorrencias)
                break
            else:
                print("O número de ocorrências deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


# 3. ANÁLISE DE DADOS


# a) Total de eventos registrados
total_eventos = len(tipos_eventos)

# b) Soma total das áreas afetadas
soma_areas = 0
for area in areas_afetadas:
    soma_areas += area

# c) Média das intensidades
soma_intensidades = 0
for intens in intensidades:
    soma_intensidades += intens
media_intensidades = soma_intensidades / total_eventos

# d) Evento com maior área afetada
maior_area = max(areas_afetadas)
indice_maior_area = areas_afetadas.index(maior_area)

# e) Região com maior número de ocorrências
maior_ocorrencia = max(ocorrencias)
indice_maior_ocorrencia = ocorrencias.index(maior_ocorrencia)
regiao_mais_ocorrencias = regioes[indice_maior_ocorrencia]

# f) Densidade média (ocorrências ÷ área)
soma_densidades = 0
for j in range(total_eventos):
    soma_densidades += ocorrencias[j] / areas_afetadas[j]
densidade_media = soma_densidades / total_eventos

# g) Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0
for intens in intensidades:
    if intens > media_intensidades:
        eventos_acima_media += 1

# h) Evento mais crítico (maior intensidade + maior área)
# Calculamos uma pontuação combinada: intensidade normalizada + área normalizada
max_intensidade = max(intensidades)
max_area = max(areas_afetadas)

pontuacao_critica = []
for j in range(total_eventos):
    # Normaliza cada fator entre 0 e 1 e soma
    peso = (intensidades[j] / max_intensidade) + (areas_afetadas[j] / max_area)
    pontuacao_critica.append(peso)

indice_mais_critico = pontuacao_critica.index(max(pontuacao_critica))



# 4. RELATÓRIO DE RESULTADOS



print("\n========================================")
print("        RELATÓRIO DE ANÁLISE")
print("========================================")

print(f"\nTotal de eventos registrados: {total_eventos}")

print("\n----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")
print(f"Área total afetada: {soma_areas:.0f} km²")
print(f"Média de intensidade: {media_intensidades:.1f}")

print("\n----------------------------------------")
print("Análises")
print("----------------------------------------")
print(f"Região com maior número de ocorrências: {regiao_mais_ocorrencias}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")
print(f"Tipo: {tipos_eventos[indice_mais_critico]}")
print(f"Local: {cidades[indice_mais_critico]}, {regioes[indice_mais_critico]}, {paises[indice_mais_critico]}")
print(f"Intensidade: {intensidades[indice_mais_critico]}")
print(f"Área afetada: {areas_afetadas[indice_mais_critico]:.0f} km²")

print("\n========================================")
print(f"Total de desastres registrados: {total_eventos}")
