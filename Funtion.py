import os

def checkPath(path):
    """
    kiểm tra tồn tại thư mục không nếu không tạo thư mục
    """
    if os.path.exists(path):
        return path
    else:
        return os.system("mkdir -p %s"%path)
def getNetworkConfig(path, filename):
    """
    lấy cấu hình mạng
    """
    string = "ifconfig"+ ">"+path +"/"+ filename
    os.system(string)

def userTrace(path, filename):
    """
    dau vet nguoi dung
    """
    pathfile ="/var/log/syslog"
    pathfile1 = "/var/log/syslog.1"
    if os.path.isfile(pathfile):
        string ="cp -p" +pathfile+ " "+path+ "/"+filename
        os.system(string)
    else:
        return "Cant open file syslog"
    if os.path.isfile(pathfile1):
        string1 ="cp -p" +pathfile1+ " "+path+ "/"+filename
        os.system(string1)
    else:
        return "Cant open file syslog.1"
def getCpuConf(path, filename):
    """
    Cấu hình CPU
    """
    string = "lscpu"+ ">"+path +"/"+ filename
    os.system(string)

def getComputerConf(path, filename, passW):
    """
    Cấu hình máy
    """
    string = "lshw"+ ">"+path +"/"+ filename
    os.system("echo %s | %s"%(passW,string))

def getChromeCache(path, filename):
    """
    Lấy cache chrome
    """
    checkPath(path)
    string = "cp -avr ~/.cache/google-chrome/Default/"+ " " +path+ "/"+ filename+ "/"
    os.system(string)

def getFirefoxCache(path, filename):
    """
    lấy cache firefox
    """
    checkPath(path)
    string = "cp -avr ~/.cache/mozilla/firefox/"+ " " + path+ "/"+ filename+ "/"
    os.system(string)

def getOperaCache(path, filename):
    checkPath(path)
    string = "cp -avr ~/.cache/opera/" + " " + path + "/" + filename + "/"
    os.system(string)

#getNetworkConfig("/home/tungkthd01/doan","ifconfig.txt")
#userTrace("/home/tungkthd01/doan","userTrace.txt")
#getCpuConf("/home/tungkthd01/doan","ConfCpu.txt")
#getComputerConf("/home/tungkthd01/doan","ConfComputer.txt","tungkthd1234")
#getChromeCache("/home/tungkthd01/doan","chromeCache")
#if __name__ == '__main__':
