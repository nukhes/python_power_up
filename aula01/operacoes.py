import pyautogui as p
p.PAUSE = 0.2

def Open():
  p.hotkey("win", "space")
  p.write("brave")
  p.press("enter")
  p.sleep(1)
  p.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
  p.press("enter")

def Login(): 
  p.sleep(1)
  p.click(x=750, y=400)
  p.write("pedro@pedro.com")
  p.click(x=750, y=500)
  p.write("pedro12345-6996")
  p.click(x=750, y=400) # essa linha fecha o popup do bitwarden
  p.click(x=926, y=572)

def nextField(text):
  p.press("tab")
  p.write(text)
  
def registerProduct(table, row):
  p.click(x=1093, y=326)
  p.write(table.loc[row, "codigo"])
  nextField(str(table.loc[row, "marca"]))
  nextField(str(table.loc[row, "tipo"]))
  nextField(str(table.loc[row, "categoria"]))
  nextField(str(table.loc[row, "preco_unitario"]))
  nextField(str(table.loc[row, "custo"]))
  nextField(str(table.loc[row, "codigo"]))

  p.press("tab")
  p.press("enter")
  
  p.scroll(5000)
  p.sleep(0.25)