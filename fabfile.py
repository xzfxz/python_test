from fabric.api import *
#
def hello():
    print("Hello ,World ")

def check():
    locals('ls ~/')

def host_type():
    run('uname -s')

#定义目标主机，多个主机用列表的形式体现
env.hosts = ['192.168.10.20', '192.168.10.30']
# 定义用户名
env.user = 'root'
env.password = 'root@2018'
#password 功能一样，需要指定主机
env.passwords = {
    'root@192.168.10.20': 'root@2018',
    'root@192.168.10.30': 'root@2018'
}
#定义角色分组
env.roledefs = {
    's20': ['root@192.168.10.20'],
    's30': ['root@192.168.10.30']
}
#自定义全局变量
env.deploy_release_dir = ""

# 角色的概念 执行以下方法的主体
@roles('s20')
def remote_task():
    with cd('/data'):     # with 的左右是让后面的表达式，继承前面的状态
        run('ls -l')           # 实现 'cd /data/logs/ && ls -l' 的效果

@roles('s30')
def remote_build():
    with cd('~/'):
        run('ls -l')

def remote_deploy():
    print("remote_deploy")
    # run('tar zxvf /tmp/fabric.tar.gz')
    # run('mv /tmp/fabric/setup.py /home/www/')

#执行如上的方法
def task():
    execute(remote_build)
    execute(remote_deploy)
    execute(hello)

@roles('s20')
def scp2remote():
    filepath="./rlt.tar.gz"
    remotePath="~/"
    put(filepath,remotePath)
