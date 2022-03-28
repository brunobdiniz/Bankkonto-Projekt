print('hello world')

'''
Bankkonto-Manager
'''

#using INIT to creat classes
	#defining a costumer id
class Konto:
	def __init__(self,kunde_id):
		self.kunde_id = kunde_id

#defining Checkings Acconut's class
class GiroKonto(Konto):
	#defining deposit and adding to the total sum
	def __init__(self,kunde_id,einzahlungsbetrag):
		Konto.__init__(self,kunde_id)
		self.betrag = einzahlungsbetrag
		self.abheben_alles = 0
		self.abheben_teil = 0

		self.numstr = "%.2f" % einzahlungsbetrag

		self.betrag_alles = int(self.numstr[:self.numstr.find('.')])
		self.betrag_teil = int(self.numstr[:self.numstr.find('.')+1:])
	#defining withdraw and subtracting it from the total sum, together with if/else for control
	def einzahlung(self,einzahlungsbetrag):
		self.betrag += einzahlungsbetrag

	def abheben(self,abhebungsbetrag):
		self.abheben_alles = int(abhebungsbetrag[:abhebungsbetrag.find('.')])
		numstr = str(abhebungsbetrag)
		self.abheben_teil = int(numstr[numstr.find('.')+1:])

		if self.betrag > float(abhebungsbetrag):
			self.betrag_alles -= self.abheben_alles

			if self.abheben_teil > self.betrag_teil:
				self.betrag_teil = self.abheben_teil - self.einzahlung_teil
				self.betrag_alles -= 1
				self.betrag_teil = 100 - self.betrag_teil
			else:
				self.betrag_teil -= self.abheben_teil


			neue_betrag = str(self.betrag_alles)+"."+str(self.betrag_teil)

		else:
			print('Fehler! Sie können nicht mehr Geld abheben, als Sie haben.')
	#defining print function to the amount     
	def anzeigen_betrag(self):
		print(self.betrag)
	#defining a return function to the amount
	def bekommen_betrag(self):
		return self.betrag


#defining Savings Account class
class Sparkonto(Konto):
	def __init__(self,kunde_id,einzahlungsbetrag):
		Konto.__init__(self,kunde_id)
		self.betrag = einzahlungsbetrag
		self.abheben_alles = 0 
		self.abheben_teil = 0 

		self.numstr = "%.2f" % einzahlungsbetrag

		self.betrag_alles = int(self.numstr[:self.numstr.find('.')])

		self.betrag_teil = int(self.numstr[self.numstr.find('.')+1:])
	#defining deposit and adding to the total sum
	def einzahlung(self,einzahlungsbetrag):
		self.betrag += einzahlungsbetrag
	#defining withdraw and subtracting it from the total sum, together with if/else for control
	def withdraw(self,abhebungsbetrag):
		self.abheben_alles = int(abhebungsbetrag[:abhebungsbetrag.find('.')])
		numstr = str(abhebungsbetrag)
		self.abheben_teil = int(numstr[numstr.find('.')+1:])

		if self.betrag > float(abhebungsbetrag):
			self.betrag_alles -= self.abheben_alles

			if self.abheben_teil > self.betrag_teil:
				self.betrag_teil = self.abheben_teil - self.betrag_teil
				self.betrag_alles -= 1 
				self.betrag_alles = 100 - self.abheben_teil
			else:
				self.betrag_teil -= self.abheben_teil


			neue_betrag = str(self.betrag_alles) + "." + str(self.betrag_teil)

			self.betrag = round(float(neue_betrag),2)

		else:
			print("Fehler! Sie können nicht mehr abheben, als Sie haben.")

	#defining a print function to the amount
	def anzeigen_betrag(self):
		print(self.betrag)
	#defining a return function to the amount
	def bekommen_betrag(self):
		return self.betrag



