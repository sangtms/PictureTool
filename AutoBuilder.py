import os
import sys
import subprocess
import codecs
import json
#import builder
#import pypyodbc
#from builder import MsBuilder
import shutil
from distutils.dir_util import copy_tree
import logging
from distutils import log

def build_net_core(projPath):
	p = subprocess.call(['dotnet', 'build', projPath, '--configuration','release'])
	if p==0: return True	# exit early
		
	return False

def deploy_net_core(root_folder_path, application):
	p = subprocess.Popen(['D:\AutoDeployer\AutoDeployer.exe', root_folder_path, application], stdout=subprocess.PIPE, bufsize=1)
	with p.stdout:
		for line in iter(p.stdout.readline, b''):
			print line,
	p.wait() # wait for the subprocess to exit
	
	return True

log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)

SEPERATE_LINE = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

solution = ""
application = ""
environment = ""

if len(sys.argv) > 1:
    solution = sys.argv[1]

if len(sys.argv) > 2:
	application = sys.argv[2]
	
if len(sys.argv) > 3:
	environment = sys.argv[3]

print "Solution = %s" %solution	
print "Application = %s" %application
print "Environment = %s" %environment

root_folder_path = os.path.dirname(os.path.realpath(__file__))
print "root_folder_path %s" %root_folder_path


print SEPERATE_LINE
print "Build solution %s" % solution

if not build_net_core(solution):
	sys.exit(100)

print SEPERATE_LINE
print "Publish application"
	
if not deploy_net_core(root_folder_path, application):
	sys.exit(100)
	
print "Success !"
	
