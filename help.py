def GetUPSVars(self, ups=""):
    """ Get all available vars from the specified UPS
The result is a dictionary containing 'key->val' pairs of all
available vars.
    """
    if self.__debug:
        print("[DEBUG] GetUPSVars called...")

    self.__srv_handler.write("LIST VAR %s\n" % ups)
    result = self.__srv_handler.read_until("\n")
    if result != "BEGIN LIST VAR %s\n" % ups:
        raise PyNUTError(result.replace("\n", ""))

    ups_vars = {}
    result = self.__srv_handler.read_until("END LIST VAR %s\n" % ups)
    offset = len("VAR %s " % ups)
    end_offset = 0 - (len("END LIST VAR %s\n" % ups) + 1)

    for current in result[:end_offset].split("\n"):
        var = current[offset:].split('"')[0].replace(" ", "")
        data = current[offset:].split('"')[1]
        ups_vars[var] = data

    return (ups_vars)
