# -*- coding: utf-8 -*- 
# -*- python -*-
#
#       Formula file for openalea.pkgit
# 
#       openalea.pkgit: tool for dependencies packaging
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
from __future__ import absolute_import
__revision__ = "$Id: $"

from openalea.pkgit.formula import Formula
from openalea.pkgit.utils import checkout
from path import path

class Oalab(Formula):
    version         = "0.1"  	 # Version of the dependency (not of the formula)
    description     = "OpenAlea is an open source project primarily aimed at the plant research community."     # Description of the dependency (not of the formula)
    homepage        = "http://openalea.gforge.inria.fr/dokuwiki/doku.php"     # Url of home-page of the dependency (not of the formula)
    license         = "Cecill-C License"     # License of the dependency (not of the formula)
    authors         = "Inria, INRA, CIRAD"     # Authors of the dependency (not of the formula)
    dependencies    = ["ipython", "openalea", "plantgl", "lpy", "mtg"]  ## +Pandas   # List of dependencies of the formula
    download_name   = "oalab"     # Name of the local archive
    download_url    = "https://scm.gforge.inria.fr/svn/vplants/vplants/trunk/oalab"   	 # Url where to download sources (feel only if "DOWNLOAD = True")
    DOWNLOAD = BDIST_EGG = True
    
    def __init__(self,**kwargs):
        super(Oalab, self).__init__(**kwargs)
        self.dist_dir = path(self._get_dist_path())/"openalea"/"oalab"
        
    def _download(self):
        return checkout(self.download_url, self.eggdir)

    def bdist_egg(self):
        return sh("python setup.py build bdist_egg -d %s"%(self.dist_dir,)) == 0