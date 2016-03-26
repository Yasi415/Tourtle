# -*- coding: utf-8 -*-

global player_name
global response

from time import *
from random import *
import os,sys
# sleep(2)

DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'
TOURDESC = 'tourdesc' 
MOREDESC = 'moredesc' 

SCREEN_WIDTH = 70

#########################################################

# worldRooms #

worldRooms = {
    'Alamo Square': { 
        DESC: 'Established in 1857, Alamo Square is one of San Francisco’s more notable parks.  Alamo means popular tree in Spanish, and during its early establishment, the lone cottonwood tree on Alamo hill marked a watering hole along the horseback trail from Mission Dolores to the Presidio.',
        EAST: 'Civic Center',
        WEST: 'Haight-Ashbury',
        GROUND: ['Painted Ladies', 'Dutch Charley Duane',]},
    'Alcatraz': { 
        DESC: "In 1775, Spanish explorer Juan Manuel de Ayala mapped and named Alcatraz Island, christening it La Isla de los Alcatraces, or Island or the Pelicans, due to its large population of sea birds. From 1934 to 1963 Alcatraz, or ‘The Rock’, was America’s foremost maximum-security prison and home for the nation’s more troublesome criminals.  Today, this fortress in the bay is one of San Francisco’s most prominent landmark and a favorite tourist attraction for all." '\n\n\n\n' "During its years as a military prison, the inmates at Alcatraz included Confederate sympathizers and citizens accused of treason during the American Civil War (1861-65). Alcatraz also housed a number of “rebellious” American Indians, including 19 Hopis from the Arizona Territory who were sent to the prison in 1895 following land disagreements with the federal government. The inmate population at Alcatraz continued to rise during the Spanish-American War (1898). During the early 20th century, inmate labor fueled the construction of a new cellhouse on Alcatraz, along with a hospital, mess hall and other prison buildings. According to the National Park Service, when this new complex was finished in 1912 it was the world’s largest reinforced concrete building.",
        SOUTH: 'Fisherman’s Wharf',
        GROUND: ['Scarface', 'Creepy Karpis', 'Birdman of Alcatraz']},
    'Castro': { 
        DESC: "The Castro was one of the first gay neighborhoods in the United States. The street was named for Jose Castro, a Californio leader of Mexican opposition to U.S. rule in California in the 19th century. After the U.S. military dishonorably discharged thousands of gay servicemen from the Pacific theater in San Francisco during World War II because of their sexuality, many settled in the bay area. In 1963 the Castro's first gay bar was opened called the 'Missouri Mule'" '\n\n\n\n' "The Castro's age as a gay mecca began during the late 1960s with the Summer of Love in the neighboring Haight-Ashbury district in 1967. The two neighborhoods are separated by a large mountain, topped by Buena Vista Park. The hippie and free love movements had fostered communal living and free society ideas including housing of large groups of people in hippie communes. Androgyny became popular with men even in full beards as gay hippie men began to move into the area. ",
        SOUTH: 'Dolores Park',
        EAST: 'Mission',
        WEST: 'Noe Valley',
        GROUND: ['Harvey Milk', 'Missouri Mule', 'GLBT History Museum']},
    'Chinatown': { 
        DESC: "San Francisco has always been a city of culture and community- there is perhaps no greater example of this than the Chinatown centered on Grant Avenue.  San Francisco’s Chinatown is the oldest and second largest Chinatown in North America.  While the city is host to four Chinatowns it is the original which was established in 1848 that has become beacon to both resident and tourist alike."  "Chinatown is practically a city in itself. Within the crowded streets live a population its own customs, languages, places of worship, social clubs, and identity." '\n\n\n\n' "Home to about 15,000 Chinese, Chinatown is the densest part of the densest city in California. It is a protected historic district where Chinese-style architecture prevails while still preserving the inexpensive housing and hundreds of small shops, restaurants and stores used by residents." "Chinatown became established in the mid 1800's when there was a large boon in Chinese immigration to the United States. The political and social conditions in China were volatile during that time, so the Chinese flooded to the United States. Most entered as laborers and went to work on the railroad system, while others were drawn to the gold being discovered in California and became miners."  "At the time, the bay came up as far as Montgomery Steet, so the location of Chinatown was the port of entry for most of those immigrants.",    
        NORTH: 'North Beach',
        SOUTH: 'Union Square',
        EAST: 'Financial District',
        WEST: 'Nob Hill',
        GROUND: ['The Gateway Arch', 'Tien Hau Temple',"Old Saint Mary's Cathedral", 'Golden Gate Cookie Factory']},
    'Civic Center': {
        DESC: "Civic Center is laid out around a large symmetrical square, the Civic Center Plaza. The plaza is flanked on the south by the area's first post-1906 building, the Civic Auditorium. Bordering the Civic Center Plaza to the west side is Civic Center's most impressive building: the palatial City Hall." '\n' "At the other, east end of the plaza is the beautiful Old Library Building (now the Asian Art Museum) and the 1995 San Francisco Main Public Library, designed by Pei Cobb Freed & Partners. Between the two library buildings is the Pioneer Monument, created by Frank Happersberger in 1894. One of the few structures that survived the 1906 earthquake, the monument depicts a statue of 'California' surrounded by several figures, including an Indian, gold diggers and a Spanish monk." '\n\n\n\n' "Its central location, vast open space, and the collection of government buildings have made and continue to make Civic Center the scene of massive political rallies. It has been the scene of massive anti-war protests and rallies since the Korean War. It was also the scene of major moments of the Gay Rights Movement. Activist Harvey Milk held rallies and gave speeches there. After his assassination on November 27, 1978, a massive candlelight vigil was held there. Later, it was the scene of the White Night Riots in response to the lenient sentencing of Dan White, Milk's assassin. Recently, Civic Center was the center point of the Gay Marriage activism, as Mayor Gavin Newsom married couples there.",
        NORTH: 'Tenderloin',
        EAST: 'SOMA',
        WEST: 'Alamo Square',
        GROUND: ['City Hall','Opera House','Asian Art Museum', 'Davies Symphony Hall','Bill Graham Civic Auditorium' ]},
    'Embarcadero': {
        DESC: "The Embarcadero is the eastern waterfront and roadway of the Port of San Francisco along the Bay. It derives its name from the Spanish verb embarcar, meaning 'to embark'; embarcadero itself means 'the place to embark'. It is fitting then, that this is where our journey begins." '\n\n\n\n' "Yerba Buena Cove occupied the space between the Embarcadero and Montgomery Street before a seawall and fill turned mud flats into dry land for what is now the Financial District",
        NORTH: 'Fisherman’s Wharf',
        SOUTH: 'AT&T Ballpark',
        WEST: 'Financial District',
        GROUND: ['Ferry Building','Bay Bridge', ]},
    'Dolores Park': {
        DESC: "Dolores Park is named for Miguel Hidalgo (El Grito de Dolores), the father of Mexian Independance, and the town of Dolores Hidalgo, Guanajuato, Mexico. As a priest in Dolores, it was Hidalgo's ringing of the town's church bell and public cry for freedom that sparked the Mexican revolution." '\n' "A statue of Hidalgo and replica of the church bell at Dolores Hidalgo were erected in the park to honor the father of the Mexican independence movement, and the town where it all began." '\n\n\n\n' "In recent years, the park has been frequently and incorrectly referred to as 'Mission Dolores Park'. The confusion probably stems from the assumptions of many romanticists, that based upon its former and current names of 'Mission' and 'Dolores' suggests it must've been named after Mission Dolores two blocks to the north. Logic, however, dictates that such monuments to the most pivotal moments in Mexican history would not sit in a public space bearing the name of an institution seen by many as a symbol of Spanish colonialism and oppression.",
        NORTH: 'Castro',
        EAST: 'Mission',
        GROUND: ['Mission High School']},
    'Fillmore': {
        DESC: "The Fillmore district was created in the 1880s to provide new space for the city to grow in an effort to address overcrowding. After the 1906 earthquake Fillmore Street, which had largely avoided heavy damage, temporarily became a major commercial center as the city's downtown rebuilt and began a period where the district where migrant groups from Jews to Japanese and then African-Americans predominated. Redevelopment programs in the 1960s led to displacement and loss of the district's jazz and cultural scene.",
        EAST: 'Japantown',
        GROUND: ['Fillmore Auditorium', 'Fillmore Street Jazz Festival','Harlem of the West',]},
    'Financial District': {
        DESC: "This neighborhood serves as the main central business district. It is home to the city's largest concentration of corporate headquarters, law firms, insurance companies, real estate firms, banks, and other financial institutions.  All six San Francisco Fortune 500 companies are located in the district.",
        NORTH: 'North Beach',
        EAST: 'Embarcadero',
        WEST: 'Chinatown',
        # TOURDESC: "Under Spanish and Mexican rule, the area was the site of a harbor named Yerba Buena Cove with a small civilian outpost named Yerba Buena that served to support the military population of the Presidio and the Mission Dolores. It was not until 1835 that the first settlers established themselves on the shore of Yerba Buena Cove, with the first town plan surveyed in 1839. Yerba Buena's potential as a seaport made it the eventual center for European and American settlement.",
        GROUND: ['555 California Street', 'Transamerica Pyramid', '101 California Street', '345 California Street', 'Wall Street of the West', 'Belden Alley']},
    "Fisherman’s Wharf": {
        DESC: "San Francisco's Fisherman's Wharf gets its name and neighborhood characteristics from the city's early days of the mid to later 1800s when Italian immigrant fishermen came to the city by the bay to take advantage of the influx of population due to the gold rush.",
        NORTH: 'Ghirardelli Square',
        SOUTH: 'Embarcadero',
        EAST: 'Alcatraz',
        WEST: 'North Beach',
        GROUND: ['Pier 39', 'Maritime National Historical Park', 'Sea Lions']},
    'Ghirardelli Square': {
        DESC: "Between 1852 and 1895, Ghirardelli’s Chocolate Factory was located at four different sites before the Ghirardelli Chocolate Company took over the Pioneer Woolen Mills on North Point Street—today’s site of the Ghirardelli Chocolate Manufactory & Soda Fountain and Ghirardelli Square." '\n' "Today, Ghirardelli delights visitors with its lively retail mix, while maintaining Ghirardelli’s tradition as a trendsetter for the rest of the world. In 1982 the owners applied for and were granted National Historic Register status, a move that ensured the preservation of Ghirardelli Square for future generations." '\n\n\n\n' "Ghirardelli Square, considered the first successful adaptive reuse project in the country, has a history that spans more than a century and covers three continents. This specialty retail and dining complex, housing shops and restaurants, was originally a chocolate factory established by Domenico “Domingo” Ghirardelli." '\n' "Born in 1817 in Rapallo, Italy, Ghirardelli served as a Genoa confectioner’s apprentice and at a young age developed a strong interest in the business. He left for Uruguay when he was 20 years old, then sailed around Cape Horn to Peru where he became a coffee and chocolate merchant.",
        SOUTH: "Fisherman’s Wharf",
        GROUND: ['Ghirardelli Chocolate']},
    'Golden Gate Park': {
        DESC: "In the 1860s, San Franciscans began to feel the need for a spacious public park similar to Central Park, which was then taking shape in New York City. Golden Gate Park was carved out of unpromising sand and shore dunes that were known as the Outside Lands, in an unincorporated area west of San Francisco’s then-current borders." '\n\n\n\n\n' "Following the disastrous events of the famous 1906 San Francisco earthquake, Golden Gate Park has also served as a safe haven for survivors and refugees of the devastating catastrophe.",
        EAST: 'Haight-Ashbury',
        WEST: 'Ocean Beach',
        GROUND: ['Music Concourse Area','De Young Museum','Academy of Sciences','Japanese Tea Garden','Makoto Hagiwara','Conservatory of Flowers']},
    'Haight-Ashbury': {
        DESC: "This neighborhood is known for its history of, and being the origin of hippie subculture. The streets are named after two early San Francisco leaders: Pioneer and exchange banker Henry Haight and Munro Ashbury, a member of the San Francisco Board of Supervisors from 1863 to 1870.  The name 'Upper Haight', used by locals, is in contrast to the Haight-Fillmore or Lower Haight district; the latter being lower in elevation and part of what was previously the principal African-American and Japanese neighborhoods in San Francisco's early years." '\n\n\n\n\n' "The Haight-Ashbury district is noted for its role as center of the 1960s hippie movement. The earlier bohemians of the beat movement had congregated around San Francisco’s North Beach neighborhood from the late 1950s. Many who could not find accommodation there turned to the quaint, relatively cheap and underpopulated Haight-Ashbury. The Summer of Love, the 1960s era as a whole, and much of modern American counterculture have been synonymous with the Haight-Ashbury ever since.",
        EAST: 'Alamo Square',
        WEST: 'Golden Gate Park',
        GROUND: ['The Red Victorian', 'Haight-Ashbury Street Fair','San Francisco Oracle']},
    'Japantown': {
        DESC: "San Francisco’s Japantown is the largest and oldest such enclave in the United States. Japanese immigrants began moving into the area following the 1906 earthquake. Japantown celebrates two major festivals every year: The Northern California Cherry Blossom Festival and the Nihonmachi Street Fair." '\n\n\n\n' "In February 1942, President Franklin D. Roosevelt signed Executive Order 9066, which forced all Japanese of birth or descent, including Japanese American citizens of the United States, to be relocated from the Pacific coast and interned. By 1943 many large sections of the neighborhood remained vacant due to the forced internment. The void was quickly filled by thousands of African Americans who had left the South to find wartime industrial jobs in California as part of the Great Migration.",
        EAST: 'Tenderloin',
        WEST: 'Fillmore',
        GROUND: ['Japan Center','Peace Pagoda']},
    'Marina': {
        DESC: "The Marina sits on the site of the 1915 Panama–Pacific International Exposition, staged after the 1906 San Francisco earthquake to celebrate the reemergence of the city." '\n\n\n\n' 'Much of the Marina is built on former landfill, and is susceptible to soil liquefaction during strong earthquakes. This phenomenon caused extensive damage to the entire neighborhood during the 1989 Loma Prieta earthquake.',
        SOUTH: 'Pacific Heights',
        GROUND: ['Panama–Pacific International Exposition', 'Palace of Fine Arts', 'Tower of Jewels', 'Fort Mason', 'Golden Gate Bridge']},
    'Mission': {
        DESC: 'In the 1980s and 1990s, the neighborhood received a higher influx of immigrants and refugees from Central America, the Middle East and South America fleeing civil wars and political instability at the time. These immigrants brought in many Central American banks and companies which would set up branches, offices, and regional headquarters on Mission Street.' '\n' "From the late 1990s through the 2010s, and especially during the dot-com boom, young urban professionals, moved into the area, initiating gentrification, raising rent and housing prices,  with a number of Latino American middle-class families as well as artists moving to the Outer Mission area, or out of the city entirely to the suburbs of East Bay and South Bay area. Despite rising rent and housing prices, many Mexican and Central American immigrants continue to reside in the Mission, although the neighborhood's high rents and home prices have led to the Latino population dropping by 20 percent over the last decade." '\n\n\n\n' "The Mission is often warmer and sunnier than other parts of San Francisco. The microclimates of San Francisco create a system by which each neighborhood can have different weather at any given time, although this phenomenon tends to be less pronounced during the winter months. The Mission's geographical location insulates it from the fog and wind from the west.",
        SOUTH: 'Dolores Park',
        EAST: 'Castro',
        WEST: 'SOMA',
        GROUND: ['Mission Dolores', 'Ohlone']},
    'Nob Hill': {
        DESC: "Nob Hill was settled in the rapid urbanization happening in the city in the late 19th century. Because of the views and its central position, it became an exclusive enclave of the rich and famous on the west coast who built large mansions in the neighborhood. This included prominent tycoons such as Leland Stanford, founder of Stanford University and other members of The Big Four. For this reason, its early citizens were known as nabobs, which was shortened to nob, giving the area its eventual name.'" '\n\n\n\n' "'The Big Four' was the name popularly given to the famous and influential businessmen, philanthropists and railroad tycoons who built the Central Pacific Railroad, which formed the western portion through the Sierra Nevada and the Rocky Mountains of the First Transcontinental Railroad in the United States, built from the mid-continent at the Mississippi River to the Pacific Ocean during the middle and late 1860s.",
        EAST: 'Chinatown',
        WEST: 'Tenderloin',
        GROUND: ['Fairmont Hotel', 'Grace Cathedral', 'Masonic Temple']},
    'Noe Valley': {
        DESC: "The neighborhood is named after José de Jesús Noé, the last Mexican mayor of Yerba Buena (present day San Francisco), who owned what is now Noe Valley as part of his Rancho San Miguel.  Noe Valley was primarily developed at the end of the 19th century and at the beginning of the 20th century, especially in the years just after the 1906 San Francisco earthquake. As a result, the neighborhood contains many examples of the 'classic' Victorian and Edwardian residential architecture for which San Francisco is famous. Today, Noe Valley has one of the highest concentration of row houses in San Francisco, with streets having three to four and sometimes as many as a dozen on the same side.",
        EAST: 'Castro',
        GROUND: []},
    'North Beach': {
        DESC: "The neighborhood is San Francisco's 'Little Italy', and has historically been home to a large Italian American population.  It was also the historic center of the beatnik subculture. North Beach is noted for being San Francisco's traditional home of youth in revolt, from the socialist days at the turn of the century and through to the Lost Generation of the 1920s." '\n\n\n\n' "Beatnik was a media stereotype prevalent throughout the 1950s to mid-1960s that displayed the more superficial aspects of the Beat Generation literary movement of the 1950s. The Beat Generation was a group of authors whose literature explored and influenced American culture in the post-World War II era. The bulk of their work was published and popularized throughout the 1950s. Central elements of Beat culture are rejection of standard narrative values, the spiritual quest, exploration of American and Eastern religions, rejection of materialism, explicit portrayals of the human condition, experimentation with psychedelic drugs, and sexual liberation and exploration.",
        SOUTH: 'Chinatown',
        EAST: "Fisherman’s Wharf",
        GROUND: ['Broadway']},
    'Ocean Beach': {
        DESC: "Due in part to its sometimes inhospitable weather (high winds, cold weather and fog), the area was largely undeveloped throughout most of San Francisco's early history, when it was known as part of the 'Outside Lands.'' Development finally came in the late-19th century: a steam railroad was in place by 1884 to bring people to the first amusement ride at the city’s oceanside, a 'Gravity Railroad' roller coaster, and to the Ocean Beach Pavilion for concerts and dancing. By 1890, trolley lines reached Ocean Beach: the Ferries and Cliff House Railroad, Park & Ocean Railroad, and Sutro Railroad that encouraged commercial amusement development as a trolley park. The Cliff House, which opened in 1863, and Sutro Baths, which opened in 1896, drew thousands of visitors.",
        SOUTH: 'SF Zoo',
        EAST: 'Golden Gate Park',
        GROUND: []},
    'Pacific Heights': {
        DESC: "Pacific Heights is an affluent neighborhood of San Francisco, California, US, which is known for the notable people who reside in the area. It is located in one of the most scenic and park-like settings in Northern California, offering panoramic views of the Golden Gate Bridge, the San Francisco Bay, the Palace of Fine Arts, Alcatraz and the Presidio. Several countries have consulates in Pacific Heights. They include Germany, Greece, Italy, Portugal, Russia, South Korea, and Vietnam." '\n\n\n\n' "The oldest building in Pacific Heights, located at 2475 Pacific Avenue, was built in 1853, though the majority of the neighborhood was built after the 1906 earthquake. The architecture of the neighborhood is varied; Victorian, Mission Revival, Edwardian, and Château styles are common.",
        NORTH: 'Marina',
        SOUTH: 'Japantown',
        WEST: 'Presidio',
        GROUND: []},
    'Presidio': {
        DESC: "The Presidio had been a fortified location since September 17, 1776, when New Spain established it to gain a foothold on Alta California and the San Francisco Bay. It passed to Mexico, which in turn passed it to the United States in 1848. As part of a 1989 military reduction program under the Base Realignment and Closure (BRAC) process, Congress voted to end the Presidio's status as an active military installation of the U.S. Army. On October 1, 1994, it was transferred to the National Park Service, ending 219 years of military use." '\n\n\n\n\n' "In 1975, the Presidio became the first stop for 1,300 refugees from Vietnam. The controversial Operation Baby Lift airlifted infants and toddlers orphaned by the Vietnam War to the US for adoption by American parents. The Army agreed to house and feed the children until permanent homes were arranged, converting the drill hall into a nursery.",
        EAST: 'Pacific Heights',
        GROUND: ['Crissy Field',]},
    'SF Zoo': {
        DESC: "This zoo is the birthplace of Koko the gorilla, and also the home of 'Elly, the black rhinoceros' said to be the oldest Rhino in Northern America. It housed more than 1000 individual animals representing over 250 species as of 2016. The first exhibits built in the 1930s cost US$3.5 million, which included Monkey Island, Lion House, Elephant House, a small mammal grotto, an aviary, and bear grottos. These spacious, moated enclosures were among the first bar-less exhibits in the country. ",
        NORTH: 'Ocean Beach',
        GROUND: [ ]},
    'SOMA': {
        DESC: "South of Market is a relatively large neighborhood in the city which is located just south of Market Street. SoMa is home to many of the city's museums, to the headquarters of several major software and Internet companies. Before being called South of Market this area was called 'South of the Slot', a reference to the cable cars that ran up and down Market along the slots through which they gripped cables. While the cable cars have long since disappeared from Market Street, some 'old timers' still refer to this area by this moniker." '\n\n\n\n' "The area has long been home to bars and nightclubs. During the 1980s and 1990s, some of the warehouses there served as the home to the city's budding underground rave, punk, and independent music scene. However, in recent decades, and mostly due to gentrification and rising rents, these establishments have begun to cater to an upscale and mainstream clientele that subsequently pushed out the underground musicians and their scene.",
        NORTH: 'AT&T Ballpark',
        SOUTH: 'Financial District',
        EAST: 'Mission',
        WEST: 'Civic Center',
        GROUND: ['Museum of Modern Art','Moscone Center','Museum of African Diaspora','Cartoon Art Museum']},
    'AT&T Ballpark': {
        DESC: "AT&T park is a base park and home to the San Francisco Giants. The park stands along the San Francisco Bay, a segment of which is named McCovery Cove, in honor of former Giants player Willie McCovey. When it opened on March 31, 2000, the ballpark was the first Major League ballpark built without public funds since the completion of Dodger Stadium in 1962." 'Back during the mascot craze of the early 1980s, the Giants made an "anti-mascot" called the Crazy Crab. It was ugly, and the fans were encouraged to hate it. Unfortunately, they took that job too seriously, and enough people attacked the Crab that the guy inside the suit needed major back surgery.',
        NORTH: 'Embarcadero',
        SOUTH: 'SOMA',
        GROUND: [ ]},
    'Tenderloin': {
        DESC: 'The Tenderloin took its name from an older neighborhood in New York with similar characteristics. There are several explanations of how that neighborhood was named. Some said it was a reference to the neighborhood as the "soft underbelly" (analogous to the cut of meat) of the city, with allusions to vice and corruption, especially graft. Another popular explanation, probably folklore, attributes the name to a New York City police captain, Alexander S. Williams, who was overheard saying that when he was assigned to another part of the city, he could only afford to eat chuck steak on the salary he was earning, but after he was transferred to this neighborhood he was making so much money on the side soliciting bribes that now he could eat tenderloin instead. Another version of that story says that the officers who worked in the Tenderloin received a "hazard pay" bonus for working in such a violent area, and thus were able to afford the good cut of meat. Yet another story, also likely apocryphal, is that the name is a reference to the "loins" of prostitutes.' '\n\n\n\n' "Prior to the emergence of The Castro as a major gay village, the center of the Tenderloin at Turk and Taylor and the Polk Gulch at the western side of the Tenderloin were two of the city's first gay neighborhoods and a few of these historic gay bars and clubs still exist. The Tenderloin has a long history as a center of alternate sexualities, including several historic confrontations with police. The legendary female impersonator Rae Bourbon, a performer during the Pansy Craze, was arrested in 1933 while his show 'Boys Will Be Girls' was being broadcast live on the radio from Tait's Cafe at 44 Ellis Street.",
        NORTH: 'Union Square',
        SOUTH: 'Civic Center',
        EAST: 'Nob Hill',
        WEST: 'Japantown',
        GROUND: ['Warfield Theater','Tessie Wall']},
    'Union Square': {
        DESC: "Welcome to the shopping central of San Francisco.  This one-block plaza and the area surrounding it is one of the largest collections of department stores, upscale boutiques, art galleries, theaters, and hotels in the United States.'\n\n\n'The area got its name because it was once used for rallies and support for the Union Army during the American Civil War, and it was built and named in 1850 by San Francisco’s first mayor, John Geary." '\n\n\n\n' 'Throughout the 1850s, the Square, like all public squares in San Francisco, remained undeveloped. It was used primarily for dumping, by occasional squatters, and for sand-lot baseball games. In fact, the term sand-lot baseball is thought to have originated in San Francisco from the use of Union Square as a sandy baseball field.',
        NORTH: 'Chinatown',
        SOUTH: 'Tenderloin',
        GROUND: ['Hearts in San Francisco', 'Westin St. Francis', 'Dewey Memorial', 'Cable Car', 'Maiden Lane']},
    }


