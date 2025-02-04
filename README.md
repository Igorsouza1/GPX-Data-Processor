# GPX Data Processor

## 📌 Descrição
Este projeto permite processar arquivos GPX para extrair informações essenciais, como:
- **Distância percorrida** (km)
- **Dias ativos**
- **Tempo total de atividade** (horas e minutos)
- **Waypoints** (latitude, longitude, elevação)

Além disso, os waypoints podem ser exportados para um único arquivo XLSX ou arquivos separados por nome de arquivo.

## 🚀 Funcionalidades
✅ Suporte a múltiplos arquivos GPX simultaneamente
✅ Correção automática de coordenadas no formato incorreto (vírgulas substituídas por pontos)
✅ Cálculo preciso de distâncias com `geopy.distance`
✅ Processamento de timestamps para calcular tempo ativo
✅ Exportação de waypoints para arquivos Excel
✅ Mensagens de status detalhadas para cada arquivo

## 🛠 Tecnologias Utilizadas
- Python 3
- `gpxpy` para parsing de arquivos GPX
- `geopy.distance` para cálculo de distâncias
- `pandas` para manipulação de dados
- `google.colab` para upload e download de arquivos

## 📥 Como Usar
1. Faça a cópia do código no colab
2. Instale gpxpy geopy
3. Execute o código
4. Escolha os arquivos

Teste: https://colab.research.google.com/drive/1VzDt65irtzMp1q_-p5ocTamf89SkGphW#scrollTo=s3CbdGhDCQo8

## 📌 Exemplo de Saída
```plaintext
==================================================
📂 Arquivo: trilha1.gpx
🚶‍♂️ Distância percorrida: 12.34 km
📅 Dias ativos: 3
⏳ Tempo total de atividade: 5 horas e 45 minutos
==================================================

🎯 Resumo Final (Todos os Arquivos GPX)
==================================================
🚶‍♂️ Distância total percorrida: 30.21 km
📅 Total de dias ativos: 5
⏳ Tempo total de atividade: 12 horas e 20 minutos
==================================================
```

## 🔧 Requisitos
- Google Colab
- Bibliotecas Python instaladas: `gpxpy`, `geopy`, `pandas`

## 📌 Melhorias Futuras
🔹 Suporte a visualização de trilhas no mapa
🔹 Integração com APIs de mapas para análises geográficas
🔹 Melhor otimização no tratamento de arquivos grandes

## 📝 Licença
Este projeto é open-source e está disponível sob a licença MIT.

