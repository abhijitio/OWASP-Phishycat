import StringIO
from PIL import Image
from selenium import webdriver
from depot.manager import DepotManager

def saveImage(a):
  depot = DepotManager.get()
  driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
  driver.set_window_size(1024, 768) # set the window size  
  driver.get(a)
  
#driver.save_screenshot('carblogindia.png')

  #print a
  screen = driver.get_screenshot_as_png()

# Crop it back to the window size (it may be taller)
  box = (0, 0, 1024, 768)
  im = Image.open(StringIO.StringIO(screen))
  region = im.crop(box)
  region.save('app/static/test1.png', 'png', optimize=True, quality=95)
  #print 'lol'
  return 0

#saveImage('https://google.com')

def saveImageUrl(a):
  depot = DepotManager.get()
  driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
  driver.set_window_size(1024, 768) # set the window size  
  driver.get(a)
  
#driver.save_screenshot('carblogindia.png')

  #print a
  screen = driver.get_screenshot_as_png()

# Crop it back to the window size (it may be taller)
  box = (0, 0, 1024, 768)
  im = Image.open(StringIO.StringIO(screen))
  region = im.crop(box)
  region.save('app/static/test2.png', 'png', optimize=True, quality=95)
  #print 'lol'
  return 0
