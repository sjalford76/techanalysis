import os

class Environment:

    def get_data_path(self):
        return os.environ.get('DATA_PATH')
    
    def get_results_path(self):
        return os.environ.get('RESULTS_PATH')