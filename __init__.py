# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import platform
from subprocess import Popen, PIPE
import signal
from time import sleep
import signal

base_path = tmp_global_obj["basepath"]
folder = platform.system()
ffmpegW = os.path.join(base_path, 'modules', 'ScreenRecorder', 'bin', "windows", 'ffmpeg.exe')
ffmpegW32 = os.path.join(base_path, 'modules', 'ScreenRecorder', 'bin', "windows_32", 'ffmpeg.exe')
# ffmpegMac = os.path.join(base_path, 'modules', 'ScreenRecorder', 'bin', "darwin", 'ffmpeg')



global p
module = GetParams("module")
if module == "start":

    print("*"*30)
    print("RECORDING".center(30))
    print("*"*30)
    output = GetParams("output")

    sleep(2)
    options = " -f gdigrab -framerate 30 -i desktop " + output
    if sys.platform == "win32":
        run_ = ffmpegW32 + ' -y -f gdigrab -framerate 30 -i desktop  -vcodec libx264 "'+ output + '"'
        p = subprocess.Popen(run_, shell = True, stdin=PIPE)
    if sys.platform == "win64":
        run_ = ffmpegW +  ' -y -f gdigrab -framerate 30 -i desktop -f dshow -vcodec libx264 "'+ output + '"'
        p = subprocess.Popen(run_, shell = True, stdin=PIPE)
    if sys.platform == "darwin":
        run_ = ffmpegMac +  ' -y -f avfoundation -framerate 30 -i "1" -pix_fmt yuyv422 -vcodec libx264 "'+ output + '"'
        p = subprocess.Popen(run_, shell = True)

    sleep(5)

if module == "stop":

    pid_ = p.pid
    print("STOPING ...:" , pid_)
    
    try:
    
        platform_ = platform.system().lower()
        print(platform_)
        
        if platform_ == 'windows':
            o,e = p.communicate(input="q".encode())
            #subprocess.Popen("taskkill /F /T /PID %i" % pid_, shell=True)
        else:
            os.kill(pid_, signal.SIGKILL)

        sleep(5)
        

    except Exception as e:
        PrintException()
        raise (e)

