# Solicita ao usuário que insira as coordenadas geográficas
coordenadas = tuple(map(float, input("Digite a latitude e longitude separadas por espaço: ").split()))

# Desempacotamento da tupla
latitude, longitude = coordenadas

# Exibe as coordenadas
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
