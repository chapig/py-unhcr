import requests
from pandas import DataFrame


class UNHCR:
    """
    UNHCR API client to get data on asylum applications and decisions.
    """

    def __init__(self):
        self.url = "https://api.unhcr.org/population/v1/"
        self.limit = 100
        self.page = 1
        self.year_from = 1900
        self.year_to = 2024
        self.download_as_csv = True
        self.coo = None
        self.coa = None
        self.coo_all = False
        self.coa_all = False
        self.cf_type = None
        self.region = ""
        self.id = ""

    def set_filter(self, coo=None, coa=None, coo_all=False, coa_all=False, cf_type=None, limit=100, page=1,
                   year_from=2023, year_to=2024, region="", id=""):
        """
        Filter the data by country of origin, country of asylum, and type of claim.
        """
        self.coo = coo
        self.coa = coa
        self.coo_all = coo_all
        self.coa_all = coa_all
        self.cf_type = cf_type
        self.limit = limit
        self.page = page
        self.year_from = year_from
        self.year_to = year_to
        self.region = region
        self.id = id

        return self

    def build_url(self, endpoint):
        """
        Build the URL with the query parameters.
        """
        url = f"{self.url}{endpoint}/?limit={self.limit}&page={self.page}&yearFrom={self.year_from}&yearTo={self.year_to}"
        if self.coo:
            url += f"&coo={self.coo}"
        if self.coa:
            url += f"&coa={self.coa}"
        if self.coo_all:
            url += "&coo_all=true"
        if self.coa_all:
            url += "&coa_all=true"
        if self.cf_type:
            url += f"&cf_type={self.cf_type}"
        if self.region:
            url += f"&region={self.region}"
        if self.id:
            url += f"&id={self.id}"

        return url

    def fetch_all_data(self, endpoint, dataframe=False):
        """
        Fetch all pages of data and return them combined into a single dataframe or JSON.
        """
        all_items = []
        self.page = 1  # Reset page to 1
        while True:
            url = self.build_url(endpoint)
            url_with_page = f"{url}&page={self.page}"
            response = requests.get(url_with_page)

            if response.status_code == 200:
                data = response.json().get("items", [])
                if not data:  # Break loop if no more data
                    break
                all_items.extend(data)
                self.page += 1
            else:
                break  # Stop if there's an issue with the request

        if dataframe:
            return DataFrame(all_items)
        return all_items

    def asylum_applications(self, dataframe=False):
        """
        Asylum claims submitted by year and countries of asylum and origin.
        Claims are submitted by asylum applicants and are applications for international protection.
        """
        return self.fetch_all_data("asylum-applications", dataframe)

    def asylum_decisions(self, dataframe=False):
        """
        Decisions taken on asylum claims by year and countries of asylum and origin.
        Asylum claims are applications for international protection and decisions on asylum claims can be positive, negative or otherwise closed.
        """
        return self.fetch_all_data("asylum-decisions", dataframe)

    def countries(self, dataframe=False):
        """
        Returns the list of countries together with their codes, names, and regions.
        """
        return self.fetch_all_data("countries", dataframe)

    def demographics(self, dataframe=False):
        """
        Retrieves demographic and sub-national data, where such disaggregation is available.
        UNHCR collects this information for all population types, as well as two durable solutions (returned IDPs and refugees).
        """
        return self.fetch_all_data("demographics", dataframe)

    def footnotes(self):
        """
        Retrieves the footnotes for the specified data.
        The footnotes provide additional details, data collection issues and relevant qualifications to represent the data appropriately.
        """
        url = self.build_url("footnotes")
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["items"][0]
        return None

    def idmc(self, dataframe=False):
        """
        Retrieves the data on Internally displaced persons due to conflict and violence that is produced by the Internal Displacement Monitoring Centre.
        """
        return self.fetch_all_data("idmc", dataframe)

    def nowcasting(self, dataframe=False):
        """
        Nowcasting is a statistical method that uses historical data to predict the current year’s data.
        It is used to estimate the current year’s data when it is not yet available.
        """
        return self.fetch_all_data("nowcasting", dataframe)

    def population(self, dataframe=False):
        """
        UNHCR data on displacement at the end of the year.
        """
        return self.fetch_all_data("population", dataframe)

    def regions(self, dataframe=False):
        """
        Returns the list of regions together with their codes and names.
        """
        return self.fetch_all_data("regions", dataframe)

    def solutions(self, dataframe=False):
        """
        Data on solutions record those refugees and IDPs that have availed a durable solution.
        """
        return self.fetch_all_data("solutions", dataframe)

    def unrwa(self, dataframe=False):
        """
        Retrieves the data on Palestine refugees registered under UNRWA’s mandate.
        """
        return self.fetch_all_data("unrwa", dataframe)

    def years(self, dataframe=False):
        """
        Retrieves the list of years for which data is available.
        """
        return self.fetch_all_data("years", dataframe)
