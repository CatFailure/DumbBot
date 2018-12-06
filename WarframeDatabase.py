import sqlite3


def create_Database():
    conn = sqlite3.connect('dbWarframe.db')  # Assign a variable "conn" to connect to the database


def createTables():
    conn = sqlite3.connect('dbWarframe.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS tblWarframes
           (
              WFName       TEXT        PRIMARY KEY,
              WFDesc       TEXT           NOT NULL,
              Prime        TEXT           NOT NULL,
              Image        TEXT           NOT NULL,
              PrimeDesc    TEXT           NOT NULL,
              PrimeImg     TEXT           NOT NULL
            );''')
    conn.commit()

    conn.execute('''CREATE TABLE IF NOT EXISTS tblWFStats
    (
        WFName      TEXT        PRIMARY KEY,
        Mastery     INTEGER     NOT NULL,
        Health      INTEGER     NOT NULL,
        Shield      INTEGER     NOT NULL,
        Armour      INTEGER     NOT NULL,
        Energy      INTEGER     NOT NULL,
        SprSpd      FLOAT       NOT NULL,
        Polarities  TEXT        NOT NULL,
        Exilus      TEXT        NOT NULL,
        Aura        TEXT        NOT NULL
    );''')

    conn.execute('''CREATE TABLE IF NOT EXISTS tblWFPrimeStats
        (
            WFName      TEXT        PRIMARY KEY,
            Mastery     INTEGER     NOT NULL,
            Health      INTEGER     NOT NULL,
            Shield      INTEGER     NOT NULL,
            Armour      INTEGER     NOT NULL,
            Energy      INTEGER     NOT NULL,
            SprSpd      FLOAT       NOT NULL,
            Polarities  TEXT        NOT NULL,
            Exilus      TEXT        NOT NULL,
            Aura        TEXT        NOT NULL
        );''')

    conn.execute('''CREATE TABLE IF NOT EXISTS Prime_relics
            (
                item_       TEXT    NOT NULL,
                part_       TEXT    NOT NULL,
                tier_       TEXT    NOT NULL,
                name_       TEXT    NOT NULL,
                rarity_     TEXT    NOT NULL,
                vaulted_    TEXT    NOT NULL,
                image_      TEXT    NOT NULL
            );''')


def getAllWarframes():
    conn = sqlite3.connect('dbWarframe.db')
    cAllWarframes = conn.execute("SELECT WFName, WFDesc, Prime FROM tblWarframes")
    return (list(cAllWarframes))


def getWarframeInfo(warframeName):
    conn = sqlite3.connect('dbWarframe.db')
    cWarframeInfo = conn.execute("SELECT tblWarframes.WFName, tblWarframes.WFDesc, tblWarframes.Prime, tblWarframes.Image, \
    tblWFStats.Mastery, tblWFStats.Health, tblWFStats.Shield, tblWFStats.Armour, tblWFStats.Energy, tblWFStats.SprSpd,\
    tblWFStats.Polarities, tblWFStats.Exilus, tblWFStats.Aura FROM tblWarframes \
    INNER JOIN tblWFStats ON tblWarframes.WFName = tblWFStats.WFName \
    WHERE tblWarframes.WFName = ?", (warframeName,))
    lWarframeInfo = list(cWarframeInfo)
    return lWarframeInfo


def getPrimeInfo(warframeName):
    conn = sqlite3.connect('dbWarframe.db')
    cWarframeInfo = conn.execute("SELECT tblWarframes.Prime, tblWarframes.PrimeDesc, tblWarframes.Prime, tblWarframes.PrimeImg, \
        tblWFPrimeStats.Mastery, tblWFPrimeStats.Health, tblWFPrimeStats.Shield, tblWFPrimeStats.Armour, tblWFPrimeStats.Energy, tblWFPrimeStats.SprSpd,\
        tblWFPrimeStats.Polarities, tblWFPrimeStats.Exilus, tblWFPrimeStats.Aura, tblWarframes.WFName FROM tblWarframes \
        INNER JOIN tblWFPrimeStats ON tblWarframes.Prime = tblWFPrimeStats.WFName \
        WHERE tblWarframes.Prime = ?", (warframeName,))
    lPrimeWarframeInfo = list(cWarframeInfo)
    return lPrimeWarframeInfo

def searchItem(item):
    conn = sqlite3.connect('dbWarframe.db')
    cPrimeInfo = conn.execute("SELECT DISTINCT item_, part_ FROM Prime_relics \
                                 WHERE item_ = ?", (item,))
    lPrimeInfo = list(cPrimeInfo)
    return lPrimeInfo

def getRelicByPart(item, part):
    conn = sqlite3.connect('dbWarframe.db')
    cRelicDrops = conn.execute("SELECT DISTINCT item_, tier_, name_, rarity_, vaulted_, image_ FROM Prime_relics \
                                     WHERE item_ = ? AND part_ = ?", (item, part,))
    lRelicInfo = list(cRelicDrops)
    return lRelicInfo


def getPartByRelicAndRarity(tier, name, rarity):
    conn = sqlite3.connect('dbWarframe.db')
    cRelicDrops = conn.execute("SELECT DISTINCT item_, part_, rarity_ FROM Prime_relics \
                                         WHERE tier_ = ? AND name_ = ? AND rarity_ = ?", (tier, name, rarity,))
    lRelicDrops = list(cRelicDrops)
    return lRelicDrops

def checkIfVaulted(item):
    conn = sqlite3.connect('dbWarframe.db')
    cVauledCheck = conn.execute("SELECT DISTINCT vaulted_ FROM Prime_relics \
                                             WHERE item_ = ?", (item,))
    lVaultedCheck = list(cVauledCheck)
    print(len(lVaultedCheck))
    return len(lVaultedCheck)

def insertBlank():
    conn = sqlite3.connect('dbWarframe.db')
    for i in range(917):
        conn.execute("INSERT INTO Prime_relics\
        VALUES(0,0,0,0,0,0,0)")
    conn.commit()
