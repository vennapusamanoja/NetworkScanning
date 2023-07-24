import sys
import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__NetworkScanning__)+'/src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__NetworkScanning__)+'/tests')))

from core import main




if__name__=='__main__':
  f=open('packets/tcp.txt','r')
  g=open('packets/udp.txt','r')

  main(f)
