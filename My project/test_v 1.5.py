import pickle
questions = ["""
        Коомпания-разработчик Windows
        1) Mikrosft
        2) Melkosoft
        3) Cybersoft
        4) Microsoft
        """,
        """
        Самая "яблочная" операционная система
        1) AppleOS
        2) Linux
        3) macOS
        4) FreeBSD
        """,
        """
        Символом какой операционной системы является пингвин
        1) Linux
        2) FreeBSD
        3) OS/2
        4) Windows
        """,
        """
        Сколько бит в одном байте
        1) 8
        2) 6
        3) 4
        4) 2
        """,
        """
        Сколько байт в одном килобайте
        1) 1000
        2) 1024
        3) 1048
        4) 256
        """]
answers = [4, 3, 1, 1, 2]

datafile = open("test.dat", "wb")
pickle.dump(questions, datafile)
pickle.dump(answers, datafile)
datafile.close