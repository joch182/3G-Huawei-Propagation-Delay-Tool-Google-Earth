import sys
import pandas as pd

def validate(data_path, ept_path):
    if not (data_path.endswith('.csv') or ept_path.endswith('.csv')):
        print('Please use the correct table format (CSV)')
        sys.exit()

    data = pd.read_csv(data_path, index_col="Cell_Name")
    ept = pd.read_csv(ept_path, index_col="Cell_Name")
    
    if (len(data.columns) != 37 or data.columns.values[0] != 'Cell_Name' or data.columns.values[1] != 'VS.TP.UE.0' or data.columns.values[2] != 'VS.TP.UE.1' or data.columns.values[3] != 'VS.TP.UE.2' or data.columns.values[4] != 'VS.TP.UE.3' or data.columns.values[5] != 'VS.TP.UE.4' or data.columns.values[6] != 'VS.TP.UE.5' or data.columns.values[7] != 'VS.TP.UE.6.9' or data.columns.values[8] != 'VS.TP.UE.10.15' or data.columns.values[9] != 'VS.TP.UE.16.25' or data.columns.values[10] != 'VS.TP.UE.26.35' or data.columns.values[11] != 'VS.TP.UE.36.55' or data.columns.values[12] != 'VS.TP.UE.More55' or data.columns.values[13] != 'VS.EcNo.Mean.TP0(dB)' or data.columns.values[14] != 'VS.EcNo.Mean.TP1(dB)' or data.columns.values[15] != 'VS.EcNo.Mean.TP2(dB)' or data.columns.values[16] != 'VS.EcNo.Mean.TP3(dB)' or data.columns.values[17] != 'VS.EcNo.Mean.TP4(dB)' or data.columns.values[18] != 'VS.EcNo.Mean.TP5(dB)' or data.columns.values[19] != 'VS.EcNo.Mean.TP6.9(dB)' or data.columns.values[20] != 'VS.EcNo.Mean.TP10.15(dB)' or data.columns.values[21] != 'VS.EcNo.Mean.TP16.25(dB)' or data.columns.values[22] != 'VS.EcNo.Mean.TP26.35(dB)' or data.columns.values[23] != 'VS.EcNo.Mean.TP36.55(dB)'or data.columns.values[24] != 'VS.EcNo.Mean.TP.More55(dB)'or data.columns.values[25] != 'VS.RSCP.Mean.TP0(dBm)'or data.columns.values[26] != 'VS.RSCP.Mean.TP1(dBm)'or data.columns.values[27] != 'VS.RSCP.Mean.TP2(dBm)'or data.columns.values[28] != 'VS.RSCP.Mean.TP3(dBm)'or data.columns.values[29] != 'VS.RSCP.Mean.TP4(dBm)'or data.columns.values[30] != 'VS.RSCP.Mean.TP5(dBm)'or data.columns.values[31] != 'VS.RSCP.Mean.TP6.9(dBm)'or data.columns.values[32] != 'VS.RSCP.Mean.TP10.15(dBm)'or data.columns.values[33] != 'VS.RSCP.Mean.TP16.25(dBm)'or data.columns.values[34] != 'VS.RSCP.Mean.TP26.35(dBm)'or data.columns.values[35] != 'VS.RSCP.Mean.TP36.55(dBm)'or data.columns.values[36] != 'VS.RSCP.Mean.TP.More55(dBm)'):
        print('Data file is not according to template')
        sys.exit()

    if (len(ept.columns) != 5 or ept.columns.values[0] != 'Cell_Name' or ept.columns.values[1] != 'Lon' or ept.columns.values[2] != 'Lat' or ept.columns.values[3] != 'Azimuth' or ept.columns.values[4] != 'Beamwidth'):
        print('EPT file is not according to template')
        sys.exit()

    full_df = pd.concat([ept, data], axis=1, sort=True)
    if  not pd.Series(ept['Beamwidth']).between(0,359).all():       #If at least 1 value is out of range then fail
        print('Beamwidth columns is out of range (Value should be between 0 and 359)')
        sys.exit()

    if  not pd.Series(ept['Azimuth']).between(0,359).all():       #If at least 1 value is out of range then fail
        print('Azimuth columns is out of range (Value should be between 0 and 359)')
        sys.exit()

    if  full_df['Lon'].isnull().values.any() or full_df['Lat'].isnull().values.any():       #If at least 1 value is NaN then fail
        print('There are cells not matching between tables')
        sys.exit()
    
    print('Validation succeed')
    return full_df