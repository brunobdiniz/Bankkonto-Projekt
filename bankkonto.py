print('hello world')

'''
Bankkonto Projekt
'''

class Konto:
    def __init__(self, kunde_id):
        self.kunde_id = kunde_id


class Girokonto(Konto):
    def __init__(self, kunde_id, einzahlungs_betrag):
        Konto.__init__(self, kunde_id)
        self.betrag = einzahlungs_betrag
        self.abheben_ganz = 0
        self.abheben_teil = 0

        self.numstr = "%.2f" % einzahlungs_betrag

        self.betrag_ganz = int(self.numstr[:self.numstr.find('.')])

        self.betrag_teil = int(self.numstr[self.numstr.find('.') + 1:])

    def einzahlung(self, einzahlungs_betrag):
        self.betrag += einzahlungs_betrag

    def abheben(self, abheben_betrag):

        self.abheben_ganz = int(abheben_betrag[:abheben_betrag.find('.')])
        numstr = str(abheben_betrag)
        self.abheben_teil = int(numstr[numstr.find('.') + 1:])

        if self.betrag > float(abheben_betrag):
            self.betrag_ganz -= self.abheben_ganz

            if self.abheben_teil > self.betrag_teil:
                self.betrag_teil = self.abheben_teil - self.betrag_teil
                self.betrag_ganz -= 1
                self.betrag_teil = 100 - self.betrag_teil
            else:
                self.betrag_teil -= self.abheben_teil

            neue_betrag = str(self.betrag_ganz) + "." + str(self.betrag_teil)

            self.betrag = round(float(neue_betrag), 2)
        else:
            print("Fehler! Sie können nicht mehr Geld abheben, als Sie haben.")

    def anzeige_betrag(self):
        print(self.betrag)

    def erhalten_betrag(self):
        return self.betrag


class SparKonto(Konto):
    def __init__(self, kunde_id, einzahlungs_betrag):
        Konto.__init__(self, kunde_id)
        self.betrag = einzahlungs_betrag
        self.abheben_ganz = 0
        self.abheben_teil = 0

        self.numstr = "%.2f" % einzahlungs_betrag

        self.betrag_ganz = int(self.numstr[:self.numstr.find('.')])

        self.betrag_teil = int(self.numstr[self.numstr.find('.') + 1:])

    def einzahlung(self, einzahlungs_betrag):
        self.betrag += einzahlungs_betrag

    def abheben(self, abheben_betrag):

        self.abheben_ganz = int(abheben_betrag[:abheben_betrag.find('.')])
        numstr = str(abheben_betrag)
        self.abheben_teil = int(numstr[numstr.find('.') + 1:])

        if self.betrag > float(abheben_betrag):
            self.betrag_ganz -= self.abheben_ganz

            if self.abheben_teil > self.betrag_teil:
                self.betrag_teil = self.abheben_teil - self.betrag_teil
                self.betrag_ganz -= 1
                self.betrag_teil = 100 - self.betrag_teil
            else:
                self.betrag_teil -= self.abheben_teil

            neue_betrag = str(self.betrag_ganz) + "." + str(self.betrag_teil)

            self.betrag = round(float(neue_betrag), 2)
        else:
            print("Fehler! Sie können nicht mehr Geld abheben, als Sie haben.")

    def anzeige_betrag(self):
        print(self.betrag)

    def erhalten_betrag(self):
        return self.betrag


