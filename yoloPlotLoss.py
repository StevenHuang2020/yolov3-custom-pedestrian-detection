#Steven 24/04/2020 
#plot yolov3 training loss from log file
import argparse 
import sys
import matplotlib.pyplot as plt

#----------------------------------------------
#usgae: python yoloPlot.py .\PennFudanTiny.log
#----------------------------------------------

def getLoss(log_file,startIter=0):
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
                iters.append(iter)           
                loss.append(aveLoss)
                  
    return iters,loss

def plotLoss(iters,loss,name='PennFudan Training loss'):
    plt.title(name)
    plt.plot(iters,loss)
    plt.xlabel('iters')
    plt.ylabel('loss')
    #plt.grid()
    plt.show()
    
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("log_file",  help = "path to log file")
    parser.add_argument('-s', '--start', help = 'startIter')
     
    args = parser.parse_args()
    startIter = 0
    if args.start:
        startIter = int(args.start)
    print(args.log_file,startIter)
    iters,loss = getLoss(args.log_file,startIter)
    plotLoss(iters,loss)
    
if __name__ == "__main__":
    main(sys.argv)
    