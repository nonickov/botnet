import subprocess

# Запуск обоих файлов одновременно
process1 = subprocess.Popen(['python', '13.py'])
process2 = subprocess.Popen(['python', 'app.py'])

# Ожидание завершения обоих процессов
process1.wait()
process2.wait()
