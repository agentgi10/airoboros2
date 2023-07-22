```python
import json
import os

class DataHandler:
    def __init__(self, output_file):
        self.output_file = output_file

    def write_to_file(self, data):
        if not os.path.exists(self.output_file):
            with open(self.output_file, 'w') as f:
                f.write(json.dumps(data) + '\n')
        else:
            with open(self.output_file, 'a') as f:
                f.write(json.dumps(data) + '\n')

    def read_from_file(self):
        if os.path.exists(self.output_file):
            with open(self.output_file, 'r') as f:
                lines = f.readlines()
                return [json.loads(line) for line in lines]
        else:
            return []

    def clear_file(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
```