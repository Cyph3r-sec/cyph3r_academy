import mysql.connector
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta, time

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OuHrKuB1PHmEBWLM03IL",  # <--- cámbialo por tu contraseña real
    database="asesorias_db"
)

# --- CONFIGURACIÓN DE LA API DE GOOGLE CALENDAR ---
SCOPES = ["https://www.googleapis.com/auth/calendar"]
flow = InstalledAppFlow.from_client_secrets_file(
    r"C:\Users\Cyph3r\Documents\GitHub\cyph3r_academy\python\credentials.json",
    SCOPES
)

creds = flow.run_local_server(port=0)
service = build("calendar", "v3", credentials=creds)

# --- OBTENER REGISTROS NO SINCRONIZADOS ---
cursor = db.cursor(dictionary=True)
cursor.execute("""
    SELECT id, nombre, correo, tema, fecha, hora, mensaje 
    FROM agenda_new 
    WHERE sincronizado = FALSE AND DATE(fecha) >= CURDATE()
""")
registros = cursor.fetchall()

if not registros:
    print("⚙️ No hay nuevos registros por sincronizar.")
else:
    print(f"📅 {len(registros)} registros encontrados. Creando eventos en Google Calendar...\n")

for r in registros:
    try:
        # --- CONVERTIR HORA (maneja TIME o TIMEDELTA) ---
        if isinstance(r["hora"], timedelta):
            total_seconds = r["hora"].total_seconds()
            horas = int(total_seconds // 3600)
            minutos = int((total_seconds % 3600) // 60)
            segundos = int(total_seconds % 60)
            hora_evento = time(horas, minutos, segundos)
        else:
            hora_evento = r["hora"]

        # --- CREAR OBJETOS DATETIME COMPLETOS ---
        fecha_evento = datetime.combine(r["fecha"], hora_evento)
        fin_evento = fecha_evento + timedelta(hours=1)  # duración por defecto 1h

        # --- CONSTRUIR EVENTO PARA GOOGLE CALENDAR ---
        evento = {
            "summary": f"Asesoría con {r['nombre']} - {r['tema']}",
            "description": r["mensaje"],
            "start": {"dateTime": fecha_evento.isoformat(), "timeZone": "America/Mexico_City"},
            "end": {"dateTime": fin_evento.isoformat(), "timeZone": "America/Mexico_City"},
            "attendees": [{"email": r["correo"]}],
        }

        # --- CREAR EVENTO EN GOOGLE CALENDAR ---
        event = service.events().insert(calendarId="primary", body=evento).execute()
        print(f"✅ Evento creado para {r['nombre']} ({r['fecha']} {r['hora']}): {event.get('htmlLink')}")

        # --- MARCAR COMO SINCRONIZADO ---
        cursor_update = db.cursor()
        cursor_update.execute("UPDATE agenda_new SET sincronizado = TRUE WHERE id = %s", (r["id"],))
        db.commit()

    except Exception as e:
        print(f"⚠️ Error procesando el registro {r['id']}: {e}")

cursor.close()
db.close()
print("\n🎯 Sincronización completada.")
