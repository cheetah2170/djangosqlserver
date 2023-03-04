# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Tankcalcmetric(models.Model):
    calcid = models.AutoField(db_column='CalcID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID')  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN')  # Field name made lowercase.
    billid = models.CharField(db_column='BillID', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='Temprature', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    water = models.CharField(db_column='Water', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    specweight = models.CharField(db_column='SpecWeight', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    refinery = models.CharField(db_column='Refinery', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    naturallitr = models.CharField(db_column='NaturalLitr', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    litr60 = models.CharField(db_column='Litr60', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    hour = models.CharField(db_column='Hour', max_length=5, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    cyear = models.IntegerField(db_column='CYear', blank=True, null=True)  # Field name made lowercase.
    envtemp = models.CharField(db_column='EnvTemp', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TankCalcMetric'
    def __str__(self):
        return self.billid

class Station(models.Model):
    stationid = models.AutoField(db_column='StationID', primary_key=True)  # Field name made lowercase.
    stationname = models.CharField(db_column='StationName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationno = models.IntegerField(db_column='StationNo', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Station'
    def __str__(self):
        return self.stationname


class Tank(models.Model):
    tankid = models.AutoField(db_column='TankID', primary_key=True)  # Field name made lowercase.
    tankname = models.CharField(db_column='TankName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    tankno = models.CharField(db_column='TankNo', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    ismetric = models.BooleanField(db_column='IsMetric', blank=True, null=True)  # Field name made lowercase.
    isnew = models.BooleanField(db_column='IsNew', blank=True, null=True)  # Field name made lowercase.
    tankheight = models.DecimalField(db_column='TankHeight', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tankhusable = models.DecimalField(db_column='TankHUsable', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tankhunusable = models.DecimalField(db_column='TankHUnUsable', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    volinheight = models.DecimalField(db_column='VolInHeight', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rdate = models.DateTimeField(db_column='Rdate', blank=True, null=True)  # Field name made lowercase.
    materialh = models.CharField(db_column='MaterialH', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    materiall = models.CharField(db_column='MaterialL', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    heademptyh = models.CharField(db_column='HeadEmptyH', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    heademptyl = models.CharField(db_column='HeadEmptyL', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    recoverableh = models.CharField(db_column='RecoverableH', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    recoverablel = models.CharField(db_column='RecoverableL', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    increasemili = models.DecimalField(db_column='IncreaseMili', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tanktype = models.SmallIntegerField(db_column='TankType', blank=True, null=True)  # Field name made lowercase.
    tankcaptot = models.CharField(db_column='TankCapTot', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    tankcapallowed = models.CharField(db_column='TankCapAllowed', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tank'
    def __str__(self):
        return self.tankname

class Calibration(models.Model):
    calibrid = models.BigAutoField(db_column='CalibrID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    liters = models.DecimalField(db_column='Liters', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dasti = models.IntegerField(blank=True, null=True)
    newsize = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    newlitr = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Calibration'


class Calibration2(models.Model):
    calibrid = models.BigAutoField(db_column='CalibrID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    liters = models.DecimalField(db_column='Liters', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Calibration2'


class Amalkardmeghdarititle(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmalkardMeghdariTitle'


class Amalkardmeghdarivalue(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tid = models.IntegerField(db_column='TID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmalkardMeghdariValue'


class Amalkardton(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tid = models.IntegerField(db_column='TID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ton = models.DecimalField(db_column='Ton', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmalkardTon'


class Amountspec(models.Model):
    calcid = models.AutoField(db_column='CalcID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    sarak = models.DecimalField(db_column='Sarak', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    transfrom = models.DecimalField(db_column='TransFrom', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    transto = models.DecimalField(db_column='TransTo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    consumed = models.DecimalField(db_column='Consumed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmountSpec'


class Balancetitles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    isdaryafti = models.BooleanField(db_column='ISDaryafti', blank=True, null=True)  # Field name made lowercase.
    calculationmode = models.BooleanField(db_column='CalculationMode', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    tanktype = models.SmallIntegerField(db_column='TankType', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BalanceTitles'


class Billedition(models.Model):
    yrid = models.AutoField(db_column='YRID', primary_key=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    litr60 = models.CharField(db_column='Litr60', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillEdition'


class Billedition2(models.Model):
    yrid = models.IntegerField(db_column='YRID')  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    litr60 = models.CharField(db_column='Litr60', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillEdition2'




class Calibrationpi(models.Model):
    calibrid = models.BigAutoField(db_column='CalibrID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    liters = models.DecimalField(db_column='Liters', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationPI'


class Constmounth(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    prid = models.IntegerField(db_column='PrId', blank=True, null=True)  # Field name made lowercase.
    tot = models.DecimalField(db_column='Tot', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConstMounth'


class Consumptionmarakez(models.Model):
    stationid = models.IntegerField(db_column='StationID', primary_key=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    litr60 = models.BigIntegerField(db_column='Litr60', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsumptionMarakez'
        unique_together = (('stationid', 'rdate', 'productid'),)


class Dailyreplinestations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyRepLineStations'


class Dailyreplineval(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdId', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyRepLineVal'


class Dailyrepmanual(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rdate = models.DecimalField(db_column='RDate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lid = models.IntegerField(db_column='LID', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyRepManual'


class Dailyrepstation(models.Model):
    did = models.AutoField(db_column='DID', primary_key=True)  # Field name made lowercase.
    lid = models.IntegerField(db_column='LID', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyRepStation'


class Dailyreportset(models.Model):
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    reyentered = models.BooleanField(db_column='ReyEntered', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyReportSet'


class Daliyrepline(models.Model):
    lid = models.AutoField(db_column='LID', primary_key=True)  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=150, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DaliyRepLine'


class Daycalc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    makhzanname = models.TextField(db_column='MakhzanName', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    istgahname = models.TextField(db_column='Istgahname', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    productname = models.TextField(db_column='ProductName', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    ghabz = models.TextField(db_column='Ghabz', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    ekhtelaf = models.BigIntegerField(db_column='Ekhtelaf', blank=True, null=True)  # Field name made lowercase.
    datenow = models.TextField(db_column='DateNow', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    datereport = models.TextField(db_column='DateReport', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    tankid = models.TextField(db_column='TankId', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.TextField(db_column='StationId', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    productid = models.TextField(db_column='Productid', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    sid = models.IntegerField(db_column='Sid', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    mount = models.TextField(db_column='Mount', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    sumdgree = models.TextField(db_column='Sumdgree', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    sumkarkard = models.TextField(db_column='Sumkarkard', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DayCalc'


class Detailtank(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    thankid = models.IntegerField(db_column='ThankId', blank=True, null=True)  # Field name made lowercase.
    start = models.DecimalField(db_column='Start', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    inc = models.DecimalField(db_column='Inc', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailTank'


class Detailtaraz(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    btid = models.IntegerField(db_column='BTID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PId', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailTaraz'


class Exceldbcode(models.Model):
    excelcode = models.IntegerField(db_column='ExcelCode', blank=True, null=True)  # Field name made lowercase.
    dbcode = models.IntegerField(db_column='DBCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXCELDBCode'


class Editionratio(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='Temprature', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    api = models.CharField(db_column='API', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    ratio = models.DecimalField(db_column='Ratio', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EditionRatio'


class Fraction(models.Model):
    fractionid = models.AutoField(db_column='FractionID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    milno = models.DecimalField(db_column='MilNo', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    litr = models.DecimalField(db_column='Litr', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fraction'


class Fractionlitr(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    litr = models.IntegerField(db_column='Litr', blank=True, null=True)  # Field name made lowercase.
    ll = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FractionLitr'


class Linedetails(models.Model):
    linedetid = models.AutoField(db_column='LineDetID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    gravity = models.CharField(db_column='Gravity', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LineDetails'


class Linepriority(models.Model):
    spid = models.AutoField(db_column='SPID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LinePriority'


class Lines(models.Model):
    lineid = models.AutoField(db_column='LineID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=100, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    diameter = models.CharField(db_column='Diameter', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    linekm = models.CharField(db_column='LineKm', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lines'


class Monthlyrepdate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    expdate = models.CharField(db_column='EXPdate', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MonthlyRepDate'


class Mountprint(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    istgahname = models.CharField(db_column='IstgahName', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    makhzancode = models.CharField(db_column='MakhzanCode', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    ticket = models.CharField(db_column='Ticket', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    statee = models.CharField(db_column='Statee', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    dgree = models.CharField(db_column='Dgree', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    water = models.CharField(db_column='Water', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    nlitre = models.CharField(db_column='NLitre', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    litertahvili = models.CharField(db_column='LiterTahvili', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    tafavoottabiiei = models.DecimalField(db_column='TafavootTabiiei', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tafavoot60 = models.DecimalField(db_column='Tafavoot60', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dateaz = models.CharField(db_column='DateAz', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    dateta = models.CharField(db_column='DateTa', max_length=250, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    sid = models.IntegerField(db_column='Sid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MountPrint'


class Nirogahvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NirogahValues'


class Oilproducts(models.Model):
    prodid = models.AutoField(db_column='ProdID', primary_key=True)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OilProducts'


class Oiltazrigh(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OilTazrigh'


class Palayeshgahvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PalayeshgahValues'


class Productpriority(models.Model):
    ppid = models.AutoField(db_column='PPID', primary_key=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductPriority'


class Rawoildetailkarkard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kid = models.IntegerField(db_column='KID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilDetailKarkard'


class Rawoildetailtaraz(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    btid = models.IntegerField(db_column='BTID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilDetailTaraz'


class Rawoilkarkard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    tid = models.IntegerField(db_column='TID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    kilometer = models.CharField(db_column='Kilometer', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    spgravity = models.CharField(db_column='SpGravity', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    linetitle = models.CharField(db_column='LineTitle', max_length=150, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    linecode2 = models.CharField(db_column='LineCode2', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilKarkard'


class Rawoillinedetails(models.Model):
    linedetid = models.AutoField(db_column='LineDetID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilLineDetails'


class Rawoillines(models.Model):
    lineid = models.AutoField(db_column='LineID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=100, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilLines'


class Rawoillitr60(models.Model):
    lid = models.AutoField(db_column='LID', primary_key=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN')  # Field name made lowercase.
    litr60 = models.CharField(db_column='Litr60', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    unitid = models.SmallIntegerField(db_column='UnitID', blank=True, null=True)  # Field name made lowercase.
    daryafti = models.BooleanField(db_column='Daryafti', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilLitr60'


class Rawoiltankstock(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN')  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    litr1mm = models.CharField(db_column='Litr1mm', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    cyear = models.IntegerField(db_column='CYear', blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilTankStock'


class Rawoiltitles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    isdaryafti = models.BooleanField(db_column='ISDaryafti', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RawOilTitles'


class Reppercentage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cyear = models.IntegerField(db_column='CYear', blank=True, null=True)  # Field name made lowercase.
    tahviliperc = models.CharField(db_column='TahviliPerc', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    karkardperc = models.CharField(db_column='KarkardPerc', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepPercentage'





class Stationpriority(models.Model):
    spid = models.AutoField(db_column='SPID', primary_key=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StationPriority'


class Tanktype1(models.Model):
    tanktype = models.CharField(max_length=10, db_collation='Arabic_BIN', blank=True, null=True)
    tanktypeid = models.CharField(db_column='TankTypeID', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TANKTYPE1'


class Tafkiki(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tafkiki'





class Tankcalcmetering(models.Model):
    meterid = models.AutoField(db_column='MeterID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    temprature = models.CharField(db_column='Temprature', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    meterno = models.CharField(db_column='MeterNo', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    pressure = models.CharField(db_column='Pressure', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    meterfactor = models.CharField(db_column='MeterFactor', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    diff = models.CharField(db_column='Diff', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    gravity = models.CharField(db_column='Gravity', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    bsw = models.CharField(db_column='BSW', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    ctl = models.CharField(db_column='CTL', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    cpl = models.CharField(db_column='CPL', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    gsv = models.CharField(db_column='GSV', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    nsv = models.CharField(db_column='NSV', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    hour = models.CharField(db_column='Hour', max_length=5, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    cyear = models.IntegerField(db_column='CYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TankCalcMetering'





class Tankmotheramount(models.Model):
    amouid = models.AutoField(db_column='AmouID', primary_key=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    litr60 = models.CharField(db_column='Litr60', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TankMotherAmount'


class Tankmothergravity(models.Model):
    mgid = models.AutoField(db_column='MGID', primary_key=True)  # Field name made lowercase.
    tankid = models.IntegerField(db_column='TankID', blank=True, null=True)  # Field name made lowercase.
    gravity = models.CharField(db_column='Gravity', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TankMotherGravity'


class Tblaccount(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    mid = models.IntegerField(db_column='Mid', blank=True, null=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='Uid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TblAccount'


class Tblentitylinedetail(models.Model):
    eid = models.AutoField(db_column='EId', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    date = models.DecimalField(db_column='Date', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    product = models.IntegerField(db_column='Product', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TblEntityLineDetail'


class Tblmenu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    menu = models.CharField(db_column='Menu', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TblMenu'


class Tbla1(models.Model):
    cm = models.IntegerField(db_column='Cm', blank=True, null=True)  # Field name made lowercase.
    litr = models.IntegerField(db_column='Litr', blank=True, null=True)  # Field name made lowercase.
    tank = models.IntegerField(db_column='Tank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tbla1'


class Units(models.Model):
    unitid = models.AutoField(db_column='UnitID', primary_key=True)  # Field name made lowercase.
    unitname = models.CharField(db_column='UnitName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Units'


class Usages(models.Model):
    perfid = models.AutoField(db_column='PerfID', primary_key=True)  # Field name made lowercase.
    linecode = models.CharField(db_column='LineCode', max_length=20, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    litr60 = models.TextField(db_column='Litr60', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    perfrormance = models.TextField(db_column='Perfrormance', db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usages'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Asd(models.Model):
    str1 = models.CharField(max_length=50, db_collation='Arabic_BIN', blank=True, null=True)
    str2 = models.CharField(max_length=50, db_collation='Arabic_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asd'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Arabic_BIN')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Arabic_BIN')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Arabic_BIN')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Arabic_BIN')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Arabic_BIN')
    first_name = models.CharField(max_length=150, db_collation='Arabic_BIN')
    last_name = models.CharField(max_length=150, db_collation='Arabic_BIN')
    email = models.CharField(max_length=254, db_collation='Arabic_BIN')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Arabic_BIN', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Arabic_BIN')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Arabic_BIN')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Arabic_BIN')
    model = models.CharField(max_length=100, db_collation='Arabic_BIN')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Arabic_BIN')
    name = models.CharField(max_length=255, db_collation='Arabic_BIN')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Arabic_BIN')
    session_data = models.TextField(db_collation='Arabic_BIN')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Linecapacity1(models.Model):
    linecode = models.CharField(max_length=10, db_collation='Arabic_BIN', blank=True, null=True)
    capacity = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linecapacity1'


class MainappTankcalcmetric(models.Model):
    id = models.BigAutoField(primary_key=True)
    tankid = models.IntegerField(db_column='TankID')  # Field name made lowercase.
    rdate = models.CharField(db_column='RDate', max_length=10, db_collation='Arabic_BIN')  # Field name made lowercase.
    billid = models.CharField(db_column='BillID', max_length=10, db_collation='Arabic_BIN')  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.
    temprature = models.CharField(db_column='Temprature', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.
    water = models.CharField(db_column='Water', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    specweight = models.CharField(db_column='SpecWeight', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.
    refinery = models.CharField(db_column='Refinery', max_length=50, db_collation='Arabic_BIN')  # Field name made lowercase.
    naturallitr = models.CharField(db_column='NaturalLitr', max_length=50, db_collation='Arabic_BIN')  # Field name made lowercase.
    litr60 = models.CharField(db_column='Litr60', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.
    hour = models.CharField(db_column='Hour', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.
    cyear = models.IntegerField(db_column='CYear')  # Field name made lowercase.
    envtemp = models.CharField(db_column='EnvTemp', max_length=20, db_collation='Arabic_BIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mainapp_tankcalcmetric'


class Oilnew(models.Model):
    a1 = models.CharField(db_column='A1', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    a2 = models.CharField(db_column='A2', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    a3 = models.CharField(db_column='A3', max_length=50, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', blank=True, null=False, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oilnew'


class Region(models.Model):
    stationid = models.CharField(db_column='StationID', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    regionnumb = models.CharField(db_column='Regionnumb', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Regionid(models.Model):
    regionnumb = models.CharField(db_column='Regionnumb', max_length=10, db_collation='Arabic_BIN', blank=True, null=True)  # Field name made lowercase.
    regionname = models.TextField(db_collation='Arabic_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regionid'


class Userpower(models.Model):
    userid = models.CharField(primary_key=True, max_length=50, db_collation='Arabic_BIN')
    username = models.CharField(max_length=50, db_collation='Arabic_BIN', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userpower'

class Regidentification(models.Model):
    regname= models.CharField(max_length=100)
    def __str__(self):
        return self.regname

class Station_Region_Relation(models.Model):
    regname=models.ForeignKey(Regidentification,on_delete=models.DO_NOTHING)
    stationname=models.ForeignKey(Station,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.regname