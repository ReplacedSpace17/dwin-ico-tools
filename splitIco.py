
class SplitIco:

    version = '2.0.7'

    def init(self, filename, outputDir ):
        import os
        import os.path
        import argparse
        import DWIN_ICO 

        try:
            """parser = argparse.ArgumentParser(description='Split .ico into JPEG files')
            parser.add_argument('filename', type=str, nargs=1,
                             help='name of input .ico file to split')
            parser.add_argument('outputDir', type=str, nargs=1,
                            help='name of output directory to create')
            args = parser.parse_args()
    """
            #filename = args.filename[0]
            #outputDir = args.outputDir[0]
            filename= filename
            outputDir= outputDir
            if not os.path.isfile(filename):
                raise RuntimeError("ICO file '%s' doesn't exist" % (filename))

            if os.path.exists(outputDir):
                raise RuntimeError("Output directory '%s' already exists." % (outputDir))

            print('Splitting %s into dir %s' % (filename, outputDir))
            ico = DWIN_ICO.DWIN_ICO_File()
            ico.splitFile(filename, outputDir)
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

