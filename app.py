from flask import Flask, request, send_file, render_template_string
import io
from main import main

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Petri → GCode</title>
  <style>
    body { font-family: monospace; background: #0d0e10; color: #e6e3dc; 
           display: flex; flex-direction: column; align-items: center; 
           justify-content: center; min-height: 100vh; margin: 0; gap: 16px; }
    h1   { font-size: 18px; letter-spacing: 0.1em; color: #b8f04a; }
    textarea { width: 480px; height: 260px; background: #141517; color: #8aad5a;
               border: 1px solid #262729; border-radius: 8px; padding: 12px;
               font-family: monospace; font-size: 12px; resize: vertical; }
    button { padding: 10px 32px; background: #b8f04a; color: #0d0e10;
             border: none; border-radius: 8px; font-family: monospace;
             font-size: 13px; font-weight: bold; cursor: pointer; }
    button:hover { background: #a0d93a; }
    #status { font-size: 12px; color: #62615d; min-height: 18px; }
    #error  { font-size: 12px; color: #e05252; min-height: 18px; }
  </style>
</head>
<body>
  <h1>Petri / Paint → GCode</h1>
  <textarea id="json-input" placeholder='Pega aquí el JSON de coordenadas...'></textarea>
  <button onclick="convertir()">Generar GCode</button>
  <div id="status"></div>
  <div id="error"></div>

  <script>
    async function convertir() {
      const raw = document.getElementById('json-input').value.trim();
      const status = document.getElementById('status');
      const errorDiv = document.getElementById('error');
      errorDiv.textContent = '';

      let data;
      try {
        data = JSON.parse(raw);
      } catch {
        errorDiv.textContent = 'JSON inválido — revisa el formato.';
        return;
      }

      status.textContent = 'Generando...';
      try {
        const res = await fetch('/convert', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });

        if (!res.ok) {
          const msg = await res.text();
          errorDiv.textContent = `Error del servidor: ${msg}`;
          status.textContent = '';
          return;
        }

        // Descargar el archivo automáticamente
        const blob = await res.blob();
        const url  = URL.createObjectURL(blob);
        const a    = document.createElement('a');
        a.href     = url;
        a.download = 'export.gcode';
        a.click();
        URL.revokeObjectURL(url);
        status.textContent = '✓ Descargado';
      } catch (err) {
        errorDiv.textContent = `Error de red: ${err.message}`;
        status.textContent = '';
      }
    }
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/convert', methods=['POST'])
def generar():
    data = request.get_json()
    if not data:
        return 'No se recibió JSON', 400
    try:
        gcode_string = main(data)
        return send_file(
            io.BytesIO(gcode_string.encode()),
            mimetype='text/plain',
            download_name='export.gcode',
            as_attachment=True,
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)