import os
import sys
import re

user_name = "Luis Garcia"

def show_warning(file, message):
	print(file)
	print('WARNING:', message)	

def is_source_code(file):
	return file.endswith(('.cpp', '.hpp'))

def check_extension(file):
	if file.endswith('.cc'):
		show_warning(file, 'The name of source files should have the .cpp extension.')
		return False

	if file.endswith('.h'):
		show_warning(file, 'The name of header files should have the .hpp extension.')
		return False

	return True

def check_file_name(file):
	if not re.match('[a-z0-9\-]*\.(hpp|cpp)', file):
		show_warning(file, 'The name of the file should match the format "file-name.cpp".')
		return False
	return True

def check_header(file, content_lines):
	expected_header = ("//",
					   "// " + file,
					   "//",
					   "// Copyright (c) 2013 " + user_name + ".",
					   "// This source file is subject to terms of the MIT License. (See accompanying file LICENSE)",
					   "//",
					   "")

	valid = True
	if len(content_lines) < len(expected_header):
		valid = False
	else:
		for i in range(0, len(expected_header)):
			if content_lines[i] != expected_header[i]:
				valid = False

	if not valid:
		show_warning(file, "The file has not a valid header.")

	return valid

def check_trailing_spaces(file, content_lines):
	valid = True
	for i in range(0, len(content_lines)):
		if content_lines[i].endswith((' ', '\t')):
			valid = False

	if not valid:
		show_warning(file, "The file has trailing spaces.")

	return valid

def check_contents(file_name, full_path):
	file = open(full_path, "r")

	lines = []
	for line in file:
		lines.append(line.rstrip('\n'))

	file.close()

	if check_header(file_name, lines) == False:
		return False

	if check_trailing_spaces(file_name, lines) == False:
		return False

	return True

def check_file(file, full_path):
	if check_extension(file) == False:
		return False
	if is_source_code(file):
		if check_file_name(file) == False:
			return False
		if check_contents(file, full_path) == False:
			return False
	return True

for root, subFolders, files in os.walk('.'):
	for file in files:
		full_path = os.path.join(root, file)
		check_file(file, full_path)
