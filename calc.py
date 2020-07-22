import math
import numpy as np

R = 6378.1 #Radius of the Earth in Km

''' From 1 coordinate point, a set distance and the angle we get the 2nd coordinate point. The 
angleRad variable is usually know as bearing (in RAD unit) '''
def getCoordinatePoint(originLat, originLon, angleRad, distance):
    originLat = np.deg2rad(originLat)
    originLon = np.deg2rad(originLon)

    lat2 = math.asin(math.sin(originLat)*math.cos(distance/R) + math.cos(originLat)*math.sin(distance/R)*math.cos(angleRad))
    lon2 = originLon + math.atan2(math.sin(angleRad)*math.sin(distance/R)*math.cos(originLat), math.cos(distance/R)-math.sin(originLat)*math.sin(lat2))
    coord = {
        'lat2': np.rad2deg(lat2),
        'lon2': np.rad2deg(lon2)
    }
    return coord

def getCoordinateTP0(originLat, originLon, Azimuth, BW, tpProportion):
    splitBW = BW/4
    tpProportion = round(tpProportion * 1500/100,2)  #2200 is an estimated value to shown different levels on the TP in GE
    coordString = str(originLon) + ',' + str(originLat) + ',' + str(tpProportion) + ' '
    for i in range(5):
            distance = 0.234
            angle = Azimuth - (BW/2) + (i*splitBW)
            if angle >= 360:
                angle = angle - 360
            if angle < 0:
                angle = angle + 360

            genCord = getCoordinatePoint(originLat, originLon, np.deg2rad(angle), distance)
            coordString = coordString + str(genCord['lon2']) + ',' + str(genCord['lat2']) + ',' + str(tpProportion) + ' '
    coordString = coordString + str(originLon) + ',' + str(originLat) + ',' + str(tpProportion)
    return coordString

def getCoordinateTPMoreThan0(originLat, originLon, Azimuth, BW, tpProportion, TPLevel):
    splitBW = BW/4
    tpProportion = round(tpProportion * 1500/100,2)  #2200 is an estimated value to shown different levels on the TP in GE
    coordString = ''
    #coordString = str(originLon) + ',' + str(originLat) + ',' + str(tpProportion) + ' '
    lowerDistance = {
        1: 0.16,
        2: 0.39,
        3: 0.62,
        4: 0.86,
        5: 1.1,
        6: 1.3,
        10: 2.3,
        16: 3.7,
        26: 6,
        36: 8.3,
        55: 12.8
    }

    ''' We get the points for the lower curve '''
    distance = lowerDistance.get(TPLevel, 'Invalid lower TP level')
    for i in range(5):
        angle = Azimuth - (BW/2) + (i*splitBW)
        if angle >= 360:
            angle = angle - 360
        if angle < 0:
            angle = angle + 360
        genCord = getCoordinatePoint(originLat, originLon, math.radians(angle), distance)
        if i == 0:
            origin = genCord
        coordString = coordString + str(genCord['lon2']) + ',' + str(genCord['lat2']) + ',' + str(tpProportion) + ' '
    
    higherDistance = {
        1: 0.39,
        2: 0.62,
        3: 0.86,
        4: 1.1,
        5: 1.3,
        6: 2.3,
        10: 3.7,
        16: 6,
        26: 8.3,
        36: 12.8,
        55: 16
    }
    ''' We get the points for the higher curve '''
    distance = higherDistance.get(TPLevel, 'Invalid higher TP level')
    for i in reversed(range(5)):
        angle = Azimuth - (BW/2) + (i*splitBW)
        if angle >= 360:
            angle = angle - 360
        if angle < 0:
            angle = angle + 360
        genCord = getCoordinatePoint(originLat, originLon, math.radians(angle), distance)
        coordString = coordString + str(genCord['lon2']) + ',' + str(genCord['lat2']) + ',' + str(tpProportion) + ' '

    coordString = coordString + str(origin['lon2']) + ',' + str(origin['lat2']) + ',' + str(tpProportion)
    return coordString

