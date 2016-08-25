#encoding:utf-8
import urllib2
import re

def getpage(url):
	page = urllib2.urlopen(url).read()
	return page

def gettds(html_cont):
	alllines = re.findall('class="blob-code blob-code-inner js-file-line">(.*?)</td>', html_cont, re.S);
	return alllines

def gethtml(html_score):
	'''将获得的html页面为干净的html'''
	html = ""
	html += ("<html>")
	html += ("<head>")
	html += ('<meta http-equiv="content-type" content="text/html; charset=utf-8" />')
	html += ("</head>")
	html += ("<body>")
	html += ("<table border='1px'>")
	html += html_score
	html += ("</table>")
	html += ("</body>")
	html += ("</html>")
	return html	

def getHost(split):
	url = "https://github.com/racaljk/hosts/blob/master/hosts"
	page = getpage(url)
	hosts = ""
	for line in gettds(page):
		hosts += line + split
	return hosts

def writeToWindows(hosts):
	with open('c:/Windows/System32/drivers/etc/hosts', 'w') as f:
		f.write(hosts)

if __name__ == '__main__':
	# hosts = getHost('<br/>')
	# print gethtml(hosts)
	hosts = getHost('\n')
	writeToWindows(hosts)
