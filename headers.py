# original header names and header names that should replace orginal headers during preprocessing
orignal_column_headers = [
"placeholder_row_zero",
"Antwort ID",
"Datum Abgeschickt",
"Letzte Seite",
"Start-Sprache",
"Zufallsgeneratorstartwert",
"Datum gestartet",
"Datum letzte Aktivität",
"Weiterleitungs-URL",
"bla",
"Sind Sie schon mit einem Lastenrad gefahren?",
"{if(!is_empty(random.NAOK), random.NAOK, rand(1,4))}",
"Wie oft fahren Sie mit einem Lastenfahrrad in Hamburg?",
"Wofür verwenden Sie das Lastenrad? [Einkauf / Besorgungen]",
"Wofür verwenden Sie das Lastenrad? [Ausflüge, Events etc]",
"Wofür verwenden Sie das Lastenrad? [Kinder transportieren]",
"Wofür verwenden Sie das Lastenrad? [Arbeitsweg (zum Pendeln)]",
"Wofür verwenden Sie das Lastenrad? [Arbeit (als Dienstfahrzeug)]",
"Besitzen oder leihen Sie ein Lastenrad? [Ich besitze ein Lastenrad]",
"Besitzen oder leihen Sie ein Lastenrad? [Ich leihe eins von Freunden/Familie (privat)]",
"Besitzen oder leihen Sie ein Lastenrad? [Ich nutze ein Leih-Lastenrad Angebot (z.B. lokale Organisation, StadtRAD, o.Ä)]",
"Besitzen oder leihen Sie ein Lastenrad? [Ich nutze ein Lastenrad beruflich]",
"Haben Sie vor sich ein eigenes Lastenrad zu kaufen?",
"Was hält Sie davon ab sich ein Lastenrad anzuschaffen?",
"Was hält Sie davon ab sich ein Lastenrad anzuschaffen? [Sonstiges]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten?",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten? [Sonstiges]",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten?",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten? [Sonstiges]",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten?",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten? [Sonstiges]",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten?",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten? [Sonstiges]",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten?",
"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten? [Sonstiges]",
"Die kommenden Fragen beziehen sich auf das Parken von Lastenrädern im öffentlichen Raum, nicht am Wohnort. Bitte stellen Sie sich vor, dass Sie das Rad nur für Ihre Erledigung abstellen und nicht über einen längeren Zeitraum wie z.B. über Nacht. Wie einfach oder schwierig ist es für Sie, das Lastenrad unterwegs in Hamburg zu parken? (nicht an Ihrem Wohnort)",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Einfache Möglichkeit den Rahmen anzuschließen]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Sichtbarkeit als Lastenradparkplatz]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Überwachung]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Beleuchtung]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Räumliche Nähe zum Ziel]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Genügend Platz]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Wettergeschützter Parkplatz]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Ebener Zugang zum Parkplatz (z.B. ohne Bordsteinkanten)]",
"Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Sonstiges]",
"Kennen Sie den neuen Lastenrad-Parkplatz vor Edeka in der Großen Bergstraße?",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Einfache Möglichkeit den Rahmen anzuschließen]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Umgebung ausreichend beleuchtet]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Nah an wichtigen Zielort(en)]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Genügend Platz]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Gut sichtbar als Lastenradparkplatz zu erkennen?]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Einfache Möglichkeit den Rahmen anzuschließen]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Umgebung ausreichend beleuchtet]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Nah an wichtigen Zielort(en)]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Genügend Platz]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Gut sichtbar als Lastenradparkplatz zu erkennen?]",
"Haben Sie konkrete Vorschläge zur Gestaltung des Lastenradstellplatzes in der Großen Bergstraße (z.B. Materialbeschaffenheit, Größe, Anschliessmöglichkeiten, usw.)?",
"Haben Sie konkrete Vorschläge für Lastenradstellplätze an anderen Orten im öffentlichen Raum? (Bitte Ort und Begründung)",
"Können Sie sich vorstellen ein Lastenrad zu nutzen?",
"Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Einkauf / Besorgungen]",
"Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Ausflüge, Events etc]",
"Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Pendeln zur Arbeit]",
"Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Kinder transportieren]",
"Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Beruflich (für die Ausübung meiner Arbeit)]",
"Haben Sie vor sich ein eigenes Lastenrad anzuschaffen?",
"Was hält Sie davon ab sich ein Lastenrad anzuschaffen?",
"Was hält Sie davon ab sich ein Lastenrad anzuschaffen? [Sonstiges]",
"Kennen Sie die Lastenrad Leihangebote in Hamburg (z.B. Stadtrad, Klara, usw.)",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Sonstiges]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Sonstiges]",
"Diese Frage bezieht sich auf das Parken von Lastenrädern im öffentlichen Raum, nicht am Wohnort. Bitte stellen Sie sich vor, dass Sie das Rad nur für Ihre Erledigung abstellen und nicht über einen längeren Zeitraum wie z.B. über Nacht. Wie einfach oder schwierig stellen Sie es vor, ein Lastenrad unterwegs in Hamburg zu parken? (nicht am Wohnort)",
"Kennen Sie den neuen Lastenrad-Parkplatz vor Edeka in der Großen Bergstraße?",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Einfache Möglichkeit den Rahmen anzuschließen]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Umgebung ausreichend beleuchtet]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Nah an wichtigen Zielort(en)]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Genügend Platz]",
"Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Gut sichtbar als Lastenradparkplatz zu erkennen?]",
"Haben Sie konkrete Vorschläge für Lastenradstellplätze an anderen Orten im öffentlichen Raum? (Bitte Ort und Begründung)",
"Wir würden gerne auch soziodemografische Daten erheben. Diese sind wie bereits erwähnt anonym und lassen keine direkten Rückschlüsse auf ihre Person zu. Diese Informationen sind sehr wichtig, um Aussagen zu den Nutzer*innen treffen zu können. Was ist Ihr Geschlecht?",
"In welchem Stadtteil Hamburgs wohnen Sie?",
"Wie alt sind Sie?",
"Wie viele Menschen leben in Ihrem Haushalt? (inkl. Kinder, Mitbewohner*innen, Partner*in)",
"Lebt mindestens ein minderjähriges Kind in Ihrem Haushalt?",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [ÖPNV (S-/U-Bahn, Bus, Fähre)]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Auto (privat)]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Auto (Carsharing)]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Zu Fuß]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Fahrrad (privat)]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Lastenrad (privat)]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Leihräder (z.B. StadtRAD, Klara usw.)]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Motorrad/Roller]",
"Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Sonstiges]",
"Gesamtzeit",
"Gruppenzeit: Einstiegsfrage",
"Fragenzeit: test",
"Fragenzeit: AA01A",
"Fragenzeit: random",
"Gruppenzeit: Nutzer - Nutzung",
"Fragenzeit: BN01A",
"Fragenzeit: BN02A",
"Fragenzeit: BN03A",
"Fragenzeit: BN03B",
"Fragenzeit: BN03C",
"Gruppenzeit: Nutzer - Herausforderungen",
"Fragenzeit: BH01A1",
"Fragenzeit: BH01A2",
"Fragenzeit: BH01A3",
"Fragenzeit: BH01A4",
"Fragenzeit: BH01A5",
"Fragenzeit: BH02A1",
"Fragenzeit: BH02A2",
"Fragenzeit: BH02A3",
"Fragenzeit: BH02A4",
"Fragenzeit: BH02A5",
"Gruppenzeit: Nutzer - Evaluierung",
"Fragenzeit: BE01A",
"Fragenzeit: BE02A",
"Fragenzeit: BE03A",
"Fragenzeit: BE03B1",
"Fragenzeit: BE03B2",
"Fragenzeit: BE03C",
"Fragenzeit: BE03D",
"Gruppenzeit: Nichtnutzer - Nutzung",
"Fragenzeit: CN01A",
"Fragenzeit: CN01B",
"Fragenzeit: CN01C",
"Fragenzeit: CN01D",
"Fragenzeit: CN02A",
"Gruppenzeit: Nichtnutzer - Herausforderungen",
"Fragenzeit: CH01A1",
"Fragenzeit: CH01A2",
"Fragenzeit: CH01A3",
"Fragenzeit: CH01A4",
"Fragenzeit: CH01A15",
"Gruppenzeit: Nichtnutzer - Evaluierung",
"Fragenzeit: CE01A",
"Fragenzeit: CE02A",
"Fragenzeit: CE03B",
"Fragenzeit: CE03D",
"Gruppenzeit: Demographische Fragen",
"Fragenzeit: AD01A",
"Fragenzeit: AD02A",
"Fragenzeit: AD03A",
"Fragenzeit: AD04A",
"Fragenzeit: AD05A",
"Fragenzeit: AD06A"
]


