label poem:
    stop music fadeout 2.0
    play music t2

    scene bg club_day
    with dissolve_scene_full
    # Get word list
    python:
        wordlist = MASPoemWordList(mas_poemwords)

    $ pg_args = dict()

    # Game Configuration
    menu:
        "Collect word ?"
        "Yes":
            $ pg_args["gather_words"] = True
        "No":
            pass

    menu:
        "Glitch the words ?"
        "Yes":
            call getnum("Space instead of letter (1 out of x)") from _call_getnum
            $ space_odds = _return

            if space_odds <= 0:
                $ space_odds = 5

            call getnum("Nonunicode instead of letter ? (1 out of x)") from _call_getnum_1
            $ nonuni_odds = _return

            if nonuni_odds <= 0:
                $ nonuni_odds = 5

            $ pg_args["glitch_words"] = (True, space_odds, nonuni_odds)

        "No":
            pass

    menu:
        "Poemgame music ?"
        "Yes":
            pass
        "No":
            $ pg_args["music_filename"] = "BACK"

    menu:
        "Add Monika ?"
        "Yes":
            pass
        "No":
            $ pg_args["show_monika"] = False

    menu:
        "Add Sayori ?"
        "Yes":
            $ pg_args["show_sayori"] = True
        "No":
            $ pg_args["show_sayori"] = False

    menu:
        "Add Natsuki ?"
        "Yes":
            $ pg_args["show_natsuki"] = True
        "No":
            $ pg_args["show_natsuki"] = False

    menu:
        "Add Yuri ?"
        "Yes":
            menu:
                "Sleeves rolled up ?"
                "Yes":
                    $ pg_args["show_yuri_cut"] = True
                "No":
                    pass
            $ pg_args["show_yuri"] = True
        "No":
            pass

    menu:
        "Glitched counter ?"
        "Yes":
            $ pg_args["one_counter"] = True
        "No":
            pass

    call getnum("How many words ?") from _call_getnum_2
    $ count = _return

    if count <= 0:
        $ count = 14
    elif count > 50:
        $ count = 50

    $ pg_args["total_words"] = count

    $ pg_args["flow"] = store.mas_poemgame_consts.STOCK_MODE
    $ pg_args["poem_wordlist"] = wordlist
    $ pg_args["show_poemhelp"] = False

    if "music_filename" not in pg_args:
        stop music fadeout 1.0

    call mas_poem_minigame(**pg_args) from _call_mas_poem_minigame
    $ results = _return

    scene bg club_day with dissolve_scene_full

    if "music_filename" not in pg_args:
        play music t3 fadein 1.0

    if "gather_words" in pg_args:
        $ words = results.pop("words")
        python:
            for word in words:
                mc(word.word)
        pass

    python:
        for k,v in results.iteritems():
            mc(k + " received " + str(v) + " points from your choices.")
    pass

    #$ from store.mas_poemgame_consts import STOCK_MODE
    #call mas_poem_minigame(STOCK_MODE,music_filename=music_filename,show_monika=show_monika,show_natsuki=show_natsuki,show_sayori=show_sayori,show_yuri=show_yuri,show_poemhelp=show_poemhelp,total_words=total_words,poem_wordlist=poem_wordlist,only_winner=only_winner,gather_words=gather_words,sel_sound=sel_sound,trans_in=trans_in,trans_out=trans_out,music_fadein=music_fadein,music_fadeout=music_fadeout,trans_fast=trans_fast) from _call_poem_minigame_actone
    #call mas_poem_minigame(STOCK_MODE,music_filename=audio.t4,show_monika=True,show_natsuki=False,show_sayori=False,show_yuri=False,glitch_nb=False,show_poemhelp=False,total_words=20,poem_wordlist=None,trans_in=True,one_counter=False,only_monika=False,glitch_words=None,trans_out=True,glitch_wordscare=None,only_winner=False,glitch_baa=None,gather_words=False,sel_sound=gui.activate_sound,hop_monika=False,show_yuri_cut=False,show_yuri_scary=None,show_eyes=None,glitch_wordscare_sound=None,music_fadein=2.0,music_fadeout=2.0,trans_fast=False) from _call_mas_poem_minigame

    return

label getnum(msg):
    python:
        sel_num = renpy.input(
            "[msg]",
            allow="0123456789",
            length=2
        )
        if len(sel_num) <= 0:
            sel_num = 0
        else:
            sel_num = int(sel_num)

    return sel_num