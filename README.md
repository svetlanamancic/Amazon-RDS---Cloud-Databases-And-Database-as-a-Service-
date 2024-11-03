U doba modernih informacionih tehnologija, gde obim podataka i brzina njihovog prikupljanja eksponencijalno rastu, tradicionalne metode upravljanja podacima postaju neadekvatne. Tradicionalni pristup upravljanju bazama podataka, koji se oslanja na lokalni hardver i softver, nailazi na prepreke u suočavanju sa eskalacijom obima podataka, promenljivim radnim opterećenjem i odazivom u realnom vremenu. Ovi izazovi predstavljaju ograničenja lokalne infrastrukture, koja se često bori da efikasno skalira kako bi zadovoljila promenljive zahteve. Kako bi se oni prevazišli, neophodna je stalna nadogradnja i održavanje lokalnog hardvera, što zahteva značajne finansijske izdatke i operativne troškove. 

Kao odgovor na ove izazove pojavilo se računarstvo u oblaku, koje omogućava organizacijama da prevaziđu ograničenja lokalne infrastrukture. Klaud pruža pristup ogromnoj količini računarskih resursa i kapacitetima skladištenja na zahtev. Skalabilnost i elastičnost infrastrukture oblaka omogućava da se trenutno obezbede resursi, neprimetno skaliranje i optimizaciju troškova, time što se plaćaju samo resursi koji se koriste. Osim toga, usluge u oblaku koriste napredne metode enkripcije i mehanizme rezervnih kopija, čime se jača integritet podataka i otpornost na potencijalne pretnje, kao i globalno distribuirane data centre, koji obezbeđuju visoku dostupnost i oporavak od katastrofe. 

U cilju demonstracije rada Amazon RDS servisa kreirana je instanca na AWS-u, a sistem opisan u radu prikazan je na sledećoj slici.


![image](https://github.com/user-attachments/assets/3985fbd2-eecf-4cf4-9014-f34f30dcc496)



RDS instanca je povezana sa EC2 instancom, koja se nalazi u istom VPC kao i RDS instanca.
Na EC2 instanci pokrenut je server napisan u Pythonu, koji ima nekoliko endpointa, čija je funkcija pribavljanje podataka iz baze u cilju demonstracije povezivanja i rada sa Amazon RDS instancom.

Instance su uništene nakon izrade seminarskog rada i više nisu dostupne na adresama prikazanim na slikama.
