file = open("logfile.txt")

failed_count = 0
user_attempts = {}

for line in file:
    print(line.strip())

    if "failed" in line.lower():
        print("ALERT: Failed login detected")
        failed_count = failed_count + 1

        if "admin" in line.lower():
            print("CRITICAL ALERT: Admin account failure!")

        username = line.split()[0]

        if username in user_attempts:
            user_attempts[username] = user_attempts[username] + 1
        else:
            user_attempts[username] = 1

print("Total failed logins:", failed_count)

print("\nFailed attempts by user:")
for usr in user_attempts:
    print(usr, ":", user_attempts[usr])

print("\nRepeat attacker check:")
for usr in user_attempts:
    if user_attempts[usr] > 1:
        print("WARNING:", usr, "has multiple failed login attempts")

file.close()
