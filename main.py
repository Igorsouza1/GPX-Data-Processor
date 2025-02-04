import gpxpy
import gpxpy.gpx
import pandas as pd
import os
import re
from datetime import timedelta
from google.colab import files

# 🔧 Função para corrigir arquivos GPX mal formatados
def fix_gpx_format(file_path):
    """
    Corrige arquivos GPX que possuem coordenadas no formato errado, trocando vírgulas por pontos.
    Retorna o caminho do novo arquivo corrigido.
    """
    fixed_path = file_path.replace(".gpx", "_fixed.gpx")

    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    # Substituir vírgulas por pontos apenas em coordenadas GPS
    fixed_content = re.sub(r'(-?\d+),(\d+)', r'\1.\2', content)

    with open(fixed_path, 'w', encoding="utf-8") as f:
        f.write(fixed_content)

    return fixed_path

# 🏃 Função para processar arquivos GPX
def process_gpx(file_path):
    """
    Processa arquivos GPX para extrair distância percorrida, tempo total e waypoints.
    """

    # 📌 Corrigir possíveis erros de formatação
    fixed_file_path = fix_gpx_format(file_path)

    try:
        with open(fixed_file_path, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
    except Exception as e:
        print(f"\n🚨 ERRO ao processar {file_path}: {e}")
        return 0, set(), timedelta(), []

    total_distance = 0
    activity_per_day = set()
    total_time = timedelta()
    waypoints = []
    file_name = os.path.basename(file_path)

    # 📍 Processar trilhas
    for track in gpx.tracks:
        for segment in track.segments:
            for i in range(1, len(segment.points)):
                total_distance += segment.points[i - 1].distance_2d(segment.points[i])
                activity_per_day.add(segment.points[i].time.date())

            if segment.points:
                start_time = segment.points[0].time
                end_time = segment.points[-1].time
                total_time += (end_time - start_time)

    # 🗺️ Processar waypoints
    for waypoint in gpx.waypoints:
        waypoints.append([file_name, waypoint.name, waypoint.latitude, waypoint.longitude, waypoint.elevation])

    total_distance_km_all += total_distance_km
    total_active_hours_all += total_active_hours

    horas_inteiras = int(total_active_hours)
    minutos = int((total_active_hours - horas_inteiras) * 60)

    # 📢 Exibir resultado individual do arquivo
    print("=" * 50)
    print(f"📂 **Arquivo:** {file_name}")
    print(f"🚶‍♂️ Distância percorrida: {total_distance_km:.2f} km")
    print(f"📅 Dias ativos: {len(activity_per_day)}")
    print(f"⏳ Tempo total de atividade: {int(horas_inteiras)} horas e {int(minutos)} minutos")
    print("=" * 50)
    print("\n")

    return total_distance_km, activity_per_day, total_time, waypoints

# 📤 Upload de arquivos pelo usuário
uploaded_files = files.upload()

total_distance_km_all = 0
all_active_days = set()
total_time_all = timedelta()
all_waypoints = []

# 🔄 Processar cada arquivo enviado
for file_name in uploaded_files.keys():
    distance, days, time, waypoints = process_gpx(file_name)
    total_distance_km_all += distance
    all_active_days.update(days)
    total_time_all += time
    all_waypoints.extend(waypoints)

horas_inteiras_all, minutos_all = divmod(total_time_all.total_seconds() // 60, 60)

# 📢 Exibir resumo final de todos os arquivos juntos
print("🎯 **Resumo Final (Todos os Arquivos GPX)**")
print("=" * 50)
print(f"🚶‍♂️ Distância total percorrida: {total_distance_km_all:.2f} km")
print(f"📅 Total de dias ativos: {len(all_active_days)}")
print(f"⏳ Tempo total de atividade: {int(horas_inteiras_all)} horas e {int(minutos_all)} minutos")
print("=" * 50)

# 🗂️ Salvar waypoints se houver
if all_waypoints:
    df = pd.DataFrame(all_waypoints, columns=["Arquivo", "Nome", "Latitude", "Longitude", "Elevação"])
    xlsx_path = "waypoints.xlsx"
    df.to_excel(xlsx_path, index=False)
    files.download(xlsx_path)
else:
    print("\n🚨🚨🚨 NENHUM WAYPOINT ENCONTRADO NOS ARQUIVOS 🚨🚨🚨\n")
