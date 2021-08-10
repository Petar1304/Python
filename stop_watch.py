import time

while True:
	cmd = input('>>> ')
	if cmd == 'start':
		start_time = time.time()
	
	if cmd == 'stop':
		end_time = time.time()

	if cmd == 'time':
		print(f'>>> {end_time - start_time}')

	if cmd == 'exit':
		break