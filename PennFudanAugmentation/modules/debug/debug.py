import sys

def get_cur_info(str=None):
    #print(sys._getframe().f_back)

    print(sys._getframe(0).f_code.co_filename,end=' line:') #cur fuc name
    print(sys._getframe().f_lineno,end=' func=')  # cur line no
    #print(sys._getframe(0).f_code.co_name,end = ' ')  # cur fuc name
    #print(sys._getframe(0).f_code.co_line)  # cur fuc name
    #print(sys._getframe(0).f_code.co_firstlineno)  # cur fuc start line no
    print(sys._getframe(1).f_code.co_name,end=' ') #fuc name which call this fuc or module
    if str:
        print(str)

class __LINE__(object):
    def __repr__(self):
        try:
            raise Exception
        except:
            return str(sys.exc_info()[2].tb_frame.f_back.f_lineno)

class __FILE__(object):
    def __repr__(self):
        try:
            raise Exception
        except:
            #return str(sys.exc_info()[2].tb_frame.f_code.co_filename)
            return sys._getframe(1).f_code.co_filename

if __name__ == '__main__':
    #get_cur_info('hhh')
    line = __LINE__()
    file = __FILE__()
    #print('line:',line)
    #print('file:',file,'line:',line)
    print(__FILE__(),__LINE__())

