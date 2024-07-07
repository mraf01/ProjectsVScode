from documento import Documento, Email, File

email = Email(mittente="mario@example.com", destinatario="fabio@example.com", titolo="Incontro", testo="Ciao Fabio, possiamo incontrarci domani?")

print(email.getText())

email.writeToFile("email1.txt")

print(email.isInText("incontrarci"))

file_path = "document.txt"
with open(file_path, 'w') as file:
    file.write("Questo e' il contenuto del file.")
file_document = File(file_path)

print(file_document.getText())

print(file_document.isInText("percorso"))