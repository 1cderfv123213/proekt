import os
import glob
import shutil
import numpy as np
import time
import json
import random
import dela
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
k=int(input())
S=2
f=1
while f!=0:
    f=(k//7)*2
    o=k%7
    if f!=0:
        S+=k-o
        k=f+o
    else:
        S+=k
        if k>=5:
            S+=2
print(S)