##########################################################

# worldItems #

worldItems = {

#ALAMO SQUARE #

    'Painted Ladies':{ 
        GROUNDDESC: 'The Painted Ladies stand across Alamo Square.',
        SHORTDESC: 'the painted ladies',
        LONGDESC: 'Located on Steiner Street across from Alamo Square park it is sometimes known as “Postcard Row” or the "Seven Sisters".  These Queen Anne houses were built between 1892 and 1896 by developer Matthew Kavanaugh, who lived next door.  The Painted Ladies have been a media favorite for years- their imagery one of many synonymous with San Francisco itself.'  '\n\n\n\n' "Despite popular belief, the term 'Painted Ladies' actually refers to any Victorian or Edwardian- styles building painted with three or more colors to enhance its architectural and angular details. So while these houses were built from the mid 1800's to the early 1900's the moniker wasn't born until 1978.",
        TAKEABLE: False,
        DESCWORDS: ['Painted’,Ladies']},
    'Dutch Charley Duane': { 
        GROUNDDESC: 'A man by the name of Dutch Charlie Duane stands here.',
        SHORTDESC: 'dutch charley duane',
        LONGDESC: "Outlawed twice by the San Francisco Committee of Vigilance, first in 1851 and again in 1856, Charles P. 'Dutch Charley' Duane was one of the most colorful and controversial figures of the California Gold Rush. He played many roles in his life: politician, saloon keeper, fire chief, gambler, election rigger, gunfighter, bare knuckle boxer, and squatter. The common thread running through almost all of Charley Duane's violent behavior was his refusal to back down from a fight, and his violent retaliation of verbal insults and physical threats." '\n\n\n\n' 'He is a man some twenty-five or thirty years old, large, blond, a man of superb physique. He seems to be of more than ordinary intelligence and is generous even to the point of being prodigal. A born leader, ambitious, and a good mixer, he is usually to be found in one of the gambling houses. A notorious politician as well, he has a thousand votes at his command to be disposed of at elections by the simple plan of having his adherents vote three times in different sections of the city. Naturally he is flattered and bowed down to by all the political leaders. Although he has no visible means of support he lives regally on credit. . . . With his capriciousness, his viciousness, and his undeniable charm he would be a dangerous man in any walk of life -- whether in society, political life, or love-affairs.',
        TAKEABLE: False,
        DESCWORDS: ['Dutch','Charley','Duane']},

#===============================================================#

    # ALCATRAZ #

    'Scarface': { 
        GROUNDDESC: 'Al "Scarface" Capone',
        SHORTDESC: 'al capone',
        LONGDESC: 'Al "Scarface" Capone spent four-and-a-half years in Alcatraz during the 1930s - he was among the earliest federal prisoners there. Capone was sent to Alcatraz because his incarceration in Atlanta, Georgia, had allowed him to remain in contact with the outside world and continue to run his criminal operation in Chicago. He was also known to corrupt prison officers - all of that ended when he was sent to Alcatraz.' '\n\n\n\n' "Al Capone actually hated his famous nickname. In 1917, Capone's face was slashed during a fight at the Harvard Inn, after he insulted a female patron and her brother retaliated, leaving him with three scars on the left side of his face. Capone would attempt to shield the scarred side of his face in photographs, and tried to write them off as war wounds - although he never served in the military. After achieving prominence as a ganster, Capone was dubbed Scarface by the press.",
        TAKEABLE: False,
        DESCWORDS: ['scarface' ,'al', 'capone']},
    'Creepy Karpis': { 
        GROUNDDESC: 'Alvin "Creepy Karpis" Karpis',
        SHORTDESC: 'creepy karpis',
        LONGDESC: 'Nicknamed "Creepy" for his sinister smile, Alvin Karpis is known for being one of the three leaders of the Barker-Karpis gang in the 1930s. There were only four "public enemies" ever given the title of "Public Enemy #1" by the FBI and he was the only one to be taken alive. He also spent the longest time as a federal prisoner in Alcatraz, serving twenty-six years.' '\n\n\n' "His main job at Alcatraz was working in the bakery and was known as an obsessive reader. Karpis served his time quietly in Alcatraz, though he was far from a model prisoner due to frequently fighting with other inmates.",
        TAKEABLE: False,
        DESCWORDS: ['alvin', 'creepy', 'karpis']},
    'Birdman of Alcatraz': { 
        GROUNDDESC: 'Robert "The Birdman of Alcatraz" Stroud',
        SHORTDESC: 'the birdman of alcatraz',
        LONGDESC: "Robert Stroud was probably the most famous inmate to ever reside on Alcatraz. In 1909 he brutally murdered a bartender who had allegedly failed to pay a prostitute for whom Stroud was pimping in Alaska. After shooting the bartender to death, Stroud took the man's wallet to ensure that he and the prostitute would receive compensation for her services. On one occasion, Stroud viciously assaulted a hospital orderly who he insisted had reported him to the administration for attempting to procure narcotics through intimidation and threats. On other occasions he stabbed a fellow inmate and a guard." '\n\n\n\n' "Over the course of Stroud's thirty years of imprisonment at Leavenworth, he developed a keen interest in canaries, after finding an injured bird in the recreation yard. Stroud was initially allowed to breed birds and maintain a lab inside two adjoining segregation cells, since it was felt that this activity would provide for productive use of his time. As a result of this privilege, Stoud was able to author two books on canaries and their diseases, having raised nearly 300 birds in his cells, carefully studying their habits and physiology, and he even developed and marketed medicines for various bird ailments. Although it is widely debated whether the remedies he developed were effective, Stroud was able to make scientific observations that would later benefit research on the canary species. However, after several years of Stroud's informal research, prison officials discovered that some of the equipment he had requested was actually being used to construct a still to make an alcoholic brew.",
        TAKEABLE: False,
        DESCWORDS: ['robert', 'birdman', 'alcatraz','stroud']},
    

#===============================================================#
    
    # CASTRO #

    'Missouri Mule': { 
        GROUNDDESC: 'The Missouri Mule',
        SHORTDESC: 'missouri mule',
        LONGDESC: "The Missouri Mulee, the Castro's first gay bar, opened in 1963.  When the bar first opened, San Francisco’s gay population was then established in the Polk, having first flourished in North Beach and then the Tenderloin."  "When it eventually closed a decade later in 1973 to make way for another bar, over thirty gay businesses had opened in the neighborhood - making the Castro the epicenter of gay life in San Francisco and quite likely the world.",
        TAKEABLE: False,
        DESCWORDS: ['missouri', 'mule']},
    'Harvey Milk': { 
        GROUNDDESC: 'Harvey Milk',
        SHORTDESC: 'harvey milk',
        LONGDESC: 'Harvey Milk was an American politician who became the first openly gay person to be elected to public office in California, when he won a seat on the San Francisco Board of Supervisors. Politics and gay activism were not his early interests; he was not open about his homosexuality and did not participate in civic matters until around the age of 40, after his experiences in the counterculture of the 1960s.' 'Harvey Milk predicted his own assassination. Facing death threats every day, Milk recorded several versions of his will, "to be read in the event of my assassination." On one tape, he prophesied, "If a bullet should enter my brain, let that bullet destroy every closet door."',
        TAKEABLE: False,
        DESCWORDS: ['harvey', 'milk']},
    # 'Castro Theater': { 
    #     GROUNDDESC: 'The Castro Theater',
    #     SHORTDESC: 'castro theatre',
    #     LONGDESC: "The Castro Theatre was built in 1922 by pioneer San Francisco theatre entrepreneurs, the Nasser brothers, who started with a nickelodeon in 1908 in the Castro neighborhood. The designer was Timothy L. Pflueger who went on to become a famous Bay Area architect. In 1977, the Castro was designated City of San Francisco registered landmark number 100. It is one of the few remaining movie palaces in the nation from the 1920s that is still in operation." '\n\n\n\n\n\n' "Timothy Pflueger chose an exterior design reminiscent of a Mexican cathedral. The large windows, the shape of the roof line of the front wall of the building and the plaster wall decorations all combine to convey a look of grandeur in keeping with the large scale of many theatres built in the 1920s. The marquee and the vertical neon sign are additions from the late 1930s, but the glazed tile street foyer, ornate tent-like box office and the wooden doors are all from the early 1920s." '\n' "The Castro's interior is very diverse. One can sense Spanish, Oriental and Italian influences. The auditorium seats over 1400 in a fantasy setting that is both lavish and intimate. Both side walls of the auditorium are covered with classic motif murals which were created in a wet plaster process called scrafitto. This type of wall decoration is rare.",
    #     TAKEABLE: False,
    #     DESCWORDS: ['castro','theater']},
    'GLBT History Museum': { 
        GROUNDDESC: 'GLBT History Museum',
        SHORTDESC: 'glbt history museum',
        LONGDESC: "Often referred to as San Francisco’s 'queer Smithsonian', the GLBT Historical Society houses one of the world's largest collections of lesbian, gay, bisexual and transgender historical material." 'The GLBT History Museum is the first full-scale, stand-alone museum of its kind in the United States. The archives contain papers, photos, art and artifacts, ephemera and audiovisual recordings spanning a century of queer history.',
        TAKEABLE: False,
        DESCWORDS: ['glbt', 'history','museum']},


#===============================================================#

    # CHINATOWN #
    
    'The Gateway Arch': { 
        GROUNDDESC: 'The Gateway Arch',
        SHORTDESC: 'the gateway arch',
        LONGDESC: 'The Gateway Arch, also known as Dragon Gate, marks the entry to Chinatown.  Dedicated in 1970, this archway is the only authentic Chinatown Gate in North America (it uses old historic materials donated by The Republic of China in 1969).  The gate is embellished with sculptures of dragons and fish and is bordered by two large lion statues or fou lions, which are meant to hinder evil-spirits. Like similar ceremonial gates in Chinese villages this gate contains three passageways: the largest for dignitaries and the two smaller ones for the common people.',
        TAKEABLE: False,
        DESCWORDS: ['gateway', 'arch', 'dragon']},
    'Tien Hau Temple': {
        GROUNDDESC: 'The Tien Hau Temple',
        SHORTDESC: 'tien hau temple',
        LONGDESC: "The oldest Taoist/Buddhist temple in the United States. It was founded in 1852 and now in a 1911 building, it was dedicated in honor of the Goddess of Heaven and Sea - Tien Hau. If you want to see inside the place of worship you will need to walk up four floors. From the balcony outside you also get a considerable view of Chinatown.",
        TAKEABLE: False,
        DESCWORDS: ['tien', 'hau','temple']},
    "Old Saint Mary's Cathedral": {
        GROUNDDESC: "Old Saint Mary's Cathedral",
        SHORTDESC: "old saint mary's cathedral",
        LONGDESC: "Built in 1854 and rebuilt in 1909 after the earthquake fire. This beautiful Catholic Cathedral was the first Asian church in North America.",
        TAKEABLE: False,
        DESCWORDS: ["old", "saint", "mary's", "cathedral"]},
    'Golden Gate Cookie Factory': {
        GROUNDDESC: 'Golden Gate Cookie Factory',
        SHORTDESC: 'golden gate cookie factory',
        LONGDESC: 'Located down Ross Alley, this factory has been supplying fortune cookies to Chinatown and around the world since 1962',
        TAKEABLE: False,
        DESCWORDS: ['golden', 'gate', 'cookie', 'factory']},
    
#===============================================================#
    
    # CIVIC CENTER #

    'City Hall': { 
        GROUNDDESC: 'San Francisco City Hall',
        SHORTDESC: 'city hall',
        LONGDESC: "San Francisco City Hall is the seat of government for the City and County of San Francisco, California. Re-opened in 1915 in its open space area in the city's Civic Center, it is a Beaux-Arts monument to the City Beautiful movement that epitomized the high-minded American Renaissance of the 1880s to 1917. The structure's dome is taller than that of the United States Capitol by 42 feet."  "The principal architect was Arthur Brown, Jr., of Bakewell & Brown, whose attention to the finishing details extended to the doorknobs and the typeface to be used in signage. Brown's blueprints of the building are preserved at the Bancroft Library at the University of California, Berkeley. Brown also designed the San Francisco War Memorial Opera House, Veterans Building, Temple Emanuel, Coit Tower and the Federal office building at 50 United Nations Plaza.",
        TAKEABLE: False,
        DESCWORDS: ['city', 'hall']},
    'Opera House': { 
        GROUNDDESC: 'Opera House',
        SHORTDESC: 'opera house',
        LONGDESC: "It was founded in 1923 by Gaetano Merola and is the second largest opera company in North America. The Opening Night Gala of San Francisco Opera is considered to be one of the most prominent events in the musical and social life of San Francisco."  "The first performance given by San Francisco Opera was La bohème, with Queena Mario and Giovanni Martinelli, on 26 September 1923, in the city's Civic Auditorium and conducted by Merola, whose involvement in opera in the San Francisco Bay Area had been ongoing since his first visit in 1906.",
        TAKEABLE: False,
        DESCWORDS: ['opera','house']},
    'Asian Art Museum': { 
        GROUNDDESC: 'Asian Art Museum',
        SHORTDESC: 'asian art museum',
        LONGDESC: "The Asian Art Museum of San Francisco is one of the most comprehensive Asian art collections in the world, with over 18,000 works of art in its permanent collection, some as old as 6,000 years old." '\n\n\n\n\n\n\n' "The museum owes its origin to a donation to the city of San Francisco by Chicago millionaire Avery Brundage, who was a major collector of Asian art. The Society for Asian Art, incorporated in 1958, was the group that formed specifically to gain Avery Brundage's collection. The museum opened in 1966 as a wing of the M. H. de Young Memorial Museum in Golden Gate Park. Brundage continued to make donations to the museum, including the bequest of all his remaining personal collection of Asian art on his death in 1975. In total, Brundage donated more than 7,700 Asian art objects to San Francisco.",
        TAKEABLE: False,
        DESCWORDS: ['asian','art','museum']},
    'Davies Symphony Hall': { 
        GROUNDDESC: 'Davies Symphony Hall',
        SHORTDESC: 'davies symphony hall',
        LONGDESC: "The San Francisco Symphony was founded in 1911, as part of the revitalization of the city after the 1906 earthquake. The Symphony finally got its own home when the Louise M. Davies Symphony Hall opened in 1980. Davies Hall took two years to build and cost $27.5 million dollars. Davies Symphony Hall is named after Louise M. Davies, who donated $5 million for the building and an additional $3 million to attract guest conductors. Davies, who was the widow of an oil millionaire, died in 1998." '\n\n\n\n' "Architects created acoustic isolation of the performance space by constructing a building within a building. The outer building uses one inch thick structural glass as a curtain wall, with the next structural wall forming the back wall of the lobby spaces. Passing through a door leads to a hallway, bounded on one side by the lobby wall and on the other by the structural wall of the inner building. This continuous hallway acts as an acoustical isolator and is surfaced with sound absorbing material.",
        TAKEABLE: False,
        DESCWORDS: ['davies','symphony','hall']},
    'San Francisco Ballet': { 
        GROUNDDESC: 'San Francisco Ballet',
        SHORTDESC: 'san francisco ballet',
        LONGDESC: "San Francisco ballet was the first professional ballet in the United States. It is among the world's leading dance companies , presenting over 100 performances annually, with a repertoire that spans both classical and contemporary ballet."  "In 1938, the company's first major production was Coppélia, choreographed by Willam Christensen.[8] In 1940, it staged Swan Lake, the first time that the ballet was produced in its entirety by an American company. On Christmas Eve 1944, the company staged Nutcracker—the first complete production of Tchaikovsky's most popular piece ever danced in the United States.",
        TAKEABLE: False,
        DESCWORDS: ['san', 'francisco', 'ballet']},
    'Bill Graham Civic Auditorium': { 
        GROUNDDESC: 'The Bill Graham Civic Auditorium',
        SHORTDESC: 'bill graham civic auditorium',
        LONGDESC: 'The Bill Graham Civic Auditorium is a multi-purpose arena, currently named after promoter Bill Graham - who was responsible for bringing so much great live music to the arena and to the city of San Francisco. The arena holds 7,000 people and was built in 1915 as part of the Panama-Pacific International Exposition.' '\n\n\n\n' "Bill Graham was born in 1931 in Berlin, Germany. Escaping the rise of the Nazis, Grahamwas raised in New York City. He began his promotion career in the 1960s in San Francisco, and was a large part of the counterculture of the era, working with such figures as Lawrence Ferlinghetti and Allen Ginsberg, and bands like the Grateful Dead and the Who.",
        TAKEABLE: False,
        DESCWORDS: ['bill','graham','civic','auditorium']},

#===============================================================#
    
    # EMBARCADERO #

    'Ferry Building': { 
        GROUNDDESC: 'The Ferry Building',
        SHORTDESC: 'ferry building',
        LONGDESC: 'The San Francisco Ferry Building is a terminal for ferries that travel across the San Francisco Bay. On top of the building is a 245-foot tall clock tower, which can be seen from Markey Street. Designed in 1892 by American architect A. Page Brown in the Beaux Arts style, the ferry building was completed in 1898. At its opening, it was the largest project undertaken in the city up to that time.'"Brown designed the clock tower after the 12th-century Giralda bell tower in Seville, Spain, and the entire length of the building on both frontages is based on an arched arcade. During daylight, on every full and half-hour, the clock bell chimes portions of the Westminster Quarters.",
        TAKEABLE: False,
        DESCWORDS: ['ferry','building']},
    'Bay Bridge': { 
        GROUNDDESC: 'The Bay Bridge',
        SHORTDESC: 'bay bridge',
        LONGDESC: 'The San Francisco-Oakland Bay Bridge is a complex of bridges spanning San Francisco Bay. As part of Interstate 80 and the direct road between San Francisco and Oakland, it carries about 240,000 vehicles a day.' "The San Francisco Bay Bridge was once the longest high-level, steel bridge in the world. The deepest pier extends 242 feet below the water's surface and contains more concrete than the Empire State Building.",
        TAKEABLE: False,
        DESCWORDS: ['bay','bridge']},

#===============================================================#
    
    # DOLORES PARK #

    'Mission High School': { 
        GROUNDDESC: 'Mission High School',
        SHORTDESC: 'mission high school',
        LONGDESC: 'Mission is the oldest high school on its original site in San Francisco. The school is two blocks from Mission Dolores, from which it gets its name. The current student body is diverse, with Latino and African American students constituting the two largest ethnic groups, although neither group makes up a majority of the student body.' '\n\n\n' "Mission High school is the first public school to have a LGBTQ/ Drag show assembly. This event has helped spread awareness and acceptance around LGBT issues and other forces",
        TAKEABLE: False,
        DESCWORDS: ['mission','high','school']},

#===============================================================#
    
    # FILMORE #

    'Fillmore Auditorium': { 
        GROUNDDESC: "Fillmore Auditorium",
        SHORTDESC: 'fillmore auditorium',
        LONGDESC: "The Fillmore is a historic music venue, made famous by Bill Graham. It is situated in the historical center of the Western Addition neighborhood, on the edge of the Fillmore District and Upper Fillmore (lately known as Lower Pacific Heights). From the 1930s through the '60s, before redevelopment, this location was considered the heart of the San Francisco Fillmore District." '\n\n\n\n' "In the mid-1960s, the Fillmore Auditorium became the focal point for psychedelic music and counterculture in general, with such acts as The Grateful Dead, The Steve Miller Band, Jefferson Airplane, The Doors, Jimi Hendrix Experience, The Byrds, Santana, Frank Zappa's The Mothers of Invention, Creedence Clearwater Revival, and British acts The Who, Cream, Led Zeppelin, and Pink Floyd all performing at the venue. Besides rock, Graham also featured non-rock acts such as Lenny Bruce, Miles Davis, Rahsaan Roland Kirk, Charles Lloyd, Aretha Franklin, and Otis Redding as well as poetry readings. The Grateful Dead were regulars at The Fillmore, having played a total of 51 concerts from 1965 through 1969.",
        TAKEABLE: False,
        DESCWORDS: ['fillmore','auditorium']},
    'Fillmore Street Jazz Festival': { 
        GROUNDDESC: 'Fillmore Street Jazz Festival',
        SHORTDESC: 'fillmore street jazz festival',
        LONGDESC: "Blending art and soul in one of the country's most unique neighborhoods, the Fillmore Jazz Festival is the largest free Jazz festival on the West Coast, drawing over 100,000 visitors over the Independence Day weekend. From sunup to sundown, visitors can groove to the sounds of live music from multiple stages, browse the offerings of over 12 blocks of fine art and crafts and enjoy gourmet food and beverages. Asian to Cajun, paintings to pottery, old favorites and new directions, the Fillmore Jazz Festival is not to be missed."  "In the 1980's, a renaissance gave rise to the next generation of the Fillmore District. Merchant associations helped launch the first Fillmore Jazz Festival in 1985, giving new expression to the storied neighborhood. In 1999, the festival came home to the newly revitalized Jazz Preservation District.",
        TAKEABLE: False,
        DESCWORDS: ['fillmore','street','jazz''festival']},
    'Harlem of the West': { 
        GROUNDDESC:  'Harlem of the West',
        SHORTDESC: 'harlem of the west',
        LONGDESC: 'The Fillmore earned this name during the 1940s and 1950s as it became the national center for jazz. This "Harlem of the West" had attracted many leading jazz luminaries including Louis Armstrong, John Coltrane, Ella Fitzgerald, Billie Holiday and the "Bird" (Charlie Parker).'  "A Fillmore club at the time, Jimbo's Bop City, nationally known for its all-night jam sessions is reported to be the only venue to host Parker and Armstrong together at the same time.",
        TAKEABLE: False,
        DESCWORDS: ['harlem', 'of', 'the', 'west']},

#===============================================================#

    # FINANCIAL DISTRICT

    '555 California Street': { 
        GROUNDDESC: '555 California Street',
        SHORTDESC: '555 california street',
        LONGDESC: '555 California Street was meant to display the wealth, power, and importance of Bank of America. The skyscraper has thousands of bay windows thanks to its unique design, meant to improve the rental value and to symbolize the bay windows common in San Francisco residential real estate. The irregular cutout areas near the top of the building were designed to suggest the Sierra mountains.'  "The Bank of America Building became immediately popular with the film industry. In 1971, it was featured in the movie Dirty Harry in the beginning sequences; the killer shoots his victim from the building's roof. A few years later, the building served as the infamous Glass Tower in the disaster movie hit, The Towering Inferno.",
        TAKEABLE: False,
        DESCWORDS: ['555', 'california', 'street']},

    'Transamerica Pyramid': { 
        GROUNDDESC: 'Transamerica Pyramid',
        SHORTDESC: 'transamerica pyramid',
        LONGDESC: "The Transamerica Pyramid is the tallest skyscraper in the San Francisco skyline. The building no longer houses the headquarters of the Transamerica Corporation, which moved their U.S. headquarters to Baltimore, Maryland, but it is still associated with the company and is depicted in the company's logo. Designed by architect William Pereira and built by Hathaway Dinwiddie Construction Company, at 853 ft, on completion in 1972 it was the eighth tallest building in the world."  "The building is covered in crushed white quartz, giving it its pure white color." '\n' "The foundation of the building is 9 feet thick, which took 72 hours of continuous concrete pouring. Several thousand dollars in spare change were thrown into the pit during the pouring for good luck.",
        TAKEABLE: False,
        DESCWORDS: ['transamerica', 'pyramid']},

    '101 California Street': { 
        GROUNDDESC: '101 California Street',
        SHORTDESC: '101 california street',
        LONGDESC: 'This cylindrical tower features a seven story, glass enclosed lobby and a granite plaze with flower beds and a fountain.' "The building is the site of what has become known as the 101 California Street shootings, a mass murder which occurred there in 1993. On July 1, Gian Luigi Ferri, a disgruntled client of the law firm Pettit & Martin, entered their offices on the 34th floor and killed eight people and wounded six before killing himself. The event was a catalyst in the passage of the Violent Crime Control and Law Enforcement Act of 1994, a drive initiated by California Senator Dianne Feinstein to ban assault weapons.[6] A terraced garden in the plaza in front of the building is now dedicated to the victims.",
        TAKEABLE: False,
        DESCWORDS: ['101', 'california', 'street']},

    '345 California Street': { 
        GROUNDDESC: '345 California Street',
        SHORTDESC: '345 california street',
        LONGDESC: 'Completed in 1986, this 695 feet tower is the third-tallest in the city. Initally planned as condominiums, the top eleven floors of the building are the Loews Regency San Francisco.'  "While the towers's address is 345 California street, the Loews Regency San Francisco in the tower is addressed as 222 Sansome Street.  The twin towers of hotel were situated at 45-degree angles relative to teh rest of the building with several glass skybridges that offer views of the San Francisco Bay Area.",
        TAKEABLE: False,
        DESCWORDS: ['345','california','street']},

    'Wall Street of the West': { 
        GROUNDDESC: 'Wall Street of the West',
        SHORTDESC: 'wall street of the west',
        LONGDESC: 'The Montgomery Street in San Francisco started its transformation from the street with wood shacks, warehouses and retail stores in the 1850s. By the 1870s, more notable buildings were constructed to replace the old wood shacks and the mud flats. The street continued to develop from that point with financial services companies located in that area.' "The Montgomery Street has been known as 'Wall Street of the West' to date. The Financial District has been expanded to cover the triangular area east of Grant Avenue, south of Washington Street, and west of the Embarcadero. In 2012, when the Occupy movement had a protest at the San Francisco's Financial District as a continuation of Occupy San Francisco, the protesters went through the financial district under the banner 'Occupy Wall Street West'",
        TAKEABLE: False,
        DESCWORDS: ['wall','street','of','the','west']},

    'Belden Alley': { 
        GROUNDDESC: 'Belden Alley',
        SHORTDESC: 'belden alley',
        LONGDESC: "Belden Alley is a narrow lane in the Financial District that serves as the hub of the city's small French American community. Sometimes, though not universally, referred to as San Francisco’s French Quarter for its historic ties to early French immigrants, and its popular contemporary French restaurants and institutions," 'The area was home to San Francisco’s first French settlers.  Approximately 3,000, sponsored by the French government, arrived near the end of the Gold Rush in 1851. According to historians, the French shared Dupont Street (now Grant Avenue) with early Chinese settlers during the early days of Chinatown, and were more sympathetic than others to their concerns.',
        TAKEABLE: False,
        DESCWORDS: ['belden', 'alley']},

#===============================================================#
    
    # FISHERMAN'S WHARF #

    'Pier 39': { 
        GROUNDDESC: 'Pier 39',
        SHORTDESC: 'pier 39',
        LONGDESC: "Pier 39 is a shopping center and popular tourist attraction built on a pier in San Francisco, California. At Pier 39, there are shops, restaurants, a video arcade, street performances, the Aquarium of the Bay, virtual 3D rides, and views of California sea lions hauled out on docks on Pier 39's marina." "October 4, 1978 – PIER 39 opens on schedule to fanfare in San Francisco. Originally, PIER 39 had 50 stores, a diving pool and street performers. The PIER also had 23 restaurants. Some of the original restaurants—Pier Market Seafood Restaurant, Neptune’s Bar & Grill, Eagle Cafe and Swiss Louis Italian & Seafood Restaurant—are still open today.",
        TAKEABLE: False,
        DESCWORDS: ['pier','39']},
    'Maritime National Historical Park': { 
        GROUNDDESC: 'Maritime National Historical Park',
        SHORTDESC: 'maritime national historic park',
        LONGDESC: "The park includes a fleet of historic vessels, a visitor center, a maritime museum, and a library/research facility. The Maritime Research Center focuses on sail and steam on the West Coast of the United States and the Pacific Basin from 1520 to the present, including library collections and the archived records of many ship builders and ship owners. It includes 1,500 feet of documents, including 120,000 vessel and shipyard architectural drawings, and about 5,000 charts and maps." '\n\n\n\n\n\n\n\n\n\n' "The historic fleet of the San Francisco Maritime National Historical Park is moored at the park's Hyde Street Pier. The fleet consists of the following major vessels: " "Balclutha: an 1886 built square rigged sailing ship -- 'C.A. Thayer: an 1895 built schooner -- 'Eureka: an 1980 built steam ferryboat -- Alma: an 1891 built scow schooner -- Hercules: a 1907 built steam tug -- Eppleton Hall: a 1914 built paddlewheel tug.",
        TAKEABLE: False,
        DESCWORDS: ['maritime', 'national', 'historic', 'park']},
    'Sea Lions': { 
        GROUNDDESC: 'Sea Lions',
        SHORTDESC: 'sea lions',
        LONGDESC: "California sea lions have always frequented the San Francisco Bay, especially during the winter months when herring spawn in the bay. The Marine Mammal Center’s biologists believe that the sea lions have chosen to haul out at PIER 39’s K-Dock because there’s plenty of food nearby in the bay and ocean, their natural predators (white sharks and orcas) do not typically feed in the bay and there is plenty of space. As the tide goes in and out, the floating docks move up and down on the water, so the sea lions just keep sleeping rather then having to scramble up and down rocks with the tide." "From late summer to late spring, there are typically hundreds of sea lions hauled out at K-Dock. In June and July, most of the sea lions head south to breeding grounds on the Channel Islands, although a handful to a few dozen have remained throughout the summer in recent years. In late July, non-breeding sub-adult males and juvenile females begin to migrate north again. Other breeding males travel north later, and some males migrate as far north as Alaska and British Columbia, Canada.",
        TAKEABLE: False,
        DESCWORDS: ['sea','lions']},


#===============================================================#
    
    # GHIRARDELLI SQUARE #

    'Ghirardelli Chocolate': { 
        GROUNDDESC: 'Ghirardelli Chocolate',
        SHORTDESC: 'ghirardelli chocolate',
        LONGDESC: 'Ghirardelli is one of the few companies in America that controls the entire chocolate-making process from bean to bar.' "The heart of the cocoa bean, called the nib, is roasted rather than the whole bean. This results in a more consistent flavor compared to other brands.",
        TAKEABLE: False,
        DESCWORDS: ['ghirardelli','chocolate']},

#===============================================================#
    
    # GOLDEN GATE PARK #

    'Music Concourse Area': { 
        GROUNDDESC: 'Music Concourse Area',
        SHORTDESC: 'music concourse area',
        LONGDESC: 'The Music Concourse is a sunken, oval-shaped open-air plaza originally excavated for the California Midwinter International Exposition of 1894. Its focal point is the Spreckels Temple of Music, also called the "Bandshell," where numerous music performances have been staged.' "The structure was built in 1899, in advance of the Music Concourse's completion in 1900. It was severely damaged in the 1906 and 1989 earthquakes, has repeatedly undergone extensive renovation, and has served as a stage for numerous performers over the years ranging from Luciano Pavarotti to the Grateful Dead.",
        TAKEABLE: False,
        DESCWORDS: ['music','concourse','area']},
    'De Young Museum': { 
        GROUNDDESC: 'De Young Museum',
        SHORTDESC: 'de young museum',
        LONGDESC: "Named for M. H. de Young, the San Francisco newspaper magnate, the De Young Museum is a fine arts museum that was opened in January 1921. Its original building, the Fine Arts Building, was part of the 1894 Midwinter Exposition, of which Mr. de Young was the director. By 1916, the Fine Arts Building’s collection had grown to 1,000,000 items, and a more suitable museum was necessary." "The new building is mostly constructed of copper, and its unique design was created with the idea that the building would be enhanced not only by sunlight but also by San Francisco’s constant fog.",
        TAKEABLE: False,
        DESCWORDS: ['de','young','museum']},
    'Academy of Sciences': { 
        GROUNDDESC: 'Academy of Sciences',
        SHORTDESC: 'academy of sciences',
        LONGDESC: "The California Academy of Sciences was founded in 1853, just three years after California was made a state, making it the oldest scientific institution in the western United States. Evolutionist Charles Darwin corresponded on the initial organization of the early institution."  "The museum is currently one of the ten largest natural history museums in the world and holds 18 million scientific specimens between the research institute and public exhibits.",
        TAKEABLE: False,
        DESCWORDS: ['academy', 'of', 'sciences']},
    'Japanese Tea Garden': { 
        GROUNDDESC: 'Japanese Tea Garden',
        SHORTDESC: 'japanese tea garden',
        LONGDESC: "The Japanese Tea Garden is the oldest public Japanese garden in the United States. George Turner Marsh, an Australian immigrant, originally created the garden for the 1894 Midwinter Exposition. The landscaping and design was maintained by Makoto Hagiwara until 1942 and includes still-standing features such as the Drum Bridge and the Tea House." 'The Japanese Tea Garden serves as a spot of tranquility in the middle of the various activities that take place at the Golden Gate Park and provides visitors "a place in which it is possible to be at one with nature, its rhythms, and changing beauties."',
        TAKEABLE: False,
        DESCWORDS: ['japanese','tea','garden']},
    'Makoto Hagiwara': { 
        GROUNDDESC: 'Makoto Hagiwara',
        SHORTDESC: 'makoto hagiwara',
        LONGDESC: "Makoto Hagiwara was a Japanese American immigrant and landscape designer responisble for the creation and maintenance of the Japanese Tea Garden at Golden Gate Park from 1895 until his death in 1925. He is often credited with the invention of the fortune cookie in California." "David Jung, founder of the Hong Kong Noodle Company in Los Angeles, has made a competing claim that he invented the cookie in 1918. San Francisco's Court of Historical Review attempted to settle the dispute in 1983. During the proceedings, a fortune cookie was introduced as a key piece of evidence with a message reading, 'S.F. Judge who rules for L.A. Not Very Smart Cookie'. A federal judge of the Court of Historical Review determined that the cookie originated with Hagiwara and the court ruled in favor of San Francisco. Subsequently, the city of Los Angeles condemned the decision.",
        TAKEABLE: False,
        DESCWORDS: ['makoto', 'hagiwara']},
    'Conservatory of Flowers': { 
        GROUNDDESC: 'Conservatory of Flowers',
        SHORTDESC: 'conservatory of flowers',
        LONGDESC: "The Conservatory of Flowers opened in 1879, standing today as the oldest building in Golden Gate Park. The Conservatory of Flowers is one of the world's largest conservatories, as well as one of few large Victorian greenhouses in the United States."  "Built of traditional wood and glass panes, the Conservatory stands at 12,000 square feet and houses 1,700 species of tropical, rare and aquatic plants.",
        TAKEABLE: False,
        DESCWORDS: ['conservatory','of','flowers']},


#==============================================================#
# HAIGHT-ASHBURY #

    'The Red Victorian': { 
        GROUNDDESC: 'The Red Victorian',
        SHORTDESC: 'the red victorian',
        LONGDESC: "The Red Victorian is a Bed and Breakfast/community space constructed in 1904 in San Francisco's Haight Ashbury District. The building has seen many names and eras - it was originally named the Jefferson Hotel, which is rumored to have been a brothel. In 1967, it became the Jeffrey Haight during the Summer of Love." 'In 1977, Dr. Sami Sunchild, environmental artist and social activist, acquired the building, painted the Victorian facade red and named it the "Red Victorian". She intended the business to embody the ideas of the area, including the peace movement, the environmental movement, the cooperative community movement, and the social justice movement.',
        TAKEABLE: False,
        DESCWORDS: ['the','red','victorian']},
    'Haight-Ashbury Street Fair': { 
        GROUNDDESC: 'Haight-Ashbury Street Fair',
        SHORTDESC: 'haight-ashbury street fair',
        LONGDESC: "The Haight-Ashbury Street Fair is a non-profit organization dedicated to celebrating the cultural history and diversity of one of San Francisco's most internationally celebrated neighborhoods. Since 1978, HASF has produced the annual street fair that features arts and crafts, food booths, three musical stages, a Family Area and more. It also serves as a means for community groups and mercantile vendors to interact with the public and expand their base." "The street fair was developed in response to the re-birth of the economic and residential spirit of the community in the mid-1970's. With the assistance of the late San Francisco Supervisor Harvey Milk, the first District 5 and openly Gay supervisor, a group of neighborhood merchants, activists and residents developed this organization with the idea of sponsoring a day long community celebration. The first Haight-Ashbury Street Fair was held on April 30, 1978, to the fanfare of the neighborhood and the City.",
        TAKEABLE: False,
        DESCWORDS: ['haight-ashbury', 'haight', 'ashbury','street']},


#==============================================================#    
    # JAPANTOWN #

    'Japan Center': { 
        GROUNDDESC: 'Japan Center',
        SHORTDESC: 'japan center',
        LONGDESC: 'The Japan Center is a shopping center in the Japantown neighborhood of San Francisco, California. It opened in March 1968 and was originally called the Japanese Cultural and Trade Center.' 'The architecture of the site, created by Minoru Yamasaki, has been described as "Brutalist slabwork. Brutalist architecture are typically massive in character, fortress-like, with a predominance of exposed concrete construction, or in the case of the "brick brutalists," ruggedly combine detailed brickwork and concrete. In its ruggedness and lack of concern to look comfortable or easy, Brutalism can be seen as a reaction by a younger generation to the lightness, optimism, and frivolity of some 1930s and 1940s architecture.',
        TAKEABLE: False,
        DESCWORDS: ['japan','center']},
    'Peace Pagoda': { 
        GROUNDDESC: 'Peace Pagoda',
        SHORTDESC: 'peace pagoda',
        LONGDESC: "The Peace Pagoda is a five-tiered concrete stupa in Nihonmachi (Japantown). It is part of the Japan Center complex which opened in 1968. It was designed by Japanese architect Yoshiro Taniguchi and presented to San Francisco by the people of Osaka, Japan. This stupa is not associated with Nipponzan-Myōhōji." "A Peace Pagoda is a Buddhist stupa; a monument to inspire peace, designed to provide a focus for people of all races and creeds, and to help unite them in their search for world peace. Most (though not all) peace pagodas built since World War II have been built under the guidance of Nichidatsu Fujii (1885–1985), a Buddhist monk from Japan and founder of the Nipponzan-Myōhōji Buddhist Order.",
        TAKEABLE: False,
        DESCWORDS: ['peace','pagoda']},

#===============================================================#
    
    # MARINA #

    'Panama-Pacific International Exposition': { 
        GROUNDDESC: 'Panama-Pacific International Exposition',
        SHORTDESC: 'panama-pacific international exposition',
        LONGDESC: "The Panama–Pacific International Exposition was a world's fair held in San Francisco, in the United States, between February 20 and December 4 in 1915. Its ostensible purpose was to celebrate the completion of the Panama Canal, but it was widely seen in the city as an opportunity to showcase its recovery from the 1906 earthquake." "Among the exhibits at the Exposition was the C. P. Huntington, the first steam locomotive purchased by Southern Pacific Railroad.  A telephone line was also established to New York City so people across the continent could hear the Pacific Ocean. The Liberty Bell traveled by train on a nationwide tour from Philadelphia, Pennsylvania to attend the exposition. After that trip, the Liberty Bell returned to Philadelphia, and has not made any further journeys since.",
        TAKEABLE: False,
        DESCWORDS: ['panama-pacific', 'panama', 'pacific','international','exposition']},
    'Palace of Fine Arts': { 
        GROUNDDESC: 'Palace of Fine Arts',
        SHORTDESC: 'palace of fine arts',
        LONGDESC: "The Palace of Fine Arts in the Marina District of San Francisco, California, is a monumental structure originally constructed for the 1915 Panama-Pacific Exposition in order to exhibit works of art presented there. One of only a few surviving structures from the Exposition, it is still situated on its original site. It was rebuilt in 1965, and renovation of the lagoon, walkways, and a seismic retrofit were completed in early 2009." "The Palace of Fine Arts was designed by Bernard Maybeck, who took his inspiration from Roman and Greek architecture in designing what was essentially a fictional ruin from another time. While most of the exposition was demolished when the exposition ended, the Palace was so beloved that a Palace Preservation League, founded by Phoebe Apperson Hearst, was founded while the fair was still in progress.",
        TAKEABLE: False,
        DESCWORDS: ['palace','of','fine','arts']},
    'Tower of Jewels': { 
        GROUNDDESC: 'Tower of Jewels',
        SHORTDESC: 'tower of jewels',
        LONGDESC: "Also known as the Tower of the Sun, was the central building at the Panama-Pacific International Exposition, the 1915 world's fair held in San Francisco, California. Designed by architect Thomas Hastings,] the combination triumphal arch-and-tower was 435 feet tall. It was covered with more than 100,000 Novagems, cut glass 'jewels' that sparkled in the sunlight, and were illuminated at night by more than fifty spotlights." "In front of the Tower, the Fountain of Energy flowed at the center of the South Gardens, flanked by the Palace of Horticulture on the west and the Festival Hall to the east. The arch of the Tower served as the gateway to the Court of the Universe, leading to the Court of the Four Seasons to the west and the Court of Abundance to the east.",
        TAKEABLE: False,
        DESCWORDS: ['tower','of','jewels']},
    'Fort Mason': { 
        GROUNDDESC: 'Fort Mason',
        SHORTDESC: 'fort mason',
        LONGDESC: 'Fort Mason, once known as San Francisco Port of Embarkation, US Army, in San Francisco, California, is a former United States Army post located in the northern Marina District, alongside San Francisco Bay. Fort Mason served as an Army post for more than 100 years, initially as a coastal defense site and subsequently as a military port facility. During World War II, it was the principal port for the Pacific campaign.' 'Over the years of the war, 1,647,174 passengers and 23,589,472 measured tons moved from the port into the Pacific. This total represents two-thirds of all troops sent into the Pacific and more than one-half of all Army cargo moved through West Coast ports. The highest passenger count was logged in August 1945 when 93,986 outbound passengers were loaded.',
        TAKEABLE: False,
        DESCWORDS: ['fort','mason']},
    'Golden Gate Bridge': { 
        GROUNDDESC: 'Golden Gate Bridge',
        SHORTDESC: 'golden gate bridge',
        LONGDESC: 'xoxo',
        MOREDESC: 'xoxoxo',
        TAKEABLE: False,
        DESCWORDS: ['golden','gate','bridge']},

#==============================================================#
    
    # MISSION #

    'Mission Dolores': { 
        GROUNDDESC: 'Mission Dolores',
        SHORTDESC: 'mission dolores',
        LONGDESC: 'Mission Dolores, is the oldest surviving structure in San Francisco and the seventh religious settlement established as part of the California chain of missions. The Mission was founded on June 29, 1776, by Lieutenant José Joaquin Moraga and Francisco Palóu (a companion ofJunípero Serra), both members of the de Anza Expedition, which had been charged with bringing Spanish settlers to upper California, and evangelizing the local Natives, the Ohlone.' 'The settlement was named for St. Francis of Assisi, the founder of the Franciscan Order, but was also commonly known as "Mission Dolores" owing to the presence of a nearby creek named Arroyo de Nuestra Señora de los Dolores, meaning "Our Lady of Sorrows Creek."',
        TAKEABLE: False,
        DESCWORDS: ['mission','dolores']},
    'Ohlone': { 
        GROUNDDESC: 'Ohlone',
        SHORTDESC: 'ohlone',
        LONGDESC: "Prior to the arrival of Spanish missionaries, the area which now includes the Mission District was inhabited by the Ohlone people who populated much of the San Francisco bay area. The Yelamu Indians inhabited the region for over 2,000 years. Spanish missionaries arrived in the area during the late 18th century. They found these people living in two villages on Mission Creek. It was here that a Spanish priest named Father Francisco Palóu founded Mission San Francisco de Asis on June 29, 1776." "The Mission was moved from the shore of Laguna Dolores to its current location in 1783. Franciscan friars are reported to have used Ohlone slave labor to complete the Mission in 1791. This period marked the beginning of the end of the Yelamu culture. The Indian population at Mission Dolores dropped from 400 to 50 between 1833 and 1841.",
        TAKEABLE: False,
        DESCWORDS: ['ohlone']},


#============================================================#
    
    # PRESIDIO #

    'Crissy Fields': { 
        GROUNDDESC: 'Crissy Fields',
        SHORTDESC: 'crissy fields',
        LONGDESC: "Crissy Field has been transformed from one of the country's most important and active military airstrips into an abandoned stretch of crumbling asphalt into the recent crowning achievement of the Golden Gate National Parks Association." "After the airfield was closed in 1974, the closure left San Francisco as the only county in California without an airport in its boundaries (San Francisco International Airport is located in San Mateo County.",
        TAKEABLE: False,
        DESCWORDS: ['crissy','fields']},

#============================================================#

    # UNION SQUARE #

    'Dewey Memorial': { 
            GROUNDDESC: 'Dewey Memorial',
            SHORTDESC: 'the dewey memorial',
            LONGDESC: 'Standing at 97 feet tall this monument was built in 1903 by Robert Aitken in dedication to Admiral George Dewey’s victory at the Battle of Manila Bay during the Spanish-American War.  The memorial also commemorates U.S. President William McKinley, who had been recently assassinated.  The artist Robert Aitken was a native San Franciscan and studied at the Mark Hopkins Institute of Art - now known as the San Francisco Art Institute.' "The model of the memorial, Alma de Bretteville, met her future husband as a result of its creation.  This particular statue was selected from several entries and just barely made the cut.  The deciding factor was the vote of the chair of the Citizens’ Committee, Adolph Spreckels.  Adolph, despite being over 20 years her senior, fell in love with Alma and married her following a five-year courtship in 1908.  Because he was head of the Spreckels Sugar Company, Alma often referred to her husband as her ‘sugar daddy’",
            TAKEABLE: False,
            DESCWORDS: ['dewey', 'memorial']},
    'Hearts in San Francisco': { 
            GROUNDDESC: 'The Hearts of San Francisco',
            SHORTDESC: 'hearts in san francisco',
            LONGDESC: 'An annual public art installation started by the San Francisco General Hospital Foundation for the purpose of fundraising.  Each year, several heart sculptures are painted by different artists and placed at locations throughout San Francisco.  The sculptures are then auctioned off at the end of each year’s installation with the proceeds being donated.' "The choice of hearts is inspired by the Tony Bennett song ‘I Left My Heart in San Francisco’",
            TAKEABLE: False,
            DESCWORDS: ['the', 'hearts', 'of', 'san', 'francisco']},
    'Westin St. Francis': { 
            GROUNDDESC: 'Westin St. Francis',
            SHORTDESC: 'westin st. francis',
            LONGDESC: 'A survivor of the 1906 earthquake this hotel provides both luxury and history to its many guests.  Their guests have ranged from artists, to celebrities, to even Presidents themselves (At least the Republican ones as the Democrats usually stay at the Fairmont) - Woodrow Wilson, Charlie Chaplin, Sinclair Lewis, and the Duke Kahanamoku are just a handful of an incredibly notable guests on this list.' '\n\n\n\n\n\n\n\n' "In 1921, the St. Francis was the scene of Hollywood’s first great scandal- known today as the Fatty Arbuckle scandal." "Arbuckle and friends had rented rooms at the hotel and invited several women to the suite for a party. Later that night a guest, a woman by the name of Virginia Rappe became seriously ill.  Originally believed to be a result of intoxication, Rappe was not hospitalized until two days later."  "At the hospital a companion of Rappe, Maude Delmont, told the doctor that Rappe had been raped by Arbuckle. The doctor found no evidence but shortly after Rappe died in the hopital due to a ruptured bladder. Maude had repeated her accusation to the police and what followed was a highly sensationalized media event fueled by yellow journalism and forced false witness statements. The resulting scandal destroyed Arbuckle's career and his personal life." "Arbuckle faced three trials. Despite being acquitted and receiving an apology from the jury, his reputation had been irreparably destroyed.",
            TAKEABLE: False,
            DESCWORDS: ['westin', 'st.','francis']},
    'Cable Car': { 
            GROUNDDESC: 'A cable car passes by Union Square',
            SHORTDESC: 'cable car',
            LONGDESC: "Before the Great Earthquake of 1906, there were more than 600 cable cars in San Francisco. By 1912, there were less than 100. Today, there are only 44." "The first female was hired as a gripman in 1998. A cable car requires two people to operate: a conductor, and a gripman. The gripman handles a 365-pound device that literally grabs the cable as it rattles under the track at 9.45 mph."  "Fannie Mae Barnes was 52 when she took Muni's 25-day grip course. She'd been a conductor for six years- but no woman had ever made it past the first day of training before." 'The idea of the cable car system came from a man named Andrew Smith Hallidie after he witnessed a horrible accident in the summer of 1869. Hallidie saw the toll slippery grades could extract when a horse-drawn streetcar slid backwards under its heavy load. The steep slope with the wet cobblestones and a heavily weighted vehicle combined to drag several horses to their death.'  "Hallidie's father filed the first patent for the manufacture of wire-rope and Hallidie himself had found several uses for it in the California. It wasn't until that fateful accident that the idea of a cable car railway system to deal with San Francisco's fearsome hills came to mind.",
            TAKEABLE: False,
            DESCWORDS: ['cable', 'car']},
    'Maiden Lane': { 
        GROUNDDESC: 'Maiden Lane',
        SHORTDESC: 'maiden lane',
        LONGDESC: "A former section of the city's red light district, Maiden Lane is now home to high-end boutiques and art galleries. This street also serves as the location of San Francisco's only Frank Lloyd Wright (a famous American architect) designed building - the V.C. Morris Gift Shop, which is a San Francisco Designated Landmark." "Prior to the 1906 earthquake, the street was called Morton Street and was the center of San Francisco’s red-light district. Historically, the street reported one murder a week. The earthquake, which leveled much of the city, rendered this two-block stretch of rubble, and the brothels were destroyed. It was renamed Maiden Lane by an enterprising jeweler who wanted to conjure the Maiden Lanes of London and New York.",
        TAKEABLE: False,
        DESCWORDS: ['maiden', 'lane']},
    'Fairmont Hotel': {
        GROUNDDESC: 'Fairmont Hotel',
        SHORTDESC: 'fairmont hotel',
        LONGDESC: "The hotel was named after mining magnate and U.S. Senator James Graham Fair, by his daughters, who built the hotel in his honor. The Venetian Room at the Fairmont Hotel was where Tony Bennett first sang 'I Left My Heart in San Francisco' in December 1961." "In 1945, the Fairmont hosted international statesmen for meetings which culminated in the creation of the United Nations. The United Nations Charter was drafted in the hotel's Garden Room and a plaque at the hotel memorializes the event.",
        TAKEABLE: False,
        DESCWORDS: ['fairmont','hotel']},
    'Grace Cathedral': {
        GROUNDDESC: 'Grace Cathedral',
        SHORTDESC: 'grace cathedral',
        LONGDESC: "It is the cathedral church of the Episcopal Diocese of California. The cathedral is famed for its mosaics by Jan Henryk De Rosen, a replica of Ghiberti's Gates of Paradise, two labyrinths, varied stained glass windows, Keith Haring AIDS Chapel altarpiece, and medieval and contemporary furnishings, as well as its forty-four bell carillon, three organs, and choirs." "Contained in the cathedral are 7,290 square feet of stained glass windows by noted artists that depict over 1100 figures ranging from Adam and Eve to Albert Einstein.",
        TAKEABLE: False,
        DESCWORDS: ['grace','cathedral']},
    'Masonic Temple': {
        GROUNDDESC: 'Masonic Temple',
        SHORTDESC: 'masonic temple',
        LONGDESC: "An icon of mid-century modernist architecture, the California Masonic Memorial Temple atop Nob Hill was designed by Albert Roller and dedicated on Sept. 29, 1958. The temple houses the Masonic Auditorium, the Grand Lodge of California, the Henry W. Coil Library and Museum.  The sculpture on the outside of the building, created by Emile Norman, is a war memorial, with the four 12-foot high figures representing the branches of the armed forces, as well as 14 marble figures engaged in a tug-of-war, representing the struggle between good and evil." "Inside the Masonic Center, it has a unique mosaic window designed by artist Emile Norman. The mosaic depicts a variety of natural themes as well as the professions. It contains gravel and soil from each of the 58 counties in California.",
        TAKEABLE: False,
        DESCWORDS: ['masonic','temple']},
    'San Francisco Oracle': {
        GROUNDDESC: 'San Francisco Oracle',
        SHORTDESC: 'san francisco oracle',
        LONGDESC: "The Oracle was an underground newspaper published in 12 issues from September 20, 1966, to February 1968 in the Haight-Ashbury neighborhood. Allen Cohen, the editor during the paper's most vibrant period, and Michael Bowen, the art director, were among the founders of the publication. The Oracle was an early member of the Underground Press Syndicate. The Oracle combined poetry, spirituality, and multicultural interests with psychedelic design, reflecting and shaping the countercultural community as it developed in the Haight-Ashbury. Arguably the outstanding example of psychedelia within the countercultural 'underground' press, the publication was noted for experimental multicolored design.",
        TAKEABLE: False,
        DESCWORDS: ['san','Francisco','oracle']},
    'Broadway': {
        GROUNDDESC: 'Broadway',
        SHORTDESC: 'broadway',  
        LONGDESC: "The Broadway area of North Beach created innovations for the strip club industry. The Condor Club, on the corner of Columbus and Broadway, was opened in 1964 as America's first topless bar, which it is again today. The Lusty Lady was the first striptease club to be structured as a worker cooperative, which meant that it was managed by the dancers who worked at that peep-show establishment. Broadway strip clubs owe their legacy to the Barbary Coast, which was located just one block south on Pacific Street during the late 19th-century.",
        TAKEABLE: False,
        DESCWORDS: ['broadway']},
    'Golden Gate Bridge': {
        GROUNDDESC: 'Golden Gate Bridge',
        SHORTDESC: 'golden gate bridge',
        LONGDESC: "This bridge is one of the most internationally recognized symbols of San Francisco, California, and the United States. It has been declared one of the Wonders of the Modern World by the American Society of Civil Engineers. It opened in 1937 and was, until 1964, the longest suspension bridge main span in the world, at 4,200 feet" "The Bridge has an influence in directing the fog as it pushes up and pours down around the Bridge. Sometimes, high pressure squashes it close to the ground.",
        TAKEABLE: False,
        DESCWORDS: ['golden','gate','bridge']},
    'Museum of Modern Art': {
        GROUNDDESC: 'Museum of Modern Art',
        SHORTDESC: 'museum of modern art',
        LONGDESC: 'The Museum of Modern Art holds an internationally recognized collection of modern and contemporary art and was the first museum on the West Coast devoted solely to 20th-century art. The museum’s current collection includes over 29,000 works of painting, sculpture, photography, architecture, design, and media arts.',
        TAKEABLE: False,
        DESCWORDS: ['museum','modern','art']},
    'Moscone Center': {
        GROUNDDESC: 'Moscone Center',
        SHORTDESC: 'moscone center',
        LONGDESC: 'The Moscone Center is the largest convention and exhibition complex in the city. Although the Center is named after the murdered mayor, Moscone opposed the development of the area when he served on the SF Board of Supervisors in the 1960s because he felt it would displace elderly and poor residents of the area.' "The Democratic Party of the United States held its 1984 convention at the Convention Center, nominating Walter Mondale for President of the United States and Geraldine Ferraro for Vice President (the first time a woman had ever been nominated by a major party for either office); they went on to lose the election to Republican incumbents Ronald Reagan and George H. W. Bush by the second-largest electoral margin ever.",
        TAKEABLE: False,
        DESCWORDS: []},
    'Warfield Theater': {
        GROUNDDESC: 'Warfield Theater',
        SHORTDESC: 'warfield theater',
        LONGDESC: "In the 1920s, The Warfield was a popular location that featured vaudeville and other major performances, such as Al Jolson, Louis Armstrong, and Charlie Chaplin. New Life came to the Warfield in 1979 when Bob Dylan played 14 shows at the start of his first Gospel Tour in November 1979, and again 12 shows in November 1980 during his 'A Musical Retrospective Tour'. The Warfield had an appeal as a rock concert venue because it has more intimacy and better sound quality than an arena, yet has an occupancy of over 2000 persons. The venerable hall has been rocking ever since." "The Warfield served as a home for the Grateful Dead for many years. In 1980, the Dead played 15 sold-out shows there, featuring both an acoustic and two electric sets. The shows were a celebration of the band's fifteenth anniversary and done as a show of appreciation for their loyal fans.",
        TAKEABLE: False,
        DESCWORDS: ['warfield','theater']},
    'Tessie Wall': {
        GROUNDDESC: 'Tessie Wall',
        SHORTDESC: 'tessie wall',
        LONGDESC: "In an era when cheap prostitution was rife in San Francisco, Tessie Wall’s brothel in the then fashionable Tenderloin district was a beacon of elegance and good taste, making her the best known and most successful parlor-house madam in town. In 1898 she opened her first brothel at 211 O’Farrell Street but this was  destroyed by one of the many fires triggered by the earthquake of 1906.  Undaunted she reopened it in a three storey brick building with terracotta facing at 337 O’Farrell Street.  It was a grand affair with the first floor comprising a saloon whilst upstairs was a large, mirrored ballroom, dining room, kitchen, twelve bedrooms and several parlors." "As he entered the main receiving room he would be confronted by a needlepoint motto that read “If every man was as true to his country as he is to his wife – God help the USA”.",
        TAKEABLE: False,
        DESCWORDS: ['tessie','wall']},
    'Museum of African Diaspora': {
        GROUNDDESC: 'Museum of African Diaspora',
        SHORTDESC: 'museum of african diaspora',
        LONGDESC: "The Museum of the African Diaspora is uniquely positioned as one of the few museums in the world focused exclusively on African Diaspora culture and on presenting the rich cultural heritage of the people of Africa and of African descendant cultures all across the globe. MoAD introduces visitors to the original African diaspora—the original movement of Homo sapiens (from the earliest human remains found in Africa)—to eventually all inhabited regions. The museum asks visitors 'when did you first realize you are African?'' The museum espouses the scientifically accepted idea of panethnicity, wherein all humans have a common African origin." "The African American Cultural Institute grew out of the research and development process that began in 2002. The new museum was renamed Museum of the African Diaspora to reflect a broadened scope and mission.",
        TAKEABLE: False,
        DESCWORDS: ['museum','african','diaspora']},
    'Cartoon Art Museum': {
        GROUNDDESC: 'Cartoon Art Museum',
        SHORTDESC: 'cartoon art museum',
        LONGDESC: "The Cartoon Art Museum is a California art museum that specializes in the art of comics and cartoons. It is the only museum in the Western United States dedicated to the preservation and exhibition of all forms of cartoon art. The permanent collection features some 7,000 pieces as of 2015, including original animation cels, comic book pages and sculptures.",
        TAKEABLE: False,
        DESCWORDS: ['cartoon','art','museum']},
    }



 