#defining Business Account class
class Geschäftskonto(Konto):
	def __init__(self,kunde_id,einzahlungsbetrag):
		Konto.__init__(self,kunde_id)
		self.betrag = einzahlungsbetrag
		self.abheben_alles = 0
		self.abheben_teil = 0

		self.numstr = "%.2f" % einzahlungsbetrag

		self.betrag_alles = int(self.numstr[:self.numstr.find('.')])

		self.betrag_teil = int(self.numstr[self.numstr.find('.')+1:]) 
	#defining deposit and adding to the total sum
	def deposit(self,einzahlungsbetrag):
		self.betrag += einzahlungsbetrag
	#defining withdraw and subtracting it from the total sum, together with if/else for control
	def abheben(self,abhebungsbetrag):
		self.abheben_alles = int(abhebungsbetrag[:abhebungsbetrag.find('.')])
		numstr = str(abhebungsbetrag)
		self.abheben_teil = int(numstr[numstr.find('.')+1:])

		if self.betrag > float(abhebungsbetrag):
			self.betrag_alles -= self.abheben_alles

			if self.abheben_teil > self.betrag_teil:
				self.betrag_teil = self.abheben_teil - self.betrag_teil
				self.betrag_alles -= 1 
				self.betrag_teil = 100 - self.abheben_teil
			else:
				self.betrag_teil -=self.abheben_teil

			neue_betrag = str(self.betrag_alles) + "." + str(self.betrag_teil)
		else:
			print("Fehler! Sie können nicht mehr abheben, als Sie haben.")
	#defining a print function to the amount
	def anzeigen_betrag(self):
		print(self.betrag)
	#defining a return function to the amount
	def bekommen_betrag(self):
		return self.betrag


#running logic

#if statement for customer's access and allowing movements in the account
	#create function for customers numbers and amounts available

if __name__ == '__main__':
	isSessionOn = True
	isCustomer = False 

	def init_objekte():
		global jana_giro, manuel_geschäfts, jana_spar, master_list

		jana_giro = GiroKonto(1, 8578.50)
		manuel_geschäfts = Geschäftskonto(2, 74589.40)
		jana_spar = Sparkonto(1,93401.04)
		master_list = [[jana_giro,1,1][manuel_geschäfts,2,2][jana_spar,1,3]]

		return None

		init_objekte()

	#while loop for client's access
	while isSessionOn is True:
		print("Willkommen beim 24-Stunden-Geldautomatenservice.")
		print("Karte einlegen.")

		kundenID = input("Geben Sie Ihre Kunden ID ein: ")
		print("\n")

		kunden_konten = []
		for k in master_list:
			if k[1] == kundenID:
				kunden_konten.append(k[2])
				isCustomer = True

	#if/while with booleans for inputs
		if isCustomer is True:
			isAccountSelected = False

			while isAccountSelected is False:
				print("1 für Girokonto eingeben")
				print("2 für Sparkonto eingeben")
				print("3 für Geschäftskonto eingeben")
				konto_typ = input("Geben Sie das zu verwendende Konto an: ")

				if konto_typ in kunden_konten:
					for x in master_list:
						if konto_typ == x[2]:
							objectName = x[0]

					isAccountSelected = True
					isAccountSessionOn = True

					while isAccountSessionOn is True:
						print("Wie kann ich Ihnen helfen?")
						print("Drücken Sie 1 für die Waagenansicht.")
						print("Drücken Sie 2 für Abhebung.")
						print("Drücken Sie 3 zum Beended.")

						input_action = input("Bitte geben Sie Ihre Wahl ein: ")

						if input_action == 1:
							objectName.anzeigen_betrag()

						if input_action == 2:
							betrag_z_abhebung = input("Geben Sie den zu entnehmenden Betrag ein: ")
							format_str = str(betrag_z_abhebung)

							einstellen_betrag = "%.2f" % betrag_z_abhebung
							objectName.abheben(einstellen_betrag)
							print("Das aktuelle Gleichgewicht ist:",objectName.bekommen_betrag())

						if input_action == 3:
							isAccountSessionOn = False
							print("Vielen Dank für die Nutzung des 24-Stunden-Automaten-Service.")
							print("Ich wünsche Ihnen einen schönen Tag.")

					else:
						print("Fehler. Sie haben dieses Konto nicht.")
						print("Bitte versuchen Sie noch ein mal.")
    #Finalize section
				else:
					print("Wir können Ihren Eintrag nicht finden.")
					print("Bitte holen Sie Ihre Karte.")
					print("Beenden dieser Sitzung.")
