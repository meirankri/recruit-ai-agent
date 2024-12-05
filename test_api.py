import requests
import json
from time import sleep

API_URL = "http://localhost:8000/analyze/"

# Données de test
job_offers = {
    "Technicien_cablage": """
    {"jobTitle":"TECHNICIEN DE CABLAGE DE PRODUCTION (F/H)-REF 2402-02","companyName":"Alcatel Submarine Networks","postLocation":{"city":"Clamart","country":"France","workplaceType":"onsite"},"description":"<p><strong>À propos du poste :</strong></p><ol><li data-list=\"bullet\">Contexte et objectifs principaux :</li><li data-list=\"bullet\">Fabrication d'instruments de mesure et de contrôle de haute fiabilité</li><li data-list=\"bullet\">Réalisation de montages et interconnections pour l'intégration de sous-ensembles électroniques</li><li data-list=\"bullet\">Contribution à l'amélioration des produits et des processus de production</li></ol><p><br></p><p> <strong>Vos missions :</strong></p><ol><li data-list=\"bullet\"><strong>Assemblage et test :</strong> Assemblage et test de cartes et d’ensembles électroniques, de capteurs et d’outils de haute technicité</li><li data-list=\"bullet\"><strong>Inspection :</strong> Inspections de la conformité des pièces avant l’intégration</li><li data-list=\"bullet\"><strong>Traçabilité :</strong> Enregistrement des informations de traçabilités des composants intégrés</li><li data-list=\"bullet\"><strong>Mise à jour :</strong> Mise à jour du statut de production de sa cellule de production</li><li data-list=\"bullet\"><strong>Maintenance :</strong> Maintenance du parc d’instruments sous sa responsabilité</li><li data-list=\"bullet\"><strong>Analyse des défaillances :</strong> Participation à l’analyse des défaillances constatées lors des opérations de tests</li><li data-list=\"bullet\"><strong>Démarche 5S+1 :</strong> Participation à la démarche « 5S+1 » dans son environnement de production</li><li data-list=\"bullet\"><strong>Amélioration continue :</strong> Contribution au processus d’amélioration continue de la ligne de produit</li></ol><p><br></p><p> <strong>Environnement technique :</strong></p><ol><li data-list=\"bullet\">Fabrication : Techniques d’assemblage de cartes électroniques, d’ensembles électroniques et capteurs : brasure, sertissage, collage, frettage</li><li data-list=\"bullet\">Electronique : Schémas électriques et électroniques, nomenclature</li><li data-list=\"bullet\">Tests : Instruments électroniques de base (multimètre, oscilloscope), système de test automatisé (LabVIEW, Agilent VEE)</li><li data-list=\"bullet\">Mécanique : Montage, couple de serrage, matériaux</li></ol><p><br></p><p> <strong>Conditions de travail :</strong></p><ol><li data-list=\"bullet\">Lieu de travail : Clamart, France</li><li data-list=\"bullet\">Type de contrat : CDI</li><li data-list=\"bullet\">Temps de travail : Temps plein</li></ol>","profile":"<p><strong>Formation et expérience :</strong></p><ol><li data-list=\"bullet\">Formation : BTS ou BUT dans le domaine de l’électronique, ou titre équivalent, ou un CAP dans le domaine de câblage et électronique</li><li data-list=\"bullet\">Certification : IPC 610 ou 620 est un atout supplémentaire</li><li data-list=\"bullet\">Habilitation électrique</li><li data-list=\"bullet\">Expérience : Expériences professionnelles dans un atelier d’intégration des produits haute technologie, de préférence dans l’industrie pétrolière ou aéronautique</li></ol><p><br></p><p> <strong>Compétences techniques :</strong></p><ol><li data-list=\"bullet\"><strong>Fabrication :</strong> Techniques d’assemblage de cartes électroniques, d’ensembles électroniques et capteurs</li><li data-list=\"bullet\"><strong>Electronique :</strong> Schémas électriques et électroniques, nomenclature</li><li data-list=\"bullet\"><strong>Tests :</strong> Instruments électroniques de base, système de test automatisé</li><li data-list=\"bullet\"><strong>Mécanique :</strong> Connaissance générale en mécanique</li></ol><p><br></p><p> <strong>Compétences comportementales :</strong></p><ol><li data-list=\"bullet\">Sécurité : Identification et réduction des risques, application des règles de sécurité</li><li data-list=\"bullet\">Qualité : Souci constant de la qualité</li><li data-list=\"bullet\">Planification et organisation : Facultés d'adaptation, capacité à établir un planning</li><li data-list=\"bullet\">Travail d’équipe : Qualités humaines nécessaires au travail en équipe</li><li data-list=\"bullet\">Communication : Communication avec les autres membres de l'organisation Manufacturing</li><li data-list=\"bullet\">Informatique : Bonnes connaissances des logiciels de bureautique</li><li data-list=\"bullet\">Langue : Pratique de l'anglais est un atout supplémentaire</li></ol>","employeeCount":1,"culture":null,"salary":{"salary":{"max":"38","min":"32","period":"year"}},"contract":{"type":"CDI","workingTime":"full"}}
    """
}

