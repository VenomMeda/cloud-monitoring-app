import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    network_info = psutil.net_io_counters()

    cpu_info = {
        'percent': cpu_percent,
        'message': "High CPU Usage! Consider scaling up." if cpu_percent > 80 else None
    }
    mem_info = {
        'percent': mem_percent,
        'message': "High Memory Usage! Consider scaling up." if mem_percent > 80 else None
    }
    network_sent = network_info.bytes_sent
    network_recv = network_info.bytes_recv

    return render_template("index.html", cpu_info=cpu_info, mem_info=mem_info, network_sent=network_sent, network_recv=network_recv)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
