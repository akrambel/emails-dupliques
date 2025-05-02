fichier_path = r"C:\Users\Administrator\Desktop\Elektriker\emails.txt"

try:
    with open(fichier_path, 'r', encoding='utf-8') as fichier:
        emails = [ligne.strip() for ligne in fichier if ligne.strip()]

    emails_uniques = []
    vus = set()

    for email in emails:
        if email not in vus:
            vus.add(email)
            emails_uniques.append(email)

    # Overwrite the file with unique emails
    with open(fichier_path, 'w', encoding='utf-8') as fichier:
        for email in emails_uniques:
            fichier.write(email + '\n')

    print("Les doublons ont été supprimés. Une seule occurrence de chaque adresse e-mail est conservée.")
    print(f"{len(emails_uniques)} adresses e-mail uniques écrites dans le fichier.")

except FileNotFoundError:
    print(f"Le fichier {fichier_path} est introuvable.")

input("\nAppuyez sur Entrée pour fermer...")
