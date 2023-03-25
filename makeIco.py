
class MakeIco:
    version = '2.0.7'

    def successful():
        import os
        os.system ("cls") 
        os.system ("clear")
        print("\n\nSe generó exitosamente... \n\n")

    def init(self, filename, iconDir ):
        import os
        import os.path
        import argparse
        import DWIN_ICO 

        try:
            """parser = argparse.ArgumentParser(description='Make .ico from JPEG files')
            parser.add_argument('iconDir', type=str, nargs=1,
                            help='name of directory containing icon JPGs')
            parser.add_argument('filename', type=str, nargs=1,
                            help='name of new .ico file to create')
            args = parser.parse_args()

            filename = args.filename[0]
            iconDir = args.iconDir[0]
            """
            filename=filename
            iconDir=iconDir
            if os.path.isfile(filename):
                raise RuntimeError("ICO file '%s' already exists." % (filename))

            if not os.path.exists(iconDir):
                raise RuntimeError("Icon directory '%s' doesn't exist." % (iconDir))
           
            print("Making .ico file '%s' from contents of '%s'" % (filename, iconDir))
            ico = DWIN_ICO.DWIN_ICO_File()
            ico.createFile(iconDir, filename)
            os.system ("cls") 
            ##os.system ("clear")
            print("\n\nSe generó exitosamente... \n\n")
        except Exception as e:
            print('Error: ', e)




"""                  ████████████                                                        
                ██████▒▒████████████                                                  
        ░░▓▓▓▓▓▓████▒▒██▒▒████████████▓▓                                              
    ▓▓▓▓▓▓▓▓▓▓████████▒▒████████████████▓▓                                            
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓                                          
            ████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                        
              ████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                      
                ██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒                                    
                  ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                  
                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                
                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████                              
                    ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████                            
                      ████▓▓▓▓▓▓▓▓▓▓████████████████████████                          
                      ▓▓██▓▓▓▓▓▓▓▓████████████████████████████                        
                        ██▓▓▓▓▓▓▓▓██████████████████████████████                      
                        ▓▓██▓▓▓▓▓▓████████████████████████████████                    
                        ▓▓██▓▓▓▓▓▓████████████████████████████████                    
                        ░░████▓▓▓▓████████████████████████████████▓▓                  
                          ▓▓██▓▓▓▓██████████████████████████████████                  
                            ████▓▓████████████████████████████████████                
                              ████▓▓████████████████████████████████████              
                              ▓▓██▓▓██████████████████████████████████████            
                                ▓▓██▓▓████████████████████████████████████            
                                  ▓▓██▓▓████████████████████████████████████          
                                    ▓▓██████████▓▓██████████████████████████          
                                      ████▓▓██████▓▓██████████████████████████        
                                        ██████▓▓████▓▓▓▓██████████████████████        
                                          ██████▓▓▓▓██▓▓▓▓████████████████████        
                                              ▓▓▓▓▓▓██▓▓▓▓██████████████████████      
                                                ▓▓████▓▓████  ██████████████████      
                                                ████  ▓▓██        ████████████████    
                                                ▒▒    ████          ██████████████    
                                                ▒▒      ▒▒            ██████████████  
                                              ▒▒      ▒▒                ████████████  
                                              ▒▒      ▒▒                  ████████████
                                            ░░      ░░▒▒                    ██████████
                                          ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                  ██  ████
                                      ▒▒▒▒      ▒▒▒▒        ▒▒                        
"""
     