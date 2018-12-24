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

    conn.execute('''CREATE TABLE IF NOT EXISTS tblWeapons
               (
                  weap_name_                TEXT        PRIMARY KEY,
                  weap_trigger_type_        TEXT        NOT NULL,
                  weap_dmg_                 TEXT        NOT NULL,
                  weap_crit_chance_         TEXT        NOT NULL,
                  weap_crit_mult_           TEXT        NOT NULL,
                  weap_stat_chance_         TEXT        NOT NULL,
                  weap_projectile_type_     TEXT        NOT NULL,
                  weap_firerate_            INTEGER     NOT NULL,
                  weap_magsize_             INTEGER     NOT NULL,
                  weap_reload_              INTEGER     NOT NULL,
                  weap_mastery_             INTEGER     NOT NULL,
                  weap_disposition_         TEXT        NOT NULL,
                  weap_image_               TEXT        NOT NULL
                );''')

    conn.execute('''CREATE TABLE IF NOT EXISTS tblMelee
                   (
                      melee_name_               TEXT        PRIMARY KEY,
                      melee_type_               TEXT        NOT NULL,
                      melee_normal_             TEXT        NOT NULL,
                      melee_slide_              TEXT        NOT NULL,
                      melee_attack_speed_       INTEGER     NOT NULL,
                      melee_crit_chance_        TEXT        NOT NULL,
                      melee_crit_damage_        TEXT        NOT NULL,
                      melee_stat_chance_        TEXT        NOT NULL,
                      melee_mastery_            INTEGER     NOT NULL,
                      melee_stance_             TEXT        NOT NULL,
                      melee_disposition_        TEXT        NOT NULL,
                      melee_image_              TEXT        NOT NULL
                    );''')
    conn.commit()

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
    return lVaultedCheck


def insertBlank():
    conn = sqlite3.connect('dbWarframe.db')
    for i in range(917):
        conn.execute("INSERT INTO Prime_relics\
        VALUES(0,0,0,0,0,0,0)")
    conn.commit()


def getWeaponInfo(itemName):
    conn = sqlite3.connect('dbWarframe.db')
    cWeaponInfo = conn.execute("SELECT weap_name_, weap_trigger_type_, weap_dmg_, weap_crit_chance_, \
    weap_crit_mult_, weap_stat_chance_, weap_projectile_type_, weap_firerate_, weap_magsize_, \
    weap_reload_, weap_mastery_, weap_disposition_, weap_image_ FROM tblWeapons WHERE weap_name_ = ?", (itemName,))
    lWeaponInfo = list(cWeaponInfo)
    return lWeaponInfo


def getMeleeInfo(itemName):
    conn = sqlite3.connect('dbWarframe.db')
    cMeleeInfo = conn.execute("SELECT melee_name_, melee_normal_, melee_slide_, melee_attack_speed_, \
            melee_crit_chance_, melee_crit_damage_, melee_stat_chance_, melee_mastery_, melee_stance_, \
            melee_disposition, melee_image_ FROM tblMelee WHERE melee_name_ = ?", (itemName,))
    lMeleeInfo = list(cMeleeInfo)
    return lMeleeInfo