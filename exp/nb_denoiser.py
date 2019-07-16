
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/denoiser.ipynb

from sklearn.decomposition import TruncatedSVD

def denoise(data):
    svd = TruncatedSVD(n_components=1, n_iter=7, random_state=0)
    svd.fit(data)
    pc = svd.components_
    data -= data.dot(pc.T) * pc
    return data