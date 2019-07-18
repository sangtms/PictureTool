import os
import sys
import subprocess
import codecs
import json
import builder
#import pypyodbc
from builder import MsBuilder
import shutil
from distutils.dir_util import copy_tree
import logging
from distutils import log

log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)

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

def build_net_core(projPath):
	p = subprocess.call(['dotnet', 'build', projPath, '--configuration','release'])
	if p==0: return True	# exit early
		
	return False

def deploy_net_core(application):
	process = subprocess.Popen(['D:\AutoDeployer\AutoDeployer.exe', application], stdout=sys.stdout)
	process.communicate()
