import subprocess
import sys, getopt

file = ''
hashfile = ''

opts, args = getopt.getopt(sys.argv[1:], "hf:t:")

if (sys.argv[1:] == []):
	print("Usage: verify-sha256.py -f <filename> -t <hashfile>")

for opt, arg in opts:
	
	if opt == "-h" or arg == " ":
		print("Usage: verify-sha256.py -f <filename> -t <hashfile>")	
		sys.exit()
	
	elif opt == "-f":
		file = arg

	elif opt == "-t":
		hashfile = arg

shasum_output = subprocess.run(["shasum", file, "-a",  "256", "-c", hashfile], capture_output=True, text=True)

arr = shasum_output.stdout.split("\n")

for i in arr:
	if i.find("OK") > 0:
		print(i) 
