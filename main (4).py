def linearSearchProduct(productlist,targetProduct):
  indicies = []
  for index,product in  enumerate (productlist):
    if product==targetProduct:
      indicies.append(index)
  return indicies 
products =["shoes","boot","loafer","shoes","sandal","shoes"]
target ="shoes"
result = linearSearchProduct ( products,target)
print(result)
