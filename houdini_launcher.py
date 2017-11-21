import os
import subprocess
import re
import time

import platform

def locateHoudini(ver=()):
	if(len(ver)==0):ver=(9999,0,9999)
	elif(len(ver)==1):ver=(ver[0],0,9999)
	elif(len(ver)==2):
		if(ver[1]<10):ver=(ver[0],ver[1],9999)
		else:ver=(ver[0],0,ver[1])
	elif(len(ver)>3):raise ValueError("version must have max 3 components")
	#now ver has format (XX.X.XXX)
	
	system=platform.system()
	
	if(system=='Windows'):
		commonpaths = [r"C:\Program Files\Side Effects Software"]
	elif(system=='Linux'):
		commonpaths = [r"/opt"]
	elif(system=='Darwin'):
		commonpaths = ["r/Applications/Houdini"]
	else:
		raise RuntimeError("looks like someone purposefully deleted you OS from jedi archives...")
	
	houdinies={}
	for path in commonpaths:
		dirs=[]
		try:
			dirs=os.listdir(path)
		except:
			continue
			
		for dir in dirs:
			if (system == 'Windows'):
				matchexpr=r"[Hh]oudini ?(\d+)(\.(\d))?(\.(\d{3,}))?"
			elif(system == 'Linux'):
				matchexpr = r"hfs(\d+)(\.(\d))(\.(\d{3,}))" #we want full versions, not links or shortcuts
			elif(system == 'Darwin'):
				matchexpr = r"[Hh]oudini ?(\d+)(\.(\d))(\.(\d{3,}))"
			match = re.match(matchexpr, dir)
			if(not match):continue
			cver=(int(match.group(1)),0 if match.group(3)=="" else int(match.group(3)), 9999 if match.group(5)=="" else int(match.group(5)))
			if(system=='Windows' or system=='Linux'):
				houdinies[cver] = os.path.join(path, dir)
			elif(system=='Darwin'):
				houdinies[cver] = os.path.join(path, dir,'Frameworks','Houdini.framework','Version',"%s.%s.%s"%cver,'Resources')
		
		vers=houdinies.keys()
		if(len(vers)==0):raise RuntimeError("houdini not found!!")
		#elif(len(vers)==1):return houdinies[vers[0]]
		
		sortvers=[((abs(x[0]-ver[0]),abs(x[1]-ver[1]),abs(x[2]-ver[2])),x) for x in vers]
		
		sortvers.sort(key=lambda el:el[0][0])
		sortvers=[x for x in sortvers if x[0][0]==sortvers[0][0][0]]
		sortvers.sort(key=lambda el:el[0][1])
		sortvers=[x for x in sortvers if x[0][1]==sortvers[0][0][1]]
		sortvers.sort(key=lambda el:el[0][2])
		sortvers=[x for x in sortvers if x[0][2]==sortvers[0][0][2]]
		
		return os.path.join(houdinies[sortvers[0][1]],"bin","houdinifx")
			

def launchHoudini(ver,vars):

	for var in vars:
		os.environ[var]=vars[var]
		print("%s set to %s"%(str(var),str(vars[var])))
	houbin=locateHoudini(ver)
	print("Calling closest found version: %s"%(houbin,))
	subprocess.Popen(houbin,stdin=None,stdout=None,stderr=None)
	print("Done!")
	
	
print("Welcome to houdini hsite launcher ver. %s !!"%("0.0.0.003 preAlphaTechDemo"))
print("----------")
jobpath=os.path.join(os.path.split(os.getcwd())[0],"fxproject")
launchHoudini((16,0,600),{'HOUDINI_VEX_PATH':os.getcwd()+'/vex'+os.pathsep+'&','HOUDINI_OTLSCAN_PATH':os.getcwd()+'/otls'+os.pathsep+'&'})
print("----------")
print("you can now close this window, it will close automatically in 5 sec")
time.sleep(5)