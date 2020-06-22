import os
import os.path

port = int(os.environ['port']) if 'port' in os.environ else 8080

data_dir = os.environ['data-dir'] if 'data-dir' in os.environ else os.path.abspath(os.path.join(__file__, os.pardir))


