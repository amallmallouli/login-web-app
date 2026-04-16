FROM python:3.11-slim

WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'application
COPY app.py .
COPY templates/ templates/

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]