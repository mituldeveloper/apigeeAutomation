import git, os

Automation_Target = os.getenv('Automation_Target')
print ('Proxies:')
print ('Select 1 to deploy apigee_mitultest1')
print ('Select 2 to deploy apigee_mitultest2')

proxy = input('Which proxy do you want to deploy? ')
if proxy == "1": 
	Automation_Target+='\\apigee_mitultest1'
elif proxy == "2": 
	Automation_Target+='\\apigee_mitultest2'

print (Automation_Target)
g = git.cmd.Git(Automation_Target)
g.pull()