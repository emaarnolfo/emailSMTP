import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP y credenciales
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'emaarnolfo@gmail.com'
smtp_password = 'osrgiisnkkafmuez'

# Información del remitente y destinatario
remitente = 'emaarnolfo@gmail.com'
destinatario = 'facundo.olivacuneo@unc.edu.ar'

# Creación del objeto de mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = 'Correo de prueba SMTP'  # Asunto con formato HTML

# Cuerpo del mensaje
cuerpo_mensaje = 'Este correo se ha enviado mediante el protocolo SMTP configurado en un archivo python.'
mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

try:
    # Establecer conexión con el servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Envío del correo electrónico
    server.send_message(mensaje)

    # Cierre de la conexión con el servidor SMTP
    server.quit()
    print('El correo electrónico se ha enviado exitosamente.')

except Exception as e:
    print('Ocurrió un error al enviar el correo electrónico:', str(e))
