import PyNUT

nut_handler = PyNUT.PyNUTClient(host=10.0.0.205, port=port, login=login, password=password)
upses = nut_handler.GetUPSList()

ups_list = upses.keys()
ups_list.sort()
