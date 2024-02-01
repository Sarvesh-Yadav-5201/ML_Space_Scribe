'''
This python Script will be used to extract the Necessary information/data from NASA / ADS 
public repository using an API 
'''

# importing the libraries

import numpy as np
import requests
from urllib.parse import urlencode, quote_plus
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

# Since, for extracting the information of the Research Papers from NASA / ADS. We will have to use keywords to query 
# for diverse papers. For that purpose we have created a list of approximately 400 keywords. Which will be used while querying for the papers :

query_keywords = [
    'stars', 'galaxies', 'planets', 'asteroids', 'comets', 'quasars', 'pulsars', 'nebulae',
    'supernovae', 'black holes', 'cosmic rays', 'gravitational waves', 'dark matter', 'dark energy',
    'radio astronomy', 'optical astronomy', 'infrared astronomy', 'X-ray astronomy',
    'general relativity', 'quantum mechanics', 'string theory', 'cosmology',
    'telescopes', 'spectrometers', 'detectors', 'satellites', 'space probes',
    'exoplanets', 'astrobiology', 'multi-messenger astronomy', 'machine learning in astronomy',
    'celestial mechanics', 'interstellar medium', 'astrochemistry', 'gamma-ray bursts',
    'cosmic microwave background', 'solar flares', 'heliophysics', 'planetary atmospheres',
    'exoplanet atmospheres', 'interplanetary dust', 'interstellar dust', 'heliosphere',
    'astrostatistics', 'astrometry', 'astroinformatics', 'astroengineering', 'astroecology',
    'intergalactic medium', 'space weather', 'planetary geology', 'planetary geophysics',
    'space missions', 'space exploration', 'space agencies', 'space technology', 'satellite missions',
    'interplanetary missions', 'interstellar missions', 'near-Earth objects', 'Kuiper Belt', 'Oort Cloud',
    'star clusters', 'globular clusters', 'open clusters', 'planetary rings', 'binary stars',
    'variable stars', 'red giants', 'white dwarfs', 'brown dwarfs', 'planetary formation',
    'circumstellar disks', 'planetary rings', 'planetary migration', 'planetary habitability',
    'SETI', 'astroethics', 'space law', 'space policy', 'space governance', 'space debris', 'space junk',
    'orbital dynamics', 'space propulsion', 'ion propulsion', 'plasma propulsion', 'rocket science',
    'space habitats', 'space colonies', 'space settlement', 'terraforming', 'space elevators',
    'space mining', 'space resources', 'space manufacturing', 'space medicine', 'astrogeology',
    'astrogeophysics', 'cosmic inflation', 'magnetic fields in space', 'interstellar travel',
    'relativistic astrophysics', 'time dilation', 'space-time curvature', 'gravitational lensing',
    'space-time ripples', 'pulsar timing arrays', 'dark sky preservation', 'telescope arrays',
    'interferometry', 'adaptive optics', 'cosmic censorship', 'event horizon', 'cosmic strings',
    'black hole thermodynamics', 'Hawking radiation', 'primordial black holes', 'cosmic censorship',
    'event horizon telescope', 'primordial nucleosynthesis', 'big bang nucleosynthesis',
    'anthropic principle', 'cosmic censorship', 'fine-tuning of the universe', 'extragalactic astronomy',
    'large-scale structure of the universe', 'cosmic web', 'cosmic voids', 'galaxy clusters',
    'dark energy survey', 'gravitational lensing', 'cosmic microwave background', 'cosmic archaeology',
    'redshift surveys', 'large hadron collider', 'particle astrophysics', 'cosmic rays',
    'high-energy astrophysics', 'cosmic neutrinos', 'gamma-ray astronomy', 'cosmic accelerators',
    'cosmic ray showers', 'cosmic ray observatories', 'neutrino telescopes', 'cosmic ray propagation',
    'cosmic ray interactions', 'ultra-high-energy cosmic rays', 'cosmic-ray detection',
    'cosmic-ray composition', 'cosmic-ray astronomy', 'heliospheric physics', 'solar wind', 'solar flares',
    'coronal mass ejections', 'solar activity', 'solar cycle', 'solar physics', 'solar observations',
    'solar telescopes', 'solar magnetic fields', 'solar prominences', 'solar granulation',
    'solar coronal heating', 'solar photosphere', 'solar chromosphere', 'solar limb', 'solar spectrum',
    'solar radio bursts', 'solar cosmic rays', 'solar energetic particles', 'solar flares and space weather',
    'solar-terrestrial relations', 'space climate', 'cosmic dust', 'interstellar dust', 'interplanetary dust',
    'zodiacal light', 'cometary dust', 'micrometeorites', 'cosmic impact hazard', 'meteoroid streams',
    'meteor showers', 'meteoroids in space', 'meteoritic material', 'meteorite classification',
    'meteorite impact craters', 'atmospheric entry', 'meteorite flux', 'meteorite isotopes',
    'meteorite age dating', 'meteorite composition', 'meteoritic abundances', 'meteorite mineralogy',
    'meteorite petrology', 'meteorite micrometeorites', 'meteorite cosmic ray exposure',
    'meteorite preservation', 'meteorite recovery', 'meteorite research',
    'gravitational interactions', 'stellar evolution', 'cosmic ray origins', 'galactic magnetic fields',
    'dark matter candidates', 'quantum entanglement in space', 'supernova remnants', 'galactic dynamics',
    'cosmic microwave background polarization', 'solar magnetic storms', 'stellar atmospheres', 'neutrino oscillations',
    'pulsar wind nebulae', 'active galactic nuclei', 'interstellar clouds', 'galactic archaeology', 'dark sector physics',
    'exoplanet detection methods', 'habitable zones', 'extrasolar planetary systems', 'orbital debris mitigation',
    'space-based interferometers', 'solar neutrinos', 'neutron star mergers', 'stellar nucleosynthesis',
    'gravitational wave astronomy', 'neutrino astrophysics', 'solar wind interactions with planets',
    'cosmic dust in protoplanetary disks', 'helium abundance in the universe', 'neutrinoless double beta decay',
    'magnetic reconnection in astrophysics', 'interstellar medium dynamics', 'helioseismology', 'gamma-ray bursts progenitors',
    'binary star evolution', 'quantum gravity in the cosmos', 'helium reionization', 'stellar magnetic cycles',
    'neutrino detectors in space', 'cosmic magnetic fields', 'planetary migration in protoplanetary disks',
    'dark matter halos', 'solar prominence dynamics', 'supermassive black holes', 'cosmic strings',
    'neutrino astronomy', 'solar neutrino oscillations', 'radiation pressure in space', 'cosmic inflation models',
    'plasma astrophysics', 'solar limb observations', 'supernova shock waves', 'solar cycle variations',
    'galactic center observations', 'dark energy constraints', 'orbital debris tracking', 'space debris removal methods',
    'planetary nebulae', 'dwarf galaxies', 'microlensing events', 'solar magnetic field reversals',
    'cosmic gamma-ray background', 'galactic cosmic rays', 'supernova explosions', 'quantum fluctuations in the early universe',
    'neutron star atmospheres', 'helium abundance in stars', 'cosmic shear surveys', 'solar coronal mass ejections',
    'planetesimal formation', 'stellar activity cycles', 'cosmic microwave background anomalies', 'quantum tunnelling in astrophysics',
    'helioseismic inversions', 'supernova light curves', 'stellar metallicity', 'dark matter distribution in galaxies',
    'neutrino oscillation experiments', 'cosmic neutrino background', 'solar magnetic field topology', 'cosmic void dynamics',
    'interstellar scintillation', 'cosmic ray modulation', 'solar granulation patterns', 'planetary ring dynamics',
    'stellar occultations', 'dark matter annihilations', 'neutron star mergers as kilonovae', 'solar atmospheric heating',
    'cosmic inflation predictions', 'quantum entanglement in quantum gravity', 'stellar winds', 'neutrino flavor oscillations',
    'cosmic dust in the interstellar medium', 'magnetic fields in protostellar clouds', 'solar supergranulation',
    'helium recombination in the early universe', 'dark matter particle candidates', 'exoplanet habitability',
    'gamma-ray astronomy observatories', 'supernova nucleosynthesis', 'quantum tunnelling in stellar interiors',
    'helium enrichment in galaxies', 'neutrino oscillation patterns', 'cosmic void surveys', 'solar radio emissions',
    'planet formation in protoplanetary disks', 'stellar convection zones', 'dark energy models', 'orbital debris collision risk',
    'space-based gravitational wave detectors', 'planetary migration theories', 'solar neutrino flux variations',
    'cosmic ray isotopic composition', 'galactic magnetic field reversals', 'supernova remnant shocks',
    'quantum coherence in cosmic scales', 'helioseismology techniques', 'stellar accretion disks', 'neutrino mass hierarchy',
    'cosmic microwave background polarization anomalies', 'dark matter interactions with ordinary matter',
    'exoplanet atmosphere composition', 'habitable exomoons', 'orbital debris disposal methods', 'solar magnetic activity cycles',
    'stellar population synthesis', 'neutrino scattering experiments', 'cosmic ray propagation models',
    'galactic cosmic ray acceleration', 'supernova neutrinos', 'quantum entanglement in black hole thermodynamics',
    'helium abundance in quasar spectra', 'dark matter decays', 'neutron star cooling', 'solar prominence eruptions',
    'cosmic gamma-ray bursts', 'planetary ring compositions', 'stellar magnetic activity cycles', 'cosmic void simulations',
    'interstellar polarization', 'cosmic ray showers in the atmosphere', 'solar granulation lifetimes',
    'dark matter substructure', 'exoplanet habitability zones', 'gamma-ray bursts afterglows', 'supernova nucleosynthesis yields',
    'quantum entanglement in wormholes', 'helioseismic inversions techniques', 'stellar magnetic field evolution',
    'neutrino oscillation experiments in space', 'cosmic neutrino oscillations', 'solar coronal heating mechanisms',
    'cosmic void evolution', 'interstellar scintillation observations', 'cosmic ray modulation effects', 'solar granulation patterns',
    'planetary ring dynamics simulations', 'stellar magnetic field reversals', 'dark matter indirect detection experiments',
    'neutron star mergers as gravitational wave sources', 'helium enrichment in the intergalactic medium',
    'supernova nucleosynthesis in massive stars', 'quantum coherence in cosmic structures', 'helioseismic inversions applications',
    'stellar accretion disk instabilities', 'neutrino oscillation experiments on Earth', 'cosmic microwave background polarization measurements',
    'dark matter in the Milky Way halo', 'exoplanet atmosphere escape', 'habitable exoplanets detection methods', 'orbital debris mitigation strategies',
    'solar magnetic activity cycles variations', 'stellar population synthesis models', 'neutrino scattering experiments with astrophysical neutrinos',
    'cosmic ray propagation models in the interstellar medium', 'galactic cosmic ray acceleration mechanisms', 'supernova neutrinos detection methods',
    'quantum entanglement in black hole information paradox', 'helium abundance in quasar spectra variations', 'dark matter decays in galaxies',
    'neutron star cooling models', 'solar prominence eruptions mechanisms', 'cosmic gamma-ray bursts observations', 'planetary ring compositions analysis',
    'stellar magnetic activity cycles variations', 'cosmic void simulations methods', 'interstellar polarization measurements', 'cosmic ray showers in the atmosphere observations',
    'solar granulation lifetimes variations', 'dark matter substructure simulations', 'exoplanet habitability zones variations', 'gamma-ray bursts afterglows observations',
    'supernova nucleosynthesis yields variations', 'quantum entanglement in wormholes applications', 'helioseismic inversions techniques improvements',
    'stellar magnetic field evolution simulations'
]

