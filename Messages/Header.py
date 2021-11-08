# Glossary
# T: DTag size
# N: Fragment Compressed Number (FCN) size
# M: Window identifier (present only if windows are used) size
# U: Reassembly Check Sequence (RCS) size


class Header:
    profile = None

    RULE_ID = ""
    DTAG = ""
    W = ""
    FCN = ""
    C = ""

    string = ""
    bytes = None

    def __init__(self, profile, rule_id, dtag, w, fcn, c=""):  # rule_id is arbitrary, as it's not applicable for F/R
        
        self.profile = profile

        direction = profile.direction
        # print(direction)
        if direction == "DOWNLINK":
            self.FCN = ""
            self.C = c
        # print('rule_id: {}, len(rule_id): {}, profile.RULE_ID_SIZE: {}'.format(rule_id, len(rule_id), profile.RULE_ID_SIZE))
        if len(rule_id) != profile.RULE_ID_SIZE:
            print('RULE must be of length RULE_ID_SIZE')
        else:
            self.RULE_ID = rule_id
        # print("profile.T: {}".format(profile.T))
        if profile.T == 0:
            self.DTAG = ""
        elif len(dtag) != profile.T:
            print('DTAG must be of length T')
        else:
            self.DTAG = dtag

        if len(w) != profile.M:
            print(w)
            print(profile.M)
            print('W must be of length M')
        else:
            self.W = w

        if fcn != "":
            if len(fcn) != profile.N:
                print('FCN must be of length N')
            else:
                self.FCN = fcn

        self.string = "".join([self.RULE_ID, self.DTAG, self.W, self.FCN, self.C])
        self.bytes = bytes(int(self.string[i:i + 8], 2) for i in range(0, len(self.string), 8))

    def test(self):

        print("HEADER:")
        print(self.string)

        if len(self.string) != self.profile.HEADER_LENGTH:
            print('The header has not been initialized correctly.')


class HeaderNoACK(Header):
    """ Class that extends Header class customize to Sigfox Uplink NoACK 1 byte header 
        4.5.1.1.  Uplink No-ACK Mode (draft-ietf-lpwan-schc-over-sigfox-03.txt)
        The RECOMMENDED Fragmentation Header size is 8 bits, and it is
        composed as follows:
        - RuleID size: 4 bits
        - DTag size (T): 0 bits
        - Fragment Compressed Number (FCN) size (N): 4 bits
        - As per [RFC8724], in the No-ACK mode the W (window) field is not present.
        - RCS: Not used

    """
    def __init__(self, profile, rule_id, fcn, c=""):  # rule_id is arbitrary, as it's not applicable for F/R

        self.profile = profile

        direction = profile.direction

        if direction == "DOWNLINK":
            self.FCN = ""
            self.C = c

        if len(rule_id) != profile.RULE_ID_SIZE:
            print('RULE must be of length RULE_ID_SIZE')
        else:
            self.RULE_ID = rule_id

        # if profile.T == "0":
        #     self.DTAG = ""
        # elif len(dtag) != profile.T:
        #     print('DTAG must be of length T')
        # else:
        #     self.DTAG = dtag

        # if len(w) != profile.M:
        #     print(w)
        #     print(profile.M)
        #     print('W must be of length M')
        # else:
        #     self.W = w

        if fcn != "":
            if len(fcn) != profile.N:
                print('FCN must be of length N')
            else:
                self.FCN = fcn

        self.string = "".join([self.RULE_ID, self.DTAG, self.W, self.FCN, self.C])
        self.bytes = bytes(int(self.string[i:i + 8], 2) for i in range(0, len(self.string), 8))