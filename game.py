


import random

def game(comp,you):
          if(comp==you):
                    print(&quot;Game is a tie.&quot;)
          elif(comp==&#39;rock&#39;):
                    if(you==&#39;paper&#39;):
                              print(&quot;you
win&quot;)
                    elif(you==&#39;scissor&#39;):
                              print(&quot;you
loss&quot;)
          elif(comp==&#39;paper&#39;):
                    if(you==&#39;scissor&#39;):
                              print(&quot;you
win&quot;)
                    elif(you==&#39;rock&#39;):
                              print(&quot;you
loss&quot;)
          elif(comp==&#39;scissor&#39;):
                    if(you==&#39;paper&#39;):
                              print(&quot;you
loss&quot;)
                    elif(you==&#39;rock&#39;):
                              print(&quot;you
win&quot;)

print(&quot;computer&#39;s turn : rock paper or
scissor : &quot;)
random=random.randint(1,3)
if(random==1):
          comp=&quot;rock&quot;
elif(random==2):
          comp=&quot;paper&quot;
elif(random==3):
          comp=&quot;scissor&quot;

you=input(&quot;your turn: rock , paper or scissor
: &quot;)
print(&quot;computer choice is :&quot;,comp)
print(&quot;your choice is :&quot;,you)

game(comp,you)