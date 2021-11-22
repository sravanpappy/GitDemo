import sys

sys.stderr.write("this is stdrr error text\n")
sys.stderr.flush()
sys.stdout.write("this is stdout text\n")

print(sys.argv)
