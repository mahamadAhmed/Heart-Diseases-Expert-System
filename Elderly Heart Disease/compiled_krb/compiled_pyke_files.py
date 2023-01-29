# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_rules.krb'):
           [1672062834.376908, 'bc_rules_fc.py'],
         ('', '', 'questions.kqb'):
           [1672062834.38241, 'questions.qbc'],
         ('', '', 'symptoms.kfb'):
           [1672062834.383059, 'symptoms.fbc'],
        },
        compiler_version)

