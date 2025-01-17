import os
import subprocess
from flask import Flask, render_template
from flask_cors import CORS

if __name__ == "__main__":
  app = Flask(__name__)

  cors = CORS(app)
  app.config['CORS_HEADERS'] = 'Content-Type'

  FOLDER = subprocess.run("pwd", text=True, capture_output=True).stdout.strip()
  PROCNAME = 'recIdPr'
  LOCATION=f'http://recorder.local'

  def get_proc_file():
    return f'{FOLDER}/{PROCNAME}'

  @app.route("/record", methods=['POST'])
  def start_record():
    if os.path.exists(get_proc_file()):
      return 'Já está gravando'
    
    subprocess.run(['./recorder.sh', 'record', FOLDER])
    return 'Gravando'
  
  @app.route('/stop', methods=['POST'])
  def stop_record():
    if not os.path.exists(get_proc_file()):
      return 'Nenhuma gravação ativa'
    
    subprocess.run(['./recorder.sh', 'stop_record', FOLDER])
    return 'Parado'
  
  @app.route('/')
  def index():
    return render_template('index.html', appLocation = LOCATION)
  
  app.run(debug=False, port=5300, host='0.0.0.0', use_evalex=False)