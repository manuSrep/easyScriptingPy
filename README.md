# README
miscpy is a light python module which will facilitate your (research) work if you often have to do boring stuff like saving or reading lot's of files.


## Install
 To install simply type:
    
   ```
    pip install miscpy
   ```  

## Most useful functions
   ```
    prepareLoading(filename, path="", extension="") : Create filename for loading.
    multiLoading(identifier='*', path="", SUBPATH=False) : Load multiple files.
    prepareSaving(filename, path="", extension="") : Create filename for saving.
   ```
  
## Most useful classe
   ```
    hstr : Subclass of str which sorts after intuitive human behaviour.
   ```


## Issues
Please, feel free to contribute in any way, e.g. in reporting bugs, contributing code or making suggestion for improvements. Preferable use gitHubs "issue" and "pull requests" but you can also contact me directly:  
Manuel_Tuschen@web.de.

## Version

#### 0.1
    * Basic file checking for saving and loading.
    * Get multiple files for batch loading.
#### 0.2
    * Human sortable strings.