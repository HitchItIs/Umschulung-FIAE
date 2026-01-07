# --- SYSTEM COMPONENT : SERVER MONITOR ---
# Beschreibung: Logic zur Berechnung von Server-Ressourcen

#1, System-Status ( Input Daten ) 
server_name = "Dortmund-Core-01"
ram_total_gb = 64                  #Integer (Ganzzahl)
ram_used_gb  = 24.5                #Float (Dezimahlzahl)
is_active = True                   #Boolean (Wahrheitswert) 

#2. Berechnung (Logik) 
# Wir berechnen der Freien Arbeitsspeicher 

ram_free_gb = ram_total_gb - ram_used_gb

ram_limit = 50.0

#3. Status Output
print(f"--- Systemstatus : {server_name} ---") 
print(f"--- Status Online: {is_active}---")
print(f"--- Freier Ram : {ram_free_gb} GB von {ram_total_gb} GB")

if ram_used_gb > ram_limit:
  print ("Warnung: Speicher voll!")
else:
  print (f" Noch {ram_free_gb} Gb Frei !") 
