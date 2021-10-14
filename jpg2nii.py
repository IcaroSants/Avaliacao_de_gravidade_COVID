import nibabel as nib
import cv2 as cv 
import numpy as np
import os

class jpg2nii:
    def __init__(self,path_atual,path_final):
        self.path_atual = path_atual
        self.dir_atual = os.getcwd()
        self.path_final = path_final
        

    
    def set_path_final(self):
        
        if not os.path.exists(self.path_final):
            os.mkdir(self.path_final)
            return True
        else:
            print('Diretorio ja existente')
            return False            
    
    def get_lista_path_pacientes(self):
        lista_pacientes = os.listdir(self.path_atual)
        lista_path_pacientes = []
        for arq in lista_pacientes:
            path_img = os.path.join(self.path_atual, arq) +  os.sep + arq + os.sep + 'CT'
            lista_path_pacientes.append(path_img)
        
        
        return lista_pacientes, lista_path_pacientes
    
    def concatImage(self,path):
         list_img = os.listdir(path)
         if len(list_img) == 1:
            arq = cv.imread(os.path.join(path,list_img[0]),0)#deixando as imagens em escalas de cinza
            return arq
         else:
            arq = cv.imread(os.path.join(path,list_img[0]),0)#deixando as imagens em escalas de cinza
            arq_red = np.reshape(arq,(1,arq.shape[0],arq.shape[1],1))
        
            for img in list_img[1:]:
                fatia = cv.imread(os.path.join(path,list_img[0]),0)
                fatia_red = np.reshape(fatia,(1,fatia.shape[0],fatia.shape[1],1))
            
                arq_red = np.vstack((arq_red,fatia_red))
            
         return arq_red
        
    def save_nii(self,data,name):
        new_img = nib.Nifti1Image(data,affine = None)
        nib.save(new_img, os.path.join(self.path_final,name))