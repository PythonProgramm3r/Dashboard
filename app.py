from flask import Flask, jsonify
import random
import time
from alpha_vantage.timeseries import TimeSeries
app = Flask(__name__)

@app.route('/data')
def get_data():
    
ts = TimeSeries(key='PGWS9CLS8AR5Z42D')
    data, _ = ts.get_intraday('AAPL', interval='1min')
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)