import boto3
from time import sleep
Ids=['i-02978a6140df0f82d','i-0a5b6f13f1ff04963', 'i-0bbf4bef8c22faef4']
ec2 = boto3.resource('ec2')

x = ec2.instances.filter(InstanceIds=Ids).start()

#output
print("stopping instances")
sleep(5)
print(x)
