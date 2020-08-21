class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      from googlesearch import search
      import webbrowser
      import time
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
         count += 1
         print(f'Opening {i}')
         time.sleep(5)
         webbrowser.open(i)
if __name__=='__main__':
   import time
   import webbrowser
   s = input("Search: ")
   print('Processing... Preparing results...')
   time.sleep(5)
   if 'http://' in s or 'www.' in s or 'https://' in s:
      webbrowser.open(s)
      exit()
   print('Opening Google Search... Also opening closest website...')
   time.sleep(5)
   webbrowser.open(f'www.google.com/search?q={s}')
   gs = Gsearch_python(s)
   gs.Gsearch()
