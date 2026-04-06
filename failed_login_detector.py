file = open("logfile.txt")

failed_count = 0

for line in file:
    print(line.strip())

    if "failed" in  line.lower():
            print("Alert: Failed login detected")
            failed_count = failed_count +1
            
file.close()

print("Total failedlogins:", failed_count)
