import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettyXML(xml_doc):
    xmlstr = minidom.parseString(ET.tostring(xml_doc)).toprettyxml(indent="    ")
    with open("3G_TP_Results.kmz", "w") as f:
        f.write(xmlstr)
    return

def generateXML(df):
    xml_doc = ET.Element('kml')
    xml_doc.set('xmlns', 'http://www.opengis.net/kml/2.2')
    xml_doc.set('xmlns:gx', 'http://www.google.com/kml/ext/2.2')
    xml_doc.set('xmlns:kml', 'http://www.opengis.net/kml/2.2')
    xml_doc.set('xmlns:atom', 'http://www.w3.org/2005/Atom')

    document = ET.SubElement(xml_doc, 'Document')
    ET.SubElement(document, 'name').text = '3G_TP_Analiysis.KMZ'

    #For per row

    for row in df.itertuples():
        cellName = ET.SubElement(document, 'Folder')
        ET.SubElement(cellName, 'name').text = str(row[0])
        ET.SubElement(cellName, 'open').text = '0'

        #TP0
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.0'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '64F00A14'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '64F00A14'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '0-156m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[18])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[30])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[6])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[42])

        #TP1
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.1'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '64F07800'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '64F07800'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '156m-390m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[19])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[31])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[7])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[43])

        #TP2
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.2'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '643C8214'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '643C8214'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '390m-624m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[20])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[32])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[8])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[44])

        #TP3
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.3'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '6400E614'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '6400E614'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '624m-858m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[21])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[33])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[9])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[45])

        #TP4
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.4'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '6414F046'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '6414F046'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '858m-1092m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[22])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[34])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[10])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[46])

        #TP5
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.5'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '64B478F0'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '64B478F0'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '1092m-1326m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[23])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[35])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[11])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[47])

        #TP6
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.6.9'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '6414F0BE'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '6414F0BE'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '1326m-2262m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[24])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[36])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[12])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[48])

        #TP10
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.10.15'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '6414F0FF'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '6414F0FF'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '2262m-3666m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[25])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[37])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[13])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[49])

        #TP16
        placemark = ET.SubElement(cellName, 'Placemark')
        ET.SubElement(placemark, 'name').text = 'VS.TP.UE.16.25'
        #Creating placemark/style
        style = ET.SubElement(placemark,'Style')
        linestyle = ET.SubElement(style, 'LineStyle')
        ET.SubElement(linestyle, 'color').text = '6414B4FF'
        ET.SubElement(linestyle, 'width').text = '0'
        polystyle = ET.SubElement(style, 'PolyStyle')
        ET.SubElement(polystyle, 'color').text = '6414B4FF'
        #Creating placemark/description
        description = ET.SubElement(placemark, 'description')
        table = ET.SubElement(description, 'table')
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Cell Name: '
        ET.SubElement(tr, 'td').text = str(row[0])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Azimuth: '
        ET.SubElement(tr, 'td').text = str(row[3])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'BW: '
        ET.SubElement(tr, 'td').text = str(row[4])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Distance: '
        ET.SubElement(tr, 'td').text = '3666m-6006m'
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
        ET.SubElement(tr, 'td').text = str(row[26])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
        ET.SubElement(tr, 'td').text = str(row[38])
        tr = ET.SubElement(table, 'tr')
        ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
        ET.SubElement(tr, 'td').text = str(row[14])
        #Creating placemark/polygon
        polygon = ET.SubElement(placemark, 'Polygon')
        ET.SubElement(polygon, 'extrude').text = '1'
        ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
        outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
        linearring = ET.SubElement(outerboundaryis, 'LinearRing')
        ET.SubElement(linearring, 'coordinates').text = str(row[50])

        if (row[15] > 1 or row[16] > 1 or row[17] > 1):             #If following TP have less than 1% of proportion no need to graph it
            #TP26
            placemark = ET.SubElement(cellName, 'Placemark')
            ET.SubElement(placemark, 'name').text = 'VS.TP.UE.26.35'
            #Creating placemark/style
            style = ET.SubElement(placemark,'Style')
            linestyle = ET.SubElement(style, 'LineStyle')
            ET.SubElement(linestyle, 'color').text = '641478FF'
            ET.SubElement(linestyle, 'width').text = '0'
            polystyle = ET.SubElement(style, 'PolyStyle')
            ET.SubElement(polystyle, 'color').text = '641478FF'
            #Creating placemark/description
            description = ET.SubElement(placemark, 'description')
            table = ET.SubElement(description, 'table')
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Cell Name: '
            ET.SubElement(tr, 'td').text = str(row[0])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Azimuth: '
            ET.SubElement(tr, 'td').text = str(row[3])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'BW: '
            ET.SubElement(tr, 'td').text = str(row[4])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Distance: '
            ET.SubElement(tr, 'td').text = '6006m-8346m'
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
            ET.SubElement(tr, 'td').text = str(row[27])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
            ET.SubElement(tr, 'td').text = str(row[39])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
            ET.SubElement(tr, 'td').text = str(row[15])
            #Creating placemark/polygon
            polygon = ET.SubElement(placemark, 'Polygon')
            ET.SubElement(polygon, 'extrude').text = '1'
            ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
            outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
            linearring = ET.SubElement(outerboundaryis, 'LinearRing')
            ET.SubElement(linearring, 'coordinates').text = str(row[51])

        if (row[16] > 1 or row[17] > 1):
            #TP36
            placemark = ET.SubElement(cellName, 'Placemark')
            ET.SubElement(placemark, 'name').text = 'VS.TP.UE.36.55'
            #Creating placemark/style
            style = ET.SubElement(placemark,'Style')
            linestyle = ET.SubElement(style, 'LineStyle')
            ET.SubElement(linestyle, 'color').text = '64143CFF'
            ET.SubElement(linestyle, 'width').text = '0'
            polystyle = ET.SubElement(style, 'PolyStyle')
            ET.SubElement(polystyle, 'color').text = '64143CFF'
            #Creating placemark/description
            description = ET.SubElement(placemark, 'description')
            table = ET.SubElement(description, 'table')
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Cell Name: '
            ET.SubElement(tr, 'td').text = str(row[0])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Azimuth: '
            ET.SubElement(tr, 'td').text = str(row[3])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'BW: '
            ET.SubElement(tr, 'td').text = str(row[4])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Distance: '
            ET.SubElement(tr, 'td').text = '8346m-12792m'
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
            ET.SubElement(tr, 'td').text = str(row[28])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
            ET.SubElement(tr, 'td').text = str(row[40])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
            ET.SubElement(tr, 'td').text = str(row[16])
            #Creating placemark/polygon
            polygon = ET.SubElement(placemark, 'Polygon')
            ET.SubElement(polygon, 'extrude').text = '1'
            ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
            outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
            linearring = ET.SubElement(outerboundaryis, 'LinearRing')
            ET.SubElement(linearring, 'coordinates').text = str(row[52])

        if (row[17] > 1):
            #TPMore55
            placemark = ET.SubElement(cellName, 'Placemark')
            ET.SubElement(placemark, 'name').text = 'VS.TP.UE.More55'
            #Creating placemark/style
            style = ET.SubElement(placemark,'Style')
            linestyle = ET.SubElement(style, 'LineStyle')
            ET.SubElement(linestyle, 'color').text = '64140078'
            ET.SubElement(linestyle, 'width').text = '0'
            polystyle = ET.SubElement(style, 'PolyStyle')
            ET.SubElement(polystyle, 'color').text = '64140078'
            #Creating placemark/description
            description = ET.SubElement(placemark, 'description')
            table = ET.SubElement(description, 'table')
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Cell Name: '
            ET.SubElement(tr, 'td').text = str(row[0])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Azimuth: '
            ET.SubElement(tr, 'td').text = str(row[3])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'BW: '
            ET.SubElement(tr, 'td').text = str(row[4])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Distance: '
            ET.SubElement(tr, 'td').text = '>12792m'
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Avg. RSCP: '
            ET.SubElement(tr, 'td').text = str(row[29])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Avg. ECNO: '
            ET.SubElement(tr, 'td').text = str(row[41])
            tr = ET.SubElement(table, 'tr')
            ET.SubElement(tr, 'td').text = 'Propagation Delay (%): '
            ET.SubElement(tr, 'td').text = str(row[17])
            #Creating placemark/polygon
            polygon = ET.SubElement(placemark, 'Polygon')
            ET.SubElement(polygon, 'extrude').text = '1'
            ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
            outerboundaryis = ET.SubElement(polygon, 'outerBoundaryIs')
            linearring = ET.SubElement(outerboundaryis, 'LinearRing')
            ET.SubElement(linearring, 'coordinates').text = str(row[53])

        prettyXML(xml_doc)
    return