def generateKMLData(df):
    df['Bearing'] = df['Beamwidth'].apply(np.deg2rad)
    df['TP_Sum'] = df['VS.TP.UE.0'] + df['VS.TP.UE.1'] + df['VS.TP.UE.2'] + df['VS.TP.UE.3'] + df['VS.TP.UE.4'] + df['VS.TP.UE.5'] + df['VS.TP.UE.6.9'] + df['VS.TP.UE.10.15'] + df['VS.TP.UE.16.25'] + df['VS.TP.UE.26.35'] + df['VS.TP.UE.36.55'] + df['VS.TP.UE.More55']
    df['Proportion_TP0'] = round(100 * (df['VS.TP.UE.0']/df['TP_Sum']),2)
    df['Proportion_TP1'] = round(100 * (df['VS.TP.UE.1']/df['TP_Sum']),2)
    df['Proportion_TP2'] = round(100 * (df['VS.TP.UE.2']/df['TP_Sum']),2)
    df['Proportion_TP3'] = round(100 * (df['VS.TP.UE.3']/df['TP_Sum']),2)
    df['Proportion_TP4'] = round(100 * (df['VS.TP.UE.4']/df['TP_Sum']),2)
    df['Proportion_TP5'] = round(100 * (df['VS.TP.UE.5']/df['TP_Sum']),2)
    df['Proportion_TP6.9'] = round(100 * (df['VS.TP.UE.6.9']/df['TP_Sum']),2)
    df['Proportion_TP10.15'] = round(100 * (df['VS.TP.UE.10.15']/df['TP_Sum']),2)
    df['Proportion_TP16.25'] = round(100 * (df['VS.TP.UE.16.25']/df['TP_Sum']),2)
    df['Proportion_TP26.35'] = round(100 * (df['VS.TP.UE.26.35']/df['TP_Sum']),2)
    df['Proportion_TP36.55'] = round(100 * (df['VS.TP.UE.36.55']/df['TP_Sum']),2)
    df['Proportion_TPMore55'] = round(100 * (df['VS.TP.UE.More55']/df['TP_Sum']),2)

    df['Avg.RSCP_TP0'] = df['VS.RSCP.Mean.TP0(dBm)'] - 115
    df['Avg.RSCP_TP1'] = df['VS.RSCP.Mean.TP1(dBm)'] - 115
    df['Avg.RSCP_TP2'] = df['VS.RSCP.Mean.TP2(dBm)'] - 115
    df['Avg.RSCP_TP3'] = df['VS.RSCP.Mean.TP3(dBm)'] - 115
    df['Avg.RSCP_TP4'] = df['VS.RSCP.Mean.TP4(dBm)'] - 115
    df['Avg.RSCP_TP5'] = df['VS.RSCP.Mean.TP5(dBm)'] - 115
    df['Avg.RSCP_TP6.9'] = df['VS.RSCP.Mean.TP6.9(dBm)'] - 115
    df['Avg.RSCP_TP10.15'] = df['VS.RSCP.Mean.TP10.15(dBm)'] - 115
    df['Avg.RSCP_TP16.25'] = df['VS.RSCP.Mean.TP16.25(dBm)'] - 115
    df['Avg.RSCP_TP26.35'] = df['VS.RSCP.Mean.TP26.35(dBm)'] - 115
    df['Avg.RSCP_TP36.55'] = df['VS.RSCP.Mean.TP36.55(dBm)'] - 115
    df['Avg.RSCP_TPMore55'] = df['VS.RSCP.Mean.TP.More55(dBm)'] - 115

    df['Avg.ECNO_TP0'] = round((df['VS.EcNo.Mean.TP0(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP1'] = round((df['VS.EcNo.Mean.TP1(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP2'] = round((df['VS.EcNo.Mean.TP2(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP3'] = round((df['VS.EcNo.Mean.TP3(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP4'] = round((df['VS.EcNo.Mean.TP4(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP5'] = round((df['VS.EcNo.Mean.TP5(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP6.9'] = round((df['VS.EcNo.Mean.TP6.9(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP10.15'] = round((df['VS.EcNo.Mean.TP10.15(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP16.25'] = round((df['VS.EcNo.Mean.TP16.25(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP26.35'] = round((df['VS.EcNo.Mean.TP26.35(dB)'] - 49)/2,2)
    df['Avg.ECNO_TP36.55'] = round((df['VS.EcNo.Mean.TP36.55(dB)'] - 49)/2,2)
    df['Avg.ECNO_TPMore55'] = round((df['VS.EcNo.Mean.TP.More55(dB)'] - 49)/2,2)

    df = df.drop(['VS.TP.UE.0','VS.TP.UE.1','VS.TP.UE.2','VS.TP.UE.3','VS.TP.UE.4','VS.TP.UE.5','VS.TP.UE.6.9','VS.TP.UE.10.15','VS.TP.UE.16.25','VS.TP.UE.26.35','VS.TP.UE.36.55','VS.TP.UE.More55','VS.EcNo.Mean.TP0(dB)','VS.EcNo.Mean.TP1(dB)','VS.EcNo.Mean.TP2(dB)','VS.EcNo.Mean.TP3(dB)','VS.EcNo.Mean.TP4(dB)','VS.EcNo.Mean.TP5(dB)','VS.EcNo.Mean.TP6.9(dB)','VS.EcNo.Mean.TP10.15(dB)','VS.EcNo.Mean.TP16.25(dB)','VS.EcNo.Mean.TP26.35(dB)','VS.EcNo.Mean.TP36.55(dB)','VS.EcNo.Mean.TP.More55(dB)','VS.RSCP.Mean.TP0(dBm)','VS.RSCP.Mean.TP1(dBm)','VS.RSCP.Mean.TP2(dBm)','VS.RSCP.Mean.TP3(dBm)','VS.RSCP.Mean.TP4(dBm)','VS.RSCP.Mean.TP5(dBm)','VS.RSCP.Mean.TP6.9(dBm)','VS.RSCP.Mean.TP10.15(dBm)','VS.RSCP.Mean.TP16.25(dBm)','VS.RSCP.Mean.TP26.35(dBm)','VS.RSCP.Mean.TP36.55(dBm)','VS.RSCP.Mean.TP.More55(dBm)','TP_Sum'], axis=1)


    df['Coordinates_TP0'] = df.apply(lambda x: getCoordinateTP0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP0']), axis=1)
    df['Coordinates_TP1'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP1'], 1), axis=1)
    df['Coordinates_TP2'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP2'], 2), axis=1)
    df['Coordinates_TP3'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP3'], 3), axis=1)
    df['Coordinates_TP4'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP4'], 4), axis=1)
    df['Coordinates_TP5'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP5'], 5), axis=1)
    df['Coordinates_TP6'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP6.9'], 6), axis=1)
    df['Coordinates_TP10'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP10.15'], 10), axis=1)
    df['Coordinates_TP16'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP16.25'], 16), axis=1)
    df['Coordinates_TP26'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP26.35'], 26), axis=1)
    df['Coordinates_TP36'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TP36.55'], 36), axis=1)
    df['Coordinates_TP55'] = df.apply(lambda x: getCoordinateTPMoreThan0(x['Lat'],x['Lon'],x['Azimuth'],x['Beamwidth'],x['Proportion_TPMore55'], 55), axis=1)

    print(df.head())
    return df
