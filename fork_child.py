import os

def child():
   print('A new child ',  os.getpid())
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("Parent: %d, \t Child: %d\n" % pids)
      reply = input("Press q for quit or c for new fork")
      print("--"*5)
      if reply == 'c': 
          continue
      else:
          break


parent()