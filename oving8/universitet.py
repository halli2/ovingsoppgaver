def les_heltall(sporsmaal):
    svar = 0
    fortsett = True
    while fortsett:
        try:
            svar = int(input(sporsmaal))
            fortsett = False
        except ValueError:
            print("Du må skrve et heltall. prøv på nytt.")
    return svar


class Student:
    neste_studentnummer = 1

    def __init__(self, etternavn, fornavn, studieprogram, aarskurs=1):
        self.__studentnummer = Student.neste_studentnummer
        Student.neste_studentnummer += 1
        self.etternavn = etternavn
        self.fornavn = fornavn
        self.studieprogram = studieprogram
        self.aarskurs = aarskurs
        self.emner = []

    @property
    def studentnummer(self):
        return self.__studentnummer

    @property
    def aarskurs(self):
        return self.__aarskurs

    @aarskurs.setter
    def aarskurs(self, nytt_aarskurs):
        if nytt_aarskurs < 1:
            raise ValueError("Årskurs kan ikke være under 1!")
        if nytt_aarskurs > 5:
            raise ValueError("Årskurs kan ikke være over 5!")
        self.__aarskurs = nytt_aarskurs

    
    # A)

    def nytt_emne(self, nytt_emne):
        self.emner.append(nytt_emne)
        # Gjør at legger til i emner?
        


    # B)
    def belastning(self):
        belastning = 0
        for emne in self.emner:
            belastning += emne.studiepoeng
        return belastning

    # C)
    def emneutskrift(self):
        emner_til_studenten = ''
        for emne in self.emner:
            emner_til_studenten += f'{emne.emnenavn} \n'
        return f'{self.fornavn} {self.etternavn} har følgende emner:\n{emner_til_studenten}'


    def __str__(self):
        return f"Student {self.__studentnummer}: {self.fornavn} {self.etternavn}, studerer {self.studieprogram} i" \
            f" {self.aarskurs} årskurs."


class Foreleser:
    def __init__(self, etternavn, fornavn, fagfelt, kontor, epost):
        self.etternavn = etternavn
        self.fornavn = fornavn
        self.fagfelt = fagfelt
        self.kontor = kontor
        self.epost = epost

    def __str__(self):
        return f"Foreleser {self.fornavn} {self.etternavn} i {self.fagfelt}."


class Emne:
    def __init__(self, emnekode, emnenavn, studiepoeng=10, semester="H", emneansvarlig=None, kontakt_epost=None):
        self.emnekode = emnekode
        self.emnenavn = emnenavn
        self.studiepoeng = studiepoeng
        self.semester = semester
        self.emneansvarlig = emneansvarlig
        self.studenter = []
        if kontakt_epost == None and emneansvarlig == None:
             self.kontakt_epost = None
        elif emneansvarlig == None:
            self.kontakt_epost = kontakt_epost
        else:
            self.kontakt_epost = emneansvarlig.epost

    # D)
    # lag en liste med alle studentene som har emne
    def sett_kontakt_epost(self, ny_kontakt_epost):
        self.kontakt_epost = ny_kontakt_epost

    def legg_til_student(self, student: Student):
        if self in student.emner:
            self.studenter.append(student)
        else:
            student.emner.append(self)
            self.studenter.append(student)

    def klasseliste(self):
        klasseliste = f'Studenter som tar emne {self.emnenavn}:\n'
        for student in self.studenter:
            klasseliste += f'{student.fornavn} {student.etternavn}\n'
        return klasseliste
        

    def __str__(self):
        return f"Emne {self.emnekode} {self.emnenavn} på {self.studiepoeng} studiepoeng i " \
            f"semester {self.semester} og har {self.emneansvarlig}. Kontaktepost er {self.kontakt_epost}"


