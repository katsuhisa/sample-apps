import subprocess
from flask import escape

def run_scripts(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    # run_scripts.sh を実行
    try:
        completed_process = subprocess.run(["./run_scripts.sh"], check=True, text=True, capture_output=True)
        return f'Scripts ran successfully: {completed_process.stdout}'
    except subprocess.CalledProcessError as e:
        return f'Error occurred: {e.stderr}'