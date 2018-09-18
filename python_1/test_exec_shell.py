import subprocess

rlt = subprocess.call(['pwd'])
print('rlt: {}'.format(rlt))

rlt = subprocess.run('pwd')
print(rlt.returncode)
print('rlt:{}'.format(rlt.stdout))
rlt = subprocess.Popen('pwd',stdout=subprocess.PIPE,shell=True,universal_newlines=True).communicate()[0]
print('rlt {}'.format(rlt))
#print('rlt {}'.format(rlt.decode('utf-8')))
