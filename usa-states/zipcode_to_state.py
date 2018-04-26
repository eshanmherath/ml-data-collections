import pandas as pd


class USAGeo:
    def __init__(self):
        self.geo_data = pd.read_csv('geo-data.csv')

    def get_state(self, zip_code=None):
        if zip_code is None:
            return 'na'
        else:
            state = self.geo_data[self.geo_data['zipcode'] == zip_code].iloc[0]['state_abbr']
            return state


if __name__ == '__main__':
    geo = USAGeo()
    state = geo.get_state(zip_code='35006')
    print(state)