class System:
    def __init__(self):
        self.studenter = []
        self.forelesere = []
        self.emner = []

    def skriv_inn_student(self):
        print("Skriv inn student: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        studieprogram = input("Studieprogram: ")
        aarskurs = int(input("Årskurs: "))
        studenten = Student(etternavn, fornavn, studieprogram, aarskurs)
        self.studenter.append(studenten)

    def skriv_inn_foreleser(self):
        print("Skriv inn foreleser: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        fagfelt = input("Fagfelt: ")
        kontor = input("Kontor: ")
        epost = input("Epost: ")
        foreleseren = Foreleser(etternavn, fornavn, fagfelt, kontor, epost)
        self.forelesere.append(foreleseren)

    def skriv_inn_emne(self):
        print("Skriv inn emne: ")
        emnekode = input("Emnekode: ")
        navn = input("Navn: ")
        studiepoeng = int(input("Studiepoeng: "))
        semester = input("Semester (H for høst, V for vår): ")
        emnet = Emne(emnekode, navn, studiepoeng, semester)
        self.emner.append(emnet)

    def skriv_studenter(self):
        print("Studentene: ")
        for index, student in enumerate(self.studenter):
            print(f"{index}: {student}")

    def skriv_foreleserne(self):
        print("Foreleserne: ")
        for index, foreleser in enumerate(self.forelesere):
            print(f"{index}: {foreleser}")

    def skriv_emner(self):
        print("Emnene: ")
        for index, emne in enumerate(self.emner):
            print(f"{index}: {emne}")

    def sett_foreleser_for_emne(self):
        self.skriv_foreleserne()
        self.skriv_emner()
        emneindex = les_heltall("Velg emne: ")
        foreleserindex = les_heltall("Velg foreleser: ")
        self.emner[emneindex].emneansvarlig = self.forelesere[foreleserindex]

    def sett_inn_standard_data(self):
        self.forelesere.append(Foreleser("Tøssebro", "Erlend", "Data", "E-442", "et@uis.no"))
        self.forelesere.append(Foreleser("Eielsen", "Arnfinn", "Elektro", "E-454", "ae@uis.no"))
        self.forelesere.append(Foreleser("Hervik", "Sigbjørn", "Matematikk", "E-543", "sh@uis.no"))
        self.emner.append(Emne("DAT110", "Grunnleggende programmering", 10, "V", self.forelesere[0]))
        self.emner.append(Emne("ING100", "Ingeniørfaglig Innføringsemne"))
        self.emner.append(Emne("MAT100", "Matematiske metoder 1"))
        self.emner.append(Emne("RED101", "Kjemi for data og elektro", 5))
        self.emner.append(Emne("RED102", "Fysikk for data og elektro", 5))
        self.studenter.append(Student("Nilsen", "Arne", "Data"))
        self.studenter.append(Student("Torgersen", "Ida", "Data"))
        self.studenter.append(Student("Ås", "Erling", "Elektro"))
        self.studenter.append(Student("Fredriksen", "Anne", "Elektro"))

        # metodene under kaller metodene laget i oppgaven.

    def skriv_inn_emne_student(self):
        self.skriv_studenter()
        svar_stud = les_heltall("Velg student: ")
        self.skriv_emner()
        svar_nytt_emne = les_heltall("Velg emne: ")
        self.emner[svar_nytt_emne].legg_til_student(self.studenter[svar_stud])


    def belastning_til_student(self):
        self.skriv_studenter()
        svar = les_heltall("Velg student: ")
        belastning = self.studenter[svar].belastning()
        print(f"Studenten har belastning på {belastning} studiepoeng.")

    def emneutskrift_til_student(self):
        for idx, student in enumerate(self.studenter):
            print(f'{idx}: {student}')
        svar = les_heltall("Velg student: ")
        print(self.studenter[svar].emneutskrift())
    
    def studenter_i_emne(self):
        for idx, emne in enumerate(self.emner):
            print(f'{idx}: {emne}')
        svar = les_heltall("Velg emne: ")
        print(self.emner[svar].klasseliste())

        
    def legg_til_kontakt_epost(self):
        for idx, emne in enumerate(self.emner):
            print(f'{idx}: {emne}')
        svar = les_heltall("Velg emne: ")
        ny_kontakt_epost = input("Skriv inn epost: ")
        self.emner[svar].sett_kontakt_epost(ny_kontakt_epost)

    def meny(self):
        fortsetter = True
        while fortsetter:
            print("\n meny: ")
            print("0: Skriv inn student")
            print("1: Skriv inn foreleser")
            print("2: skriv inn emne")
            print("3: skriv ut studentene")
            print("4: skriv ut foreleserne")
            print("5: skriv ut emnene")
            print("6: Angi foreleser for et emne")
            print("7: Legg til emne for student")
            print("8: Skriv ut belastning til student")
            print("9: Skriv ut emner til student")
            print("10: Skriv ut studenter som har emne")
            print("11: Sett kontakt-epost for emne")
            print("s: Sett inn standard data (for testing)")
            print("a: avslutt")
            valg = input("Valg: ")
            if valg == "0":
                self.skriv_inn_student()
            elif valg == "1":
                self.skriv_inn_foreleser()
            elif valg == "2":
                self.skriv_inn_emne()
            elif valg == "3":
                self.skriv_studenter()
            elif valg == "4":
                self.skriv_foreleserne()
            elif valg == "5":
                self.skriv_emner()
            elif valg == "6":
                self.sett_foreleser_for_emne()
            elif valg == "7":
                self.skriv_inn_emne_student()
            elif valg == "8":
                self.belastning_til_student()
            elif valg == "9":
                self.emneutskrift_til_student()
            elif valg == "10":
                self.studenter_i_emne()
            elif valg == "11":
                self.legg_til_kontakt_epost()
            elif valg == "s":
                self.sett_inn_standard_data()
            elif valg == "a":
                fortsetter = False


if __name__ == "__main__":
    system = System()
    system.meny()