class GeschaftsKonto(Konto):
    def __init__(self, kunde_id, einzahlungs_betrag):
        Konto.__init__(self, kunde_id)
        self.betrag = einzahlungs_betrag
        self.abheben_ganz = 0
        self.abheben_teil = 0

        self.numstr = "%.2f" % einzahlungs_betrag

        self.betrag_ganz = int(self.numstr[:self.numstr.find('.')])

        self.betrag_teil = int(self.numstr[self.numstr.find('.') + 1:])

    def einzahlung(self, einzahlungs_betrag):
        self.betrag += einzahlungs_betrag

    def abheben(self, abheben_betrag):

        self.abheben_ganz = int(abheben_betrag[:abheben_betrag.find('.')])
        numstr = str(abheben_betrag)
        self.abheben_teil = int(numstr[numstr.find('.') + 1:])

        if self.betrag > float(abheben_betrag):
            self.betrag_ganz -= self.abheben_ganz

            if self.abheben_teil > self.betrag_teil:
                self.betrag_teil = self.abheben_teil - self.betrag_teil
                self.betrag_ganz -= 1
                self.betrag_teil = 100 - self.betrag_teil
            else:
                self.betrag_teil -= self.abheben_teil

            neue_betrag = str(self.betrag_ganz) + "." + str(self.betrag_teil)

            self.betrag = round(float(neue_betrag), 2)
        else:
            print("Fehler! Sie können nicht mehr Geld abheben, als Sie haben.")

    def anzeige_betrag(self):
        print(self.betrag)

    def erhalten_betrag(self):
        return self.betrag


if __name__ == '__main__':
    isSessionOn = True
    isCustomer = False

    def initialise_objects():
        global manuel_giro, jana_geschaft, jana_spar, zusammen_liste

        manuel_giro = Girokonto(1, 2567.50)
        jana_geschaft = GeschaftsKonto(2, 12890.01)
        jana_spar = SparKonto(2, 14500.40)

        zusammen_liste = [[manuel_giro, 1, 1], [jana_geschaft, 2, 2], [jana_spar, 2, 3]]

        return None

    initialise_objects()

    while isSessionOn is True:
        print("Willkommen beim 24-Stunden-Geldautomatenservice.")
        print("Stecken Sie Ihre Karte ein.")

        kundenID = input("Geben Sie Ihre Kundennummer ein: ")
        print("\n")

        kunden_kontos = []
        for i in zusammen_liste:
            if i[1] == kundenID:
                kunden_kontos.append(i[2])
                isCustomer = True

        if isCustomer is True:
            isAccountSelected = False

            while isAccountSelected is False:
                print("1 für Girokonto eingeben")
                print("2 für Sparkonto eingeben")
                print("3 für Geschäftskonto eingeben")
                konto_type = input("Geben Sie das zu verwendende Konto an: ")

                if konto_type in kunden_kontos:
                    for x in zusammen_liste:
                        if konto_type == x[2]:
                            objectName = x[0]

                    isAccountSelected = True
                    isAccountSessionOn = True

                    while isAccountSessionOn is True:
                        print("\nWie kann ich Ihnen helfen?")
                        print("Drücken Sie 1 für die Waagenansicht.")
                        print("Drücken Sie 2 für Abhebungen")
                        print("Drücken Sie 3 zum Beenden.")

                        action_value = input("Please enter your choice: ")

                        if action_value == 1:
                            objectName.anzeige_betrag()
                            print("\n")

                        if action_value == 2:
                            betrag_zu_abheben = input("Geben Sie den zu abheben Betrag ein: ")
                            temp_str = str(betrag_zu_abheben)

                            verrechnungswert = "%.2f" % betrag_zu_abheben
                            
                            objectName.abheben(verrechnungswert)

                            print("Das aktuelle Gleichgewicht ist", objectName.erhalten_betrag())
                            print("\n")

                        if action_value == 3:
                            isAccountSessionOn = False
                            print("Vielen Dank für die Nutzung des 24-Stunden-Automaten-Service.")
                            print("Ich wünsche Ihnen einen schönen Tag.")
                            print("\n\n")
                            print("##########################################")
                else:
                    print("Fehler. Sie haben dieses Konto nicht.")
                    print("Bitte versuchen Sie es erneut.\n")

        else:
            print("Ich kann Ihren Eintrag nicht finden.")
            print("Bitte holen Sie Ihre Karte.")
            print("Beenden dieser Sitzung...")
