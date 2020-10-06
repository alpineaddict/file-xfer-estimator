'''
Framework for mathematical functions that GUI relies on to perform
data transfer equation.
'''

def convert_to_bits(dataset_size, data_total):
    '''
    Convert given amount of data to bits.
    '''
    bits = 0
    
    if   dataset_size == 'KB':
        bits = (data_total * 1024) * 8
    elif dataset_size == 'MB':
        bits = ((data_total * 1024) * 1024) * 8
    elif dataset_size == 'GB':
        bits = (((data_total * 1024) * 1024) * 1024) * 8
    elif dataset_size == 'TB':
        bits = ((((data_total * 1024) * 1024) * 1024) * 1024) * 8
    
    return bits

def get_transfer_time(units, bits, transfer_speed):
    '''
    Get total amount of time to complete transfer. Return time in seconds.
    '''
    time = 0
    
    if units == 'Kbps':
        time = bits / (transfer_speed * 1000)
    elif units == 'Mbps':
        time = bits / ((transfer_speed * 1000) * 1000)
    elif units == 'Gbps':
        time = bits / (((transfer_speed * 1000) * 1000) * 1000)
    
    return time

def convert_time(seconds):
    '''
    Accept variable assigned to total time for data transfer operation and
    convert to days, hours, minutes, seconds.
    '''
    
    time     = seconds
    days     = int(time // (24 * 3600))
    time     = time % (24 * 3600)
    hours    = int(time // 3600)
    time    %= 3600
    minutes  = int(time // 60)
    time    %= 60
    seconds  = round(time)
    
    converted = (f" Day(s): {days} // Hour(s): {hours} // Minute(s): {minutes} // "
                f"Second(s): {seconds}")

    return converted
