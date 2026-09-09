from flask import Flask, request, render_template_string, send_file
import os
import yt_dlp

app = Flask(__name__)

DOWNLOAD_DIR = "/app/downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

PLATAFORMAS = ["YouTube", "Instagram", "TikTok", "Facebook", "LinkedIn"]

HTML_TEMPLATE = """
<html>
<head>
    <title>Descargador de Videos</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background:#f4f6f7; }
        h1 { color: #028090; }
        form { margin-top: 30px; }
        input[type=text] {
            width: 400px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;
        }
        input[type=submit] {
            padding: 10px 20px; background: #028090; color: white; border: none;
            border-radius: 5px; cursor: pointer; margin-left: 10px;
        }
        .plataformas { margin-top: 15px; color: #555; }
        .mensaje { margin-top: 25px; font-weight: bold; color: #c62828; }
    </style>
</head>
<body>
    <h1>🎬 Descargador de Videos de Redes Sociales</h1>
    <p class="plataformas">Compatible con: {{ plataformas }}</p>
    <form method="POST" action="/download">
        <input type="text" name="url" placeholder="Pega aquí el enlace del video" required>
        <input type="submit" value="Descargar">
    </form>
    {% if message %}
        <p class="mensaje">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, plataformas=", ".join(PLATAFORMAS), message=None)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url", "").strip()

    if not url:
        return render_template_string(HTML_TEMPLATE, plataformas=", ".join(PLATAFORMAS), message="Debes ingresar una URL válida.")

    ydl_opts = {
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if not filename.endswith('.mp4'):
                filename = os.path.splitext(filename)[0] + '.mp4'
            
            # Esto obliga al navegador a descargar el archivo directamente a tu PC
            return send_file(filename, as_attachment=True)
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, plataformas=", ".join(PLATAFORMAS), message=f"Error al descargar: {str(e)}")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)