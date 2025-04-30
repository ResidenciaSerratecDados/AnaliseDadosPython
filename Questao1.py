area = float(input("Digite a área do cômodo: "))
watts = area * 3
lampada = int(area/3)
potencia_lampada = int(watts/lampada)
potencia_total = lampada * potencia_lampada 

print("\n")
print("Potência Máxima do Cômodo é " + str(watts) + " Watts")
print("Quantidade de Lâmpadas: ", lampada)
print("Potência de cada Lâmpada é " + str(potencia_lampada) + " Watts")
print("Potência Total no Cômodo: ", potencia_total)