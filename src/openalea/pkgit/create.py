# -*- coding: utf-8 -*- 
# -*- python -*-
#
#       Formula file for OpenAlea.release
# 
#       OpenAlea.release: tool for dependencies packaging
#
#       Copyright 2013 INRIA - CIRAD - INRA
#
#       File author(s):
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
__revision__ = "$Id: $"

txt="""# -*- coding: utf-8 -*- 
# -*- python -*-
#
#       Formula file for OpenAlea.release
# 
#       OpenAlea.release: tool for dependencies packaging
#
#       Copyright 2013 INRIA - CIRAD - INRA
#
#       File author(s):
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
__revision__ = "$Id: $"

from openalea.release.formula import Formula

class %s(Formula):
    version         = ""  	 # Version of the dependency (not of the formula)
    description     = ""     # Description of the dependency (not of the formula)
    homepage        = ""     # Url of home-page of the dependency (not of the formula)
    license         = ""     # License of the dependency (not of the formula)
    authors         = ""     # Authors of the dependency (not of the formula)
    dependencies    = ""     # List of dependencies of the formula
    download_name   = ""     # Name of the local archive
    download_url    = ""   	 # Url where to download sources (feel only if "DOWNLOAD = True")
"""

from openalea.release import formula
from path import path
import sys
import warnings

def default_formula(name):
    name = str(name).lower()
    name = is_correct(name)
    formulapath = path(formula.__file__).abspath().splitpath()[0]
    filename = formulapath/"formulas"/"%s.py"%name
    classname = name[0].capitalize() + name[1:]
    text = txt%classname
    f = open(filename, "w")
    f.write(text)
    f.close()
    
    print("Formula %s created %s !"%(classname,filename))
    
def is_correct(name):
    if " " in name:
        warnings.warn("Don't use space in the name of your formula")
        sys.exit()
    if any(c in name for c in 'éèêëàâäûùüîïöô'):
        warnings.warn("Don't use accent in the name of your formula")
        sys.exit()
    if any(c in name for c in '&~*+-/\\<>^|#@=$£¤%§!:;.?,°[]{}()²\'"'):
        warnings.warn("Don't use special character in the name of your formula")
        sys.exit()
    return name