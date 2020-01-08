import yaml
import os
import sys
import twitter
import argparse

root_dir = os.path.dirname(__file__)

class global_Obj:

	def __init__(self):
		self.settings = self.load_yaml_file(os.path.join(root_dir, 'settings.yaml'))
		self.connect_to_twitter()
		self.get_args()
		self.create_csv_folder()

	def get_args(self):
		parser = argparse.ArgumentParser(description='Creating a dataset using twitter')
		parser.add_argument('--csv_file_name', help='name of the csv file to save', required=True)
		self.args = parser.parse_args()
		try:
			self.handles = self.settings['handles']
		except KeyError:
			print('\033[91m Please enter twitter handles to generate text from \033[0m')
			sys.exit()

	def create_csv_folder(self):
		if not os.path.isdir('../csv'):
			os.mkdir('../csv')


	def load_yaml_file(self, filename):
		key_file_path = os.path.join(os.path.dirname(sys.argv[0]),filename)
		yaml_file = open(key_file_path, 'r')
		contents = yaml.load(yaml_file)
		yaml_file.close()
		return contents

	def connect_to_twitter(self):
		self.api = twitter.Api(consumer_key=self.settings['twitter_consumer_key'],
                      consumer_secret=self.settings['twitter_comsumer_secret'],
                      access_token_key=self.settings['twitter_access_token_key'],
                      access_token_secret=self.settings['twitter_access_token_secret'],
                      tweet_mode='extended')
		print(self.api.VerifyCredentials())



globalManager = global_Obj()