# These keywords will be used while querying for the research papers.


####################################################################################################

# Setting up the credentials 

api_token  =  'aramvBIBu9gBnsShqXquy0HzVh2x9D6uIu6qNVeQ'

####################################################################################################

# Function to Extract information / Data 
def fetch_data(keyword , start = 0 , rows = 2000 ):
    '''
    Extracting information from only those research papers which has been published after 1990 and before 2021
    '''
    # Making the query:
    encoded_query = urlencode({ "q": 'year:1990-2021' + " " + keyword,
                                "fl": "bibcode, id, eprint, author, title, year, doi, keyword, abstract, classic_factor, citation_count, read_count, reference_count, readers,metrics",
                                "rows": rows,
                                "start": start,
                                "sort": "classic_factor desc"
                              })
    try: 
      # Making an API request
      results = requests.get(f"https://api.adsabs.harvard.edu/v1/search/query?{encoded_query}",
                            headers={'Authorization': 'Bearer ' + api_token})

      # returns the dictionary of all the responses if API returns the request for the query
      if results.status_code == 200:
        return results.json()['response']['docs']
      
      # if request get denied
      else :
        return 'request denied'
      
    except:
       return 'request denied'
    

####################################################################################################
    
# Fetching all the responses for all the by querying for all Keywords:
all_data = []

for i , keyword in enumerate(query_keywords):
    
    # Fetching information by calling 'fetch_data' function 
    response  = fetch_data(str(keyword))

    if response != 'request denied':

        # appending the responsed in all_data list
        all_data.append(response)

    print(f'{i} : done')


#####################################################################################################
    
# Once, we have got all the necessary information in a list, we will now move ahead and create a Dataframe:
dicts = []

for array in  all_data:
    for i in array:
        dicts.append(i)

# Creating Pandas dataframe from the list of Dictionaries:
df = pd.DataFrame.from_dict(list(dicts))

# droping duplicate instances based on 'bibcode'
df = df.drop_duplicates(subset=['bibcode'])

# Adding one more column having the arXiv PDF downloadable link
df['PDF_link_url'] = df['bibcode'].apply(lambda x: f"https://ui.adsabs.harvard.edu/link_gateway/{x}/EPRINT_PDF")

# Saving Dataframe:
df.to_csv("D:\GITHUB REPOS\ML_Space_Scribe\Generated_Data\Dataframe_Papers.csv", index=False)

####################################################################################################