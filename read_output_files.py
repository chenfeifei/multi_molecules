'''
Created on 2011-03-09

@author: kai
'''
from scipy import *
import pickle,sys,os
#pickle file related
dpList = []
#End

#variables to hold info from molecular_property.pkl
freq = 0
reducedmass = 0
coor = []
atomType = []
dis = []
#End

#global variables
muxdipole = []
muydipole = []
muzdipole = []
alphaxx = []
alphaxy = []
alphaxz = []
alphayx = []
alphayy = []
alphayz = []
alphazx = []
alphazy = []
alphazz = []
#End


#Program parameters
points = 7
#End

class dipoleProperty:
    __module__ = os.path.splitext(os.path.basename(__file__))[0]
    def _init_(self):
        self.mus = []
        self.alphas = []
        self.freq = 0
        self.Mode_number = 0
        self.coordinates = []
        self.atomType = []
        self.reducedmass = 0

def empty_globals():
    global muxdipole
    global muydipole
    global muzdipole
    global alphaxx
    global alphaxy
    global alphaxz
    global alphayx
    global alphayy
    global alphayz
    global alphazx
    global alphazy
    global alphazz
    muxdipole = []
    muydipole = []
    muzdipole = []
    alphaxx = []
    alphaxy = []
    alphaxz = []
    alphayx = []
    alphayy = []
    alphayz = []
    alphazx = []
    alphazy = []
    alphazz = []
def read_files_for_aMode(mode):
    for rot in range(-int(points/2),int(points/2)+1,1):
        filename1 =sys.argv[2]+'_mode_'+ str(mode) + '_point_' + str(rot) + '.out'
        try:
            hndl = open(filename1, 'rt')
            data = hndl.readlines()
            hndl.close()     
            isGracefully = False
            correct = "ddikick.x: exited gracefully."
            for line in data:
                if line.find(correct) != -1 :
                    isGracefully = True
            if isGracefully == True: # only proceed when the file has "ddikick.x: exited gracefully."
                for quest in range(len(data)):
                    if data[quest].startswith(' DIPOLE #'):
                        if (data[quest-2].startswith('                   ----DIPOLE BASED RESULTS----')):
                            xdip = float(data[quest+2].split()[1])
                            ydip = float(data[quest+2].split()[2])
                            zdip = float(data[quest+2].split()[3])
                            axx = float(data[quest+6].split()[2])
                            axy = float(data[quest+6].split()[3])
                            axz = float(data[quest+6].split()[4])
                            ayx = float(data[quest+7].split()[2])
                            ayy = float(data[quest+7].split()[3])
                            ayz = float(data[quest+7].split()[4])
                            azx = float(data[quest+8].split()[2])
                            azy = float(data[quest+8].split()[3])
                            azz = float(data[quest+8].split()[4])
                            
                            dipmat = matrix([[xdip],[ydip],[zdip]])
                            alphamat = matrix([[axx,axy,axz],[ayx,ayy,ayz],[azx,azy,azz]])
                            
                            mumu = dipmat
                            muxdipole.append(float(mumu[0]))
                            muydipole.append(float(mumu[1]))
                            muzdipole.append(float(mumu[2]))
                            alphaxx.append(alphamat[0,0])
                            alphaxy.append(alphamat[0,1])
                            alphaxz.append(alphamat[0,2])
                            alphayx.append(alphamat[1,0])
                            alphayy.append(alphamat[1,1])
                            alphayz.append(alphamat[1,2])
                            alphazx.append(alphamat[2,0])
                            alphazy.append(alphamat[2,1])
                            alphazz.append(alphamat[2,2])
            else:
		print 'file: ', filename1, ' did not exit gracefully.'
                return False
        except IOError: # if the file does not exist skip the file
	    print 'file: ', filename1, ' may not exist, an error has occured'
            pass
    return True

def write_for_aMode(mode):
    xrange = arange(-int(points/2),int(points/2)+1.,1.)
    (amuxdip,bmuxdip,cmuxdip) = polyfit(xrange,muxdipole,2)
    (amuydip,bmuydip,cmuydip) = polyfit(xrange,muydipole,2)
    (amuzdip,bmuzdip,cmuzdip) = polyfit(xrange,muzdipole,2)
    (aalphaxxdip,balphaxxdip,calphaxxdip) = polyfit(xrange,alphaxx,2)
    (aalphaxydip,balphaxydip,calphaxydip) = polyfit(xrange,alphaxy,2)
    (aalphaxzdip,balphaxzdip,calphaxzdip) = polyfit(xrange,alphaxz,2)
    (aalphayxdip,balphayxdip,calphayxdip) = polyfit(xrange,alphayx,2)
    (aalphayydip,balphayydip,calphayydip) = polyfit(xrange,alphayy,2)
    (aalphayzdip,balphayzdip,calphayzdip) = polyfit(xrange,alphayz,2)
    (aalphazxdip,balphazxdip,calphazxdip) = polyfit(xrange,alphazx,2)
    (aalphazydip,balphazydip,calphazydip) = polyfit(xrange,alphazy,2)
    (aalphazzdip,balphazzdip,calphazzdip) = polyfit(xrange,alphazz,2)
    
    object_dp = dipoleProperty()
    object_dp._init_()
    object_dp.alphas = [balphaxxdip,balphaxydip,balphaxzdip,balphayxdip,balphayydip,balphayzdip,balphazxdip,balphazydip,balphazzdip]
    object_dp.atomType = atomType
    object_dp.coordinates = coor
    object_dp.freq = freq[mode-1]
    object_dp.Mode_number = mode
    object_dp.mus = [bmuxdip,bmuydip,bmuzdip]
    object_dp.reducedmass = reducedmass[mode-1]
    
    dpList.append(object_dp)
    
    empty_globals()


if __name__ == "__main__":
    # read molecular_property.pkl
    hndl = open(sys.argv[1],'rt')

    pickle_file_name = sys.argv[3]
    freq= pickle.load(hndl)
    coor = pickle.load(hndl)
    dis = pickle.load(hndl)
    atomType = pickle.load(hndl)
    reducedmass = pickle.load(hndl)
    hndl.close()
    
    for mode in range(int(sys.argv[4]),int(sys.argv[5])+1,1):
        result = read_files_for_aMode(mode)        
        if result: # if reading of all files of a mode is sucessfully carry on, else skip the mode
            write_for_aMode(mode)
        else:
            print mode, " is skipped" #one may want to do something about it if modes are being skipped
	    
	    empty_globals()

    hndl = open(pickle_file_name,'wt')
    pickle.dump(dpList,hndl)
    hndl.close()



