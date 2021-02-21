from model.odd_headers import OddHeaders


class OddEnum:
  BET365 = OddHeaders('BET365H', 'BET365D', 'BET365A')
  BLUE_SQUARE = OddHeaders('BSH', 'BSD', 'BSA')
  BET_AND_WIN = OddHeaders('BWH', 'BWD', 'BWA')
  GAMEBOOKERS = OddHeaders('GBH', 'GBD', 'GBA')
  INTERWETTEN = OddHeaders('IWH', 'IWD', 'IWA')
  LADBROKES = OddHeaders('LBH', 'LBD', 'LBA')
  PINNACLE = OddHeaders('PSH', 'PSD', 'PSA')
  SPORTING_ODDS = OddHeaders('SOH', 'SOD', 'SOA')
  SPORTINGBET = OddHeaders('SBH', 'SBD', 'SBA')
  STAN_JAMES = OddHeaders('SJH', 'SJD', 'SJA')
  STANLEYBET = OddHeaders('SYH', 'SYD', 'SYA')
  VC_BET = OddHeaders('VCH', 'VCD', 'VCA')
  WILLIAM_HILL = OddHeaders('WHH', 'WHD', 'WHA')

  def __iter__(self):
    return iter(vars(self).values())
