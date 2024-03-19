temperatura = int(input("quantos graus está?\n"))

if temperatura <= 15:
    print("está frio")
elif temperatura >= 25:
    print("está calor")
elif temperatura <= 24 and temperatura >= 16:
    print("temperatura esta agradavel")