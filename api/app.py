from flask import Flask, request, send_file, render_template_string
import io
from main import main_stream

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>GPlotter - Fablab Puebla</title>
  <style>
    body { font-family: monospace; background: #0d0e10; color: #e6e3dc; 
           display: flex; flex-direction: column; align-items: center; 
           justify-content: center; min-height: 100vh; margin: 0; gap: 16px; }
    h1   { font-size: 18px; letter-spacing: 0.1em; color: #4a66f0; }
    textarea { width: 480px; height: 260px; background: #141517; color: #7080d3;
               border: 1px solid #262729; border-radius: 8px; padding: 12px;
               font-family: monospace; font-size: 12px; resize: vertical; }
    button { padding: 10px 32px; background: #4a66f0; color: #0d0e10;
             border: none; border-radius: 8px; font-family: monospace;
             font-size: 13px; font-weight: bold; cursor: pointer; }
    button:hover { background: #a0d93a; }
    #status { font-size: 12px; color: #62615d; min-height: 18px; }
    #error  { font-size: 12px; color: #e05252; min-height: 18px; }
  </style>
</head>
<body>
  <h1>Dotter GPlotter - Fablab Puebla</h1>
  <textarea id="json-input" placeholder='Paste your JSON here...'></textarea>
  <button onclick="convert()">Generate GCode</button>
  <div id="status"></div>
  <div id="error"></div>

  <script>
    async function convert() {
      const raw = document.getElementById('json-input').value.trim();
      const status = document.getElementById('status');
      const errorDiv = document.getElementById('error');
      errorDiv.textContent = '';

      let data;
      try {
        data = JSON.parse(raw);
      } catch {
        errorDiv.textContent = 'Invalid JSON. Please check your input.';
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
          errorDiv.textContent = `Server error: ${msg}`;
          status.textContent = '';
          return;
        }

        const blob = await res.blob();
        const url  = URL.createObjectURL(blob);
        const a    = document.createElement('a');
        a.href     = url;
        a.download = 'export.gcode';
        a.click();
        URL.revokeObjectURL(url);
        status.textContent = '✓ Downloaded';
      } catch (err) {
        errorDiv.textContent = `Network error: ${err.message}`;
        status.textContent = '';
      }
    }
  </script>
</body>
</html>
"""

@app.route('/convert', methods=['POST'])
def generate_gcode():
    data = request.get_json()
    if not data:
        return 'No se recibió JSON', 400

    def generate():
        try:
            for chunk in main_stream(data):
                yield chunk
        except Exception as e:
            yield f"\n; ERROR: {str(e)}"

    return Response(
        generate(),
        mimetype='text/plain',
        headers={'Content-Disposition': 'attachment; filename="export.gcode"'}
    )
