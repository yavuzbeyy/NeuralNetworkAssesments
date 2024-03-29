#%%
import torch


class TinyModel(torch.nn.Module):


   def __init__(self, x = 1024):
       super(TinyModel, self).__init__()


       self.activation = torch.nn.LeakyReLU()
       self.linear1 = torch.nn.Linear(1, x)
       self.linear2 = torch.nn.Linear(x, x)
       self.linear3 = torch.nn.Linear(x, 1)
      
   def forward(self, x):
       x = self.linear1(x)
       x = self.activation(x)
       x = self.linear2(x)
       x = self.activation(x)
       x = self.linear3(x)
       return x


if __name__=='__main__':
   tinymodel = TinyModel()
	
   print("model params: %i"%sum([param.nelement() for param in model.parameters()]))


   print('The model:')
   print(tinymodel)


   print("Model params: %i"%sum([param.nelement() for param in tinymodel.parameters()]))
      
   #test
   x = torch.rand(10, 1)
   print("x = ", x.size())
   y = tinymodel(x)
   print("y = ", x.size())
# %%
