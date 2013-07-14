import getopt, os, sys, json, io

version = '0.1.0'

class CommandArgumentsError(RuntimeError):
	def __init__(self, arg):
		self.args = arg

class SubstituteError(RuntimeError):
	def __init__(self, arg):
		self.args = arg

def substitute_text(contents, context, strict):
	with io.BytesIO() as output:
		index = 0
		while index < len(contents):
			if contents[index] == '%':
				end = index + 1
				while end < len(contents) and contents[end] != '%':
					end = end + 1

				if end == len(contents):
					if not strict:
						print('Warning: unmatched % was found. Ignored.')
					else:
						raise SubstituteError(('unmatched % was found.',))
				elif end - index == 1:
					output.write('%')
				else:
					variable_name = contents[index + 1:end]
					if variable_name in context:
						output.write(context[variable_name].encode('utf-8'))
					else:
						if not strict:
							print('Warning: variable %' + variable_name + '% was not found in context. Ignored.')
						else:
							raise SubstituteError(('variable %' + variable_name + '% was not found in context.',))

					
				index = end + 1
			else:
				output.write(contents[index])
				index = index + 1
		return output.getvalue()

def read_context_file(context_file):
	with open(context_file, 'r') as file:
		data = json.loads(file.read())
		return data['context']

def substitute_file(input_file_path, output_file_path, context_file, strict):
	try:
		with open(input_file_path, 'r') as input_file:
			contents = input_file.read()

			context = {}
			if context_file != '':
				context = read_context_file(context_file)

			processed_output = substitute_text(contents, context, strict)

			with open(output_file_path, 'w') as output_file:
				output_file.write(processed_output)

		return 0
	except SubstituteError as err:
		print('Error: ' + err.args[0])
		print('Operation aborted.')
		return 1

def read_arguments(args):
	input_file = ''
	output_file = ''
	context_file = ''
	strict = False

	try:
		opts, args = getopt.getopt(args, 'i:o:c:s', [ 'input=', 'output=', 'context=', 'strict' ])
		for opt, arg in opts:
			if opt in ('-i', '--input'):
				input_file = arg
			elif opt in ('-o', '--output'):
				output_file = arg
			elif opt in ('-c', '--context'):
				context_file = arg
			elif opt in ('-s', '--strict'):
				strict = True

		if input_file == '' or output_file == '':
			raise CommandArgumentsError(('you must specify both input and output file. See usage.',))
	except getopt.GetoptError as err:
		raise CommandArgumentsError(err.args)

	return input_file, output_file, context_file, strict

def usage():
	print('Usage: python substitute.py -i <input-file> -o <output-file> [-c <context-file>]')
	print('Version: ' + version)
	print('Copyright (c) 2013 Luis Garcia')
	print('')
	print('Read README for more info.')

def main(args):
	try:
		input_file, output_file, context_file, strict = read_arguments(args)
	except CommandArgumentsError as err:
		print('Error: ' + err.args[0])
		print('')
		usage()
		sys.exit(2)

	return_code = substitute_file(input_file, output_file, context_file, strict)
	sys.exit(return_code)	

main(sys.argv[1:])