cvs = {
    "candidate_pertinent1": """
        Technicien Monteur Câbleur 
        + 10 années d’exp 
        
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE 
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.com 
        1 
        
        
        Responsable d'atelier  
        ▪ Suivi et gestion de la production  
        ▪ Mise en place des AIC  
        ▪ Mise en place de la maintenance 1er niveau et résolution de problèmes  
        ▪ Gestion et suivi de la sécurité HSE 
        ▪ Présentation Team brief  
        ▪ Suivi des équipes et de l'évolution de chaque collaborateur  
        ▪ Gestion des entretiens individuels et annuels  
        
        Monteur de tube HF 
        ▪ Soudure à l'étain  
        ▪ Mesure électrique sur banc d'essai  
        ▪ Lecture de schéma  
        ▪ Passage des câbles en tube HF  
        ▪ Préparation et dépôt de colle  
        ▪ Nettoyage  
        ▪ Pyrolyse sur poste HF  
        ▪ Dépôt de couche mince via bâti de pulvérisation  
        ▪ Pyrolyse via bâti hyper fréquence  
        ▪ Utilisation four à recuit sous vide et sous air  
        ▪ Création de programme sur banc de test Référent technique  
        ▪ Formateur au poste de travail  
        
        Câbleur électronique  
        ▪ Câblage filaire  
        ▪ Soudure composants (CMS) sur carte  
        ▪ Test sur banc d'essai 
        
        
        
        ▪ SAP 
        ▪ MES 
        ▪ FOR YOU 
        ▪ WORKDAY 
        ▪ Pack Office 
        
        
        
        DOMAINES DE COMPETENCES 
        OUTILS  
        ----------------Page (0) Break----------------
        YCH 
        Technicien Monteur Câbleur 
        + 10 années d’exp 
        
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE 
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.com 
        2 
        
        
        ▪ Aéronautique  
        
        
        
        ▪ BAC           2019 
        Microtechnique 
        DAVA, Versailles [78]. 
        
        ▪ BEP           2007 
        Electrotechnique 
        Lycée J. Vaucanson, Les Mureaux [78]. 
        
        ▪ Formation Interne          2013 - 2023 
        IPC A 610 / IPC A 620  
        Habillage tube préréglé, tube durci, habillage tube durci,  
        Le tube le fondamentale  
        Résolution de problèmes les basiques  
        Méthode 5s  
        Les basiques de Lean et le Lean en production  
        Clean Concept  
        Formation de Formateur au poste de travail  
        Le traitement de surface par couche mince  
        Initiation au vide 
        
        
        
        
        ▪ Anglais :   Notion 
        ▪ Français :  Maternelle 
        
        
        SECTEUR D’ACTIVITE 
        DIPLOMES / FORMATION 
        LANGUES 
        ----------------Page (1) Break----------------
        YCH 
        Technicien Monteur Câbleur 
        + 10 années d’exp 
        
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE 
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.com 
        3 
        SAFRAN (6 mois) – 11/2023 – 05/2024   
        
        Monteur Câbleur  
        
        ▪ Montage Mécanique  
        ▪ Intégration Electronique 
        ▪ Brasure, Etamage 
        ▪ Sertissage 
        ▪ Câblage filaire sur harnais 
        ▪ Intégration de gaine 
        ▪ Passage de gaine blindé 
        
        
        THALES (2 ans) – 2021 – 2023   
        
        Responsable d’Atelier   
        
        ▪ Suivi et gestion de la production  
        ▪ Mise en place des AIC  
        ▪ Mise en place de la maintenance 1er niveau et résolution de problèmes  
        ▪ Gestion et suivi de la sécurité HSE  
        ▪ Présentation Team brief  
        ▪ Suivi des équipes et de l'évolution de chaque collaborateur  
        ▪ Gestion des entretiens individuels et annuels 
        
        
        THALES (4 ans) – 2017 – 2021   
        
        Monteur de tube 
        
        ▪ Transformation chimique de composants  
        ▪ Programmation 
        ▪ Dépôt sur le montant 
        ▪ Test sur Banc d’essais  
        ▪ Rédaction de PV  
        ▪ Référent de l’Atelier  
        ▪ Création de programme 
        ▪ Formation des nouveaux arrivants 
        
        
        EXPERIENCES PROFESSIONNELLES 
        ----------------Page (2) Break----------------
        YCH 
        Technicien Monteur Câbleur 
        + 10 années d’exp 
        
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE 
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.com 
        4 
        THALES (4 ans) – 2013 – 2017   
        
        Monteur câbleur Electronique 
        
        ▪ Montage mécanique,  
        ▪ Câblage filaire sur cartes électroniques, 
        ▪ Sertissage, 
        ▪ Essais sur tube hyperfréquence, 
        ▪ Etamage, 
        ▪ Traçabilité de la production 
        ▪ Fiche suiveuse 
        ▪ Utilisation quotidienne de SAP 
        ▪ Gamme papier 
        
        
        TRACETEL (4 mois) – 2007   
        
        Monteur Câbleur Electronique   
        
        ▪ Câblage filaire 
        ▪ Soudure de composants 

    """,
    
    "candidate_pertinent2": """

        LRB
        Technicien Monteur Câbleur Filaire
        15 ans exp
        DOMAINES DE COMPETENCES
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        Certification IPC A 610 / IPC A 620
        Câblage filaire (Torons, boudinette, reprise de blindage, nœud de frette)
        Test Fonctionnel
        Montage et assemblage d’ensemble électronique
        Sertissage, collage, brasage
        Traçabilité de la production
        Lecture schéma et nomenclature
        Fabrication, réalisation câblage aéronautique aérospatiale
        Installation, intégration
        Réparation des faisceaux équipements électriques réservoir Ariane
        OUTILS
        ▪
        ▪
        ▪
        Couple de sertissage, Multimètre, Fer à souder
        SAP
        Pack Office
        SECTEUR D’ACTIVITE
        ▪
        ▪
        ▪
        ▪
        Aéronautique
        Spatial
        Militaire
        Automobile
        DIPLOMES / FORMATION
        ▪CFA
        Câblage Aéronefs
        CFA Massy Palaiseau2015
        ▪NEC AERO
        Formation électronique aéronautique
        Interne à Dassault2006 - 2011
        ▪BAC1999
        Certification :
        ▪
        Certification IPC A (610 et 620)
        2021
        1
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.comLRB
        Technicien Monteur Câbleur Filaire
        15 ans exp
        LANGUES
        ▪
        ▪
        Anglais :
        Français :
        Intermédiaire
        Natif
        EXPERIENCES PROFESSIONNELLES
        MOTORS SPORT
        (5 mois) – 10/2023 – 02/2024
        Technicienne Câbleur Filaire – Prototypiste
        ▪
        ▪
        ▪
        ▪
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        SABENA TECHNICS
        (1 an) – 2022 – 2023
        Technicienne Câbleur Filaire
        ▪
        ▪
        ▪
        ▪
        ▪
        Avion pour la DGA (prototype)
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        MBG FOKKER DGA
        (1 an) – 2022 – 2023
        Technicienne Câbleur
        ▪
        ▪
        ▪
        ▪
        ▪
        Rack cabine avionique
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        2
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.comLRB
        Technicien Monteur Câbleur Filaire
        15 ans exp
        DASSAULT
        (3 mois) – 2021 – 2022
        Technicienne Câbleur
        ▪
        ▪
        ▪
        ▪
        ▪
        Fabrication confection des faisceaux avioniques (Falcon)
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        AIRBUS / ARIANE
        (3 ans) – 2019 – 2021
        Technicienne Câbleur
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        Confection fabrication des faisceaux, des mats, des jauges pour réservoir Ariane 5 avec plans de câblage
        Dénudage thermique, sertissage des fils avec outillages spécifiques, test.
        Contrôle de fonctionnement électrique
        Installation
        Intégration des câbles des portes ARIANE
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        RATP
        (4 mois) – 2021 – 2022
        Technicienne Contrôle Qualité
        ▪
        ▪
        Réparation changement des composants des cartes électronique
        Test de fonctionnement
        3
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE
        Simon ZANA • 06 13 53 23 81 • simon.zana@nava-eng.comLRB
        Technicien Monteur Câbleur Filaire
        15 ans exp
        WAGO
        (3 mois) – 2017 – 2018
        Technicienne Câbleur
        ▪
        ▪
        ▪
        ▪
        ▪
        Fabrication confection des faisceaux avioniques (Falcon)
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        DASSAULT
        (3 ans) – 2014 – 2017
        Technicienne Câbleur / Maintenance
        ▪
        ▪
        ▪
        ▪
        ▪
        ▪
        Réparation des câbles
        Des prises électriques Cabine avion Falcon
        Confections des faisceaux
        Sertissages, dénudages
        Installations des câbles
        Test
        AAA – AIRBUS
        (5 ans) – 2006 – 2011
        Technicienne Câbleur / Maintenance
        ▪
        ▪
        ▪
        ▪
        ▪
        Mise en conformité les câbles AIRBUS 380
        Câblage filaire
        Test fonctionnel
        Suivis de la production
        Montage et assemblage ensemble électronique
        4
        NAVA ENGINEERING • 9-11 AVENUE MICHELET, 93400 SAINT-OUEN-SUR-SEINE
    """,
    "candidate_non_pertinent1": """
            Langues
            Anglais
            Niveau C1
            Espagnol
            Niveau C1
            Réseaux sociaux
            Informatique
            Word / Excel
            Centres d'intérêt
            Voyages
            Ile de la Réunion (famille)
            Football
            Pratique du football au club de
            Villabé avec implication pour le
            bon fonctionnement du club
             jacques.felici@free.fr
             06 85 73 11 25
             91250 St Germain Les Corbeil
             Ile de France
             Marié avec enfants
            Permis A
            Permis B
            
            @https://www.linkedin.com/in/jacq
            ues-felici-b2a8472
            
            Jacques FELICI
            Monteur câbleur aéronautique
            Après 32 années passées à évoluer dans l'imprimerie Helio, un bilan de compétences m'a
            permis de prendre la décision de m'orienter vers le passionnant secteur de l'aéronautique.
            Compétences
            Travail en équipe
            Gestion de personnel (env. 10 personnes)
            Capacité d'adaptation
            Suivi des évolutions technologiques
            Formateur
            Dispense de formations pour le personnel:
            cessions de 10 et 20 personnes
            Coupe, dénudage, sertissage de câbles
            Contrôler l'aspect et la qualité d'un produit
            Respect et mise en place de procédures
            Identifier les anomalies ou les dysfonctionnements d'une production
            Atouts
            Rigoureux et organisé
            Posé et réfléchi
            Altruiste et généreux
            Expériences professionnelles
            Diplômes et Formations
            Câbleur installateur
            Depuis juillet 2023 Heli-Union Toussus Le Noble (78117)
            Travaux en atelier et sur hélicoptère
            Stage monteur câbleur
            De décembre 2022 à mars 2023 REC Electronique Le Plessis-Pâté
            En entreprise dans le cadre de ma formation
            2 stages de 4 semaines chacun
            Cadre Responsable relations techniques clientèle et préparation cylindres
            De 2004 à 2021 Imprimerie HELIO CORBEIL Corbeil Essonnes
            2 postes occupés en partage de temps:
            Préparation cylindres: traitements fichiers, gravure cylindres et galvanoplastie
            Qualité: suivi et contrôle de la production tout au long de la chaîne graphique et
            échanges avec clientèle
            Contremaître préparation cylindres
            De 1997 à 2004 Imprimerie HELIO CORBEIL Corbeil Essonnes
            Poste en 3X8
            Participation à la formation IPC
            Décembre 2022 Entreprise REC Electronique 91220 Le Plessis-Pâté
            Formation habilitation électrique B0/B1V
            Depuis avril 2023 Lycée Pierre de Coubertin Meaux
            CAP Aéronautique / Avionique
            D'octobre 2022 à avril 2023 Lycée Pierre de Coubertin Meaux, France
            Sauveteur Secouriste au Travail (SST)
            Octobre 2022 Lycée Pierre de Coubertin Meaux, France
            Bilan de compétences
            2022 Actiforces Lieusaint, France
            Formation chez les fournisseurs
            De 2004 à 2005 Fournisseurs Douai et région parisienne
            Formations encre, papier, colorimétrie... lors de l'accession au poste de Responsable
            relations techniques clientèle ( qualité produits)
            DEUG LEA
            1988 Sorbonne Nouvelle Censier PARIS
    """,
    "candidate_non_pertinent2": """
        PATRICK EHOUNDOU
        5/7 Rue De l’Avenir, 91620 Juvisy Sur Orge, Paris FRANCE
        pehoundou_45@yahoo.com
        Paris, France : 07.58.28.02.31
        Technicien SAV International
        Assistance Technique et Mise en Service des Equipements Sur site industriel
        Avec une expérience de plusieurs années comme assistant technique en bureaux d’études ingénieur. J’ai pendant plus de
        quatre ans travailler dans l’installation et la mise en service des machines sur sites de production clients en France et à
        l’étranger. Assurer le suivie de la maintenance préventive et curative des machines connecter à distance et sur terrain.
        Intervenant dans les phases de modifications, commissioning et garantie des équipements pétrochimie et ferroviaire.
        Expérience Professionnelles
        Alstom Group Canada/FranceTechnicien PI-SAV/R2N-ONO2018-2022
        SIEMENS CanadaTechnicien Electronique2017-2018
        Sander Geophysics LtdTechnicien Electronique2013-2014
        Scintrex Ltd USA/CanadaIngénieur Technicien Électronique2007-2012
        CVMR Inc. CanadaTechnicien Process Instrumentation2004-2006
        Diplômes et Habilitations Technique
        High School Diploma (BAC-Technologies)
        1995
        Option: Electronics Technology
        Hillcrest High School, Queens, New York, USA
        Parker and Viking instrument & Control Ltd
        2004
        Certificate of Basic Principles of Process Tube line Manufacturing
        Electromechanical Engineering Technician Diploma
        2005
        Option: Industrial Automation and Robotics
        Humber College, School of Applied Technology, Toronto, CANADA
        CVMR-Chemical Vapour Metal Refining Inc.
        2007
        Certificate of Safe Handling and Storage of Compress Gases
        IPC-A-610 / J-STD-001 Certified Specialist
        2008
        Certificate of Electrical and Electronics assembly and soldering
        ENSIL Canada Ltd, Toronto, CANADA
        Habilitation Electrique - B2V / BR / BC / H2V Essai
        2020
        Attestation de Formation Habilitation Electrique
        Forma-Protec : Marly, France
        Langues Courante : Bilingue-Français et Anglais (USA/Canada)
        Rôles et Taches Technique Présent
        Technicien SAV Maintenance Industrielle (Automatisme et Instrumentation Industrielle)
        Déploiement des machines industriel et intégration des systèmes : pneumatique, hydraulique, électrique et automatique
        Réaliser la formation des operateurs machines et personnel de maintenance client sur site de production.
        Diagnostiquer, corriger, et fiabiliser les installations des machines dans le respect des règles de sécurité.
        Effectuer l’optimisation des machines selon les besoins techniques du client : Rétrofite, addition de nouvelles fonctions.
        Réaliser le diagnostic et la maintenance curative des installations sur les process électrochimie sur site client.
        Suivi et maintenance électromécanique des équipements industriels automatisés en module interconnecter.
        Assemblage et test des armoires de control Pneumatique, et des systèmes hydraulique d’actuation de pression machines.
        Installation et configuration des réseaux de communication industrielle (Ethernet, HMI-Human Machine Interface).CV envoyé par HelloWork. Contient des données personnelles : ne pas utiliser, diffuser, copier sans le consentement de son auteur.
        PI-Product Introduction Sur Site Client
        Assure la mise en service des machines sur site de production clients en France comme à l’étranger
        Production les rapports quantitatif et qualitatif des PV sur les tests, essaies, et maintenance des machines sur site clients.
        Assurer la fidélisation des clients tout en garantissant la qualité des équipements et l’établissement de relations favorables.
        Réalisation de la communication interne et externe des besoins logistique avec les fournisseurs des pièces de maintenance.
        Préparation logistique tout en assurant la disponibilité des kits de maintenance et sécurité du travail sur les sites.
        Etablir le cahier des charges, restituer la gestion des priorités de planification des taches en court et à moyen terme.
        Compétences Informatique et Technologique
        Automatisme Industriel :
        ▪Programmable Logic Controller-PLC: Allen Bradley; SIMENS-S7; DCS-Emerson-DELTV; C-Programing
        ▪Industrial Networking: CAN, Ethernet; Modbus-DP; WinSCP, Hart Communication, FTP- puTTY, HMI, Mozilla
        filetransfer
        Logiciels applications:
        ▪
        Electrical Schematics: AutoCAD-Electrical, AutoCAD LT-2014 Mechanical, Electronic Multisim, GED, GMAO
        Logiciels Bureautique: Word, Excel, Power Point, Outlook, MS-Office Project
        Publications et Projets Technologique
        •
        https://www.cvmr.ca/pilotplants.php
        CVMR® in Toronto, Canada, has a range of piloting facilities to undertake various metallurgical tests,
        experimental and pilot plant work in application with Carbonyl Processes using laterite ores.
        •
        http://publications.gov.sk.ca/documents/310/95142-Seigel%20Open%20House%202009.pdf
        Résultat des tests effectué sur sites d’exploration minier avec la sonde Gravilog de mesure gravimétrique
        Complément de Formations
        Formation operateur R486 Plateformes Elévatrices Mobiles de Personnel (CACES-CAT : A-B Débutant), Marly-France
        Formation Travail en Hauteur et port du harnais, Forma-Protec, Marly-France
        Medical First Aid Training and H2S Tickets; EMP-Canada and Scintrex Ltd, 2010
        REFERENCES SERONT FOURNIES SUR DEMANDE
    """
}

def test_combination(job_title, cv_title):
    print(f"\nTest: {job_title} vs {cv_title}")
    print("-" * 50)
    
    payload = {
        "job_offer": {"text": job_offers[job_title]},
        "cv": {"text": cvs[cv_title]}
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            print(f"Score de compatibilité: {result['compatibilityScore']}")
            print(f"Points forts: {result['strengths']}")
            print(f"Compétences manquantes: {result['missingSkills']}")
            print(f"Review: {result['review']}")
        else:
            print(f"Erreur: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Erreur lors de la requête: {str(e)}")
    
    print("-" * 50)
    sleep(1)  # Pause entre les requêtes

def run_all_tests():
    # Test toutes les combinaisons
    for job_title in job_offers.keys():
        for cv_title in cvs.keys():
            test_combination(job_title, cv_title)

def run_specific_test(job_title, cv_title):
    test_combination(job_title, cv_title)

if __name__ == "__main__":
    # Pour tester toutes les combinaisons
    run_all_tests()
    
    # Pour tester une combinaison spécifique
    # run_specific_test("dev_fullstack", "candidate_1") 