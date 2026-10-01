"""Start one static preview server when the Codespace starts."""
import socket
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
with socket.socket() as probe:
    running = probe.connect_ex(("127.0.0.1", 8000)) == 0
if not running:
    with open("/tmp/ng27-preview.log", "ab") as log:
        subprocess.Popen(
            [sys.executable, "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", str(root)],
            cwd=root, stdout=log, stderr=log, start_new_session=True,
        )
