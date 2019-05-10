#Code for visual assesment test from finding out number of clusters
#Author: Samiran Kundu
#Date: 10-05-2019 


#library imports
import pandas as pd
import numpy as np
import time
from numpy import unravel_index
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

#class for implementation of VAT algorithm
class VAT:

	def __init__(self,input_df):
		"""function will initialize the class VAT with input data"""
		self.input_df=input_df
		#converting the dataframe into 2D matrix and then scaling it
		matrix=pd.DataFrame(distance_matrix(self.input_df.values, self.input_df.values), index=self.input_df.index, columns=self.input_df.index)
		matrix=matrix-matrix.min()/(matrix.max()-matrix.min())
		self.array_values=matrix.values

	def find_min_cor(self,I,J):
		"""function will find the co-ordinate of the smallest element
		   of the matrix with its rows belonging in I and column in J."""
		min_value=100000
		min_cor=(-1,-1)
		
		list_I=list(I)
		list_J=list(J)
		
		for i in list_I:
			for j in list_J:
				if(self.array_values[i][j]<min_value):
					min_value=self.array_values[i][j]
					min_cor=(i,j)
		return(i,j)
	
	def plot(self):
		"""function for final plot of the VAT image"""
		start_time=time.time()
		#MST algorithm
		P=[]
		I=set()
		J=set()
		K=set(range(len(self.array_values)))
		J=K
		i=unravel_index(self.array_values.argmax(), self.array_values.shape)[0]
		I.add(i)
		J.difference(I)
		P.append(i)
		
		for r in range(1,len(self.array_values)):
			j=self.find_min_cor(I,J)[1]
			I.add(j)
			J=J.difference(I)
			P.append(j)
		your_permutation =P
		i = np.argsort(your_permutation)
		ordered_array=self.array_values[:,i][i,:]
		plt.imshow(ordered_array,cmap="inferno", interpolation='nearest')
		plt.show()
		
		print("Time taken {}".format(time.time()-start_time))

if __name__=='__main__':
	#Iris data set
	input_file_location="/iris.csv"
	input_df=pd.read_csv(input_file_location,index_col=0).drop(["species"],axis=1)	
	vat=VAT(input_df)
	vat.plot()
