    def get_desktop_environment(self):
        #From http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
        # and http://ubuntuforums.org/showthread.php?t=652320
        # and http://ubuntuforums.org/showthread.php?t=652320
        # and http://ubuntuforums.org/showthread.php?t=1139057
        if sys.platform in ["win32", "cygwin"]:
            return "windows"
        elif sys.platform == "darwin":
            return "mac"
        else: #Most likely either a POSIX system or something not much common
            var_0 = os.environ.get("DESKTOP_SESSION")
            if var_0 is not None: #easier to match if we doesn't have  to deal with caracter cases
                var_0 = var_0.lower()
                if var_0 in ["gnome","unity", "cinnamon", "mate", "xfce4", "lxde", "fluxbox", 
                                       "blackbox", "openbox", "icewm", "jwm", "afterstep","trinity", "kde"]:
                    return var_0
                ## Special cases ##
                # Canonical sets $DESKTOP_SESSION to Lubuntu rather than LXDE if using LXDE.
                # There is no guarantee that they will not do the same with the other desktop environments.
                elif "xfce" in var_0 or var_0.startswith("xubuntu"):
                    return "xfce4"
                elif var_0.startswith('ubuntustudio'):
                    return 'kde'
                elif var_0.startswith('ubuntu'):
                    return 'gnome'     
                elif var_0.startswith("lubuntu"):
                    return "lxde" 
                elif var_0.startswith("kubuntu"): 
                    return "kde" 
                elif var_0.startswith("razor"): # e.g. razorkwin
                    return "razor-qt"
                elif var_0.startswith("wmaker"): # e.g. wmaker-common
                    return "windowmaker"
            if os.environ.get('KDE_FULL_SESSION') == 'true':
                return "kde"
            elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                    return "gnome2"
            #From http://ubuntuforums.org/showthread.php?t=652320
            elif self.is_running("xfce-mcs-manage"):
                return "xfce4"
            elif self.is_running("ksmserver"):
                return "kde"
        return "unknown"

    def is_running(self, var_1):
        #From http://www.bloggerpolis.com/2011/05/how-to-check-if-a-process-is-running-using-python/
        # and http://richarddingwall.name/2009/06/18/windows-equivalents-of-ps-and-kill-commands/
        try: #Linux/Unix
            var_2 = subprocess.Popen(["ps", "axw"],stdout=subprocess.PIPE)
        except: #Windows
            var_2 = subprocess.Popen(["tasklist", "/v"],stdout=subprocess.PIPE)
        for x in var_2.stdout:
            if re.search(var_1, x):
                return True
        return False
