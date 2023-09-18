import os
import ctypes
import sys

class Utils:
    @staticmethod
    def is_process_admin() -> bool:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
        
    @staticmethod
    def get_hosts_file_location() -> str:
        return os.path.join(os.environ['WINDIR'], 'System32', 'Drivers', 'etc', 'hosts')
    
    @staticmethod
    def get_attributes_to_hostfile() -> str:
        return """
127.0.0.1       localhost
::1             localhost
127.0.0.1       data.microsoft.com
127.0.0.1       msftconnecttest.com
127.0.0.1       azureedge.net
127.0.0.1       activity.windows.com
127.0.0.1       bingapis.com
127.0.0.1       msedge.net
127.0.0.1       assets.msn.com
127.0.0.1       scorecardresearch.com
127.0.0.1       edge.microsoft.com
        """

if __name__ == "__main__":
    if Utils.is_process_admin() == False:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        
    with open(Utils.get_hosts_file_location(), 'a') as hosts_file:
        hosts_file.write(Utils.get_attributes_to_hostfile())

    print("Done! Blocked all Microsoft domains!")