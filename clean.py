import os
import glob

pwd = os.getcwd();
for file in os.listdir(pwd):
	if file.endswith(".pyc") or file.endswith(".csv") or file.endswith(".json"):
		os.remove(file)