# [question_code, subquestion_code, header_text]
question_codes = [
[None,None,"placeholder_row_zero"],
[None,None,"Antwort ID"],
[None,None,"Datum Abgeschickt"],
[None,None,"Letzte Seite"],
[None,None,"Start-Sprache"],
[None,None,"Zufallsgeneratorstartwert"],
[None,None,"Datum gestartet"],
[None,None,"Datum letzte Aktivität"],
[None,None,"Weiterleitungs-URL"],
["AA01A",None,"Sind Sie schon mit einem Lastenrad gefahren?"],
["RAND",None,"Randomization Group"],
["BN01A",None,"Wie oft fahren Sie mit einem Lastenfahrrad in Hamburg?"],
["BN02A","SQ001","Wofür verwenden Sie das Lastenrad? [Einkauf / Besorgungen]"],
["BN02A","SQ002","Wofür verwenden Sie das Lastenrad? [Ausflüge, Events etc]"],
["BN02A","SQ003","Wofür verwenden Sie das Lastenrad? [Kinder transportieren]"],
["BN02A","SQ004","Wofür verwenden Sie das Lastenrad? [Arbeitsweg (zum Pendeln)]"],
["BN02A","SQ005","Wofür verwenden Sie das Lastenrad? [Arbeit (als Dienstfahrzeug)]"],
["BN03A","SQ001","Besitzen oder leihen Sie ein Lastenrad? [Ich besitze ein Lastenrad]"],
["BN03A","SQ001","Besitzen oder leihen Sie ein Lastenrad? [Ich leihe eins von Freunden/Familie (privat)]"],
["BN03A","SQ002","Besitzen oder leihen Sie ein Lastenrad? [Ich nutze ein Leih-Lastenrad Angebot (z.B. lokale Organisation, StadtRAD, o.Ä)]"],
["BN03A","SQ003","Besitzen oder leihen Sie ein Lastenrad? [Ich nutze ein Lastenrad beruflich]"],
# TODO choose answerID for other or merge to one column?
["BN03B + CN01C",None,"Haben Sie vor sich ein eigenes Lastenrad zu kaufen?"],
["BN03C + CN01D",None,"Was hält Sie davon ab sich ein Lastenrad anzuschaffen?"],
["BN03C+ CN01D",None,"Was hält Sie davon ab sich ein Lastenrad anzuschaffen? [Sonstiges]"],
["BH01A1","SQ001","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]"],
["BH01A1","SQ002","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]"],
["BH01A1","SQ003","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]"],
["BH01A1","SQ004","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]"],
["BH01A1","SQ005","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]"],
["BH01A1","SQ006","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]"],
["BH01A1","SQ007","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]"],
["BH01A1","SQ008","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]"],
["BH01A1","SQ009","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]"],
["BH01A1","OTHER","Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]"],
["BH02A1",None, "Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten?"],
["BH02A1",None,"Welche Verbesserung der Infrastruktur oder des Angebots sollte die höchste Priorität erhalten? [Sonstiges]"],
["BE01A",None,"Wie einfach oder schwierig ist es für Sie, das Lastenrad unterwegs in Hamburg zu parken? (nicht an Ihrem Wohnort)"],
["BE02A","SQ001","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Einfache Möglichkeit den Rahmen anzuschließen]"],
["BE02A","SQ002","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Sichtbarkeit als Lastenradparkplatz]"],
["BE02A","SQ003","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Überwachung]"],
["BE02A","SQ004","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Beleuchtung]"],
["BE02A","SQ005","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Räumliche Nähe zum Ziel]"],
["BE02A","SQ006","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Genügend Platz]"],
["BE02A","SQ007","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Wettergeschützter Parkplatz]"],
["BE02A","SQ008","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Ebener Zugang zum Parkplatz (z.B. ohne Bordsteinkanten)]"],
["BE02A","OTHER","Ein guter Lastenradstellplatz im öffentlichen Raum (nicht am Wohnort) sollte diese Merkmale aufweisen: [Sonstiges]"],
["BE03A + CE02A",None,"Kennen Sie den neuen Lastenrad-Parkplatz vor Edeka in der Großen Bergstraße?"],
["BE03B1 + CE03B","SQ001","Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Einfache Möglichkeit den Rahmen anzuschließen]"],
["BE03B1 + CE03B","SQ002","Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Umgebung ausreichend beleuchtet]"],
["BE03B1 + CE03B","SQ003","Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Nah an wichtigen Zielort(en)]"],
["BE03B1 +CE03B","SQ004","Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Genügend Platz]"],
["BE03B1 +CE03B","SQ005","Sind folgende Kriterien an dem Lastenrad-Parkplatz in der Großen Bergstraße erfüllt: [Gut sichtbar als Lastenradparkplatz zu erkennen?]"],
["BE03C",None,"Haben Sie konkrete Vorschläge zur Gestaltung des Lastenradstellplatzes in der Großen Bergstraße (z.B. Materialbeschaffenheit, Größe, Anschliessmöglichkeiten, usw.)?"],
["BE03D + CE03D",None,"Haben Sie konkrete Vorschläge für Lastenradstellplätze an anderen Orten im öffentlichen Raum? (Bitte Ort und Begründung)"],
["CN01A",None,"Können Sie sich vorstellen ein Lastenrad zu nutzen?"],
["CN01B","SQ001","Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Einkauf / Besorgungen]"],
["CN01B","SQ002","Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Ausflüge, Events etc]"],
["CN01B","SQ003","Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Pendeln zur Arbeit]"],
["CN01B","SQ004","Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Kinder transportieren]"],
["CN01B","SQ005","Für welche Zwecke können Sie sich vorstellen ein Lastenrad zu nutzen? [Beruflich (für die Ausübung meiner Arbeit)]"],
["CN02A",None,"Kennen Sie die Lastenrad Leihangebote in Hamburg (z.B. Stadtrad, Klara, usw.)"],
["CH01A1","SQ001","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]"],
["CH01A1","SQ002","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]"],
["CH01A1","SQ003","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]"],
["CH01A1","SQ004","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]"],
["CH01A1","SQ005","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]"],
["CH01A1","SQ006","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]"],
["CH01A1","SQ007","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]"],
["CH01A1","SQ008","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]"],
["CH01A1","SQ009","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]"],
["CH01A1","OTHER","Was denken Sie sind die größte Herausforderungen bei der Nutzung von Lastenrädern? [Sonstiges]"],
["CE01A",None,"Wie einfach oder schwierig stellen Sie es vor, ein Lastenrad unterwegs in Hamburg zu parken? (nicht am Wohnort)"],
["AD01A",None,"Was ist Ihr Geschlecht?"],
["AD02A",None,"In welchem Stadtteil Hamburgs wohnen Sie?"],
["AD03A","","Wie alt sind Sie?"],
["AD04A","","Wie viele Menschen leben in Ihrem Haushalt? (inkl. Kinder, Mitbewohner*innen, Partner*in)"],
["AD05A","","Lebt mindestens ein minderjähriges Kind in Ihrem Haushalt?"],
["AD06A","SQ001","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [ÖPNV (S-/U-Bahn, Bus, Fähre)]"],
["AD06A","SQ002","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Auto (privat)]"],
["AD06A","SQ003","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Auto (Carsharing)]"],
["AD06A","SQ004","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Zu Fuß]"],
["AD06A","SQ005","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Fahrrad (privat)]"],
["AD06A","SQ006","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Lastenrad (privat)]"],
["AD06A","SQ007","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Leihräder (z.B. StadtRAD, Klara usw.)]"],
["AD06A","SQ008","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Motorrad/Roller]"],
["AD06A","OTHER","Welche Verkehrsmittel nutzen Sie am häufigsten für Ihre alltäglichen Wege? [Sonstiges]"],
]



challenges_summary_headers = [
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten wenn unterwegs (z.B. für Besorgungen)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Wohnort]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende sichere Parkmöglichkeiten am Arbeitsplatz]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Fehlende Infrastruktur (Radwege)]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Wegekanten, Bordsteinkanten, Höhenunterschiede]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Unebenheiten, Schlaglöcher, Baumwurzeln im Wegebelag]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Anschaffungskosten des Lastenrads]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Hohe Leihgebühren für Lastenräder]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Eingeschränkte Verfügbarkeit von Leih-Lastenrädern]",
"Was sind die größten Herausforderungen für Sie bei der Nutzung von Lastenrädern? [Sonstiges]",
]
