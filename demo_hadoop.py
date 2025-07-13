#Console en ADMIN
#hdfs namenode -format
#sbin/start_all.cmd
#hdfs dfs -ls /
#hdfs dfs -put LICENSE.txt /


import hdfs
client = hdfs.InsecureClient("http://localhost:50070")
print(client.list("/"))
print(client.status("/LICENSE.txt"))
with client.read("/LICENSE.txt") as f:
    print(f.read())