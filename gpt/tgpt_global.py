import yaml
import os
import sys
import gpt_2_simple as gpt2
import argparse

root_dir = os.path.dirname(__file__)

class global_Obj:

	def __init__(self):
		self.settings = self.load_yaml_file(os.path.join(root_dir, '../settings.yaml'))
		self.get_args()
		self.download_model()

	def get_args(self):
		parser = argparse.ArgumentParser(description='Getting data for GPT2 training')
		parser.add_argument('--model_name', help='name of the model you want to download 124M,355M,774M,1558M', required=True)
		parser.add_argument('--csv_file', help='path of the csv file to train with', required=True)
		parser.add_argument('--steps', help='how many steps you want to train for',type=int, required=True)
		parser.add_argument('--run_name', help='name of the run you want to save in checkpoints folder', required=True)
		self.args = parser.parse_args()

	def download_model(self):
		if not os.path.isdir(os.path.join("models", self.args.model_name)):
			print(f"Downloading {self.args.model_name} model...")
			gpt2.download_gpt2(model_name=self.args.model_name)
		else:
			print(f"Model {self.args.model_name}  already downloaded")


	def load_yaml_file(self, filename):
		key_file_path = os.path.join(os.path.dirname(sys.argv[0]),filename)
		yaml_file = open(key_file_path, 'r')
		contents = yaml.load(yaml_file)
		yaml_file.close()
		return contents



globalManager = global_Obj()
