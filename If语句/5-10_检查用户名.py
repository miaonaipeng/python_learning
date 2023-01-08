current_users = ['Jenny', 'Tom', 'Kim', 'Jane', 'Kanye']
new_users = ['Miao', 'Tim', 'Tom', 'Jane', 'Mary', 'JENNY']
upper_current_users = []
for current_user in current_users:
    upper_current_users.append(current_user.upper())
for new_user in new_users:
    if new_user.upper() in upper_current_users:
        print("You need input another username.")
    else:
        print(new_user + " have not been used.")
