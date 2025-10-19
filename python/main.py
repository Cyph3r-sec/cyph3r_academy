import mysql.connector
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TU_PASSWORD",
    database="asesorias_db"
)

# --- CONFIGURACIÓN DE LA API DE GOOGLE CALENDAR ---
SCOPES = ["https://www.googleapis.com/auth/calendar"]
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
creds = flow.run_local_server(port=0)
service = build("calendar", "v3", credentials=creds)

# --- LEER LOS REGISTROS DE LA BASE DE DATOS ---
cursor = db.cursor(dictionary=True)
cursor.execute("SELECT * FROM agenda WHERE DATE(fecha) >= CURDATE()")
registros = cursor.fetchall()

for r in registros:
    fecha_evento = datetime.combine(r["fecha"], r["hora"])
    fin_evento = fecha_evento + timedelta(hours=1)  # Duración por defecto de 1 hora

    evento = {
        "summary": f"Asesoría con {r['nombre']} - {r['tema']}",
        "description": r["mensaje"],
        "start": {"dateTime": fecha_evento.isoformat(), "timeZone": "America/Mexico_City"},
        "end": {"dateTime": fin_evento.isoformat(), "timeZone": "America/Mexico_City"},
        "attendees": [{"email": r["correo"]}]
    }

    event = service.events().insert(calendarId="primary", body=evento).execute()
    print(f"✅ Evento creado: {event.get('htmlLink')}")

cursor.close()
db.close()
