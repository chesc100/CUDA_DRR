from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("SiddonGpuPy",
                             sources=["SiddonGpuPy.pyx"],
                             include_dirs=[numpy.get_include(), 
                                           "/home/ubuntu/Downloads/CUDA_DigitallyReconstructedRadiographs-master/SiddonPythonModule/include",
                                           "/usr/local/cuda/include"],
                             library_dirs = ["/home/ubuntu/Downloads/CUDA_DigitallyReconstructedRadiographs-master/SiddonPythonModule/lib",
                                             "/usr/local/cuda/lib64"],
                             libraries = ["SiddonGpu", "cudart_static"],
                             language = "c++")]
)
