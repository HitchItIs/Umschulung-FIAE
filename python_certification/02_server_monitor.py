import time
import random


#  ---  Module 02: Server Monitor (Loops)  ---  
# Purpose : Simulates a continues server monitoring programm 

# 1. Configuartion ( Variables)  
server_name = "Dortmund-Core-01" 
ram_total_gb = 64
ram_limit_gb = 50.0

print(f"--- Starting Monitor for {server_name} --- ")

      # 2. Infinite Loop ( The Daemon) 
      # This Loop runs forever until manually stopped (ctrl+C)

while True:

# Simulation : Generate random RAM uusage between 20.0 and 64.0 
 
      current_usage_gb = random.uniform (20.0, 64.0) 
      
# Logic: Calculate remaining free space
      
      free_space_gb = ram_total_gb - current_usage_gb

# Output: Round numbers to 2 decimal places for better readability 

print(f" Checking status... Used: {round(current_usage_gb, 2)} GB / Free: {round(free_space_gb, 2)} GB")

#3 Decision Logic ( Threshold Check) 
  if current_usage_gb < ram_limit_gb:
    print(">>> Alert: Critical RAM usage detected! <<<")
    print(">>>Please check running processes.")
  else:
print">>> Status: System is stable.")

    print("-" * 40) # Seperator Line for better UI

#Wait 3 second before the next check
time.sleep(3) 
      