##########################################################

#The value in the location variable will always be a key in the world variable

location = 'Embarcadero' # start in town square
showFullExits = True

import cmd, textwrap

def displayLocation(loc):
    """A helper function for displaying an area's description and exits."""
    # Print the room name.
    print "                 "
    print loc
    print'=' * len(loc)

    # Print the room's description (using textwrap.wrap())
    print'\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH))

    # Print all the items on the ground.
    if len(worldRooms[loc][GROUND]) > 0:
        print'                              '
        for item in worldRooms[loc][GROUND]:
            print worldItems[item][GROUNDDESC]

    # Print all the exits.
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST):
        if direction in worldRooms[loc].keys():
            exits.append(direction.title())
    print'                                  '
    if showFullExits:
        for direction in (NORTH, SOUTH, EAST, WEST):
            if direction in worldRooms[location]:
                print'%s: %s' % (direction.title(), worldRooms[location][direction])
    else:
        print'Exits: %s' % ' '.join(exits)


def moveDirection(direction):
    """A helper function that changes the location of the player."""
    global location

    if direction in worldRooms[location]:
        print'You move to the %s.' % direction
        location = worldRooms[location][direction]
        displayLocation(location)
    else:
        print'You cannot move in that direction'


def getAllDescWords(itemList):
    """Returns a list of "description words" for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.extend(worldItems[item][DESCWORDS])
    return list(set(descWords))

def getAllFirstDescWords(itemList):
    """Returns a list of the first "description word" in the list of
    description words for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.append(worldItems[item][DESCWORDS][0])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            return item
    return None

