#
# Random files selector example
#

import os
import random

# Get a list of a folder's files
def get_files_from(dir):
	files_list = list()
	for file in os.listdir(dir):
		if file.endswith('.txt'):
			files_list.append(file)
	return files_list


# Select a bunch of random files
def select_random_files(files_list, percent):
	return random.sample(files_list, int(len(files_list) / 100 * percent))

# Get a bunch of random files from a directory
def get_random_files_from(dir, percent):
	files_list = get_files_from(dir)
	return select_random_files(files_list, percent)


def get_tupled_files(dir, percent):
	files = get_files_from(dir)
	index = int(len(files) * (percent/100))
	random.shuffle(files)
	return files[:index], files[index:]


if __name__ == '__main__':
	truc = get_random_files_from('neg', 20)
	print(truc)
	print(len(truc))