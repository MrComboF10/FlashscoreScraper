import flashscore

flashscore.start()
italy_serie_a_seasons = flashscore.scrap_league_seasons("italy", "serie-a", 2017, 2017)
flashscore.create_wb(italy_serie_a_seasons)
flashscore.write_taticas_rosques()
flashscore.write_jogos_quinados()
flashscore.close()