def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    matchingItems = []
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems


class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print'I do not understand that command. Type "help" for a list of commands.'

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()



    # These direction commands have a long (i.e. north) and show (i.e. n) form.
    # Since the code is basically the same, I put it in the moveDirection()
    # function.
    def do_north(self, arg):
        # """Go to the area to the north, if possible."""
        moveDirection('north')

    def do_south(self, arg):
        # """Go to the area to the south, if possible."""
        moveDirection('south')

    def do_east(self, arg):
        # """Go to the area to the east, if possible."""
        moveDirection('east')

    def do_west(self, arg):
        # """Go to the area to the west, if possible."""
        moveDirection('west')


    # Since the code is the exact same, we can just copy the
    # methods with shortened names:
    do_n = do_north
    do_s = do_south
    do_e = do_east
    do_w = do_west
    
    def do_exits(self, arg):
        # """Toggle showing full exit descriptions or brief exit descriptions."""
        global showFullExits
        showFullExits = not showFullExits
        if showFullExits:
            print'Showing full exit descriptions.'
        else:
            print'Showing brief exit descriptions.'



    def do_take(self, arg):
        """"take <item> - Take an item on the ground."""

        # put this value in a more suitably named variable
        itemToTake = arg.lower()

        if itemToTake == '':
            print'Take what? Type "look" the items on the ground here.'
            return

        cantTake = False

        # get the item name that the player's command describes
        for item in getAllItemsMatchingDesc(itemToTake, worldRooms[location][GROUND]):
            if worldItems[item].get(TAKEABLE, True) == False:
                cantTake = True
                continue # there may be other items named this that you can take, so we continue checking
            print'You take %s.' % (worldItems[item][SHORTDESC])
            worldRooms[location][GROUND].remove(item) # remove from the ground
            inventory.append(item) # add to inventory
            return

        if cantTake:
            print'You cannot take "%s".' % (itemToTake)
        else:
            print'That is not on the ground.'


   


    def do_look(self, arg):
