import subprocess

def change_ip():
    try:
        subprocess.run('ipconfig /release', check=True)
        subprocess.run('ipconfig /renew', check=True)
        print("La dirección IP interna se ha cambiado exitosamente.")
    except subprocess.CalledProcessError:
        print("No se pudo cambiar la dirección IP interna.")

change_ip()
