import media
import fresh_tomatoes


battleship = media.Movie("Battleship",
                         "An intense battle fought by an international fleet of\
                         ships with an alien armada whom they come across\
                         while on Naval war games exercise.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI5NTM5MDA2N15BMl5BanBnXkFtZTcwNjkwMzQxNw@@._V1_UY1200_CR64,0,630,1200_AL_.jpg",
                         "https://www.youtube.com/watch?v=cp3646Zf8rg")

bahubali_1 = media.Movie("Baahubali: The Beginning",
                         "Shiva, the son of Bahubali, falls in love with\
                         warrior girl avantika and helps her in rescuing\
                         devsena from Bhallal Dev.",
                         "http://www.cinebucket.com/wp-content/uploads/2015/05/11181939_711834958926211_1222094694353706802_o.jpg",
                         "https://www.youtube.com/watch?v=sOEg_YZQsTI")

bahubali_2 = media.Movie("Baahubali 2: The Conclusion",
                         "Shiva, the son of Bahubali, begins to search for\
                         answers after he learns about his heritage.",
                         "https://www.thetelugufilmnagar.com/wp-content/uploads/2017/05/Baahubali-2-The-Conclusion-5th-Week-Posters_thetelugufilmnagar-2.jpg",
                         "https://www.youtube.com/watch?v=qD-6d8Wo3do")

mahabharat = media.Tv_series("Mahabharatam", "1",
                             "Story of wars between pandavas sons of king Pandu\
                             and Kauravas, sons of king Dhritarastra",
                             "http://indiaopines.com/wp-content/uploads/2014/10/mahabharat-arjuna-yudhisthira-kurukshetra-war.jpg",
                             "https://www.youtube.com/watch?v=J-YUqPle-h4")

siya_ke_ram = media.Tv_series("Siya Ke Ram", "1",
                              "Story of how Ram defeats Ravan who kidnaps Sita\
                              wife of Ram",
                              "http://media2.intoday.in/indiatoday/images/stories/sia-ke-ram-story_647_111615062816.jpg",
                              "https://www.youtube.com/watch?v=scTsU_A9h_s")

dhruva = media.Movie("Dhruva",
                     "Story of a policeman who succeds in defeating a criminal\
                     minded person who is very inetlligent scientist for \
                     the society.",
                     "http://data1.ibtimes.co.in/cache-img-600-0-photo/en/full/46346/1479554395_ram-charans-dhruva-first-look-poster-revealed.jpg",
                     "https://www.youtube.com/watch?v=r_yVN37aCYI")


movies = [bahubali_1, bahubali_2, dhruva,  battleship, mahabharat, siya_ke_ram]


fresh_tomatoes.open_movies_page(movies)
