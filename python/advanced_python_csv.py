
email_list = list(df['email'])
with open("emails.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in email_list:
        writer.writerow([val])