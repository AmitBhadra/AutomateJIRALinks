from jira import JIRA
import re

#main_issue = 'DS-abcde' 
#DS should be followed by 5 digits and be a valid jira number
main_issue = ''
issues = []
type = 'is back-ported in'
#enter your own type

options = {'server':'http://enter.your.server.here'}
#let's assume you're logged in otherwise we need to add login details(jira-link2.0?)
jira = JIRA(options)
issue = jira.issue(main_issue)

description = issue.fields.description

find = re.finditer('DS', description)
indices = [iter.start(0) for iter in find]
for iter in indices:
	num = description[iter+3:iter+8]
	if num.isnumeric:
		issue_num = description[iter:iter+8]
		print issue_num
	issues += issue_num

for issue_num in issues:
	outwardIssue = jira.issue(issue_num)
	create_issue_link(type, inwardIssue = main_issue, outwardIssue, comment=None)
	
