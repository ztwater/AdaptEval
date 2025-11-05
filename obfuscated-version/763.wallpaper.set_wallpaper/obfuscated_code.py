    def set_wallpaper(self,var_0, var_1):
        # Note: There are two common Linux desktop environments where 
        # I have not been able to set the desktop background from 
        # command line: KDE, Enlightenment
        var_2 = self.get_desktop_environment()
        try:
            if var_2 in ["gnome", "unity", "cinnamon"]:
                var_3 = "'file://%s'" % var_0
                try:
                    var_4 = "org.gnome.desktop.background"
                    var_5 = "picture-uri"
                    var_6 = Gio.Settings.new(var_4)
                    var_6.set_string(var_5, var_3)
                except:
                    var_7 = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", var_3]
                    subprocess.Popen(var_7)
            elif var_2=="mate":
                try: # MATE >= 1.6
                    # info from http://wiki.mate-desktop.org/docs:gsettings
                    var_7 = ["gsettings", "set", "org.mate.background", "picture-filename", "'%s'" % var_0]
                    subprocess.Popen(var_7)
                except: # MATE < 1.6
                    # From https://bugs.launchpad.net/variety/+bug/1033918
                    var_7 = ["mateconftool-2","-t","string","--set","/desktop/mate/background/picture_filename",'"%s"' %var_0]
                    subprocess.Popen(var_7)
            elif var_2=="gnome2": # Not tested
                # From https://bugs.launchpad.net/variety/+bug/1033918
                var_7 = ["gconftool-2","-t","string","--set","/desktop/gnome/background/picture_filename", '"%s"' %var_0]
                subprocess.Popen(var_7)
            ## KDE4 is difficult
            ## see http://blog.zx2c4.com/699 for a solution that might work
            elif var_2 in ["kde3", "trinity"]:
                # From http://ubuntuforums.org/archive/index.php/t-803417.html
                var_7 = 'dcop kdesktop KBackgroundIface setWallpaper 0 "%s" 6' % var_0
                subprocess.Popen(var_7,shell=True)
            elif var_2=="xfce4":
                #From http://www.commandlinefu.com/commands/view/2055/change-wallpaper-for-xfce4-4.6.0
                if var_1:
                    var_8 = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-path", "-s", var_0]
                    var_9 = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-style", "-s", "3"]
                    var_10 = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-show", "-s", "true"]
                    subprocess.Popen(var_8)
                    subprocess.Popen(var_9)
                    subprocess.Popen(var_10)
                var_7 = ["xfdesktop","--reload"]
                subprocess.Popen(var_7)
            elif var_2=="razor-qt": #TODO: implement reload of desktop when possible
                if var_1:
                    var_11 = configparser.ConfigParser()
                    # Development version
                    var_12 = os.path.join(self.get_config_dir("razor"),"desktop.conf") 
                    if os.path.isfile(var_12):
                        var_13 = r"screens\1\desktops\1\wallpaper"
                    else:
                        var_12 = os.path.join(self.get_home_dir(),".razor/desktop.conf")
                        var_13 = r"desktops\1\wallpaper"
                    var_11.read(os.path.join(var_12))
                    try:
                        if var_11.has_option("razor",var_13): #only replacing a value
                            var_11.set("razor",var_13,var_0)
                            with codecs.open(var_12, "w", encoding="utf-8", errors="replace") as f:
                                var_11.write(f)
                    except:
                        pass
                else:
                    #TODO: reload desktop when possible
                    pass 
            elif var_2 in ["fluxbox","jwm","openbox","afterstep"]:
                #http://fluxbox-wiki.org/index.php/Howto_set_the_background
                # used fbsetbg on jwm too since I am too lazy to edit the XML configuration 
                # now where fbsetbg does the job excellent anyway. 
                # and I have not figured out how else it can be set on Openbox and AfterSTep
                # but fbsetbg works excellent here too.
                try:
                    var_7 = ["fbsetbg", var_0]
                    subprocess.Popen(var_7)
                except:
                    sys.stderr.write("ERROR: Failed to set wallpaper with fbsetbg!\n")
                    sys.stderr.write("Please make sre that You have fbsetbg installed.\n")
            elif var_2=="icewm":
                # command found at http://urukrama.wordpress.com/2007/12/05/desktop-backgrounds-in-window-managers/
                var_7 = ["icewmbg", var_0]
                subprocess.Popen(var_7)
            elif var_2=="blackbox":
                # command found at http://blackboxwm.sourceforge.net/BlackboxDocumentation/BlackboxBackground
                var_7 = ["bsetbg", "-full", var_0]
                subprocess.Popen(var_7)
            elif var_2=="lxde":
                var_7 = "pcmanfm --set-wallpaper %s --wallpaper-mode=scaled" % var_0
                subprocess.Popen(var_7,shell=True)
            elif var_2=="windowmaker":
                # From http://www.commandlinefu.com/commands/view/3857/set-wallpaper-on-windowmaker-in-one-line
                var_7 = "wmsetbg -s -u %s" % var_0
                subprocess.Popen(var_7,shell=True)
            ## NOT TESTED BELOW - don't want to mess things up ##
            #elif desktop_env=="enlightenment": # I have not been able to make it work on e17. On e16 it would have been something in this direction
            #    args = "enlightenment_remote -desktop-bg-add 0 0 0 0 %s" % file_loc
            #    subprocess.Popen(args,shell=True)
            #elif desktop_env=="windows": #Not tested since I do not run this on Windows
            #    #From https://stackoverflow.com/questions/1977694/change-desktop-background
            #    import ctypes
            #    SPI_SETDESKWALLPAPER = 20
            #    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, file_loc , 0)
            #elif desktop_env=="mac": #Not tested since I do not have a mac
            #    #From https://stackoverflow.com/questions/431205/how-can-i-programatically-change-the-background-in-mac-os-x
            #    try:
            #        from appscript import app, mactypes
            #        app('Finder').desktop_picture.set(mactypes.File(file_loc))
            #    except ImportError:
            #        #import subprocess
            #        SCRIPT = """/usr/bin/osascript<<END
            #        tell application "Finder" to
            #        set desktop picture to POSIX file "%s"
            #        end tell
            #        END"""
            #        subprocess.Popen(SCRIPT%file_loc, shell=True)
            else:
                if var_1: #don't spam the user with the same message over and over again
                    sys.stderr.write("Warning: Failed to set wallpaper. Your desktop environment is not supported.")
                    sys.stderr.write("You can try manually to set Your wallpaper to %s" % var_0)
                return False
            return True
        except:
            sys.stderr.write("ERROR: Failed to set wallpaper. There might be a bug.\n")
            return False

    def get_config_dir(self, var_14=APP_NAME):
        if "XDG_CONFIG_HOME" in os.environ:
            var_15 = os.environ['XDG_CONFIG_HOME'] 
        elif "APPDATA" in os.environ: # On Windows
            var_15 = os.environ['APPDATA'] 
        else:
            try:
                from xdg import BaseDirectory   
                var_15 =  BaseDirectory.xdg_config_home
            except ImportError: # Most likely a Linux/Unix system anyway
                var_15 =  os.path.join(self.get_home_dir(),".config")
        var_16 = os.path.join(var_15,var_14)
        return var_16

    def get_home_dir(self):
        if sys.platform == "cygwin":
            var_17 = os.getenv('HOME')
        else:
            var_17 = os.getenv('USERPROFILE') or os.getenv('HOME')
        if var_17 is not None:
            return os.path.normpath(var_17)
        else:
            raise KeyError("Neither USERPROFILE or HOME environment variables set.")
