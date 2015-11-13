
#this is used for tlv grammer

TLV_HEAD_LEN = 4
SMALLEST_FOUR_BYTES = 4
SMALLEST_EIGHT_BYTES = 8


type_dict = {'01D0': 'USECONFIG', '000C': 'EPGROUP'}

test_data = "01 D0 00 2C 00 0C 00 04 00 00 03 04 00 0B 00 04 01 02 03 04 00 0A 00 08 01 02 03 04 05 06 07 08 00 23 00 04 09 08 07 06"




def IsSmallestLength(input):
    FOUR_BYTES_TLV = SMALLEST_FOUR_BYTES + TLV_HEAD_LEN
    EIGHT_BYTES_TLV = SMALLEST_EIGHT_BYTES + TLV_HEAD_LEN

    return SMALLEST_FOUR_BYTES == len(input) or  SMALLEST_EIGHT_BYTES == len(input)

def OutPutTheTlvBuffer(tlv_array):

    if tlv_array[0] + tlv_array[1] in type_dict:
        type_tlv = type_dict[tlv_array[0] + tlv_array[1]]
    else:
        type_tlv = tlv_array[0] + tlv_array[1]
    length_tlv = tlv_array[2] + tlv_array[3]
    value_tlv = " ".join(tlv_array[TLV_HEAD_LEN:TLV_HEAD_LEN + int(length_tlv, 16)])

    print "type is %s\r\nlength is %s\r\nvalue is %s\r\n" % (type_tlv, length_tlv, value_tlv)

def GetTheStartIndex(tlv_array):

    length_tlv = int(tlv_array[2] + tlv_array[3], 16)

    result = 0

    if (SMALLEST_FOUR_BYTES == length_tlv) or (SMALLEST_EIGHT_BYTES == length_tlv):
        result = length_tlv + TLV_HEAD_LEN
    else:
        result = TLV_HEAD_LEN

    return result
    

def parse_tlv(input):
    TLV_HEAD_LEN = 8

    OutPutTheTlvBuffer(input)

    startIndex = GetTheStartIndex(input)
    endIndex = len(input)

    if IsSmallestLength(input):
        return

    return parse_tlv(input[startIndex:endIndex] )







if __name__ == "__main__":
    """this is used for tlv grammer"""
    print "start to parse tlv..."
    parse_tlv(test_data.split(" "))