#        Look at an item, direction, or the area:
# "look" - display the current area's description
# "look <direction>" - display the description of the area in that direction
# "look exits" - display the description of all adjacent areas
# "look <item>" - display the description of an item on the ground or in your inventory

        lookingAt = arg.lower()
        if lookingAt == '':
            # "look" will re-print the area description
            displayLocation(location)
            return

        if lookingAt == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST):
                if direction in worldRooms[location]:
                    print'%s: %s' % (direction.title(), worldRooms[location][direction])
            return

        if lookingAt in ('north', 'west', 'east', 'south', 'n', 'w', 'e', 's'):
            if lookingAt.startswith('n') and NORTH in worldRooms[location]:
                print(worldRooms[location][NORTH])
            elif lookingAt.startswith('w') and WEST in worldRooms[location]:
                print(worldRooms[location][WEST])
            elif lookingAt.startswith('e') and EAST in worldRooms[location]:
                print(worldRooms[location][EAST])
            elif lookingAt.startswith('s') and SOUTH in worldRooms[location]:
                print(worldRooms[location][SOUTH])
            else:
                print'There is nothing in that direction.'
            return

        # see if the item being looked at is on the ground at this location
        item = getFirstItemMatchingDesc(lookingAt, worldRooms[location][GROUND])
        if item != None:
            print'\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH))



    def complete_look(self, text, line, begidx, endidx):
        possibleItems = []
        lookingAt = text.lower()

        # # get a list of all "description words" for each item in the inventory
        
        groundDescWords = getAllDescWords(worldRooms[location][GROUND])
        

    

        # if the user has only typed "look" but no item name, show all items on ground and directions:
        if lookingAt == '':
            possibleItems.extend(getAllFirstDescWords(worldRooms[location][GROUND]))
            for direction in (NORTH, SOUTH, EAST, WEST):
                if direction in worldRooms[location]:
                    possibleItems.append(direction)
            return list(set(possibleItems)) # make list unique

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for descWord in groundDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

       

        # check for matching directions
        for direction in (NORTH, SOUTH, EAST, WEST):
            if direction.startswith(lookingAt):
                possibleItems.append(direction)



        return list(set(possibleItems)) # make list unique





    

if __name__ == '__main__':
    print "(----------------------------------------------------)"
    print "(   ___________                 __    _              )"
    print "(  /____  ____/_____  _________|  |__| | ___         )"
    print "(      / / /  _  \||  |||  __|__   __| |/ _ \        )"
    print "(     / / |  |_|  ||  ||| |    |  |  | |   __        )"
    print "(    /_/   \_____/||__|||_|    |__|  |_|\___/        )"
    print "(                                                    )"
    print "(----------------------------------------------------)"
    print '                     '
    print '(Type "help" for commands.)'
    print '                     '
    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print 'Thanks for playing!'