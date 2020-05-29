#Steven 24/04/2020 
#plot yolov3 training loss from log file
import argparse 
import sys
import matplotlib.pyplot as plt

#----------------------------------------------
#usgae: python yoloPlot.py .\PennFudanTiny.log
#----------------------------------------------

def getLoss(log_file,startIter=0,stopIter=None):
    numbers = {'1','2','3','4','5','6','7','8','9'}
    with open(log_file, 'r') as f:
        lines  = [line.rstrip("\n") for line in f.readlines()]
        
        iters = []
        loss = []
        for line in lines:
            trainIterRes = line.split(' ')
            if trainIterRes[0][-1:]==':' and trainIterRes[0][0] in numbers :
                try:
                    aveLoss = float(trainIterRes[2])
                    iter = int(trainIterRes[0][:-1])
                except:
                    continue  

                if(iter<startIter):
                    continue       
                if stopIter and  iter > stopIter:
                    break
                iters.append(iter)           
                loss.append(aveLoss)
                  
    return iters,loss

def plotLoss(ax,iters,loss,label='',name='PennFudan Training loss'):
    ax.set_title(name)
    ax.plot(iters,loss,label=label)
    ax.set_xlabel('Iters')
    ax.set_ylabel('Loss')
    #ax.legend()
     
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--list', nargs='+', help='path to log file', required=True)
    parser.add_argument('-s', '--start', help = 'startIter')
    parser.add_argument('-t', '--stop', help = 'stopIter')
    
    args = parser.parse_args()
    startIter = 0
    stopIter = None
    if args.start:
        startIter = int(args.start)
    if args.stop:
        stopIter = int(args.stop)
        
    print(args.list,startIter,stopIter)
    
    ax = plt.subplot(1,1,1)
    for i in args.list:
        iters,loss = getLoss(i,startIter,stopIter)
        plotLoss(ax,iters,loss,label='a')
    plt.show()
    
if __name__ == "__main__":
    main(sys.argv)
    