#!/usr/python 
# -*- coding: utf8 -*-
#parser.getattr(line[0],line) 

class Parser(object):
    parameters = []
    def __init__(self, lines):
        self.lines = lines
    
    def parse(self):
        for elem in self.lines:
            line = elem.split(" ")
            try :
               self.__getattribute__(line[0])(line)
            except:
                print "#[-]  : No such Command "+str(line[0])
            
    
    def ASSIGN(self, line):
        print line[1]+"="+line[2]+""
        
    #line = [ASSIGN, ...] # c'est déjà un tableau // true
    def FETCH_DIM_R(self, line):
        print line[1] +"="+line[2]+"["+line[3]+"]"
        
    #SEND_VAR !var // envoyer param pour la next fct
    def SEND_VAR(self, line):
        self.parameters.append(line[1])
        print "#param added"
    

    #SEND_VAL val // envoyer param pour la next fct
    def SEND_VAL(self, line):
        self.parameters.append(line[1])
        print "#param added"
    
    #DO_FCALL 1 $return_value 'fct'
    def DO_FCALL(self, line):
        print line[2] +"=" +line[3] +"("+",".join(self.parameters)+")"
        if line[3] == 'chr':
            print "print "+ line[2]
        self.parameters = [] 
    
    #UNSET_VAR // DO NOTHING
    def UNSET_VAR(self, line):
        print "#unsetting"
    #BRK 1 ->line
    def BRK(self, line):
        print "#brk to "+ line[2]

#ADD ~return $val1 num
#$return = $val1 + num // or $val1 + -num
    def ADD(self, line):
        print line[1]+"="+line[2]+"+"+line[3]
        print "print 'decalage:'+str("+line[3]+")" #décalage
        
    #JMP ->line
    def JMP(self, line):
        print "#JMP to"+ line[1]
    
    #BOOL $a $b
    #$a = bool($b)
    def BOOL(self, line):
        print line[1]+"="+line[2]
    
    #JMPZ ~cond ->return
    def JMPZ(self,line):
        print "#JMPZ to" + line[2] + " if " +line[1]
        
    def ISSET_ISEMPTY_VAR(self, line):
        print "#if isset("+line[1]+"):"
    
    def IS_NOT_EQUAL(self,line):
        print "print '"+line[1]+"="+line[2]+"!="+line[3]+"'"
    
if __name__ == '__main__':
    with open('dump.txt', 'r') as f:
        lines = f.read().splitlines()
        f.close()
    p =   Parser(lines)
    p.parse()







