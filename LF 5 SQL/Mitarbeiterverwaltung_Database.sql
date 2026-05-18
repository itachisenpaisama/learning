create table Mitarbeiter (
    MitarbeiterID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nachname VARCHAR(50) NOT NULL,
    Vorname VARCHAR(50),
    Gehalt DECIMAL(10, 2),
    AbteilungID INTEGER,
    FOREIGN KEY (AbteilungID) REFERENCES Abteilung(AbteilungID)
);


create table Abteilung (
    AbteilungID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50) NOT NULL
);


alter table Mitarbeiter add column Wohnort varchar(50);
insert into Mitarbeiter (Nachname, Vorname, Gehalt) values ("Müller", "Klaus", 2500.00);
insert into Abteilung (Name) values ("Einkauf");
insert into Abteilung (Name) values ("Buchhaltung");
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Schmidt', 'Anna', 1500.00, 1, 'Hamburg');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Weber', 'Lukas', 1800.50, 1, 'München');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Fischer', 'Mia', 2100.75, 2, 'Köln');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Meier', 'Jonas', 2300.00, 2, 'Frankfurt');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Bauer', 'Lea', 2600.20, 1, 'Stuttgart');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Koch', 'Tim', 2900.40, 1, 'Dortmund');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Wolf', 'Nina', 3200.10, 2, 'Düsseldorf');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Krause', 'Paul', 3600.80, 2, 'Bremen');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Lang', 'Sara', 4100.25, 1, 'Hannover');
insert into Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungID, Wohnort) values ('Pohl', 'Markus', 5000.00, 2, 'Leipzig');

Update Mitarbeiter set AbteilungID = 1 where MitarbeiterID = 1;
update Mitarbeiter set Wohnort = "Berlin" where MitarbeiterID = 1;
update Mitarbeiter set Gehalt = Gehalt * 1.015;
delete from Mitarbeiter where Nachname is null;
alter table Mitarbeiter drop column Wohnort;
drop table Abteilung;

select Mitarbeiter.Nachname, Mitarbeiter.Vorname, Mitarbeiter.Gehalt from Mitarbeiter order by Nachname ASC;
select Mitarbeiter.Nachname, Mitarbeiter.Vorname, Mitarbeiter.AbteilungID from Mitarbeiter where AbteilungID = 2;
select Mitarbeiter.Nachname, Mitarbeiter.Vorname, Abteilung.Name from Mitarbeiter, Abteilung where Abteilung.AbteilungID = 2;
select Mitarbeiter.Nachname, Mitarbeiter.Vorname, Mitarbeiter.Gehalt from Mitarbeiter where Mitarbeiter.Gehalt between 2000 and 2500;
select Mitarbeiter.Nachname, Mitarbeiter.Vorname from Mitarbeiter where Mitarbeiter.Nachname like "m%";
select Mitarbeiter.Nachname, Mitarbeiter.Vorname from Mitarbeiter where Mitarbeiter.Nachname like "%mann%";
select AVG (Mitarbeiter.Gehalt) from Mitarbeiter;

