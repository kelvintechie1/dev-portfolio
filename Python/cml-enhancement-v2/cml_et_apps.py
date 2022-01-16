from webbrowser import *
from cml_et_breakout import *

def OpenCMLMain(cmlURL=getBreakoutConfig().url):
    open(cmlURL + "/")


def OpenCMLLab(lab="fc8167", cmlURL=getBreakoutConfig().url):
    open(cmlURL + "/lab/" + lab)