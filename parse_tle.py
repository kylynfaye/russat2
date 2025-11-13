import pandas as pd

def parse_scientific_notation(string):
    try:
        if string.strip() == '+00000-0' or string.strip() == '+00000+0':
            return 0.0
        
        mantissa = float(string[0] + '.' + string[1:6])
        exponent = int(string[6:8])
        return mantissa * (10 ** exponent)
    except:
        return 0.0
    
def parse_tle_to_df(tle_list):
    data = []
    
    for tle in tle_list:
        # Skip if not a proper TLE pair
        #print(len(tle))
        print(tle)

        if not isinstance(tle, list) or len(tle) != 2:
            print(f"Skipping invalid TLE pair: {tle}")
            continue
            
        line1, line2 = tle
        line1_data = {
            'line1': line1,
            'line2': line2,
            # Line 1 elements
            'catalog_number': int(line1[2:7]),
            'classification': line1[7],
            'launch_year': line1[9:11],
            'launch_number': line1[11:14],
            'launch_piece': line1[14:17].strip(),
            'epoch_year': int(line1[18:20]),
            'epoch_day': float(line1[20:32]),
            'mean_motion_dot': float(line1[33:43]),
            'mean_motion_ddot': parse_scientific_notation(line1[44:52] + line1[52:54]),
            'bstar': parse_scientific_notation(line1[53:61] + line1[61:63]),
            'ephemeris_type': int(line1[63]) if line1[63].strip() else 0,
            'element_number': int(line1[64:68]) if line1[64:68].strip() else 0,
            # Line 2 elements
            'satellite_number': int(line2[2:7]),
            'inclination': float(line2[8:16]),
            'ra_of_asc_node': float(line2[17:25]),
            'eccentricity': float('0.' + line2[26:33]),
            'arg_of_perigee': float(line2[34:42]),
            'mean_anomaly': float(line2[43:51]),
            'mean_motion': float(line2[52:63]),
            'rev_at_epoch': int(line2[63:68]) if line2[63:68].strip() else 0
        }
        data.append(line1_data)

    return pd.DataFrame(data)